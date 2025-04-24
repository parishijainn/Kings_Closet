King's Closet: A Clueless-Inspired Fashion Game:

King’s Closet is a CMU Graphics-based recreation of Cher Horowitz’s virtual 
closet from the movie Clueless. This interactive game allows users to browse, 
try on, and grade outfits using a combination of tops and bottoms. Features 
include an outfit grader powered by KMeans clustering and a hand-tracking mode 
that enables touchless outfit navigation.

King's Closet Youtube Demo: https://youtu.be/AO7PUn8GqX4

How To Run:
1. Download or clone the repository.
2. Install the required dependencies (see below).
3. From the command line, run: python main.py
Make sure your webcam is connected to use hand-tracking features.

Dependencies:
Install the following packages:
numpy  
opencv-python  
scikit-learn  
pillow  
cmu-graphics
You can install them with: pip install numpy opencv-python scikit-learn pillow cmu-graphics

Game Controls:
Navigate Instructions:	Up / Down Arrow Keys
Change Tops:	Left / Right Arrow Keys
Change Bottoms:	Up / Down Arrow Keys
Toggle Hand-Tracking Mode:	Enabled automatically if webcam is active
Swipe Left / Right (Hand):	Change Tops
Swipe Up / Down (Hand):	Change Bottoms
Generate Random Outfit (Hand):	Show 5 fingers
Grade Outfit:	Click "Grade" Button
Dress Mannequin:	Click "Dress Me" Button
Open Store:	Click "Store" Button
Play/Pause Music:	Click music icon

Modes:
Welcome Screen: Enter your name to personalize your closet
Instructions Mode: Learn how to play the game
Browse Mode: Try on different tops and bottoms
Dress Me Mode: See your outfit on a mannequin
Grade Mode: Get feedback on outfit match quality
Store Mode: Buy new clothing using virtual currency
Hand-Tracking Mode: Navigate the closet with finger gestures
Try-On Mode: Visualize the closet on yourself

Created By: Parishi Jain, Palomi Nihalani, Lilyana Sponhouse

In depth description: 

This project is recreation of Cher's closet from 
the movie Clueless. There are tops and bottoms
preloaded into the program and the user can browse
throw the tops and bottoms to make outfits. There
is also the option for the program to randomly 
select a top and/or bottom for the user. There is an option for a store that
gives you tanks, tees, skirts, and shorts. You have a preloaded amount of coins 
which is 500 and each time you buy a new piece of clothing the money goes down. 
The user can press the "Dress Me" button to visualize the 
outfit on a mannequin. The user can press the 
"grade" button and the outfit will be graded
on how well it matches. If it is a perfect match, coins get added back. There is
a handtracking feature that allows for you to go through the clothes with your
fingers. There is also a try on feature that allows you to try your clothes on
and use handtracking to change the clothes.