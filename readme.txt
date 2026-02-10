# King's Closet (Clueless-Inspired Fashion Game)

King’s Closet is a modern interactive fashion game inspired by Cher Horowitz’s virtual closet from *Clueless*. It combines computer vision, machine learning, and gesture-based interaction to let users browse, try on, and evaluate outfits in a digital closet environment.

**Demo video:** https://youtu.be/AO7PUn8GqX4

---

## What’s included

- **Outfit browser:** mix and match tops and bottoms  
- **Outfit grading:** KMeans clustering evaluates outfit compatibility  
- **Hand-tracking navigation:** control the closet using webcam gestures  
- **Mannequin visualization:** preview outfits using the "Dress Me" feature  
- **Virtual store:** purchase new clothing using in-game currency  
- **Random outfit generator:** generate outfits automatically  
- **Try-On mode:** visualize clothing using webcam integration  
- **Personalized closet:** customized experience using player name  

---

## Tech stack

**Core:** Python, CMU Graphics  
**Computer vision:** OpenCV  
**Machine learning:** Scikit-learn (KMeans clustering)  
**Image processing:** Pillow  
**Data processing:** NumPy  

---

## Repo structure

```
KingsCloset/
├── main.py              # main game loop and UI logic
├── assets/              # clothing, UI elements, and music
│   ├── tops/
│   ├── bottoms/
│   ├── ui/
│   └── music/
├── handtracking.py     # gesture detection and webcam logic
├── grading.py          # outfit grading (KMeans clustering)
└── README.md
```

---

## Getting started

### Backend / game setup

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME
```

Install dependencies:

```bash
pip install numpy opencv-python scikit-learn pillow cmu-graphics
```

Run the game:

```bash
python main.py
```

**Note:** Webcam access is required for hand-tracking and Try-On features.

---

## Controls

**Keyboard**

- Left / Right arrows → change tops  
- Up / Down arrows → change bottoms  
- Up / Down arrows → navigate instructions  

**Mouse**

- Click **Grade** → grade outfit  
- Click **Dress Me** → view outfit on mannequin  
- Click **Store** → open clothing store  
- Click music icon → play or pause music  

**Hand tracking (webcam)**

- Swipe left / right → change tops  
- Swipe up / down → change bottoms  
- Show five fingers → generate random outfit  

---

## Game modes

- **Welcome:** enter your name and initialize your closet  
- **Instructions:** view controls and game information  
- **Browse:** explore clothing combinations  
- **Dress Me:** preview outfits on mannequin  
- **Grade:** evaluate outfit compatibility  
- **Store:** purchase new clothing using coins  
- **Try-On:** visualize clothing using webcam overlay  
- **Hand-tracking:** gesture-based navigation  

---

## Machine learning component

King’s Closet uses **KMeans clustering** to evaluate outfit compatibility. Clothing items are grouped into clusters based on similarity, and outfits that fall into stronger matching clusters receive higher scores and reward coins.

This creates a dynamic feedback system that encourages experimentation and exploration.

---

## Currency system

- Players start with **500 coins**
- Purchasing clothing decreases coin balance
- Higher-scoring outfits reward additional coins
- Encourages strategic outfit selection

---

## Inspiration

King’s Closet recreates Cher Horowitz’s iconic digital closet from *Clueless*, bringing the concept into a modern interactive experience using computer vision, gesture tracking, and machine learning.

---

## Authors

**Parishi Jain**  
**Palomi Nihalani**  
**Lilyana Sponhouse**  

---
