# AutoClientAccept

A software that auto accepts the League of Legends queue when the button "accept" shows up.

### HOW IT WORKS?
When you run the program it will display a windows notifications that tells you that it is waiting for the queue shows up. It takes a screenshot of your display every 1 sec, and it analyses the screenshot and use a algorithm to compare the button.png picture with the screenshot taked. If the algorithm returns an value of compability greather than 8 it will get the button location on the screen and move the mouse to this position and than finally click on it, accepting the queue.

### NOTES
It works fine for everyone that follows the 'how to install' guide and also you need to substitute the 'button.png' file that is
on the '/img'. Use the Spinning Tool from windows and use this to select just the word "ACCEPT" of the game's button (dont forget to substitute the original image with the same name).


### YOUTUBE VIDEO DEMONSTRATION
- 0.0.1 : https://youtu.be/pZwvg7rBcVI
- 0.0.2 : https://youtu.be/D3fWNxBScxk

### HOW TO INSTALL
- Download the zip
- Unzip it
- Install Python https://www.python.org/downloads/
- <strong>Copy</strong> the directory of the folder you unziped
    (REMEMBER TO GO INSIDE THE SRC FOLDER)
    <br>
    "(C:\Users\User\Desktop\AutoAcceptClient-master\src)"
- Open Command Prompt 
- <code>cd (paste here the directory that you copied before)</code>
- type and press enter for each of this items:
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


### DONE
- [x] find out how to move the mouse to a specific position
- [x] uses AI to make a comparison between the button and the actual screen
- [x] gets the button positioning ideally of the resolution size
- [x] take a screenshot every 1sec and compare to the button image
- [x] recognize when it finds a match
- [x] make it executable
- [x] show a notification when it start looking for queue
- [x] find a way to find the button with no needing of be looking at the client

### TODO
- [ ] notice when the client is already in select champion screen
- [ ] key blinds to activate/desactivate the auto accept
- [ ] a input to enter 5 champions names, after accepting the game the software should ban those (probably just an idea)
- [ ] after all that stuffs working create a UI with electron JS

### WONTDO
- [ ] an menu list to the user chooses the monitor resolution, based on that we know where the mouse should click

### PIP Install
- pip install pyautogui
- pip install pypiwin32
- pip install numpy
- pip3 install opencv-python
- pip3 install matplotlib
- pip install plyer
