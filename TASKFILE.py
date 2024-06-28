import customtkinter as ctk

root = ctk.CTk()
root.title("Algebra Learning Program")
root.geometry("1000x600")

current_text_color = "White"  # Store the current text color
current_appearance_mode = "System"  # Store the current appearance mode
current_widget_scaling = 1.0  # Store the current widget scaling

text_labels = []  # Store all text labels to update their colors later
buttons = []  # Store all buttons to update their text colors later
dropdowns = []  # Store all dropdowns to update their text colors later

def track_text_label(label):
    text_labels.append(label)
    label.configure(text_color=current_text_color)

def track_button(button):
    buttons.append(button)
    button.configure(text_color=current_text_color)

def track_dropdown(dropdown):
    dropdowns.append(dropdown)
    dropdown.configure(text_color=current_text_color)

def update_text_color():
    for label in text_labels:
        if label.winfo_exists():
            label.configure(text_color=current_text_color)
    for button in buttons:
        if button.winfo_exists():
            button.configure(text_color=current_text_color)
    for dropdown in dropdowns:
        if dropdown.winfo_exists():
            dropdown.configure(text_color=current_text_color)

def apply_current_settings():
    update_text_color()
    ctk.set_appearance_mode(current_appearance_mode)

# Define settings button
def settingsPress():
    global current_text_color, current_appearance_mode, current_widget_scaling

    print("SETTINGS BUTTON TEST")  # Test that the button works - will be useful later
    
    # Create "window" (frame) for settings
    settingsWindow = ctk.CTkFrame(root)
    settingsWindow.place(x=0, y=0, relwidth=1, relheight=1)

    # Dropdown boxes in settings

    # Background color dropdown box    
    def Appearance(selection):
        global current_appearance_mode
        choice_index = themes.index(optionmenu_2.get())
        if choice_index == 0:
            current_appearance_mode = "light"
            ctk.set_appearance_mode("light")
        elif choice_index == 1:
            current_appearance_mode = "dark"
            ctk.set_appearance_mode("dark")
        elif choice_index == 2:
            current_appearance_mode = "system"
            ctk.set_appearance_mode("system")

    themes = ["Light", "Dark", "System"]
    optionmenu_2 = ctk.CTkOptionMenu(settingsWindow, values=themes, command=Appearance)
    optionmenu_2.place(anchor="center", relx=0.25, rely=0.45)
    optionmenu_2.set(current_appearance_mode.capitalize())
    track_dropdown(optionmenu_2)

    # Text color dropdown box    
    def textcolourdpPress(choice):
        global current_text_color
        print("DROPDOWN TC COLOUR PRESSED: ", choice)  # Test that the button works - will be useful later
        current_text_color = choice
        update_text_color()

    textcolourDP = ctk.CTkOptionMenu(settingsWindow, values=["White", "Black", "Yellow", "Pink", "Green"], command=textcolourdpPress)
    textcolourDP.set(current_text_color)
    textcolourDP.place(anchor="center", relx=0.45, rely=0.45)
    track_dropdown(textcolourDP)

    def scalesizedPress(selection):
        global current_widget_scaling
        scale = int(selection.strip('%')) / 100
        current_widget_scaling = scale
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
    scalesizeDP.set(f"{int(current_widget_scaling * 100)}%")
    track_dropdown(scalesizeDP)

    # Text labels for dropdown boxes in settings

    # Background color DP text label
    BGDPtext = ctk.CTkLabel(settingsWindow, text=("Background color"))
    BGDPtext.place(anchor="center", relx=0.25, rely=0.35)
    track_text_label(BGDPtext)

    # Text color DP text label
    TCDPtext = ctk.CTkLabel(settingsWindow, text=("Text color"))
    TCDPtext.place(anchor="center", relx=0.45, rely=0.35)
    track_text_label(TCDPtext)

    # Size scale DP text label
    SSDPtext = ctk.CTkLabel(settingsWindow, text=("Size (scale)"))
    SSDPtext.place(anchor="center", relx=0.65, rely=0.35)
    track_text_label(SSDPtext)

    # Go back button for the settings
    def gobackPress():
        print("GO BACK TEST - SETTINGS")
        settingsWindow.destroy()

    gobackbutton = ctk.CTkButton(settingsWindow, text="Go Back", command=gobackPress)
    gobackbutton.place(x=15, y=15)
    track_button(gobackbutton)

# Define lesson button
def lessonPress():
    print("LESSON BUTTON TEST")  # Test that the button works - will be useful later

    # Create frame for lesson
    lessonWindow = ctk.CTkFrame(root)
    lessonWindow.place(x=0, y=0, relwidth=1, relheight=1)
    apply_current_settings()

    # Create text for lesson frame
    textTopLesson = ctk.CTkLabel(lessonWindow, text="Algebra is the manipulation of equations to find an unknown variable\nTake this equation as an example\n2x - 5 = 5")
    textTopLesson.place(anchor="center", relx=0.5, rely=0.3)
    track_text_label(textTopLesson)

    textMiddleLesson = ctk.CTkLabel(lessonWindow, text="The first step in solving algebra is moving all the x's to one side (in this case just the one), and all the numbers to the other.\nThis looks like this:\n2x - 5 + 5 = 5 + 5\n2x = 10")
    textMiddleLesson.place(anchor="center", relx=0.5, rely=0.5)
    track_text_label(textMiddleLesson)

    textBottomLesson = ctk.CTkLabel(lessonWindow, text="After this is done you should be left with just x on one side and numbers on the other. Now you solve for x by doing the remaining simplification if necessary:\n2x/2 = 10/2\nx = 5")
    textBottomLesson.place(anchor="center", relx=0.5, rely=0.7)
    track_text_label(textBottomLesson)

    # Go back button for the lesson
    def gobackPress():
        print("GO BACK TEST - LESSON")
        lessonWindow.destroy()

    gobackbutton = ctk.CTkButton(lessonWindow, text="Go Back", command=gobackPress)
    gobackbutton.place(x=15, y=15)
    track_button(gobackbutton)

# Define start button
def startPress():
    print("START BUTTON TEST")  # Test that the button works - will be useful later

    # Create frame 
    global quizQ1Window
    quizQ1Window = ctk.CTkFrame(root)
    quizQ1Window.place(x=0, y=0, relwidth=1, relheight=1)
    apply_current_settings()

    def wrongAnswer1():
        print("WRONG ANSWER WAS SELECTED")
        quizQ1Window.destroy()
        Answerincorrect1 = ctk.CTkFrame(root)
        Answerincorrect1.place(x=0, y=0, relwidth=1, relheight=1)
        apply_current_settings()

        wrongAnswer1text = ctk.CTkLabel(Answerincorrect1, text="❎ Wrong ❎ answer was selected. Go and try again!")
        wrongAnswer1text.place(anchor="center", relx=0.5, rely=0.4)
        track_text_label(wrongAnswer1text)

        def wrongAnswer1continue():
            Answerincorrect1.destroy()

        wrongAnswer1continue = ctk.CTkButton(Answerincorrect1, text="Continue", command=wrongAnswer1continue)
        wrongAnswer1continue.place(anchor="center", relx=0.5, rely=0.8)
        track_button(wrongAnswer1continue)

    def correctAnswer1():
        print("CORRECT ANSWER WAS SELECTED")
        quizQ1Window.destroy()
        Answercorrect1 = ctk.CTkFrame(root)
        Answercorrect1.place(x=0, y=0, relwidth=1, relheight=1)
        apply_current_settings()

        correctAnswer1text = ctk.CTkLabel(Answercorrect1, text="✅ Correct ✅ answer was selected")
        correctAnswer1text.place(anchor="center", relx=0.5, rely=0.4)
        track_text_label(correctAnswer1text)

        def correctAnswer1continue():
            Answercorrect1.destroy()
            startPress2()  # Start the Q2

        correctAnswer1continue = ctk.CTkButton(Answercorrect1, text="Continue", command=correctAnswer1continue)
        correctAnswer1continue.place(anchor="center", relx=0.5, rely=0.8)
        track_button(correctAnswer1continue)

    # Go back button for the quiz 
    def gobackPress():
        print("GO BACK TEST - QUIZ")
        quizQ1Window.destroy()

    # Buttons and labels in the frame
    # Create go back button
    gobackbutton = ctk.CTkButton(quizQ1Window, text="Go Back to main menu", command=gobackPress)
    gobackbutton.place(x=15, y=15)
    track_button(gobackbutton)

    # Create question 1
    textQuestion1 = ctk.CTkLabel(quizQ1Window, text="5x + 7 = 17")
    textQuestion1.place(anchor="center", relx=0.5, rely=0.35)
    track_text_label(textQuestion1)

    # Create question 1 answer text
    textQAnswer1 = ctk.CTkLabel(quizQ1Window, text="What is the answer?\nSelect the correct answer")
    textQAnswer1.place(anchor="center", relx=0.5, rely=0.45)
    track_text_label(textQAnswer1)

    # 1 wrong
    Q1A1btn = ctk.CTkButton(quizQ1Window, text="x = 8", command=wrongAnswer1)
    Q1A1btn.place(anchor="center", relx=0.2, rely=0.7)
    track_button(Q1A1btn)

    # 1 right
    Q1A2btn = ctk.CTkButton(quizQ1Window, text="x = 2", command=correctAnswer1)
    Q1A2btn.place(anchor="center", relx=0.4, rely=0.7)
    track_button(Q1A2btn)

    # 1 wrong
    Q1A3btn = ctk.CTkButton(quizQ1Window, text="x = 4", command=wrongAnswer1)
    Q1A3btn.place(anchor="center", relx=0.6, rely=0.7)
    track_button(Q1A3btn)

    # 1 wrong
    Q1A4btn = ctk.CTkButton(quizQ1Window, text="x = 5", command=wrongAnswer1)
    Q1A4btn.place(anchor="center", relx=0.8, rely=0.7)
    track_button(Q1A4btn)

def startPress2():
    print("START BUTTON TEST - Question 2")  # Test that the button works - will be useful later

    # Create frame 
    global quizQ2Window
    quizQ2Window = ctk.CTkFrame(root)
    quizQ2Window.place(x=0, y=0, relwidth=1, relheight=1)
    apply_current_settings()

    def wrongAnswer2():
        print("WRONG ANSWER WAS SELECTED")
        quizQ2Window.destroy()
        Answerincorrect2 = ctk.CTkFrame(root)
        Answerincorrect2.place(x=0, y=0, relwidth=1, relheight=1)
        apply_current_settings()

        wrongAnswer2text = ctk.CTkLabel(Answerincorrect2, text="❎ Wrong ❎ answer was selected. Go and try again!")
        wrongAnswer2text.place(anchor="center", relx=0.5, rely=0.4)
        track_text_label(wrongAnswer2text)

        def wrongAnswer2continue():
            Answerincorrect2.destroy()

        wrongAnswer2continue = ctk.CTkButton(Answerincorrect2, text="Continue", command=wrongAnswer2continue)
        wrongAnswer2continue.place(anchor="center", relx=0.5, rely=0.8)
        track_button(wrongAnswer2continue)

    def correctAnswer2():
        print("CORRECT ANSWER WAS SELECTED")
        quizQ2Window.destroy()
        Answercorrect2 = ctk.CTkFrame(root)
        Answercorrect2.place(x=0, y=0, relwidth=1, relheight=1)
        apply_current_settings()

        correctAnswer2text = ctk.CTkLabel(Answercorrect2, text="✅ Correct ✅ answer was selected")
        correctAnswer2text.place(anchor="center", relx=0.5, rely=0.4)
        track_text_label(correctAnswer2text)

        def correctAnswer2continue():
            Answercorrect2.destroy()
            startPress3()  # Start the Q3

        correctAnswer2continue = ctk.CTkButton(Answercorrect2, text="Continue", command=correctAnswer2continue)
        correctAnswer2continue.place(anchor="center", relx=0.5, rely=0.8)
        track_button(correctAnswer2continue)

    # Go back button for the quiz 
    def gobackPress():
        print("GO BACK TEST - QUIZ 2")
        quizQ2Window.destroy()

    # Buttons and labels in the frame
    # Create go back button
    gobackbutton = ctk.CTkButton(quizQ2Window, text="Go Back to main menu", command=gobackPress)
    gobackbutton.place(x=15, y=15)
    track_button(gobackbutton)

    # Create question 2
    textQuestion2 = ctk.CTkLabel(quizQ2Window, text="3x + 2 = 11")
    textQuestion2.place(anchor="center", relx=0.5, rely=0.35)
    track_text_label(textQuestion2)

    # Create question 2 answer text
    textQAnswer2 = ctk.CTkLabel(quizQ2Window, text="What is the answer?\nSelect the correct answer")
    textQAnswer2.place(anchor="center", relx=0.5, rely=0.45)
    track_text_label(textQAnswer2)

    # 2 wrong
    Q2A1btn = ctk.CTkButton(quizQ2Window, text="x = 1", command=wrongAnswer2)
    Q2A1btn.place(anchor="center", relx=0.2, rely=0.7)
    track_button(Q2A1btn)

    # 2 right
    Q2A2btn = ctk.CTkButton(quizQ2Window, text="x = 3", command=correctAnswer2)
    Q2A2btn.place(anchor="center", relx=0.4, rely=0.7)
    track_button(Q2A2btn)

    # 2 wrong
    Q2A3btn = ctk.CTkButton(quizQ2Window, text="x = 4", command=wrongAnswer2)
    Q2A3btn.place(anchor="center", relx=0.6, rely=0.7)
    track_button(Q2A3btn)

    # 2 wrong
    Q2A4btn = ctk.CTkButton(quizQ2Window, text="x = 5", command=wrongAnswer2)
    Q2A4btn.place(anchor="center", relx=0.8, rely=0.7)
    track_button(Q2A4btn)

def startPress3():
    # create frame for start
    global quizQ1Window
    quizQ1Window = ctk.CTkFrame(root)
    quizQ1Window.place(x=0, y=0, relwidth=1, relheight=1)
    apply_current_settings()

    def wrongAnswer1():
        print("WRONG ANSWER WAS SELECTED")
        quizQ1Window.destroy()
        Answerincorrect1 = ctk.CTkFrame(root)
        Answerincorrect1.place(x=0, y=0, relwidth=1, relheight=1)
        apply_current_settings()

        wrongAnswer1text = ctk.CTkLabel(Answerincorrect1, text="❎ Wrong ❎ answer was selected. Go and try again!")
        wrongAnswer1text.place(anchor="center", relx=0.5, rely=0.4)
        track_text_label(wrongAnswer1text)

        def wrongAnswer1continue():
            Answerincorrect1.destroy()

        wrongAnswer1continue = ctk.CTkButton(Answerincorrect1, text="Continue", command=wrongAnswer1continue)
        wrongAnswer1continue.place(anchor="center", relx=0.5, rely=0.8)
        track_button(wrongAnswer1continue)

    def correctAnswer1():
        print("CORRECT ANSWER WAS SELECTED")
        quizQ1Window.destroy()
        Answercorrect1 = ctk.CTkFrame(root)
        Answercorrect1.place(x=0, y=0, relwidth=1, relheight=1)
        apply_current_settings()

        wrongAnswer1text = ctk.CTkLabel(Answercorrect1, text="✅ Correct ✅ answer was selected")
        wrongAnswer1text.place(anchor="center", relx=0.5, rely=0.4)
        track_text_label(wrongAnswer1text)

        def wrongAnswer1continue():
            Answercorrect1.destroy()
            startPress4()

        wrongAnswer1continue = ctk.CTkButton(Answercorrect1, text="Continue", command=wrongAnswer1continue)
        wrongAnswer1continue.place(anchor="center", relx=0.5, rely=0.8)
        track_button(wrongAnswer1continue)

    # Go back button for the quiz
    def gobackPress():
        print("GO BACK TEST - QUIZ")
        quizQ1Window.destroy()

    # Buttons and labels in the frame
    # Create go back button
    gobackbutton = ctk.CTkButton(quizQ1Window, text="Go Back to main menu", command=gobackPress)
    gobackbutton.place(x=15, y=15)
    track_button(gobackbutton)

    # Create question 3
    textQuestion3 = ctk.CTkLabel(quizQ1Window, text="7x + 7 = 14")
    textQuestion3.place(anchor="center", relx=0.5, rely=0.35)
    track_text_label(textQuestion3)

    # Create question 3 answer text
    textQAnswer3 = ctk.CTkLabel(quizQ1Window, text="What is the answer?\nSelect the correct answer")
    textQAnswer3.place(anchor="center", relx=0.5, rely=0.45)
    track_text_label(textQAnswer3)

    # 3 right
    Q3A1btn = ctk.CTkButton(quizQ1Window, text="x = 1", command=correctAnswer1)
    Q3A1btn.place(anchor="center", relx=0.2, rely=0.7)
    track_button(Q3A1btn)

    # 3 wrong
    Q3A2btn = ctk.CTkButton(quizQ1Window, text="x = 3", command=wrongAnswer1)
    Q3A2btn.place(anchor="center", relx=0.4, rely=0.7)
    track_button(Q3A2btn)

    # 3 wrong
    Q3A3btn = ctk.CTkButton(quizQ1Window, text="x = 6", command=wrongAnswer1)
    Q3A3btn.place(anchor="center", relx=0.6, rely=0.7)
    track_button(Q3A3btn)

    # 3 wrong 
    Q3A4btn = ctk.CTkButton(quizQ1Window, text="x = 4", command=wrongAnswer1)
    Q3A4btn.place(anchor="center", relx=0.8, rely=0.7)
    track_button(Q3A4btn)


def startPress4():
    # create frame for start
    global quizQ1Window
    quizQ1Window = ctk.CTkFrame(root)
    quizQ1Window.place(x=0, y=0, relwidth=1, relheight=1)
    apply_current_settings()

    def wrongAnswer1():
        print("WRONG ANSWER WAS SELECTED")
        quizQ1Window.destroy()
        Answerincorrect1 = ctk.CTkFrame(root)
        Answerincorrect1.place(x=0, y=0, relwidth=1, relheight=1)
        apply_current_settings()

        wrongAnswer1text = ctk.CTkLabel(Answerincorrect1, text="❎ Wrong ❎ answer was selected. Go and try again!")
        wrongAnswer1text.place(anchor="center", relx=0.5, rely=0.4)
        track_text_label(wrongAnswer1text)

        def wrongAnswer1continue():
            Answerincorrect1.destroy()

        wrongAnswer1continue = ctk.CTkButton(Answerincorrect1, text="Continue", command=wrongAnswer1continue)
        wrongAnswer1continue.place(anchor="center", relx=0.5, rely=0.8)
        track_button(wrongAnswer1continue)

    def correctAnswer1():
        print("CORRECT ANSWER WAS SELECTED")
        quizQ1Window.destroy()
        Answercorrect1 = ctk.CTkFrame(root)
        Answercorrect1.place(x=0, y=0, relwidth=1, relheight=1)
        apply_current_settings()

        wrongAnswer1text = ctk.CTkLabel(Answercorrect1, text="✅ Correct ✅ answer was selected")
        wrongAnswer1text.place(anchor="center", relx=0.5, rely=0.4)
        track_text_label(wrongAnswer1text)

        def wrongAnswer1continue():
            Answercorrect1.destroy()
            startPress5()

        wrongAnswer1continue = ctk.CTkButton(Answercorrect1, text="Continue", command=wrongAnswer1continue)
        wrongAnswer1continue.place(anchor="center", relx=0.5, rely=0.8)
        track_button(wrongAnswer1continue)

    # Go back button for the quiz
    def gobackPress():
        print("GO BACK TEST - QUIZ")
        quizQ1Window.destroy()

    # Buttons and labels in the frame
    # Create go back button
    gobackbutton = ctk.CTkButton(quizQ1Window, text="Go Back to main menu", command=gobackPress)
    gobackbutton.place(x=15, y=15)
    track_button(gobackbutton)

    # Create question 4
    textQuestion4 = ctk.CTkLabel(quizQ1Window, text="6x + 3 = 15")
    textQuestion4.place(anchor="center", relx=0.5, rely=0.35)
    track_text_label(textQuestion4)

    # Create question 4 answer text
    textQAnswer4 = ctk.CTkLabel(quizQ1Window, text="What is the answer?\nSelect the correct answer")
    textQAnswer4.place(anchor="center", relx=0.5, rely=0.45)
    track_text_label(textQAnswer4)

    # 4 wrong
    Q4A1btn = ctk.CTkButton(quizQ1Window, text="x = 1", command=wrongAnswer1)
    Q4A1btn.place(anchor="center", relx=0.2, rely=0.7)
    track_button(Q4A1btn)

    # 4 wrong
    Q4A2btn = ctk.CTkButton(quizQ1Window, text="x = 3", command=wrongAnswer1)
    Q4A2btn.place(anchor="center", relx=0.4, rely=0.7)
    track_button(Q4A2btn)

    # 4 right
    Q4A3btn = ctk.CTkButton(quizQ1Window, text="x = 2", command=correctAnswer1)
    Q4A3btn.place(anchor="center", relx=0.6, rely=0.7)
    track_button(Q4A3btn)

    # 4 wrong 
    Q4A4btn = ctk.CTkButton(quizQ1Window, text="x = 4", command=wrongAnswer1)
    Q4A4btn.place(anchor="center", relx=0.8, rely=0.7)
    track_button(Q4A4btn)


def startPress5():
    # create frame for start
    global quizQ1Window
    quizQ1Window = ctk.CTkFrame(root)
    quizQ1Window.place(x=0, y=0, relwidth=1, relheight=1)
    apply_current_settings()

    def wrongAnswer1():
        print("WRONG ANSWER WAS SELECTED")
        quizQ1Window.destroy()
        Answerincorrect1 = ctk.CTkFrame(root)
        Answerincorrect1.place(x=0, y=0, relwidth=1, relheight=1)
        apply_current_settings()

        wrongAnswer1text = ctk.CTkLabel(Answerincorrect1, text="❎ Wrong ❎ answer was selected. Go and try again!")
        wrongAnswer1text.place(anchor="center", relx=0.5, rely=0.4)
        track_text_label(wrongAnswer1text)

        def wrongAnswer1continue():
            Answerincorrect1.destroy()

        wrongAnswer1continue = ctk.CTkButton(Answerincorrect1, text="Continue", command=wrongAnswer1continue)
        wrongAnswer1continue.place(anchor="center", relx=0.5, rely=0.8)
        track_text_label(wrongAnswer1text)

    def correctAnswer1():
        print("CORRECT ANSWER WAS SELECTED")
        quizQ1Window.destroy()
        Answercorrect1 = ctk.CTkFrame(root)
        Answercorrect1.place(x=0, y=0, relwidth=1, relheight=1)
        apply_current_settings()

        correctAnswer1text = ctk.CTkLabel(Answercorrect1, text="✅ Correct ✅ answer was selected")
        correctAnswer1text.place(anchor="center", relx=0.5, rely=0.4)
        track_text_label(correctAnswer1text)

        def wrongAnswer1continue():
            Answercorrect1.destroy()

        wrongAnswer1continue = ctk.CTkButton(Answercorrect1, text="Continue", command=wrongAnswer1continue)
        wrongAnswer1continue.place(anchor="center", relx=0.5, rely=0.8)
        track_button(wrongAnswer1continue)

    # Go back button for the quiz
    def gobackPress():
        print("GO BACK TEST - QUIZ")
        quizQ1Window.destroy()

    # Buttons and labels in the frame
    # Create go back button
    gobackbutton = ctk.CTkButton(quizQ1Window, text="Go Back to main menu", command=gobackPress)
    gobackbutton.place(x=15, y=15)
    track_button(gobackbutton)

    # Create question 5
    textQuestion5 = ctk.CTkLabel(quizQ1Window, text="8x + 2 = 18")
    textQuestion5.place(anchor="center", relx=0.5, rely=0.35)
    track_text_label(textQuestion5)

    # Create question 5 answer text
    textQAnswer5 = ctk.CTkLabel(quizQ1Window, text="What is the answer?\nSelect the correct answer")
    textQAnswer5.place(anchor="center", relx=0.5, rely=0.45)
    track_text_label(textQAnswer5)

    # 5 wrong
    Q5A1btn = ctk.CTkButton(quizQ1Window, text="x = 1", command=wrongAnswer1)
    Q5A1btn.place(anchor="center", relx=0.2, rely=0.7)
    track_button(Q5A1btn)

    # 5 wrong
    Q5A2btn = ctk.CTkButton(quizQ1Window, text="x = 3", command=wrongAnswer1)
    Q5A2btn.place(anchor="center", relx=0.4, rely=0.7)
    track_button(Q5A2btn)

    # 5 right
    Q5A3btn = ctk.CTkButton(quizQ1Window, text="x = 2", command=correctAnswer1)
    Q5A3btn.place(anchor="center", relx=0.6, rely=0.7)
    track_button(Q5A3btn)

    # 5 wrong 
    Q5A4btn = ctk.CTkButton(quizQ1Window, text="x = 4", command=wrongAnswer1)
    Q5A4btn.place(anchor="center", relx=0.8, rely=0.7)
    track_button(Q5A4btn)


# Create settings button
settingbutton = ctk.CTkButton(root, text="⚙️ Settings ⚙️", command=settingsPress)
settingbutton.place(x=15, y=15)
settingbutton = ctk.set_widget_scaling(1.2)

# Create lesson button
lessonbutton = ctk.CTkButton(root, text="🖊 Lesson 🖊", command=lessonPress)
lessonbutton.place(anchor="center", relx=0.5, rely=0.9)
track_button(lessonbutton)

# Create start button
startbutton = ctk.CTkButton(root, text="👉 Start 👈", command=startPress)
startbutton.place(anchor="center", relx=0.5, rely=0.5)
track_button(startbutton)


root.mainloop()