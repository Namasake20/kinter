from tkinter import *

class PaintBox(Frame):
    """Demonstrates drawing on canvas"""
    def __init__(self):
        """Create Canvas and bind paint method to mouse dragging"""
        Frame.__init__( self )
        self.pack( expand = YES, fill = BOTH )
        self.master.title( "A simple paint program" )
        self.master.geometry( "300x150" )
        
        self.message = Label( self,text = "Drag the mouse to draw" )
        self.message.pack( side = BOTTOM )
        
        # create Canvas component
        self.myCanvas = Canvas( self )
        self.myCanvas.pack( expand = YES, fill = BOTH )
        
        # bind mouse dragging event to Canvas
        self.myCanvas.bind( "<B1-Motion>", self.paint )

    def paint(self,event):
        """Create an oval of radius 4 around the mouse position"""
        x1, y1 = ( event.x - 4 ), ( event.y - 4 )
        x2, y2 = ( event.x + 4 ), ( event.y + 4 )
        self.myCanvas.create_oval( x1, y1, x2, y2, fill = "dodgerblue" )

def main():
    PaintBox().mainloop()

if __name__ == "__main__":
    main()
