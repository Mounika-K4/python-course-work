#Python Interview Questions
# New Questions
questions = [
    "1. What is PEP 8?",
    "2. What is the difference between list and tuple?",
    "3. What is Python’s GIL?",
    "4. What is the difference between deep copy and shallow copy?",
    "5. What is _str_() used for?",
    "6. Difference between remove() and pop() in list?",
    "7. What is Python’s ‘with’ statement mainly used for?",
    "8. Difference between Python 2 and Python 3 print?",
    "9. What is the difference between global and nonlocal?",
    "10. What is monkey patching?",
    "11. Which module is used for regular expressions?",
    "12. What is the purpose of sys.argv?",
    "13. What is Python’s pass by?",
    "14. What is the difference between @staticmethod and normal method?",
    "15. What is the use of zip() function?",
    "16. What is the purpose of enumerate()?",
    "17. What is Python’s default recursion depth?",
    "18. Which collection type allows duplicate keys?",
    "19. What is the difference between JSON and Pickle?",
    "20. How do you create a virtual environment?"
]

# Options
options = [
    ["a) Style guide", "b) Package manager", "c) Debug tool", "d) Library"],
    ["a) tuple mutable", "b) list immutable", "c) list mutable, tuple immutable", "d) same"],
    ["a) Garbage collector", "b) Global Interpreter Lock", "c) Python library", "d) Exception"],
    ["a) deep = full copy, shallow = ref copy", "b) both same", "c) shallow faster", "d) deep stores refs"],
    ["a) Destructor", "b) String representation", "c) Debug", "d) Loop"],
    ["a) remove uses index, pop uses value", "b) pop uses index, remove uses value", "c) both same", "d) pop removes all"],
    ["a) loops", "b) context manager", "c) exception", "d) function"],
    ["a) print is statement in both", "b) print is function in Python3", "c) print only in 2", "d) same"],
    ["a) global defines in module", "b) nonlocal defines in inner scope", "c) both same", "d) none"],
    ["a) changing code at runtime", "b) patching bugs", "c) inheritance", "d) new package"],
    ["a) os", "b) re", "c) sys", "d) regex"],
    ["a) command line args", "b) system info", "c) version", "d) config"],
    ["a) pass by reference", "b) pass by object reference", "c) pass by value", "d) none"],
    ["a) normal method no self", "b) staticmethod no self", "c) both same", "d) normal method uses cls"],
    ["a) combine iterables", "b) only for lists", "c) sum numbers", "d) filter"],
    ["a) gives index + value", "b) only values", "c) only index", "d) sorts list"],
    ["a) 50", "b) 100", "c) 1000", "d) 5000"],
    ["a) dict", "b) list", "c) set", "d) none"],
    ["a) JSON text, Pickle binary", "b) same", "c) JSON Python only", "d) Pickle for web"],
    ["a) virtualenv command", "b) pip install", "c) venv module", "d) docker"]
]

# Correct options
answers = [
    'a', 'c', 'b', 'a', 'b',
    'b', 'b', 'b', 'b', 'a',
    'b', 'a', 'b', 'b', 'a',
    'a', 'c', 'a', 'a', 'c'
]

# Quiz
def quiz_game():
    score = 0
    print("Welcome to the Python Interview Quiz (Set 2)\n")

    for i in range(len(questions)):
        print(questions[i])
        for opt in options[i]:
            print(opt)
        ans = input("Your answer (a/b/c/d): ").strip().lower()

        if ans == answers[i]:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong! Correct answer is:", answers[i], "\n")

    print("Final Score:", score, "/", len(questions))
    if score >= 15:
        print("Excellent! You’re interview ready 🚀")
    elif score >= 10:
        print("Good effort, revise more 🔥")
    else:
        print("Keep practicing, you’ll get there 💡")

# Run it
quiz_game()