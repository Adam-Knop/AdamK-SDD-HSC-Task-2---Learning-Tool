import customtkinter as ctk

root = ctk.CTk()
root.title("Algebra Learning Program")



#Define settings button
def settingsPress():
    print("SETTINGS BUTTON TEST") # Test that the button works - will be useful later
    
    #Create "window" (frame) for settings
    settingsWindow = ctk.CTkFrame(root)
    settingsWindow.place(x=0, y=0, relwidth=1, relheight=1)



    #Dropdown boxes in settings

    #Background colour dropdown box    
    def bgcolourdpPress(choice):
        print("DROPDOWN BG COLOUR PRESSED: ",choice) # Test that the button works - will be useful later

    backgroundDP = ctk.CTkOptionMenu(settingsWindow, values=["Grey", "Black", "White", "Blue", "Green"], command = bgcolourdpPress)
    backgroundDP.set("Grey")
    backgroundDP.place(anchor="center", relx=0.5, rely=0.45)

     #Text colour dropdown box    
    def textcolourdpPress(choice):
        print("DROPDOWN TC COLOUR PRESSED: ",choice) # Test that the button works - will be useful later

    textcolourDP = ctk.CTkOptionMenu(settingsWindow, values=["White", "Black", "Yellow", "Pink", "Green"], command = textcolourdpPress)
    textcolourDP.set("White")
    textcolourDP.place(anchor="center", relx=0.35, rely=0.45)

     #Scale dropdown box    
    def scalesizedpPress(choice):
        print("DROPDOWN SS PRESSED: ",choice) # Test that the button works - will be useful later

    scalesizeDP = ctk.CTkOptionMenu(settingsWindow, values=["100%", "80%", "60%", "120%", "140%"], command = scalesizedpPress)
    scalesizeDP.set("100%")
    scalesizeDP.place(anchor="center", relx=0.65, rely=0.45)   

     #Text labels for dropdown boxes in settings

     #Background colour DP text label
    BGDPtext = ctk.CTkLabel(settingsWindow, text=("Background colour"))
    BGDPtext.place(anchor="center", relx=0.5, rely=0.35)

     #Text colour DP text label
    TCDPtext = ctk.CTkLabel(settingsWindow, text=("Text colour"))
    TCDPtext.place(anchor="center", relx=0.35, rely=0.35)

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
    textTopLesson = ctk.CTkLabel(lessonWindow, text="SAMPLE TEXT TOP")
    textTopLesson.place(anchor="center", relx=0.5, rely=0.3)

    textMiddleLesson = ctk.CTkLabel(lessonWindow, text="SAMPLE TEXT MIDDLE")
    textMiddleLesson.place(anchor="center", relx=0.5, rely=0.5)

    textBottomLesson = ctk.CTkLabel(lessonWindow, text="SAMPLE TEXT TOP")
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

    # Create frame for start
    global quizQ1Window
    quizQ1Window = ctk.CTkFrame(root)
    quizQ1Window.place(x=0, y=0, relwidth=1, relheight=1)

    def wrongAnswer1():
        print("WRONG ANSWER WAS SELECTED")
        quizQ1Window.destroy
        Answerincorrect1 = ctk.CTkFrame(root)
        Answerincorrect1.place(x=0, y=0, relwidth=1, relheight=1)

        wrongAnswer1text = ctk.CTkLabel(Answerincorrect1, text="Wrong answer was selected")
        wrongAnswer1text.place(anchor="center", relx=0.5, rely=0.4)

        def wrongAnswer1continue():
            Answerincorrect1.destroy

        wrongAnswer1continue = ctk.CTkButton(Answerincorrect1, text="Continue", command=wrongAnswer1continue)
        wrongAnswer1continue.place(anchor="center", relx=0.5, rely=0.8)



    def correctAnswer1():
        print("CORRECT ANSWER WAS SELECTED")
        quizQ1Window.destroy
        Answercorrect1 = ctk.CTkFrame(root)
        Answercorrect1.place(x=0, y=0, relwidth=1, relheight=1)

        wrongAnswer1text = ctk.CTkLabel(Answercorrect1, text="Correct answer was selected")
        wrongAnswer1text.place(anchor="center", relx=0.5, rely=0.4)

        def wrongAnswer1continue():
            Answercorrect1.destroy

        wrongAnswer1continue = ctk.CTkButton(Answercorrect1, text="Continue")
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



    # Create answer 1 (incorrect)
    Q1A1btn = ctk.CTkButton(quizQ1Window, text="x = 8", command=wrongAnswer1)
    Q1A1btn.place(anchor="center", relx=0.2, rely=0.7)

    # Create answer 2 (correct)
    Q1A1btn = ctk.CTkButton(quizQ1Window, text="x = 2", command=correctAnswer1)
    Q1A1btn.place(anchor="center", relx=0.4, rely=0.7)

    # Create answer 3 (incorrect)
    Q1A1btn = ctk.CTkButton(quizQ1Window, text="x = 4", command=wrongAnswer1)
    Q1A1btn.place(anchor="center", relx=0.6, rely=0.7)

    # Create answer 4 (incorrect)
    Q1A1btn = ctk.CTkButton(quizQ1Window, text="x = 5", command=wrongAnswer1)
    Q1A1btn.place(anchor="center", relx=0.8, rely=0.7)    



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