# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: _"How do I keep a variable from resetting in Streamlit when I click a button?"_
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ x ] Describe the game's purpose.
  The game's purpose is for the user to guess a number within a certain range based on the difficulty level. The user is trying to find the matching target number which the game randomly generated and set.
- [ x] Detail which bugs you found.
  The bugs I found were:

1. The message of Guess a number between 1 and 100 was hardcoded for all difficulty levels
2. When the user entered a number which was higher than the target the game would say go higher and vice versa
3. The number being randomly generated was always using the range of 1 - 100 instead of the range specified by the difficulty level
4. The game would not end after the user won or lost and would persist the score and the previous guesses

- [ x] Explain what fixes you applied.
  I fixed the bug to update the message shown based on the difficulty level range.
  I also fixed the bug to show the correct hint message.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User sets difficulty to Easy
2. Message updated to Guess a number between 1 and 20
3. User enters a guess of 1
4. Game returns "Too Low"
5. User enters a guess of 20 → "Too High"
6. Score updates correctly after each guess
7. Game ends after the correct guess

**Screenshot** _(optional)_: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
