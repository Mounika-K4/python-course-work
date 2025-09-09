#PYTHON INTERVIEW QUESTIONS AND ANSWERS
# Python Quiz Game (Based on Assignment-3)

# Questions
questions = [
    "1. What is the output of: print(type([]))?",
    "2. Which keyword is used to define a function in Python?",
    "3. What is the output of 3 * '5'?",
    "4. Which of the following is immutable?",
    "5. How do you start a comment in Python?",
    "6. What does len() do in Python?",
    "7. What is the correct file extension for Python files?",
    "8. Which of the following is used to import a module?",
    "9. What is the output of bool(0)?",
    "10. What is used to define a block of code in Python?",
    "11. Which operator is used for exponentiation?",
    "12. What is the default value of 'end' in print()?",
    "13. Which function is used to read input from users?",
    "14. Which keyword is used for error handling?",
    "15. Which data structure does not allow duplicates?",
    "16. What is the output of: print(2 == 2.0)?",
    "17. Which module is used for regular expressions?",
    "18. What is the output of: print(bool(''))?",
    "19. Which keyword is used to create a class?",
    "20. Which method is called when an object is created?"
]

# Options
options = [
    ["a) <class 'list'>", "b) <class 'dict'>", "c) <class 'set'>", "d) <class 'tuple'>"],
    ["a) function", "b) def", "c) fun", "d) define"],
    ["a) 15", "b) 555", "c) Error", "d) None"],
    ["a) list", "b) dict", "c) set", "d) tuple"],
    ["a) //", "b) <!--", "c) #", "d) **"],
    ["a) Calculates size of int", "b) Returns list length", "c) Finds memory usage", "d) Loops through list"],
    ["a) .pt", "b) .python", "c) .py", "d) .pyt"],
    ["a) include", "b) import", "c) using", "d) require"],
    ["a) True", "b) False", "c) 0", "d) None"],
    ["a) Brackets {}", "b) Parentheses ()", "c) Indentation", "d) Curly braces"],
    ["a) ^", "b) **", "c) //", "d) *"],
    ["a) \\n", "b) space", "c) ;", "d) None"],
    ["a) scan()", "b) cin", "c) input()", "d) gets()"],
    ["a) error", "b) try", "c) except", "d) catch"],
    ["a) list", "b) tuple", "c) set", "d) dict"],
    ["a) False", "b) True", "c) Error", "d) None"],
    ["a) os", "b) regex", "c) re", "d) sys"],
    ["a) True", "b) False", "c) None", "d) Error"],
    ["a) def", "b) class", "c) struct", "d) object"],
    ["a) _del()", "b) __init()", "c) __str()", "d) __new_()"]
]

# Correct answers
answers = ['a', 'b', 'b', 'd', 'c', 'b', 'c', 'b', 'b', 'c',
           'b', 'a', 'c', 'c', 'c', 'b', 'c', 'b', 'b', 'b']


# Quiz Game Function
def quiz_game():
    score = 0
    print("🧪 Welcome to the Python Quiz Game!\n")

    for i in range(len(questions)):
        print(questions[i])
        for opt in options[i]:
            print(opt)
        ans = input("Your answer (a/b/c/d): ").strip().lower()

        if ans == answers[i]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is '{answers[i]}'\n")

    print("🎯 Your Final Score:", score, "/", len(questions))
    if score >= 15:
        print("🎉 Excellent! You’re ready for interviews!")
    elif score >= 10:
        print("👍 Good effort, revise more!")
    else:
        print("📖 Keep learning, you’ll get better!")


# Run the game
quiz_game()