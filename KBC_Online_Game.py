from tkinter import *
from tkinter.ttk import Progressbar
from pygame import mixer
import pyttsx3
from Questions import questions, first_option, second_option, third_option, fourth_option, correct_answers

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

mixer.init()

mixer.music.load('kbc.mp3')
mixer.music.play()


def select(event):
    callButton.place_forget()
    
    progressbarA.place_forget()
    progressbarB.place_forget()
    progressbarC.place_forget()
    progressbarD.place_forget()
    
    progressbarLabelA.place_forget()
    progressbarLabelB.place_forget()
    progressbarLabelC.place_forget()
    progressbarLabelD.place_forget()
    
    
    b = event.widget
    value = b['text']
    
    for i in range(15):
        if value == correct_answers[i]:
            if value == correct_answers[14]:
                
                def close():
                    root2.destroy()
                    root.destroy()
                
                def playagain():
                    lifeline50Button.config(state=NORMAL, image=image50)
                    audiencePoleButton.config(state=NORMAL, image=audiencePole)
                    phoneLifeLineButton.config(state=NORMAL, image=phoneImage)
                    
                    root2.destroy()
                    questionArea.delete(1.0, END)
                    questionArea.insert(END, questions[0])
                    
                    optionButton1.config(text=first_option[0])
                    optionButton2.config(text=second_option[0])
                    optionButton3.config(text=third_option[0])
                    optionButton4.config(text=fourth_option[0])
                    
                    amountLabel.config(image=amountImage)
                    
                mixer.music.load('kbcwon.mp3')
                mixer.music.play()
                root2 = Toplevel()
                root2.overrideredirect(True)
                root2.config(bg='black')
                root2.geometry('500x500+140+30')
                root2.title('You won 0 pounds')
                imgLabel = Label(root2, image=centerImage, bd=0)
                imgLabel.pack(pady=30)
                
                winLabel = Label(root2, text='Congratulations!\nYou Won\n1 Million', font=('arial',30,'bold'), bg='black', fg='white')
                winLabel.pack()
                
                playagainButton = Button(root2, text='Play Again', font=('arial', 20,'bold'), bg='black', fg='white',
                                        activebackground='black', activeforeground='white', bd=0, cursor='hand2',
                                        command=playagain)
                playagainButton.pack()
                
                closeButton = Button(root2, text='Close', font=('arial', 20,'bold'), bg='black', fg='white',
                                        activebackground='black', activeforeground='white', bd=0, cursor='hand2',
                                    command=close)
                closeButton.pack()
                
                happyImage = PhotoImage(file='happy.png')
                happyLabel = Label(root2, image=happyImage, bg='black')
                happyLabel.place(x=30, y=280)
                
                happyLabel1 = Label(root2, image=happyImage, bg='black')
                happyLabel1.place(x=400, y=280)
                
                root2.mainloop()
                break
        
            questionArea.delete(1.0, END)
            questionArea.insert(END, questions[i+1])
                
            optionButton1.config(text=first_option[i+1])
            optionButton2.config(text=second_option[i+1])
            optionButton3.config(text=third_option[i+1])
            optionButton4.config(text=fourth_option[i+1])
            amountLabel.config(image=amountImages[i])
            
        if value not in correct_answers:
            def close():
                root1.destroy()
                root.destroy()
                
            def tryagain():
                lifeline50Button.config(state=NORMAL, image=image50)
                audiencePoleButton.config(state=NORMAL, image=audiencePole)
                phoneLifeLineButton.config(state=NORMAL, image=phoneImage)
                
                root1.destroy()
                questionArea.delete(1.0, END)
                questionArea.insert(END, questions[0])
                
                optionButton1.config(text=first_option[0])
                optionButton2.config(text=second_option[0])
                optionButton3.config(text=third_option[0])
                optionButton4.config(text=fourth_option[0])
                
                amountLabel.config(image=amountImage)
                
            
            root1 = Toplevel()
            root1.overrideredirect(True)
            root1.config(bg='black')
            root1.geometry('500x400+140+30')
            root1.title('You won 0 pounds')
            imgLabel = Label(root1, image=centerImage, bd=0)
            imgLabel.pack(pady=30)
            
            looseLabel = Label(root1, text='You Loose', font=('arial',40,'bold'), bg='black', fg='white')
            looseLabel.pack()
            
            tryagainButton = Button(root1, text='Try Again', font=('arial', 20,'bold'), bg='black', fg='white',
                                    activebackground='black', activeforeground='white', bd=0, cursor='hand2',
                                    command=tryagain)
            tryagainButton.pack()
            
            closeButton = Button(root1, text='Close', font=('arial', 20,'bold'), bg='black', fg='white',
                                    activebackground='black', activeforeground='white', bd=0, cursor='hand2',
                                command=close)
            closeButton.pack()
            
            sadImage = PhotoImage(file='sad.png')
            sadLabel = Label(root1, image=sadImage, bg='black')
            sadLabel.place(x=30, y=280)
            
            sadLabel1 = Label(root1, image=sadImage, bg='black')
            sadLabel1.place(x=400, y=280)
            
            root1.mainloop()
            break
        
        
def lifeline50():
    lifeline50Button.config(image=image50X, state=DISABLED)
    if questionArea.get(1.0, 'end-1c') == questions[0]:
        optionButton1.config(text='')
        optionButton4.config(text='')
        
    if questionArea.get(1.0, 'end-1c') == questions[1]:
        optionButton3.config(text='')
        optionButton4.config(text='')
        
    if questionArea.get(1.0, 'end-1c') == questions[2]:
        optionButton2.config(text='')
        optionButton4.config(text='')
        
    if questionArea.get(1.0, 'end-1c') == questions[3]:
        optionButton1.config(text='')
        optionButton2.config(text='')
        
    if questionArea.get(1.0, 'end-1c') == questions[4]:
        optionButton1.config(text='')
        optionButton3.config(text='')
        
    if questionArea.get(1.0, 'end-1c') == questions[5]:
        optionButton1.config(text='')
        optionButton4.config(text='')
        
    if questionArea.get(1.0, 'end-1c') == questions[6]:
        optionButton1.config(text='')
        optionButton3.config(text='')
        
    if questionArea.get(1.0, 'end-1c') == questions[7]:
        optionButton1.config(text='')
        optionButton3.config(text='')
        
    if questionArea.get(1.0, 'end-1c') == questions[8]:
        optionButton2.config(text='')
        optionButton4.config(text='')
        
    if questionArea.get(1.0, 'end-1c') == questions[9]:
        optionButton1.config(text='')
        optionButton4.config(text='')
    
    if questionArea.get(1.0, 'end-1c') == questions[10]:
        optionButton2.config(text='')
        optionButton4.config(text='')
        
    if questionArea.get(1.0, 'end-1c') == questions[11]:
        optionButton1.config(text='')
        optionButton2.config(text='')
        
    if questionArea.get(1.0, 'end-1c') == questions[12]:
        optionButton2.config(text='')
        optionButton3.config(text='')
        
    if questionArea.get(1.0, 'end-1c') == questions[13]:
        optionButton1.config(text='')
        optionButton4.config(text='')
        
    if questionArea.get(1.0, 'end-1c') == questions[14]:
        optionButton3.config(text='')
        optionButton4.config(text='')
        
def audiencePoleLifeline():
    audiencePoleButton.config(image=audiencePoleX, state=DISABLED)
    progressbarA.place(x=580, y=190)
    progressbarB.place(x=620, y=190)
    progressbarC.place(x=660, y=190)
    progressbarD.place(x=700, y=190)
    
    progressbarLabelA.place(x=580, y=320)
    progressbarLabelB.place(x=620, y=320)
    progressbarLabelC.place(x=660, y=320)
    progressbarLabelD.place(x=700, y=320)
    
    if questionArea.get(1.0, 'end-1c') == questions[0]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=90)
        progressbarD.config(value=20)
        
    if questionArea.get(1.0, 'end-1c') == questions[1]:
        progressbarA.config(value=60)
        progressbarB.config(value=85)
        progressbarC.config(value=20)
        progressbarD.config(value=65)
        
    if questionArea.get(1.0, 'end-1c') == questions[2]:
        progressbarA.config(value=85)
        progressbarB.config(value=58)
        progressbarC.config(value=50)
        progressbarD.config(value=20)
        
    if questionArea.get(1.0, 'end-1c') == questions[3]:
        progressbarA.config(value=45)
        progressbarB.config(value=30)
        progressbarC.config(value=90)
        progressbarD.config(value=20)
        
    if questionArea.get(1.0, 'end-1c') == questions[4]:
        progressbarA.config(value=10)
        progressbarB.config(value=30)
        progressbarC.config(value=50)
        progressbarD.config(value=85)
        
    if questionArea.get(1.0, 'end-1c') == questions[5]:
        progressbarA.config(value=35)
        progressbarB.config(value=90)
        progressbarC.config(value=30)
        progressbarD.config(value=20)
        
    if questionArea.get(1.0, 'end-1c') == questions[6]:
        progressbarA.config(value=20)
        progressbarB.config(value=90)
        progressbarC.config(value=30)
        progressbarD.config(value=50)
        
    if questionArea.get(1.0, 'end-1c') == questions[7]:
        progressbarA.config(value=20)
        progressbarB.config(value=50)
        progressbarC.config(value=50)
        progressbarD.config(value=90)
        
    if questionArea.get(1.0, 'end-1c') == questions[8]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=90)
        progressbarD.config(value=20)
        
    if questionArea.get(1.0, 'end-1c') == questions[9]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=90)
        progressbarD.config(value=20)
        
    if questionArea.get(1.0, 'end-1c') == questions[10]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=90)
        progressbarD.config(value=20)
        
    if questionArea.get(1.0, 'end-1c') == questions[11]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=90)
        progressbarD.config(value=20)
        
    if questionArea.get(1.0, 'end-1c') == questions[12]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=20)
        progressbarD.config(value=90)
        
    if questionArea.get(1.0, 'end-1c') == questions[13]:
        progressbarA.config(value=90)
        progressbarB.config(value=50)
        progressbarC.config(value=30)
        progressbarD.config(value=20)
        
    if questionArea.get(1.0, 'end-1c') == questions[14]:
        progressbarA.config(value=10)
        progressbarB.config(value=90)
        progressbarC.config(value=40)
        progressbarD.config(value=20)
        
def phoneLifeline():
    mixer.music.load('calling.mp3')
    mixer.music.play()
    callButton.place(x=70, y=260)
    phoneLifeLineButton.config(image=phoneImageX, state=DISABLED)
          
def phoneclick():
    for i in range(15):
        if questionArea.get(1.0, 'end-1c') == questions[i]:
            engine.say(f'The answer is {correct_answers[i]}')
            engine.runAndWait()


root = Tk()

root.geometry('1290x700+120+55')
root.title('Who wants to be a Millionaire')

root.config(bg='black')

'''Left Frame of Page'''

leftframe = Frame(root, bg='black', padx=90)
leftframe.grid(row=0, column=0)

topFrame = Frame(leftframe, bg='black', pady=15)
topFrame.grid(row=0, column=0)

centerFrame = Frame(leftframe, bg='black', pady=15)
centerFrame.grid(row=1, column=0)

bottomFrame = Frame(leftframe)
bottomFrame.grid(row=2, column=0)

'''Right Frame of Page'''

rightframe = Frame(root, pady=15, padx=50, bg='black')
rightframe.grid(row=0, column=1)

''''Images In Left'''

image50 = PhotoImage(file='50-50.png')
image50X = PhotoImage(file='50-50-X.png')

lifeline50Button = Button(topFrame, image=image50, bg='black', bd=0, activebackground='black', width=180, height=80,
                          command=lifeline50)
lifeline50Button.grid(row=0, column=0)

audiencePole = PhotoImage(file='audiencePole.png')
audiencePoleX = PhotoImage(file='audiencePoleX.png')
audiencePoleButton = Button(topFrame, image=audiencePole, bg='black', bd=0, activebackground='black', width=180, height=80,
                            command=audiencePoleLifeline)
audiencePoleButton.grid(row=0, column=1)

phoneImage = PhotoImage(file='phoneAFriend.png')
phoneImageX = PhotoImage(file='phoneAFriendX.png')
phoneLifeLineButton = Button(topFrame, image=phoneImage, bg='black', bd=0, activebackground='black', width=180, height=80,
                             command=phoneLifeline)
phoneLifeLineButton.grid(row=0, column=2)

callimage = PhotoImage(file='phone.png')
callButton = Button(root, image=callimage, bd=0, bg='black', activebackground='black', cursor='hand2',
                    command=phoneclick)

centerImage = PhotoImage(file='center.png')
logoLabel = Label(centerFrame, image=centerImage, bg='black', width=300, height=200)
logoLabel.grid(row=0, column=0)

layoutImage = PhotoImage(file='lay.png')
layoutLabel = Label(bottomFrame, image=layoutImage, bg='black')
layoutLabel.grid(row=0, column=0)

# Question Area
questionArea= Text(bottomFrame, font=('arial',18,'bold'), width=34, height=2, wrap='word', bg='black', fg='white', bd=0)
questionArea.place(x=70, y=10)

questionArea.insert(END, questions[0])

# Options
# A
labelA = Label(bottomFrame, text='A:', bg='black', fg='white', font=('arial',16,'bold'))
labelA.place(x=60, y=110)

optionButton1 = Button(bottomFrame, text=first_option[0], font=('arial',18,'bold'), bg='black', fg='white', bd=0, activebackground='black', activeforeground='white', cursor='hand2')
optionButton1.place(x=100, y=100)
# B
labelB = Label(bottomFrame, text='B:', bg='black', fg='white', font=('arial',16,'bold'))
labelB.place(x=330, y=110)

optionButton2 = Button(bottomFrame, text=second_option[0], font=('arial',18,'bold'), bg='black', fg='white', bd=0, activebackground='black', activeforeground='white', cursor='hand2')
optionButton2.place(x=370, y=100)
# C
labelC = Label(bottomFrame, text='C:', bg='black', fg='white', font=('arial',16,'bold'))
labelC.place(x=60, y=190)

optionButton3 = Button(bottomFrame, text=third_option[0], font=('arial',18,'bold'), bg='black', fg='white', bd=0, activebackground='black', activeforeground='white', cursor='hand2')
optionButton3.place(x=100, y=180)
# D
labelD = Label(bottomFrame, text='D:', bg='black', fg='white', font=('arial',16,'bold'))
labelD.place(x=330, y=190)

optionButton4 = Button(bottomFrame, text=fourth_option[0], font=('arial',18,'bold'), bg='black', fg='white', bd=0, activebackground='black', activeforeground='white', cursor='hand2')
optionButton4.place(x=370, y=180)

progressbarA = Progressbar(root, orient=VERTICAL, length=120)
progressbarB = Progressbar(root, orient=VERTICAL, length=120)
progressbarC = Progressbar(root, orient=VERTICAL, length=120)
progressbarD = Progressbar(root, orient=VERTICAL, length=120)

progressbarLabelA = Label(root, text='A', font=('arial',20,'bold'), bg='black', fg='white')
progressbarLabelB = Label(root, text='B', font=('arial',20,'bold'), bg='black', fg='white')
progressbarLabelC = Label(root, text='C', font=('arial',20,'bold'), bg='black', fg='white')
progressbarLabelD = Label(root, text='D', font=('arial',20,'bold'), bg='black', fg='white')



optionButton1.bind('<Button-1>',select)
optionButton2.bind('<Button-1>',select)
optionButton3.bind('<Button-1>',select)
optionButton4.bind('<Button-1>',select)


'''Images In Right'''
amountImage = PhotoImage(file='Picture0.png')
amountImage1 = PhotoImage(file='Picture1.png')
amountImage2 = PhotoImage(file='Picture2.png')
amountImage3 = PhotoImage(file='Picture3.png')
amountImage4 = PhotoImage(file='Picture4.png')
amountImage5 = PhotoImage(file='Picture5.png')
amountImage6 = PhotoImage(file='Picture6.png')
amountImage7 = PhotoImage(file='Picture7.png')
amountImage8 = PhotoImage(file='Picture8.png')
amountImage9 = PhotoImage(file='Picture9.png')
amountImage10 = PhotoImage(file='Picture10.png')
amountImage11 = PhotoImage(file='Picture11.png')
amountImage12 = PhotoImage(file='Picture12.png')
amountImage13 = PhotoImage(file='Picture13.png')
amountImage14 = PhotoImage(file='Picture14.png')
amountImage15 = PhotoImage(file='Picture15.png')

amountImages = [amountImage1, amountImage2, amountImage3, amountImage4, amountImage5, amountImage6, amountImage7,
                amountImage8, amountImage9, amountImage10, amountImage11, amountImage12, amountImage13, amountImage14, amountImage15]

amountLabel = Label(rightframe, image=amountImage, bg='black')
amountLabel.grid(row=0, column=0)



root.mainloop()
