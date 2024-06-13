import customtkinter as ctk

root = ctk.CTk()
root.title("Algebra Learning Program")
root.geometry("1000x600")



#Define settings button
def settingsPress():
    print("SETTINGS BUTTON TEST") # Test that the button works - will be useful later
    
    #Create "window" (frame) for settings
    settingsWindow = ctk.CTkFrame(root)
    settingsWindow.place(x=0, y=0, relwidth=1, relheight=1)



    #Dropdown boxes in settings

    #Background colour dropdown box    

    def Appearance(selection):
        choice_index = themes.index(optionmenu_2.get())
        if choice_index == 0 :
            ctk.set_appearance_mode("light")
        elif choice_index == 1:
            ctk.set_appearance_mode("dark")
        elif choice_index == 2:
            ctk.set_appearance_mode("system")

    themes = ["Light", "Dark", "System"]
    optionmenu_2 = ctk.CTkOptionMenu(settingsWindow, values=themes, command=Appearance)
    optionmenu_2.place(anchor="center", relx=0.25, rely=0.45)
    optionmenu_2.set("System")
    current_theme = ctk.get_appearance_mode()


     #Text colour dropdown box    
    def textcolourdpPress(choice):
        print("DROPDOWN TC COLOUR PRESSED: ",choice) # Test that the button works - will be useful later

    textcolourDP = ctk.CTkOptionMenu(settingsWindow, values=["White", "Black", "Yellow", "Pink", "Green"], command = textcolourdpPress)
    textcolourDP.set("White")
    textcolourDP.place(anchor="center", relx=0.45, rely=0.45)
 

    def scalesizedPress(selection):
        scale = int(selection.strip('%')) / 100
        ctk.set_widget_scaling(scale)
        if selection == "125%":
            root.geometry("1200x900")
        elif selection == "100%":
            root.geometry("1000x600")
        elif selection == "150%":
            root.geometry("1360x1000")
        elif selection == "75%":
            root.geometry("800x500")
        elif selection == "50%":
            root.geometry("500x350")

    scalesizeDP = ctk.CTkOptionMenu(settingsWindow, values=["50%", "75%", "100%", "125%", "150%"], command=scalesizedPress)
    scalesizeDP.place(anchor="center", relx=0.65, rely=0.45)
    scalesizeDP.set("100%")

     #Text labels for dropdown boxes in settings

     #Background colour DP text label
    BGDPtext = ctk.CTkLabel(settingsWindow, text=("Background colour"))
    BGDPtext.place(anchor="center", relx=0.25, rely=0.35)

     #Text colour DP text label
    TCDPtext = ctk.CTkLabel(settingsWindow, text=("Text colour"))
    TCDPtext.place(anchor="center", relx=0.45, rely=0.35)

     #Size scale DP text label
    SSDPtext = ctk.CTkLabel(settingsWindow, text=("Size (scale)"))
    SSDPtext.place(anchor="center", relx=0.65, rely=0.35)



     #Go back button for the settings
    def gobackPress():
        print("GO BACK TEST - SETTINGS")
        settingsWindow.destroy()

    gobackbutton = ctk.CTkButton(settingsWindow, text="Go Back", command=gobackPress)
    gobackbutton.place(x=15, y=15)



# Define lesson button
def lessonPress():
    print("LESSON BUTTON TEST") # Test that the button works - will be useful later

    # Create frame for lesson
    lessonWindow = ctk.CTkFrame(root)
    lessonWindow.place(x=0, y=0, relwidth=1, relheight=1)

    # Create text for lesson frame
    textTopLesson = ctk.CTkLabel(lessonWindow, text="Algebra is the manipulation of equations to find an unkown variable\nTake this equation as an example\n2x - 5 = 5")
    textTopLesson.place(anchor="center", relx=0.5, rely=0.3)

    textMiddleLesson = ctk.CTkLabel(lessonWindow, text="The first step in solving algebra is moving the all the x's to one side (in this case just the one), and all the numbers to the other.\nThis looks like this:\n2x - 5 + 5 = 5 + 5\n2x = 10")
    textMiddleLesson.place(anchor="center", relx=0.5, rely=0.5)

    textBottomLesson = ctk.CTkLabel(lessonWindow, text="After this is done you should be left with just x on one side and numbers on the other. Now you solve for x by doing the remaining simplification if necessary:\n2x/2 = 10/x\nx = 5")
    textBottomLesson.place(anchor="center", relx=0.5, rely=0.7)



    # Go back button for the lesson
    def gobackPress():
        print("GO BACK TEST - LESSON")
        lessonWindow.destroy()

    gobackbutton = ctk.CTkButton(lessonWindow, text="Go Back", command=gobackPress)
    gobackbutton.place(x=15, y=15)

    

# Define start button
def startPress():
    print("START BUTTON TEST") # Test that the button works - will be useful later

    # Create frame 
    global quizQ1Window
    quizQ1Window = ctk.CTkFrame(root)
    quizQ1Window.place(x=0, y=0, relwidth=1, relheight=1)

    def wrongAnswer1():
        print("WRONG ANSWER WAS SELECTED")
        quizQ1Window.destroy()
        Answerincorrect1 = ctk.CTkFrame(root)
        Answerincorrect1.place(x=0, y=0, relwidth=1, relheight=1)

        wrongAnswer1text = ctk.CTkLabel(Answerincorrect1, text="Wrong answer was selected")
        wrongAnswer1text.place(anchor="center", relx=0.5, rely=0.4)

        def wrongAnswer1continue():
            Answerincorrect1.destroy()

        wrongAnswer1continue = ctk.CTkButton(Answerincorrect1, text="Continue", command=wrongAnswer1continue)
        wrongAnswer1continue.place(anchor="center", relx=0.5, rely=0.8)

    def correctAnswer1():
        print("CORRECT ANSWER WAS SELECTED")
        quizQ1Window.destroy()
        Answercorrect1 = ctk.CTkFrame(root)
        Answercorrect1.place(x=0, y=0, relwidth=1, relheight=1)

        wrongAnswer1text = ctk.CTkLabel(Answercorrect1, text="Correct answer was selected")
        wrongAnswer1text.place(anchor="center", relx=0.5, rely=0.4)

        def wrongAnswer1continue():
            Answercorrect1.destroy()
            startPress2()  # Start the Q2

        wrongAnswer1continue = ctk.CTkButton(Answercorrect1, text="Continue", command=wrongAnswer1continue)
        wrongAnswer1continue.place(anchor="center", relx=0.5, rely=0.8)

    # Go back button for the quiz 
    def gobackPress():
        print("GO BACK TEST - QUIZ")
        quizQ1Window.destroy()

    # Buttons and labels in the frame
    # Create go back button
    gobackbutton = ctk.CTkButton(quizQ1Window, text="Go Back to main menu", command=gobackPress)
    gobackbutton.place(x=15, y=15)

    # Create question 1
    textQuestion1 = ctk.CTkLabel(quizQ1Window, text="5x + 7 = 17")
    textQuestion1.place(anchor="center", relx=0.5, rely=0.35)

    # Create question 1 answer text
    textQAnswer1 = ctk.CTkLabel(quizQ1Window, text="What is the answer?\nSelect the correct answer")
    textQAnswer1.place(anchor="center", relx=0.5, rely=0.45)

    # 1 wrong
    Q1A1btn = ctk.CTkButton(quizQ1Window, text="x = 8", command=wrongAnswer1)
    Q1A1btn.place(anchor="center", relx=0.2, rely=0.7)

    # 1 right
    Q1A1btn = ctk.CTkButton(quizQ1Window, text="x = 2", command=correctAnswer1)
    Q1A1btn.place(anchor="center", relx=0.4, rely=0.7)

    # 1 wrong
    Q1A1btn = ctk.CTkButton(quizQ1Window, text="x = 4", command=wrongAnswer1)
    Q1A1btn.place(anchor="center", relx=0.6, rely=0.7)

    # 1 wrong
    Q1A1btn = ctk.CTkButton(quizQ1Window, text="x = 5", command=wrongAnswer1)
    Q1A1btn.place(anchor="center", relx=0.8, rely=0.7)    

def startPress2():
    # create frame for start
    global quizQ1Window
    quizQ1Window = ctk.CTkFrame(root)
    quizQ1Window.place(x=0, y=0, relwidth=1, relheight=1)

    def wrongAnswer1():
        print("WRONG ANSWER WAS SELECTED")
        quizQ1Window.destroy()
        Answerincorrect1 = ctk.CTkFrame(root)
        Answerincorrect1.place(x=0, y=0, relwidth=1, relheight=1)

        wrongAnswer1text = ctk.CTkLabel(Answerincorrect1, text="Wrong answer was selected")
        wrongAnswer1text.place(anchor="center", relx=0.5, rely=0.4)

        def wrongAnswer1continue():
            Answerincorrect1.destroy()

        wrongAnswer1continue = ctk.CTkButton(Answerincorrect1, text="Continue", command=wrongAnswer1continue)
        wrongAnswer1continue.place(anchor="center", relx=0.5, rely=0.8)

    def correctAnswer1():
        print("CORRECT ANSWER WAS SELECTED")
        quizQ1Window.destroy()
        Answercorrect1 = ctk.CTkFrame(root)
        Answercorrect1.place(x=0, y=0, relwidth=1, relheight=1)

        wrongAnswer1text = ctk.CTkLabel(Answercorrect1, text="Correct answer was selected")
        wrongAnswer1text.place(anchor="center", relx=0.5, rely=0.4)

        def wrongAnswer1continue():
            Answercorrect1.destroy()
            startPress3()

        wrongAnswer1continue = ctk.CTkButton(Answercorrect1, text="Continue", command=wrongAnswer1continue)
        wrongAnswer1continue.place(anchor="center", relx=0.5, rely=0.8)

    # Go back button for the quiz
    def gobackPress():
        print("GO BACK TEST - QUIZ")
        quizQ1Window.destroy()

    # Buttons and labels in the frame
    # Create go back button
    gobackbutton = ctk.CTkButton(quizQ1Window, text="Go Back to main menu", command=gobackPress)
    gobackbutton.place(x=15, y=15)

    # Create question 2
    textQuestion2 = ctk.CTkLabel(quizQ1Window, text="3x + 2 = 11")
    textQuestion2.place(anchor="center", relx=0.5, rely=0.35)

    # Create question 2 answer text
    textQAnswer2 = ctk.CTkLabel(quizQ1Window, text="What is the answer?\nSelect the correct answer")
    textQAnswer2.place(anchor="center", relx=0.5, rely=0.45)

    # 2 wrong
    Q2A1btn = ctk.CTkButton(quizQ1Window, text="x = 1", command=wrongAnswer1)
    Q2A1btn.place(anchor="center", relx=0.2, rely=0.7)

    # 2 riht
    Q2A2btn = ctk.CTkButton(quizQ1Window, text="x = 3", command=correctAnswer1)
    Q2A2btn.place(anchor="center", relx=0.4, rely=0.7)

    # 2 wrong
    Q2A3btn = ctk.CTkButton(quizQ1Window, text="x = 4", command=wrongAnswer1)
    Q2A3btn.place(anchor="center", relx=0.6, rely=0.7)

    # 2 wrong 
    Q2A4btn = ctk.CTkButton(quizQ1Window, text="x = 5", command=wrongAnswer1)
    Q2A4btn.place(anchor="center", relx=0.8, rely=0.7)    

def startPress3():
    # create frame for start
    global quizQ1Window
    quizQ1Window = ctk.CTkFrame(root)
    quizQ1Window.place(x=0, y=0, relwidth=1, relheight=1)

    def wrongAnswer1():
        print("WRONG ANSWER WAS SELECTED")
        quizQ1Window.destroy()
        Answerincorrect1 = ctk.CTkFrame(root)
        Answerincorrect1.place(x=0, y=0, relwidth=1, relheight=1)

        wrongAnswer1text = ctk.CTkLabel(Answerincorrect1, text="Wrong answer was selected")
        wrongAnswer1text.place(anchor="center", relx=0.5, rely=0.4)

        def wrongAnswer1continue():
            Answerincorrect1.destroy()

        wrongAnswer1continue = ctk.CTkButton(Answerincorrect1, text="Continue", command=wrongAnswer1continue)
        wrongAnswer1continue.place(anchor="center", relx=0.5, rely=0.8)

    def correctAnswer1():
        print("CORRECT ANSWER WAS SELECTED")
        quizQ1Window.destroy()
        Answercorrect1 = ctk.CTkFrame(root)
        Answercorrect1.place(x=0, y=0, relwidth=1, relheight=1)

        wrongAnswer1text = ctk.CTkLabel(Answercorrect1, text="Correct answer was selected")
        wrongAnswer1text.place(anchor="center", relx=0.5, rely=0.4)

        def wrongAnswer1continue():
            Answercorrect1.destroy()
            startPress4()

        wrongAnswer1continue = ctk.CTkButton(Answercorrect1, text="Continue", command=wrongAnswer1continue)
        wrongAnswer1continue.place(anchor="center", relx=0.5, rely=0.8)

    # Go back button for the quiz
    def gobackPress():
        print("GO BACK TEST - QUIZ")
        quizQ1Window.destroy()

    # Buttons and labels in the frame
    # Create go back button
    gobackbutton = ctk.CTkButton(quizQ1Window, text="Go Back to main menu", command=gobackPress)
    gobackbutton.place(x=15, y=15)

    # Create question 3
    textQuestion3 = ctk.CTkLabel(quizQ1Window, text="7x + 7 = 14")
    textQuestion3.place(anchor="center", relx=0.5, rely=0.35)

    # Create question 3 answer text
    textQAnswer3 = ctk.CTkLabel(quizQ1Window, text="What is the answer?\nSelect the correct answer")
    textQAnswer3.place(anchor="center", relx=0.5, rely=0.45)

    # 3 right
    Q3A1btn = ctk.CTkButton(quizQ1Window, text="x = 1", command=correctAnswer1)
    Q3A1btn.place(anchor="center", relx=0.2, rely=0.7)

    # 3 wrong
    Q3A2btn = ctk.CTkButton(quizQ1Window, text="x = 3", command=wrongAnswer1)
    Q3A2btn.place(anchor="center", relx=0.4, rely=0.7)

    # 3 wrong
    Q3A3btn = ctk.CTkButton(quizQ1Window, text="x = 6", command=wrongAnswer1)
    Q3A3btn.place(anchor="center", relx=0.6, rely=0.7)

    # 3 wrong 
    Q3A4btn = ctk.CTkButton(quizQ1Window, text="x = 4", command=wrongAnswer1)
    Q3A4btn.place(anchor="center", relx=0.8, rely=0.7)


def startPress4():
    # create frame for start
    global quizQ1Window
    quizQ1Window = ctk.CTkFrame(root)
    quizQ1Window.place(x=0, y=0, relwidth=1, relheight=1)

    def wrongAnswer1():
        print("WRONG ANSWER WAS SELECTED")
        quizQ1Window.destroy()
        Answerincorrect1 = ctk.CTkFrame(root)
        Answerincorrect1.place(x=0, y=0, relwidth=1, relheight=1)

        wrongAnswer1text = ctk.CTkLabel(Answerincorrect1, text="Wrong answer was selected")
        wrongAnswer1text.place(anchor="center", relx=0.5, rely=0.4)

        def wrongAnswer1continue():
            Answerincorrect1.destroy()

        wrongAnswer1continue = ctk.CTkButton(Answerincorrect1, text="Continue", command=wrongAnswer1continue)
        wrongAnswer1continue.place(anchor="center", relx=0.5, rely=0.8)

    def correctAnswer1():
        print("CORRECT ANSWER WAS SELECTED")
        quizQ1Window.destroy()
        Answercorrect1 = ctk.CTkFrame(root)
        Answercorrect1.place(x=0, y=0, relwidth=1, relheight=1)

        wrongAnswer1text = ctk.CTkLabel(Answercorrect1, text="Correct answer was selected")
        wrongAnswer1text.place(anchor="center", relx=0.5, rely=0.4)

        def wrongAnswer1continue():
            Answercorrect1.destroy()
            startPress5()

        wrongAnswer1continue = ctk.CTkButton(Answercorrect1, text="Continue", command=wrongAnswer1continue)
        wrongAnswer1continue.place(anchor="center", relx=0.5, rely=0.8)

    # Go back button for the quiz
    def gobackPress():
        print("GO BACK TEST - QUIZ")
        quizQ1Window.destroy()

    # Buttons and labels in the frame
    # Create go back button
    gobackbutton = ctk.CTkButton(quizQ1Window, text="Go Back to main menu", command=gobackPress)
    gobackbutton.place(x=15, y=15)

    # Create question 4
    textQuestion4 = ctk.CTkLabel(quizQ1Window, text="6x + 3 = 15")
    textQuestion4.place(anchor="center", relx=0.5, rely=0.35)

    # Create question 4 answer text
    textQAnswer4 = ctk.CTkLabel(quizQ1Window, text="What is the answer?\nSelect the correct answer")
    textQAnswer4.place(anchor="center", relx=0.5, rely=0.45)

    # 4 wrong
    Q4A1btn = ctk.CTkButton(quizQ1Window, text="x = 1", command=wrongAnswer1)
    Q4A1btn.place(anchor="center", relx=0.2, rely=0.7)

    # 4 wrong
    Q4A2btn = ctk.CTkButton(quizQ1Window, text="x = 3", command=wrongAnswer1)
    Q4A2btn.place(anchor="center", relx=0.4, rely=0.7)

    # 4 right
    Q4A3btn = ctk.CTkButton(quizQ1Window, text="x = 2", command=correctAnswer1)
    Q4A3btn.place(anchor="center", relx=0.6, rely=0.7)

    # 4 wrong 
    Q4A4btn = ctk.CTkButton(quizQ1Window, text="x = 4", command=wrongAnswer1)
    Q4A4btn.place(anchor="center", relx=0.8, rely=0.7)


def startPress5():
    # create frame for start
    global quizQ1Window
    quizQ1Window = ctk.CTkFrame(root)
    quizQ1Window.place(x=0, y=0, relwidth=1, relheight=1)

    def wrongAnswer1():
        print("WRONG ANSWER WAS SELECTED")
        quizQ1Window.destroy()
        Answerincorrect1 = ctk.CTkFrame(root)
        Answerincorrect1.place(x=0, y=0, relwidth=1, relheight=1)

        wrongAnswer1text = ctk.CTkLabel(Answerincorrect1, text="Wrong answer was selected")
        wrongAnswer1text.place(anchor="center", relx=0.5, rely=0.4)

        def wrongAnswer1continue():
            Answerincorrect1.destroy()

        wrongAnswer1continue = ctk.CTkButton(Answerincorrect1, text="Continue", command=wrongAnswer1continue)
        wrongAnswer1continue.place(anchor="center", relx=0.5, rely=0.8)

    def correctAnswer1():
        print("CORRECT ANSWER WAS SELECTED")
        quizQ1Window.destroy()
        Answercorrect1 = ctk.CTkFrame(root)
        Answercorrect1.place(x=0, y=0, relwidth=1, relheight=1)

        wrongAnswer1text = ctk.CTkLabel(Answercorrect1, text="Correct answer was selected")
        wrongAnswer1text.place(anchor="center", relx=0.5, rely=0.4)

        def wrongAnswer1continue():
            Answercorrect1.destroy()

        wrongAnswer1continue = ctk.CTkButton(Answercorrect1, text="Continue", command=wrongAnswer1continue)
        wrongAnswer1continue.place(anchor="center", relx=0.5, rely=0.8)

    # Go back button for the quiz
    def gobackPress():
        print("GO BACK TEST - QUIZ")
        quizQ1Window.destroy()

    # Buttons and labels in the frame
    # Create go back button
    gobackbutton = ctk.CTkButton(quizQ1Window, text="Go Back to main menu", command=gobackPress)
    gobackbutton.place(x=15, y=15)

    # Create question 5
    textQuestion5 = ctk.CTkLabel(quizQ1Window, text="8x + 2 = 18")
    textQuestion5.place(anchor="center", relx=0.5, rely=0.35)

    # Create question 5 answer text
    textQAnswer5 = ctk.CTkLabel(quizQ1Window, text="What is the answer?\nSelect the correct answer")
    textQAnswer5.place(anchor="center", relx=0.5, rely=0.45)

    # 5 wrong
    Q5A1btn = ctk.CTkButton(quizQ1Window, text="x = 1", command=wrongAnswer1)
    Q5A1btn.place(anchor="center", relx=0.2, rely=0.7)

    # 5 wrong
    Q5A2btn = ctk.CTkButton(quizQ1Window, text="x = 3", command=wrongAnswer1)
    Q5A2btn.place(anchor="center", relx=0.4, rely=0.7)

    # 5 right
    Q5A3btn = ctk.CTkButton(quizQ1Window, text="x = 2", command=correctAnswer1)
    Q5A3btn.place(anchor="center", relx=0.6, rely=0.7)

    # 5 wrong 
    Q5A4btn = ctk.CTkButton(quizQ1Window, text="x = 4", command=wrongAnswer1)
    Q5A4btn.place(anchor="center", relx=0.8, rely=0.7)


# Create settings button
settingbutton = ctk.CTkButton(root, text="Settings", command=settingsPress)
settingbutton.place(x=15, y=15)
settingbutton = ctk.set_widget_scaling(1.2)

# Create lesson button
lessonbutton = ctk.CTkButton(root, text="Lesson", command=lessonPress)
lessonbutton.place(anchor="center", relx=0.5, rely=0.9)

# Create start button
startbutton = ctk.CTkButton(root, text="Start", command=startPress)
startbutton.place(anchor="center", relx=0.5, rely=0.5)



root.mainloop()