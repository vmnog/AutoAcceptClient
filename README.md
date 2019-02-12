# AutoClientAccept

A software that auto accepts the League of Legends queue when the button "accept" shows up.

# YOUTUBE VIDEO DEMONSTRATION
- 0.0.1 : https://youtu.be/pZwvg7rBcVI
- 0.0.2 : https://youtu.be/D3fWNxBScxk

# HOW TO INSTALL
- Download the zip
- Unzip it
- Install Python https://www.python.org/downloads/
- Copy the directory of the folder you unziped (REMEMBER TO GO INSIDE THE SRC FOLDER)
    Something like this "(C:\Users\VMNogueira\Desktop\AutoAcceptClient-master\src)"
- Open Command Prompt 
- type:
- <code>cd folder-directory</code>
- <code>pip install pyautogui</code>
- <code>pip install pyautogui</code>
- <code>pip install pypiwin32</code>
- <code>pip install numpy</code>
- <code>pip3 install opencv-python</code>
- <code>pip3 install matplotlib</code>
- <code>pip install plyer</code>

After installing all the requirements, do :
- <code>python main.pyw</code>
Or try Executing the main.pyw by double clicking in it.

If its working you can do the shortcut:
- Create a shortcut of the main.pyw
- Edit shortcut properties and change the icon to the /images/icon.ico
- Also change the Title of the shortcut to AutoAccept


# DONE
- [x] find out how to move the mouse to a specific position
- [x] uses AI to make a comparison between the button and the actual screen
- [x] gets the button positioning ideally of the resolution size
- [x] take a screenshot every 1sec and compare to the button image
- [x] recognize when it finds a match
- [x] make it executable
- [x] show a notification when it start looking for queue

# TODO
- [ ] notice when the client is already in select champion screen
- [ ] key blinds to activate/desactivate the auto accept
- [ ] a input to enter 5 champions names, after accepting the game the software should ban those (probrably just an idea)
- [ ] find a way to find the button with no needing of be looking at the client
- [ ] after all that stuffs working create a UI with electron JS

# WONTDO
- [ ] an menu list to the user chooses the monitor resolution, based on that we know where the mouse should click

# PIP Install
- pip install pyautogui
- pip install pypiwin32
- pip install numpy
- pip3 install opencv-python
- pip3 install matplotlib
- pip install plyer
