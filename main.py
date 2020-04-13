##Write a program that will create a GUI that converts Fahrenheit temperatures to Celsius.
##Create an entry box to capture the temperature in Fahrenheit
##The box should have a label
##There should be a button to enter the input
##You will create a popup box to display the result.

#Abiodun Scott

#converts fahrenheit to celcius
import tkinter
import tkinter.messagebox as box 

class FahrenConverterGUI:
    def __init__(self):
      # Create the main window
        self.main_window = tkinter.Tk()
        #give window title
        self.main_window.title('Fahrenheit to Celcius Converter')

        # Create two frames to group widgets
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #Create the widgets for the top frame.
        self.prompt_label = tkinter.Label(self.top_frame,
                                          text = 'Enter a Fahrenheit temp')
        self.F_entry = tkinter.Entry(self.top_frame,
                                     width = 10)
        
        #Pack the top frame's widgets
        self.prompt_label.pack(side = 'left')
        self.F_entry.pack(side = 'left')
        
        #create widgets for the bottom frame
        self.calc_button = tkinter.Button(self.bottom_frame,
                                          text = 'Calculate',
                                          command = self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text = 'Quit',
                                          command = self.main_window.destroy)
        
        #Pack the bottom frame's widgets
        self.calc_button.pack(side = 'left')
        self.quit_button.pack(side ='left')
      
        # Pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        #Enter the tkinter main loop
        tkinter. mainloop()
        
    def convert(self):
        #get user input for fahrenheit
        F = float(self.F_entry.get())

        #convert F to C
        C = (F-32)/1.8

        #Display the results in an info dialog box
        tkinter.messagebox.showinfo('Results',
                                    str(F) +
                                    ' degrees F is equal to ' +
                                    str(C) + ' degrees C.')
            
#Create an instance of the FahrenConverterGUI class     
temp_converter = FahrenConverterGUI()
