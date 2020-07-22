#include <graphics.h>
#include <windows.h>
#include <conio.h>
  int main() 
  {  
      Beep(0,500);
      int gd = DETECT, gm;
      initgraph(&gd, &gm, "C:\\TC\\BGI"); 
      settextstyle(BOLD_FONT,HORIZ_DIR,2);
      outtextxy(350,0,"3D BAR GRAPH");
      setlinestyle(SOLID_LINE,0,2);
	      /* Print X and Y Axis */ 
		    
								       /* Print 3D bars */
						   setfillstyle(LTBKSLASH_FILL, GREEN);
						   bar3d(75,19, 125,427,  15, 1);     // 1
						   setfillstyle(SOLID_FILL, BLUE);
						   bar3d(150,30, 200,427,  15, 1);    // 2
						   setfillstyle(LINE_FILL, RED);
						   bar3d(225,68,275,427,  15, 1);     // 3
						   setfillstyle(SLASH_FILL, YELLOW);
						   bar3d(300,94,350,427,  15, 1);     // 4
						   setfillstyle(INTERLEAVE_FILL, CYAN);
						   bar3d(375,136,425,427,  15, 1);    // 5
						   setfillstyle(HATCH_FILL, MAGENTA);
						   bar3d(450,200,500,427,  15, 1);    // 6
									    getch(); 
										closegraph();
									    return 0;
											 } 

