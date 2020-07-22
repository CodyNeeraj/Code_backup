
import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
class basic
        
{
   public static void main(String[] args) 
    {
       frame frm = new frame();
    }
}

class frame extends JFrame implements ActionListener
{
    private JButton btn1;
    private JButton btn2;
	private JButton btn3;
	private JButton btn4;
    private JLabel  lbl1;
    private Container c;
    private JTextArea area1;
	
    frame()
    {
        c = this.getContentPane();
        setLayout(null);
        setBounds(370,200,400,350);
        setVisible(true);  
        setTitle("Registration form");
        setResizable(true);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        ImageIcon icon = new ImageIcon("logo.png");
        setIconImage(icon.getImage());
        addFocusListener(new FocusListener()
		{
			@Override
			public void focusGained(FocusEvent e) 
			{
				 System.out.println("Focus Gained");
			}

			@Override
			public void focusLost(FocusEvent e)
			{
			   System.out.println("Focus lost");
			}
		});
		
        
		area1 =  new JTextArea();
        area1.setBounds(105,150,145,60);
        area1.setEditable(false);
        area1.setLineWrap(false);
        area1.setToolTipText("JText area");
		//area.addMouseListener(this); use this when implementing the listener interface in class declaration
		area1.addMouseListener(new MouseListener()
		{
			@Override     
			public void  mouseEntered(MouseEvent e)
			{
				System.out.println("MOuse entered");
				lbl1.setText("entered");
			}
			
			@Override 
			public void mouseClicked(MouseEvent e)
			{
				System.out.println("MOuse clicked");
				lbl1.setText("clicked"); 
			}
			
			@Override 
			public void mouseReleased(MouseEvent e)
			{
				System.out.println("MOuse released");
				lbl1.setText("released");
			}
			
			@Override 
			public void mouseExited(MouseEvent e)
			{
			   System.out.println("MOuse exited");
			   lbl1.setText("exited");
			}
			
			@Override 
			public void mousePressed(MouseEvent e) 
			{
			   System.out.println("MOuse pressed");
			}
				
		});
        area1.addKeyListener(new KeyListener()
		{
			@Override
			public void keyTyped(KeyEvent e) 
			{
				System.out.println("key typed "+e.getKeyChar()/* +e.getKeyLocation() */);
			}

			@Override
			public void keyPressed(KeyEvent e)
			{
				 System.out.println("key pressed "+e.getKeyChar()/* +e.getKeyLocation() */);
			}

			@Override
			public void keyReleased(KeyEvent e)
			{
				System.out.println("key released  "+e.getKeyChar()/* +e.getKeyLocation () */);
			}
		});
        area1.addMouseMotionListener(new MouseMotionListener()
		{
			@Override
			public void mouseDragged(MouseEvent e)
			{
				 System.out.println("dragged X cords are "+e.getX()+" "+e.getY());
			}

			@Override
			public void mouseMoved(MouseEvent e) 
			{
				 System.out.println("moved on X cords are "+e.getX()+" "+e.getY());
			}
		});
        
       
	    btn1 = new JButton("btn1");
        btn1.setBounds(100,55,60,30);
        btn1.setBackground(Color.white);
        btn1.setForeground(Color.black);
        btn1.addActionListener(this);
		
        
		btn2= new JButton("btn2");
        btn2.setBounds(200,55,60,30);
        //btn2.setBounds(200,100,icon.getIconWidth(),icon.getIconHeight());
        btn2.setBackground(Color.white);
        btn2.setForeground(Color.black);
        btn2.addActionListener(this);
		
		
		btn3 = new JButton("Close");
		btn3.setBounds(100,100,60,30);
		btn3.setBackground(Color.white);
        btn3.setForeground(Color.black);
		btn3.addActionListener(this);
		
		btn4 = new JButton("New");
		btn4.setBounds(200,100,60,30);
		btn4.setBackground(Color.white);
        btn4.setForeground(Color.black);
		btn4.addActionListener(this);
		
		lbl1 = new JLabel("I'm about to go..");
        lbl1.setBounds(135,10,90,40);
        
       
        c.add(btn1);
        c.add(lbl1);
        c.add(btn2);
		c.add(btn3);
		c.add(btn4);
		
        c.add(area1);
        c.revalidate();
        
    }
	
	 @Override
	 public void actionPerformed(ActionEvent e)
	  {
		 if (e.getSource()==btn1)
		  {
			System.out.println("btn1 is presed");
			lbl1.setBounds(170,10,90,40);
			lbl1.setText("oking");
			c.setBackground(Color.yellow);
			//setResizable(false);     
			area1.append("");
			area1.append("btn1 is pressed !\n");
		  }

		  else if(e.getSource()==btn2)
		  {
			System.out.println("btn2 is presed");
			lbl1.setBounds(160,10,90,40);
			lbl1.setText("Helping");
			c.setBackground(Color.green);
			//setResizable(false);
			area1.append("");
			area1.append("btn2 is pressed !\n");
		  }
		  
		  else if(e.getSource()==btn3)
		  {
			  dispose();
		  }
		  
		  else if(e.getSource()==btn4)
		  {
			 new frame();
		  }
		  
		}          
}



                