import customtkinter as ctk

root = ctk.CTk()
root.title("Algebra Learning Program")



# Define settings button
def settingsPress():
    print("SETTINGS BUTTON TEST") #Test that the button works - will be useful later

# Define lesson button
def lessonPress():
    print("LESSON BUTTON TEST") #Test that the button works - will be useful later

    # Create "window" (frame) for lesson
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
        print("GO BACK TEST")
        lessonWindow.destroy()

    gobackbutton = ctk.CTkButton(lessonWindow, text="Go Back", command=gobackPress)
    gobackbutton.place(x=15, y=15)

    

# Define start button
def startPress():
    print("START BUTTON TEST") #Test that the button works - will be useful later



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



# Create High Score text
highscore = ctk.CTkLabel(root, text="High Score = TEST")
highscore.place(anchor="center", relx=0.5, rely=0.6)



root.mainloop()