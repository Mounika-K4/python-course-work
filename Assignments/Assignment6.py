import os
import re

# Sentiment keywords
positive_keywords = {"great", "excellent", "love", "amazing", "fast", "smooth", "good", "satisfied"}
negative_keywords = {"bad", "slow", "hate", "terrible", "poor", "buggy", "disappointed"}

# Feedback storage file
FEEDBACK_FILE = "smartphone_feedback.txt"

def analyze_sentiment(text):
    pos_pattern = r'\b(' + '|'.join(re.escape(word) for word in positive_keywords) + r')\b'
    neg_pattern = r'\b(' + '|'.join(re.escape(word) for word in negative_keywords) + r')\b'

    pos = len(re.findall(pos_pattern, text, re.IGNORECASE))
    neg = len(re.findall(neg_pattern, text, re.IGNORECASE))

    if pos > neg:
        return "Positive"
    elif neg > pos:
        return "Negative"
    else:
        return "Neutral"

def add_feedback():
    feedback = input("Enter customer feedback for the smartphone:\n")
    with open(FEEDBACK_FILE, "a", encoding="utf-8") as f:
        f.write(feedback.strip() + "\n")
    print("✅ Feedback saved.")

def view_feedback():
    if not os.path.exists(FEEDBACK_FILE):
        print("⚠️ No feedback available yet.")
        return

    with open(FEEDBACK_FILE, "r", encoding="utf-8") as f:
        entries = [line.strip() for line in f if line.strip()]

    if not entries:
        print("⚠️ No feedback available yet.")
        return

    print("\n--- All Feedback Entries ---")
    for i, entry in enumerate(entries, 1):
        sentiment = analyze_sentiment(entry)
        print(f"{i}. {entry} → Sentiment: {sentiment}")

def main():
    while True:
        print("\n📋 Smartphone Feedback Menu")
        print("1. Add Feedback")
        print("2. View All Feedback with Sentiment")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            add_feedback()
        elif choice == '2':
            view_feedback()
        elif choice == '3':
            print("👋 Exiting program.")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
