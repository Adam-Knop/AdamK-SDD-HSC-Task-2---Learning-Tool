import customtkinter as ctk

root = ctk.CTk()
root.title("Algebra Learning Program")



# Define settings button
def settingsPress():
    print("SETTINGS BUTTON TEST") # Test that the button works - will be useful later
    
    # Create "window" (frame) for settings
    settingsWindow = ctk.CTkFrame(root)
    settingsWindow.place(x=0, y=0, relwidth=1, relheight=1)



    # Dropdown boxes in settings

    # Background colour dropdown box    
    def bgcolourdpPress(choice):
        print("DROPDOWN BG COLOUR PRESSED: ",choice) # Test that the button works - will be useful later

    backgroundDP = ctk.CTkOptionMenu(settingsWindow, values=["TEST 1", "TEST 2", "TEST 3", "TEST 4", "TEST 5"], command = bgcolourdpPress)
    backgroundDP.set("TEST 1")
    backgroundDP.place(anchor="center", relx=0.5, rely=0.5)

    # Text colour dropdown box    
    def textcolourdpPress(choice):
        print("DROPDOWN TC COLOUR PRESSED: ",choice) # Test that the button works - will be useful later

    textcolourDP = ctk.CTkOptionMenu(settingsWindow, values=["TEST 1", "TEST 2", "TEST 3", "TEST 4", "TEST 5"], command = textcolourdpPress)
    textcolourDP.set("TEST 1")
    textcolourDP.place(anchor="center", relx=0.35, rely=0.5)

    # Scale dropdown box    
    def scalesizedpPress(choice):
        print("DROPDOWN SS PRESSED: ",choice) # Test that the button works - will be useful later

    scalesizeDP = ctk.CTkOptionMenu(settingsWindow, values=["TEST 1", "TEST 2", "TEST 3", "TEST 4", "TEST 5"], command = scalesizedpPress)
    scalesizeDP.set("TEST 1")
    scalesizeDP.place(anchor="center", relx=0.65, rely=0.5)   

    # Text labels for dropdown boxes in settings

    # Background colour DP text label
    BGDPtext = ctk.CTkLabel(settingsWindow, text=("BGDP TEXT TEST"))
    BGDPtext.place(anchor="center", relx=0.5, rely=0.45)

    # Text colour DP text label
    TCDPtext = ctk.CTkLabel(settingsWindow, text=("TCDP TEXT TEST"))
    TCDPtext.place(anchor="center", relx=0.35, rely=0.45)

    # Size scale DP text label
    SSDPtext = ctk.CTkLabel(settingsWindow, text=("SSDP TEXT TEST"))
    SSDPtext.place(anchor="center", relx=0.65, rely=0.45)



    # Go back button for the settings
    def gobackPress():
        print("GO BACK TEST - SETTINGS")
        settingsWindow.destroy()

    gobackbutton = ctk.CTkButton(settingsWindow, text="Go Back", command=gobackPress)
    gobackbutton.place(x=15, y=15)



# Define lesson button
def lessonPress():
    print("LESSON BUTTON TEST") # Test that the button works - will be useful later

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
        print("GO BACK TEST - LESSON")
        lessonWindow.destroy()

    gobackbutton = ctk.CTkButton(lessonWindow, text="Go Back", command=gobackPress)
    gobackbutton.place(x=15, y=15)

    

# Define start button
def startPress():
    print("START BUTTON TEST") # Test that the button works - will be useful later



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