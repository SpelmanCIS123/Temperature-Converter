##BROOKLYN NEAL

##FAHRENHEIT TO CELSIUS CONVERTER

#Your code goes here
import tkinter
import tkinter.messagebox as box 

class FahrenConverterGUI:
    def __init__(self):
      # Create the main window
        self.main_window = tkinter.Tk()

        # Create two frames to group widgets
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #Create widgets for the top frame
        self.prompt_label = tkinter.Label(self.top_frame,
                                          text = 'Enter a temperature in fahrenheit:')
        self.ftemp_entry = tkinter.Entry(self.top_frame,
                                       width = 10)
        #Pack the top frame's widgets
        self.prompt_label.pack(side = 'left')
        self.ftemp_entry.pack(side = 'left')
        
        #Create widgets for the bottom frame
        self.calc_button = tkinter.Button(self.bottom_frame,
                                          text = 'Calculate',
                                          command = self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)
        
        #Pack the buttons
        self.calc_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')
      
        # Pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        #Enter the tkinter main loop
        tkinter. mainloop()

    #The convert method is a callback function for the Calculate button
    def convert(self):
        #Get the value entered by the user into the ftemp_entry widget
        ftemp = float(self.ftemp_entry.get())

        #Convert fahrenheit to celsius
        celsius = (int(ftemp) - 32) * (5/9)

        #Display the results in an info dialog box
        tkinter.messagebox.showinfo('Results',
                                 str(ftemp) +
                                 ' temperature in fahrenhet is equal to ' +
                                 str(celsius) + ' temperature in celsius.')


#Create an instance of the TemperatureConverterGUI class
temp_converter = FahrenConverterGUI()
