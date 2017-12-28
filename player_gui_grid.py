"""
Module to create a GUI based interface to manage Player

Provides options to manage player
- create new player
- view player details
- delete players

"""
from tkinter import *
from tkinter import messagebox
from players import Player
# from PIL import Image, ImageTk

class App:
    def __init__(self, master):
        self.frame = Frame(master, height=300, width=500, borderwidth=10, relief=SUNKEN)  # Simple container to hold other widgets,
        # Padding between other widgets. Compound widgets.
        # Use Frame.config() --> give you all options available with Frame
        self.frame.grid()
        self.player_fields_display()

        #self.button = Button(frame, text="Create Player", command=Player().add_player('VIVAAN Frame', 1, 'M', ["631 E Royal Lane", "Irving", "Texas"]))
        #self.button.pack()

    def player_fields_display(self):

        # image = Image.open("foxyfib.jpg")
        # photo = ImageTk.PhotoImage(image,size=(20,20))
        # Label(self.frame, image=photo).grid(row=0, column=2)

        player_fields = ["Player Name", "Player Age ", "Player Gender",  "Player Street",
                           "Player City", "Player State"]
        for r in range(len(player_fields)):
            Label(self.frame, text=player_fields[r]).grid(row=r,sticky=W)  # grid --> row, column, sticky=NSEW, columnspan, rowspan, padx,pady,ipadx,ipady

        self.entry_cname = Entry(self.frame)
        self.entry_cname.grid(row=0,column=1)
        self.entry_cage = Entry(self.frame)
        self.entry_cage.grid(row=1,column=1)

        self.value = IntVar()
        Radiobutton(self.frame,text="F", variable=self.value, value=1).grid(row=2,column=1,sticky=W,padx=10)
        Radiobutton(self.frame, text="M", variable=self.value, value=2).grid(row=2,column=1,padx=60)

        self.entry_caddress1 = Entry(self.frame)
        self.entry_caddress1.grid(row=3,column=1)
        self.entry_caddress2 = Entry(self.frame)
        self.entry_caddress2.grid(row=4,column=1)
        self.entry_caddress3 = Entry(self.frame)
        self.entry_caddress3.grid(row=5,column=1)

        self.button_test = Button(self.frame, text="TEST ME")
        self.button_test.bind("<Button-1>", self.turn_red)
        self.button_test.grid(row=6,column=1)

        self.button_create_player = Button(self.frame, foreground="green", background="yellow", text="Create Player", width=15, command=None)
        self.button_create_player.grid(row=7,column=1)
        self.button_create_player.bind("<Button-1>", self.player_create)
        self.button_quit = Button(self.frame, foreground="red", background="yellow", text="QUIT", width=15, command=self.frame.quit)
        self.button_quit.grid(row=7, column=2)

    def player_fields_read(self):

        self.cname = StringVar()
        self.cname.set("Enter Player Name")
        self.entry_cname["textvariable"] =  self.cname
        #self.cname = self.entry_cname.get() # returns the content as string
        #print("Cname is " + self.cname)
        #cage = self.entry_cage.get()
        #cgender = self.entry_cgender.get()
        #caddress = [self.entry_caddress1.get(),self.entry_caddress2.get(),self.entry_caddress3.get()]

    def turn_red(self, event):
        event.widget["activeforeground"] = "red"

    def player_create(self,event):

        self.show_confirmation("New Player")
        gender = 'F' if self.value==1 else 'M'
        address = format(self.entry_caddress1.get()+" "+self.entry_caddress2.get()+" "+self.entry_caddress3.get())

        response = Player(name=self.entry_cname.get(), age=int(self.entry_cage.get()), gender=gender, address=address).add_player()
        self.show_message(__name__, response[1])

    def show_message(self,title, message):
        messagebox.showinfo(title, message)

    def show_confirmation(self, title):
        messagebox.askyesno(title, "Would you like to save data?")

if __name__=='__main__' :
    root = Tk()
    root.title("PLAYER MANAGEMENT")
    app = App(root)
    #app.player_fields_read()
    root.mainloop()
    root.destroy()  # Other environments may misbehave if you leave out the explicit destroy call