from tkinter import *
# from temperature import Temperature

## Temperature Calculator ###############################################################
def Temperature():
    tempForm = Tk()
    inp = StringVar()
    temp = StringVar()

    tempForm.title("Welcome to Temperature Convertor")
    label = Label(tempForm, text="Temperature")
    label.config(font=("Courier", 50))
    label.grid(columnspan=3)

    Entry(tempForm, textvariable=inp).grid(row=1, column=0)
    Entry(tempForm, textvariable=temp, state="readonly").grid(row=1, column=2)

    def fToc():
        if (inp.get().isnumeric()):
            t = 5 * (float(inp.get()) - 32) / 9
            t = round(t, 2)
            temp.set(t)
            formula = f'({inp.get()}°F * 5 - 32) / 9 = {t}°C'
            label.config(text=f"Formula: {formula}")

    def fTok():
        if (inp.get().isnumeric()):
            t = (float(inp.get()) - 32) * 5/9 + 273.15
            t = round(t, 2)
            temp.set(t)
            formula = f'({inp.get()}°F - 32) * 5/9 + 273.15 = {t}K'
            label.config(text=f"Formula: {formula}")

    def cTof():
        if (inp.get().isnumeric()):
            t = (float(inp.get()) * 9/5 ) + 32
            t = round(t, 2)
            temp.set(t)
            formula = f'({inp.get()}°C * 9/5) + 32 = {t}°F'
            label.config(text=f"Formula: {formula}")
            
    def cTok():
        if (inp.get().isnumeric()):
            t = (float(inp.get()) + 273.15)
            t = round(t, 2)
            temp.set(t)
            formula = f'{inp.get()}°C + 273.15 = {t}K'
            label.config(text=f"Formula: {formula}")

    def kToc():
        if (inp.get().isnumeric()):
            t = (float(inp.get()) - 273.15)
            t = round(t, 2)
            temp.set(t)
            formula = f'{inp.get()}K - 273.15 = {t}°C'
            label.config(text=f"Formula: {formula}")

    def kTof():
        if (inp.get().isnumeric()):
            t = (float(inp.get()) - 273.15) * 9/5 + 32
            t = round(t, 2)
            temp.set(t)
            formula = f'({inp.get()}K - 273.15) * 9/5 + 32 = {t}°F'
            label.config(text=f"Formula: {formula}")

    def sTos(S):
        t= str("{:.2f}".format(float(inp.get())))
        temp.set(t)
        formula = f'{inp.get()}{S} = {t}{S}'
        label.config(text=f"Formula: {formula}")

    def C1():
        mb1.config(text="Celsius")
        if (mb2.cget("text") == "Celsius"):
            sTos('°C')
        elif (mb2.cget("text") == "Fahrenheit"):
            cTof()
        elif (mb2.cget("text") == "Kelvin"):
            cTok()


    def F1():
        mb1.config(text="Fahrenheit")
        if (mb2.cget("text") == "Celsius"):
            fToc()
        elif (mb2.cget("text") == "Fahrenheit"):
            sTos('°F')
        elif (mb2.cget("text") == "Kelvin"):
            fTok()


    def K1():
        mb1.config(text="Kelvin")
        if (mb2.cget("text") == "Celsius"):
            kToc()
        elif (mb2.cget("text") == "Fahrenheit"):
            kTof()
        elif (mb2.cget("text") == "Kelvin"):
            sTos('K')


    def C2():
        mb2.config(text="Celsius")
        if (mb1.cget("text") == "Kelvin"):
            kToc()
        elif (mb1.cget("text") == "Fahrenheit"):
            fToc()
        elif (mb1.cget("text") == "Celsius"):
            sTos('°C')

    def F2():
        mb2.config(text="Fahrenheit")
        if (mb1.cget("text") == "Celsius"):
            cTof()
        elif (mb1.cget("text") == "Fahrenheit"):
            sTos('°F')
        elif (mb1.cget("text") == "Kelvin"):
            kTof()


    def K2():
        mb2.config(text="Kelvin")
        if (mb1.cget("text") == "Celsius"):
            cTok()
        elif (mb1.cget("text") == "Kelvin"):
            sTos('K')
        elif (mb1.cget("text") == "Fahrenheit"):
            fTok()

    mb1 = Menubutton(tempForm, text="select")
    mb1.grid(row=2, column=0)
    mb1.menu = Menu(mb1, tearoff=0)
    mb1["menu"] = mb1.menu
    mb1.menu.add_command(label="Celsius", command=C1)
    mb1.menu.add_command(label="Fahrenheit", command=F1)
    mb1.menu.add_command(label="Kelvin", command=K1)
    mb1.grid()

    Label(tempForm, text="=").grid(row=1, column=1)

    mb2 = Menubutton(tempForm, text="select")
    mb2.grid(row=2, column=2)
    mb2.menu = Menu(mb2, tearoff=0)
    mb2["menu"] = mb2.menu
    mb2.menu.add_command(label="Celsius", command=C2)
    mb2.menu.add_command(label="Fahrenheit", command=F2)
    mb2.menu.add_command(label="Kelvin", command=K2)
    mb2.grid()

    label = Label(tempForm, text="Formula: ")
    label.grid(columnspan=3, sticky=W, pady=10, padx=10)

#########################################################################################







## Intially Step is not cleared. #########################################################
try:
    is_step1_clear == True
except:
    is_step1_clear = False
    is_step2_clear = False
    is_step3_clear = False
##########################################################################################



## For taking input from Text Box#########################################################
def retrieve_input():
    input = T.get("1.0",END)    
    if (input[:4] == 'Open') and is_step1_clear and is_step2_clear and is_step3_clear:
        master.destroy()
        hint.config(text="Congrats, Now you can use Temperature calculator")
        Temperature()
    else:
        master.destroy()
        hint.config(text="You can't use Calculator")
##########################################################################################


## If steps cleared. Change hintbox ######################################################
def step1():
    hint.config(text='Now, Select both check box')
    global is_step1_clear
    is_step1_clear = True

def check_step2():
    if is_step2_clear and is_step3_clear:
        hint.config(text="Now write 'Open' in text box and click 'Done' button.")

def step2():
    global is_step2_clear
    is_step2_clear = True
    check_step2()

def step3():
    global is_step3_clear
    is_step3_clear = True
    check_step2()
###########################################################################################



## Creating 2 Screen ######################################################################
master = Tk()
hintBox = Tk()
master.title("Security Shield")
hintBox.title("Hint Box")
###########################################################################################


## HintBox Label###########################################################################
hint = Label(hintBox, text='Select option 2 only')
hint.config(font=("Courier", 30))
hint.grid()
###########################################################################################


## Final Button ###########################################################################
button = Button(master, text="Done", command=retrieve_input, relief='solid', bd=3)
button.config(font=("Courier", 20))
button.grid(row=0, column=0, padx = 40)
###########################################################################################

## Security Label #########################################################################
w = Label(master, text='Security')
w.config(font=("Courier", 30))
w.grid(row=0, column=1, sticky=E, pady = 40)
###########################################################################################

## Option Box #############################################################################
frame1 = Frame(master, relief='solid', bd=1)
frame1.grid(row=1, column=0, padx = 40, pady = 40, ipadx=25, sticky=E)
var = IntVar()
Radiobutton(frame1, text='Option1', variable=var, value=1).grid(row=0, column=0, sticky = W, pady = 10)
Radiobutton(frame1, text='Option2', variable=var, value=2, command=step1).grid(row=1, column=0, sticky = W, pady = 10)
Radiobutton(frame1, text='Option3', variable=var, value=3).grid(row=2, column=0, sticky = W, pady = 10)
############################################################################################

## Check Box ###############################################################################
frame2 = Frame(master, relief='solid', bd=1)
frame2.grid(row=1, column=1, padx = 40, pady = 40, ipadx=25, sticky=SE)
var1 = IntVar()
Checkbutton(frame2, text='Check1', variable=var1, command=step2).grid(row=0, column=1, pady = 10, sticky = W)
var2 = IntVar()
Checkbutton(frame2, text='Check2', variable=var2, command=step3).grid(row=1, column=1, pady = 10, sticky = W)
#############################################################################################

## Password input ###########################################################################
T = Text(master, height=3, width=20)
T.grid(row=1, column=2, padx=25, pady=5, sticky = W, rowspan = 3)
T.insert(END, '')
#############################################################################################


mainloop()





