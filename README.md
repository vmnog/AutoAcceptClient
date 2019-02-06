# AutoClientAccept

A software that auto accepts the League of Legends queue when the button "accept" shows up.

# YOUTUBE VIDEO DEMONSTRATION
<iframe width="560" height="315" src="https://www.youtube.com/embed/pZwvg7rBcVI?controls=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# DONE
- [x] find out how to move the mouse to a specific position
- [x] uses AI to make a comparison between the button and the actual screen
- [x] gets the button positioning ideally of the resolution size
- [x] take a screenshot every 1sec and compare to the button image
- [x] recognize when it finds a match

# TODO
- [ ] notice when the client is already in select champion screen
- [ ] key blinds to activate/desactivate the auto accept
- [ ] a input to enter 5 champions names, after accepting the game the software should ban those (probrably just an idea)
- [ ] find a way to find the button with no needing of be looking at the client
- [ ] after all that stuffs working create a UI with electron JS

# WONTDO
- [ ] an menu list to the user chooses the monitor resolution, based on that we know where the mouse should click

# PIP Install

<ul>
  <li>pip install pyautogui</li>
  <li>pip install pypiwin32</li>
  <li>pip install numpy</li>
  <li>pip3 install opencv-python</li>
  <li>pip3 install matplotlib</li>
</ul>
