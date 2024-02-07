# TIMEFRAME GUI: PYTHON-BASED DIGITAL CLOCK AND DATE DISPLAY. 

import tkinter as tk

import time 

class Digital_Clock():

    def __init__( self ):

        self.window = tk.Tk()

        self.window.geometry( "400x400" ) 
        self.window.resizable( 0,0 ) 

        self.window.title( "DIGITAL CLOCK" )

        self.frame1 = self.display_frame1()

        self.label1 = self.display_label1()

        self.frame2 = self.display_frame2()  

        self.label2 = self.display_label2()

        self.time_is() 
        self.date_is() 
    
    def display_frame1( self ): 

        frame = tk.Frame( self.window, height=200 ) 
        frame.pack( expand=True, fill="both") 
        return frame
    
    def display_label1( self ):

        label = tk.Label( self.frame1, bg="LightGray", font=( "Calibri", 32, "bold" ) ) 
        label.pack( expand=True, fill="both" ) 
        return label 

    def display_frame2( self ): 

        frame = tk.Frame( self.window, height=200 )  
        frame.pack( expand=True, fill="both") 
        return frame 
    
    def display_label2( self ):

        label = tk.Label( self.frame2, bg="Gray", font=( "Calibri", 32, "bold" ) ) 
        label.pack( expand=True, fill="both" ) 
        return label 
    
    def time_is( self ):

        timeis = time.strftime( "%I:%M:%S %p" )
        self.label1.config( text=timeis )  
        self.label1.after( 1000,self.time_is ) 

    def date_is( self ):

        dateis = time.strftime( "%D" ) 
        self.label2.config( text=dateis )

    def close( self ):

        self.window.mainloop()

if __name__ == "__main__":

    call_fun = Digital_Clock()

    call_fun.close() 
