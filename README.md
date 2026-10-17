# Hangman Game

A minimalist Hangman game built with **HTML, CSS and JavaScript**. Guess the hidden word one letter at a time before the stick figure is complete.

This project is **Task 1** of my [CodeAlpha](https://www.codealpha.tech/) tasks.

## Screenshots

| New game | Extra hint |
| :---: | :---: |
| ![New game](screenshots/start.png) | ![Extra hint](screenshots/hint.png) |

| Win | Loss |
| :---: | :---: |
| ![Win](screenshots/win.png) | ![Loss](screenshots/lose.png) |

## Features

- Random word picked from a list of **20 everyday words**
- A **clue** for every word, plus an optional **extra hint**
- **6 wrong guesses** allowed, with the hangman drawn one part at a time
- Play with your **keyboard** or the **on-screen keys**
- Used letters are marked as correct or wrong
- **Win and loss scoreboard** that counts while the page is open
- Reveals the missed letters when you lose
- **Light and dark mode** that follow your device setting
- Responsive layout that works on phones and desktops

## How to Play

1. A word is chosen at random. Each underscore is one letter, and a clue appears under the word.
2. Guess a letter by pressing a key on your keyboard or tapping a letter on the screen.
3. A correct letter fills in its place in the word. A wrong letter adds a part to the drawing.
4. Stuck? Click **Show extra hint** for a second clue. It can be used once per round.
5. Find the whole word before 6 wrong guesses to win. Click **New game** to play again.

## Project Structure

```
CodeAlpha_Task_1/
├── index.html       # Page structure
├── style.css        # Styling, layout and light/dark themes
├── script.js        # Game logic and word list
├── hangman.py       # Console (terminal) version of the game
├── screenshots/     # Images used in this README
└── README.md
```

## Run the Web Version

**Option 1: open the file**
Download or clone the repository and double-click `index.html`. It opens in your browser.

**Option 2: VS Code with Live Server**
1. Open the project folder in VS Code.
2. Install the **Live Server** extension.
3. Right-click `index.html` and choose **Open with Live Server**.

**Option 3: Python local server**
```bash
python -m http.server 8000
```
Then open `http://localhost:8000` in your browser.

To clone the project:
```bash
git clone https://github.com/Tuhintech1278/CodeAlpha_Task_1.git
cd CodeAlpha_Task_1
```

## Run the Console Version

Python 3 is required.

```bash
python hangman.py
```

On Windows, use `py hangman.py` if `python` is not recognised. The console version uses a smaller list of 5 words and shows the hangman as ASCII art. Type `hint` once per round for an extra clue.

## Customize

**Add or change words:** edit the `WORDS` list at the top of `script.js`. Each entry has three values:

```js
{ word: "apple", clue: "A round fruit that is often red or green.",
  hint: "They say one a day keeps the doctor away." }
```

Keep the word in lowercase letters only, and do not include the word itself in the clue or hint.

**Change the colours:** edit the variables at the top of `style.css`.

## Concepts Practiced

- Random selection of a word from a list
- Loops and conditions (`if` / `else`)
- Strings and arrays
- Handling keyboard and click events
- Updating the page with the DOM
- Responsive design and light/dark themes with CSS variables

## Tech Stack

- HTML5
- CSS3
- JavaScript (vanilla, no libraries)
- Python 3 (console version)

## Author

[@Tuhintech1278](https://github.com/Tuhintech1278)

Built as part of the CodeAlpha tasks.
