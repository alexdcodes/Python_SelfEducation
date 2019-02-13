from Tkinter import *
import ping


class Main:
    LABEL_TEXT = [
        """GREETING Application
        Just making sure everything is running smoothly. 
        """,
    ]
    INSTRUCTION_TEXT = [
        """
          -------------------------------------------
        THIS IS INSTRUCTIONS FOR THE APPLICATION
        first BUTTON prints text to text box, second also prints to text box, 
        third closes the program, currently the program wont run network tests 
        unless root on MAC OSX, All other operating systems work (Windows/Linux)! 
          -------------------------------------------
        """,
    ]
    DATA_TEXT = [
        """DATA  
        """
    ]

    def __init__(self, master):
        self.master = master
        master.title("AlexDCodes: Simple Application")

        self.label_index = 0
        self.label_text = StringVar()
        self.label_text.set(self.LABEL_TEXT[self.label_index])
        self.label = Label(master, textvariable=self.label_text, bg="gray")
        self.label.pack()
        Label(None, text='Welcome Button', fg='black', bg='gray', font='Helvetica 16 bold').pack()
        self.greet_button = Button(master, text="Greet", fg="black", highlightbackground='gray', command=self.greet)
        self.greet_button.pack()
        Label(None, text='Network Ping Test', fg='black', bg='gray', font='Helvetica 16 bold').pack()
        self.close_button = Button(master, text="Sup  ", fg="black", highlightbackground='gray', command=self.network_test)
        self.close_button.pack()
        Label(None, text='Data Dump', fg='black', bg='gray', font='Helvetica 16 bold').pack()
        self.close_button = Button(master, text="Sup  ", fg="black", highlightbackground='gray', command=self.data_dump)
        self.close_button.pack()
        Label(None, text='Quit/Exit', fg='black', bg='gray', font='Helvetica 16 bold').pack()
        self.close_button = Button(master, text="Close", fg="black", highlightbackground='gray', command=master.quit)
        self.close_button.pack()
        self.label_text = StringVar()
        self.label_text.set(self.INSTRUCTION_TEXT[self.label_index])
        self.label = Label(master, textvariable=self.label_text, bg="gray")
        self.label.pack()
        self.label_text = StringVar()
        self.label_text.set(self.DATA_TEXT[self.label_index])
        self.label = Label(master, textvariable=self.label_text, bg="gray", font='Helvetica 18 bold')
        self.label.pack()

    def greet(self):
        print("Greetings! 0xFB100, This is just a quick test.")
        T.insert(END, "DATA_DUMP_::GREETINGS: -- Success!..")

    def data_dump(self):
        print("""Hello, Our Program is Printing to Console..
        0xFB40: This is a long message as we want to enter in lots of data here.
        """)
        T.insert(END, "DATA_DUMP_::0xFKB400__: -- Success! ..")

    def network_test(self):
        print("Network Test\n")
        T.insert(END, ping.verbose_ping('www.google.com', count=3))

    def cycle_label_text(self, event):
        self.label_index += 1
        self.label_index %= len(self.LABEL_TEXT) # wrap around
        self.label_text.set(self.LABEL_TEXT[self.label_index])


root = Tk()
root.geometry('600x600')
root["bg"] = "gray"
my_gui = Main(root)
T = Text(root, height=9, width=80, fg="green", bg="black", font='Helvetica 10')
T.pack()
T.insert(END, "  ")
root.mainloop()