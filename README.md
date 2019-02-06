# AutoClientAccept

A software that auto accepts the League of Legends queue when the button "accept" shows up.

# YOUTUBE VIDEO DEMONSTRATION
- https://youtu.be/pZwvg7rBcVI

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
- pip install pypiwin32<
- pip install numpy
- pip3 install opencv-python
- pip3 install matplotlib
- pip install win10toast
