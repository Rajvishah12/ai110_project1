# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first played the game, the hints were all backward. For example, the secret number was 32 and when I guessed 1, it suggested guessing lower. Also, only every other guess is getting recorded in guess history, when each guess should have been recorded. As a result, the number of attempts remaining were also off - the number of remaining attempts decreased every other attempt as well. The attempts remaining also started at 7 even though 8 attempts are allowed. Also, the "Hard" level has a smaller guess range (1-50) than the "Normal" level (1-100) when the opposite should be true. Point values also did not decrease consistently -- for example, if the same guess was submitted repeatedly, the number of attempts decreased but the score didn't. 5 points should have been deducted for each incorrect answer.

## 2. How did you use AI as a teammate?

I primarily used Claude and ChatGPT for this project. One AI suggestion that was correct was the changes it suggested for the issue with higher vs lower hints. Specifically, it identified that the reverse hints were being given and swapped the messages. I verified this by reading the suggestion and also the existing pytests. One AI suggestion that was incorrect was when it tried to change a variety of factors related to streamlit when all I wanted to do was set the starting number of attempts to 0. To my understanding, it was overcomplicating the situation so I changed it manually. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
