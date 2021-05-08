import tkinter as tk
import tkinter.messagebox as messagebox
import pickle

buttons = []
window = tk.Tk()
window.geometry("341x300")
window.resizable(False,False)
window.title("Multiple Message Clipboard")

container = tk.Frame(window)
canvas = tk.Canvas(container,width=318)
scrollbar = tk.Scrollbar(container,orient="vertical",command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.create_window((0,0), window=scrollable_frame, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)

class Button():
    def __init__(self,name,output):
        self.name = name
        self.output = output
        buttons.append(self)
        self.UI = {}

    def copyButton(self):
        window.clipboard_clear()
        window.clipboard_append(self.output)

    def displayButton(self,row):
        self.UI["buttonName"] = tk.Label(scrollable_frame,text=self.name,width=19)
        self.UI["buttonOutput"] = tk.Button(scrollable_frame,text=self.name,command=self.copyButton,width=20)
        self.UI["buttonDelete"] = tk.Button(scrollable_frame,text="X",command=self.deleteButton,width=1)
        self.UI["buttonDelete"].grid(column=1,row=row)
        self.UI["buttonName"].grid(column=2,row=row)
        self.UI["buttonOutput"].grid(column=3,row=row)

    def clearButton(self):
        try:
            self.UI["buttonDelete"].destroy()
            self.UI["buttonName"].destroy()
            self.UI["buttonOutput"].destroy()
        except:
            pass
        
    def deleteButton(self):
        answer = messagebox.askokcancel(message=f"Delete Message {self.name}")
        if answer:
            buttons.pop(buttons.index(self))
            self.clearButton()

class newButtonUI():
    def __init__(self):
        self.subWindow = tk.Tk()
        self.subWindow.title("New Message: ")
        self.subWindow.geometry("290x230")
        self.nameLabel = tk.Label(self.subWindow,text="Name: ")
        self.nameEntry = tk.Text(self.subWindow,width=25,height=1)
        
        self.outputLabel = tk.Label(self.subWindow,text="Output: ")
        self.outputEntry = tk.Text(self.subWindow,width=25,height=10)

        self.submitButton = tk.Button(self.subWindow,text="Submit",command=self.submit)
        self.clearButton = tk.Button(self.subWindow,text="Cancel",command=self.cancel)

        self.nameLabel.place(x=0,y=5)
        self.nameEntry.place(x=75,y=5)
        self.outputLabel.place(x=0,y=25)
        self.outputEntry.place(x=75,y=25)
        self.submitButton.place(x=65,y=200)
        self.clearButton.place(x=165,y=200)
        
    def cancel(self):
        print(self.subWindow.geometry())
        self.subWindow.destroy()
        
    def submit(self):
        name = self.nameEntry.get("1.0","end-1c")
        output = self.outputEntry.get("1.0", "end-1c")
        if name and output:
            newButton = Button(name,output)
            newButton.displayButton(len(buttons)+1)
        self.subWindow.destroy()
        
try:
    buttons = pickle.load(open("customButtons.p","rb"))
except Exception as e:
    print(e)

addButton = tk.Button(window,text="Add New",command=newButtonUI)
addButton.pack()
searchData = tk.StringVar()
searchLabel = tk.Label(window,text="Search: ",width=22)
searchEntry = tk.Entry(window,textvariable=searchData,width=24)
searchLabel.pack()
searchEntry.pack()

def on_closing():
    saveButtons = []
    for item in buttons:
        item.UI = {}
        saveButtons.append(item)
    pickle.dump(saveButtons,open("customButtons.p","wb"))
    window.destroy()

def searchButtons():
    filteredButtons = []
    for button in buttons:
        if searchData.get().lower() in button.name.lower():
            filteredButtons.append(button)
    return filteredButtons

def listButtons():
    for button in buttons:
        button.clearButton()
    row = 1
    for button in searchButtons():
        button.displayButton(row)   
        row += 1

searchData.trace("w", lambda name, index, mode, searchData=searchData: listButtons())

container.pack()
canvas.pack(side="left")
scrollbar.pack(side="left",fill="y")

listButtons()

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
