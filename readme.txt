# 👗 King's Closet: A Clueless-Inspired Fashion Game

King’s Closet is an interactive fashion game inspired by Cher Horowitz’s iconic virtual closet from *Clueless*. Built using CMU Graphics, the game allows users to browse, try on, and evaluate outfits made from different tops and bottoms. It integrates computer vision, machine learning, and gesture-based interaction to create a fun and immersive digital closet experience.

🎥 Demo Video: https://youtu.be/AO7PUn8GqX4

---

## ✨ Features

- Browse and mix different tops and bottoms to create outfits
- Outfit grading system powered by KMeans clustering
- Hand-tracking mode for touchless navigation using your webcam
- Dress a mannequin to visualize your outfit
- Virtual store with coins to purchase new clothing items
- Random outfit generator
- Try-On mode to visualize outfits on yourself using your webcam
- Background music with play/pause controls
- Personalized closet experience using your name

---

## 🛠️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME
```

### 2. Install dependencies

```bash
pip install numpy opencv-python scikit-learn pillow cmu-graphics
```

### 3. Run the game

```bash
python main.py
```

Make sure your webcam is connected if you want to use hand-tracking or Try-On features.

---

## 🎮 Controls

### Keyboard Controls

| Action | Key |
|------|-----|
| Navigate instructions | Up / Down Arrow Keys |
| Change tops | Left / Right Arrow Keys |
| Change bottoms | Up / Down Arrow Keys |

### Mouse Controls

| Action | Button |
|------|--------|
| Grade outfit | Click "Grade" |
| Dress mannequin | Click "Dress Me" |
| Open store | Click "Store" |
| Play/Pause music | Click music icon |

### Hand-Tracking Controls (Webcam Required)

| Gesture | Action |
|--------|--------|
| Swipe left/right | Change tops |
| Swipe up/down | Change bottoms |
| Show 5 fingers | Generate random outfit |

---

## 🧩 Game Modes

- **Welcome Screen**  
  Enter your name to personalize your closet.

- **Instructions Mode**  
  Learn how to play and navigate the game.

- **Browse Mode**  
  Mix and match tops and bottoms to create outfits.

- **Dress Me Mode**  
  View your outfit on a mannequin.

- **Grade Mode**  
  Receive feedback on how well your outfit matches.

- **Store Mode**  
  Purchase new clothing items using virtual coins.

- **Hand-Tracking Mode**  
  Navigate the closet using hand gestures.

- **Try-On Mode**  
  Visualize clothing on yourself using your webcam.

---

## 🧠 Machine Learning Component

The outfit grading system uses **KMeans clustering**, a machine learning algorithm, to evaluate how well clothing items match based on learned groupings. Outfits that fall into stronger matching clusters receive higher scores and reward coins, encouraging users to experiment with combinations.

---

## 🪙 Currency System

- Players start with **500 coins**
- Purchasing clothing decreases coins
- High-scoring outfits reward additional coins
- Encourages experimentation and strategic outfit creation

---

## 🧱 Technologies Used

- Python
- CMU Graphics
- OpenCV (Computer Vision)
- Scikit-Learn (Machine Learning)
- NumPy
- Pillow

---

## 🎯 Inspiration

This project recreates Cher Horowitz’s virtual closet from *Clueless*, bringing the concept into an interactive, modern experience using computer vision and machine learning.

---

## 👩‍💻 Authors

- Parishi Jain  
- Palomi Nihalani  
- Lilyana Sponhouse  

Carnegie Mellon University

---

## 🚀 Future Improvements

- Add more clothing categories (jackets, shoes, accessories)
- Improve grading accuracy using color theory and similarity metrics
- Save user outfits and profiles
- Expand gesture recognition capabilities
- Add more Try-On realism and alignment
