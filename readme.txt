# King's Closet (Clueless-Inspired Fashion Game)

King’s Closet is an interactive fashion game inspired by Cher Horowitz’s virtual closet from *Clueless*. Built using Python, CMU Graphics, computer vision, and machine learning, the game allows users to browse, try on, and evaluate outfits. It includes gesture-based navigation using hand tracking and an outfit grading system powered by clustering.

Demo video: https://youtu.be/AO7PUn8GqX4

## What’s included

- Browse and mix tops and bottoms to create outfits
- Outfit grading system using KMeans clustering
- Hand-tracking navigation using webcam gestures
- Mannequin visualization mode ("Dress Me")
- Virtual store with in-game currency
- Random outfit generator
- Try-On mode using webcam visualization
- Personalized closet experience

## Tech stack

- Python
- CMU Graphics
- OpenCV (computer vision)
- Scikit-learn (machine learning)
- NumPy
- Pillow

## Repo structure

```
KingsCloset/
├── main.py
├── assets/
│   ├── tops/
│   ├── bottoms/
│   ├── ui/
│   └── music/
├── handtracking.py
├── grading.py
└── README.md
```

## Getting started

### 1) Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME
```

### 2) Install dependencies

```bash
pip install numpy opencv-python scikit-learn pillow cmu-graphics
```

### 3) Run the game

```bash
python main.py
```

The webcam is required for hand-tracking and Try-On features.

## Controls

### Keyboard

- Left / Right arrows: change tops  
- Up / Down arrows: change bottoms  
- Up / Down arrows: navigate instructions  

### Mouse

- Click "Grade": grade the current outfit  
- Click "Dress Me": visualize outfit on mannequin  
- Click "Store": open clothing store  
- Click music icon: play or pause music  

### Hand tracking (webcam)

- Swipe left/right: change tops  
- Swipe up/down: change bottoms  
- Show five fingers: generate random outfit  

## Game modes

- Welcome: enter your name to personalize your closet
- Instructions: learn controls and features
- Browse: select and preview outfits
- Dress Me: view outfit on mannequin
- Grade: evaluate outfit match quality
- Store: purchase new clothing items
- Try-On: visualize clothing on yourself
- Hand-tracking: navigate using gestures

## Machine learning component

The outfit grading system uses KMeans clustering to evaluate how well clothing items match. Clothing combinations that fall into stronger matching clusters receive higher scores and reward coins.

## Currency system

- Players start with 500 coins
- Purchasing clothing decreases coins
- High-scoring outfits reward additional coins

## Inspiration

This project recreates Cher Horowitz’s digital closet from *Clueless*, bringing the concept into an interactive experience using modern computer vision and machine learning tools.

## Authors

Parishi Jain  
Palomi Nihalani  
Lilyana Sponhouse  
