# DIGITAL CALCULATOR WITH GUI USING PYTHON. 

import tkinter as tk 

class Calculator:

    def __init__( self ):

        self.window = tk.Tk()

        self.window.geometry( "375x667" ) 
        self.window.resizable( 0,0 ) 

        self.window.title( "Calculator" ) 

        self.frame1 = self.frame1_display()

        self.display1 = ""
        self.display2 = "" 

        self.label1 = self.label1_display() 
        self.label2 = self.label2_display()

        self.frame2 = self.frame2_display()  

        self.frame2.rowconfigure( 0, weight=1 ) 

        for i in range(1,5):

            self.frame2.rowconfigure( i, weight=1 )
            self.frame2.columnconfigure( i, weight=1 ) 

        self.buttons_dic = {

            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            '.':(4,1), 0:(4,2) 
        }

        self.operators_dic = { '/':"\u00F7", '*':"\u00D7", '-':'-', '+':'+' } 

        self.num_buttons() 
        self.operator_buttons() 
        self.equaltoo_button()  
        self.clear_button()
        self.square_button()
        self.sqrt_button() 
        self.bind_keys() 

    def bind_keys( self ):

        self.window.bind( "<Return>", lambda event: self.equal() ) 

        for key in self.buttons_dic: 

            self.window.bind( str(key), lambda event, digit=key: self.number(digit) ) 
        
        for key in self.operators_dic:

            self.window.bind( str(key), lambda event, operator=key: self.operator(operator) ) 
    
    def frame1_display( self ):

        frame = tk.Frame( self.window, height=221 )
        frame.pack( expand=True, fill="both" ) 
        return frame 
    
    def label1_display( self ):

        label = tk.Label( self.frame1, text=self.display1, anchor=tk.E, padx=24, bg="LightGray", font=( "Calibri", 16 ) ) 
        label.pack( expand=True, fill="both" ) 
        return label 
    
    def label2_display( self ):

        label = tk.Label( self.frame1, text=self.display2, anchor=tk.E, padx=24, bg="LightGray", font=( "Calibri", 40, "bold" ) )
        label.pack( expand=True, fill="both" ) 
        return label 
    
    def frame2_display( self ):

        frame = tk.Frame( self.window )
        frame.pack( expand=True, fill="both" ) 
        return frame 
    
    def number( self, value ):

        self.display2 = self.display2 + str(value) 

        self.update_frame2()
    
    def num_buttons( self ):

        for digit,grid_val in self.buttons_dic.items():

            buttons = tk.Button( self.frame2, text=str(digit), borderwidth=0, font=( "Calibri", 24, "bold" ), command= lambda x=digit: self.number( x ) )
            buttons.grid( row=grid_val[0], column=grid_val[1], sticky=tk.NSEW ) 
    
    def operator( self, value ):

        self.display2 = self.display2 + value 

        self.display1 = self.display1 + self.display2 

        self.display2 = "" 

        self.update_frame1()
        self.update_frame2() 
    
    def operator_buttons( self ):

        i = 0 

        for operator,symbol in self.operators_dic.items():

            buttons = tk.Button( self.frame2, text=symbol, borderwidth=0, bg="Orange", font=( "Calibri", 24, "bold" ), command= lambda x=operator: self.operator( x ) ) 
            buttons.grid( row=i, column=4, sticky=tk.NSEW ) 

            i = i+1 
        
    def equal( self ):

        self.display1 = self.display1 + self.display2 
        self.update_frame1()

        try:
            
            self.display2 = str( eval( f' {self.display1} ' ) )  

            self.display1 = "" 

        except Exception:

            self.display2 = "Error" 
        
        finally:

            self.update_frame2() 
    
    def equaltoo_button( self ):

        button = tk.Button( self.frame2, text="=", borderwidth=0, bg="LightBlue", font=( "Calibri", 24, "bold" ), command= self.equal ) 
        button.grid( row=4, column=3, columnspan=2, sticky=tk.NSEW )  
    
    def clear( self ):

        self.display1 = ""
        self.display2 = ""

        self.update_frame1()
        self.update_frame2() 
    
    def clear_button( self ):

        button = tk.Button( self.frame2, text="C", borderwidth=0, bg="LightBlue", font=( "Calibri", 24, "bold" ), command= self.clear )
        button.grid( row=0, column=1, sticky=tk.NSEW ) 
    
    def square( self ):

        self.display2 = str(eval( f' {self.display2}**2 ' )) 

        self.update_frame2() 
    
    def square_button( self ):

        button = tk.Button( self.frame2, text="x\u00b2", borderwidth=0, bg="Orange", font=( "Calibri", 24, "bold" ), command= self.square )
        button.grid( row=0, column=2, sticky=tk.NSEW ) 
    
    def sqrt( self ):

        self.display2 = str(eval( f' {self.display2}**0.5 ' ))  

        self.update_frame2() 
    
    def sqrt_button( self ):

        button = tk.Button( self.frame2, text="\u221ax", borderwidth=0, bg="Orange", font=( "Calibri", 24, "bold" ), command= self.sqrt )
        button.grid( row=0, column=3, sticky=tk.NSEW ) 
    
    def update_frame1( self ):

        expression = self.display1

        for operator,symbol in self.operators_dic.items():

            expression = expression.replace( operator, f' {symbol} ' ) 

        self.label1.config( text=expression ) 
    
    def update_frame2( self ):

        self.label2.config( text=self.display2[:11] )  
    
    def close( self ): 

        self.window.mainloop() 

if __name__ == "__main__":

    call_fun = Calculator()
    call_fun.close() 