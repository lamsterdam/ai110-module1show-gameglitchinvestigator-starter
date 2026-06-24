# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  It had the difficulty set to normal and a message prompting me to provide a number bewteen 1 and 100. It showed my attempts allowed as 8 and showed how many I had left. The show hint checkbox was enabled to help me decide of to go lower or higher with my guess.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1. Changing the difficulty method between normal, easy and hard all showed the same message of guess a number between 1 and 100

  2.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input                                                     | Expected Behavior                                                                                                                                                                      | Actual Behavior                                                                                                                                                                                                                                                | Console Output / Error                             |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| changed the dfficulty level between normal, easy and hard | on easy, message should be "Guess a number between 1 and 20", for normal it should be "Guess a number between 1 and 100" and for normal it should be "Guess a number between 1 and 50" | instead it was "Guess a number between 1 and 100" on all three difficulties                                                                                                                                                                                    | none                                               |
| after I won a game and clicked the new game button        | the previous score, and previous score should be reset or empty and it should let me start a new game session                                                                          | it did not start a new game and kept showing the message that I have already won and to start a new game, and in developer debug the previous guesses and score was still shown, only the number of attempts was set to zero and the secret target was updated | "You already won. Start a new game to play again." |
| input a guess of 99 and then 100 on the normal mode       | if it shows to go higher, when I submit 100 that should be the number                                                                                                                  | it said to go higher, I submitted 100 then it said to go lower                                                                                                                                                                                                 | "📉 Go LOWER!"                                     |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  Copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  It suggested that the Go Lower and Go Higher outcome messages in check_guess function were swapped by mistake, and the fix was to switch them. After switching them I ran the app and verified that when the secret was lower than my guess, I got a Go Lower hint
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  One suggestion AI was giving me to resolve my import statement due to files being in different levels. It was suggesting to use conftest.py file but that seemed not needed for this. So I re-prompted it and it then suggested using sys.path instead

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I decided if a bug was fixed by using the logic in the app and checking whether the game behaved as I expected now. For the incorrect hint being shown I provided a high number than the secret and verified that the hint was now too high. For the message I verified that when I switched the difficulty the message changed the range
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I ran the test_guess_too_high() test and this showed me that the assertion in three of the tests were not set up correctly. They were missing the outcome part in the result, so this test needed to be updated to access the 0th index only
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  I would say that reruns in Streamlit is basically refreshing the game with the updated session state.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
    I would like to use the prompting startegy of giving an example of what I was expecting as the output and the actual output I saw.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
