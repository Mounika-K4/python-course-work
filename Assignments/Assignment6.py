import os
import re

# Directory for storing mobile reviews
REVIEWS_DIR = "mobile_reviews"

# Predefined keyword lists
positive_keywords = {"good", "excellent", "amazing", "smooth", "love", "great", "fast", "satisfied"}
negative_keywords = {"bad", "poor", "slow", "buggy", "hate", "terrible", "disappointed"}

# Ensure directory exists
if not os.path.exists(REVIEWS_DIR):
    os.makedirs(REVIEWS_DIR)

def analyze_review(filename):
    """Analyze a specific review file"""
    try:
        with open(os.path.join(REVIEWS_DIR, filename), "r") as f:
            content = f.read().lower()
        pos_found = re.findall(r'\b(?:' + "|".join(positive_keywords) + r')\b', content)
        neg_found = re.findall(r'\b(?:' + "|".join(negative_keywords) + r')\b', content)

        if pos_found and not neg_found:
            print(f"🟢 Review '{filename}' is POSITIVE (keywords: {set(pos_found)})")
        elif neg_found and not pos_found:
            print(f"🔴 Review '{filename}' is NEGATIVE (keywords: {set(neg_found)})")
        elif pos_found and neg_found:
            print(f"🟡 Review '{filename}' is MIXED (Positive: {set(pos_found)}, Negative: {set(neg_found)})")
        else:
            print(f"⚪ Review '{filename}' sentiment not detected.")
    except FileNotFoundError:
        print("❌ Review file not found.")

def analyze_all_reviews():
    """Analyze all reviews in the directory"""
    files = os.listdir(REVIEWS_DIR)
    if not files:
        print("No reviews available.")
        return
    
    summary = {"positive":0, "negative":0, "mixed":0, "neutral":0}
    
    for file in files:
        try:
            with open(os.path.join(REVIEWS_DIR, file), "r") as f:
                content = f.read().lower()
            pos_found = re.findall(r'\b(?:' + "|".join(positive_keywords) + r')\b', content)
            neg_found = re.findall(r'\b(?:' + "|".join(negative_keywords) + r')\b', content)

            if pos_found and not neg_found:
                summary["positive"] += 1
            elif neg_found and not pos_found:
                summary["negative"] += 1
            elif pos_found and neg_found:
                summary["mixed"] += 1
            else:
                summary["neutral"] += 1
        except:
            continue
    
    print("\n📊 Review Analysis Summary:")
    for k, v in summary.items():
        print(f"{k.capitalize()}: {v}")

def create_review():
    """Create a new mobile product review"""
    filename = input("Enter review filename (with .txt): ")
    content = input("Enter review content:\n")
    with open(os.path.join(REVIEWS_DIR, filename), "w") as f:
        f.write(content)
    print(f"✅ Review '{filename}' created successfully.")

def modify_review():
    """Modify an existing review"""
    filename = input("Enter review filename to modify: ")
    filepath = os.path.join(REVIEWS_DIR, filename)
    if not os.path.exists(filepath):
        print("❌ Review not found.")
        return
    with open(filepath, "r") as f:
        print("\nCurrent Review:\n", f.read())
    new_content = input("\nEnter new content to overwrite:\n")
    with open(filepath, "w") as f:
        f.write(new_content)
    print(f"✏ Review '{filename}' updated successfully.")

def delete_review():
    """Delete a review file"""
    filename = input("Enter review filename to delete: ")
    filepath = os.path.join(REVIEWS_DIR, filename)
    if os.path.exists(filepath):
        os.remove(filepath)
        print(f"🗑 Review '{filename}' deleted.")
    else:
        print("❌ Review not found.")

def main():
    """Main menu loop"""
    while True:
        print("\n--- Mobile Product Review Analyzer ---")
        print("1. Analyze a specific review")
        print("2. Analyze all reviews")
        print("3. Create new review")
        print("4. Modify existing review")
        print("5. Delete a review")
        print("6. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            fname = input("Enter review filename: ")
            analyze_review(fname)
        elif choice == "2":
            analyze_all_reviews()
        elif choice == "3":
            create_review()
        elif choice == "4":
            modify_review()
        elif choice == "5":
            delete_review()
        elif choice == "6":
            print("👋 Exiting program...")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
