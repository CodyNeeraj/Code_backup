import psutil
import socket
import json
import time
import threading
from datetime import datetime
import os
import platform
import sys

LOG_FILE = "/tmp/procnet_monitor.jsonl" if platform.system() != "Windows" else "procnet_monitor.jsonl"

dns_cache = {}
connection_cache = set()
lock = threading.Lock()
LOG_ALL_CONNECTIONS = True  # Set to False to log only new connections


def log_connection(entry):
    with lock:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def resolve_ip(ip):
    if ip in dns_cache:
        return dns_cache[ip]
    try:
        domain = socket.gethostbyaddr(ip)[0]
        dns_cache[ip] = domain
        return domain
    except socket.herror:
        dns_cache[ip] = None
        return None


def get_direction(local_ip):
    private_prefixes = ("10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "192.168.")
    return "egress" if local_ip.startswith(private_prefixes) else "ingress"


def monitor_connections(interval=2):
    print(f"[INFO] Monitoring started (interval={interval}s)...")
    while True:
        try:
            connections = psutil.net_connections(kind='inet')  # includes TCP and UDP
            if not connections:
                print("[DEBUG] No active inet connections found.")

            for conn in connections:
                if not conn.raddr and conn.status != psutil.CONN_LISTEN:
                    continue

                pid = conn.pid
                if not pid:
                    continue

                conn_tuple = (pid, conn.laddr.ip, conn.laddr.port,
                              conn.raddr.ip if conn.raddr else None,
                              conn.raddr.port if conn.raddr else None)

                if not LOG_ALL_CONNECTIONS and conn_tuple in connection_cache:
                    continue

                try:
                    proc = psutil.Process(pid)
                    proc_name = proc.name()
                    cmdline = " ".join(proc.cmdline())
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    proc_name = "N/A"
                    cmdline = ""

                direction = get_direction(conn.laddr.ip)
                timestamp = datetime.utcnow().isoformat() + "Z"

                log_entry = {
                    "timestamp": timestamp,
                    "pid": pid,
                    "process_name": proc_name,
                    "cmdline": cmdline,
                    "status": conn.status,
                    "direction": direction,
                    "local_ip": conn.laddr.ip,
                    "local_port": conn.laddr.port,
                    "remote_ip": conn.raddr.ip if conn.raddr else None,
                    "remote_port": conn.raddr.port if conn.raddr else None,
                    "domain": resolve_ip(conn.raddr.ip) if conn.raddr else None,
                    "protocol": "TCP" if conn.type == socket.SOCK_STREAM else "UDP"
                }

                log_connection(log_entry)
                connection_cache.add(conn_tuple)

                print(f"[LOGGED] {proc_name} ({pid}) {conn.laddr.ip}:{conn.laddr.port} -> "
                      f"{conn.raddr.ip if conn.raddr else 'N/A'}:{conn.raddr.port if conn.raddr else 'N/A'} [{log_entry['protocol']}]")

        except Exception as e:
            print(f"[ERROR] {e}")

        time.sleep(interval)


def main():
    if os.geteuid() != 0:
        print("[WARNING] Run as root to capture all processes and connections.")
    if not os.path.exists(LOG_FILE):
        print(f"[INFO] Creating log file at {LOG_FILE}")
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            f.write("")

    monitor_thread = threading.Thread(target=monitor_connections)
    monitor_thread.daemon = True
    monitor_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[INFO] Monitor interrupted by user. Exiting...")


if __name__ == "__main__":
    main()
