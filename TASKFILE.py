import customtkinter as ctk

root = ctk.CTk()
root.title("Algebra Learning Program")



# Define settings button
def settingsPress():
    print("SETTINGS BUTTON TEST") #Test that the button works - will be useful later

# Define lesson button
def lessonPress():
    print("LESSON BUTTON TEST") #Test that the button works - will be useful later

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