def count_total_messages(messages):
    return f"Total messages: {len(messages)}"

def unique_users(messages):
    users = {msg.split(":")[0] for msg in messages}
    return f"Unique users: {users}"

def total_words(messages):
    words = sum(len(msg.split(":")[1].split()) for msg in messages)
    return f"Total words: {words}"

def avg_words_per_message(messages):
    words = sum(len(msg.split(":")[1].split()) for msg in messages)
    avg = words / len(messages) if messages else 0
    return f"Average words per message: {round(avg, 2)}"

def longest_message(messages):
    longest = max(messages, key=lambda x: len(x.split(":")[1]))
    return f"Longest message: {longest}"

def most_active_user(messages):
    counts = {}
    for msg in messages:
        user = msg.split(":")[0]
        counts[user] = counts.get(user, 0) + 1
    user = max(counts, key=counts.get)
    return f"Most active user: {user} ({counts[user]} messages)"

def message_count_for_user(messages, username):
    count = sum(1 for msg in messages if msg.startswith(username + ":"))
    return f"Messages sent by {username}: {count}"

def most_frequent_word_by_user(messages, username):
    words = []
    for msg in messages:
        if msg.startswith(username + ":"):
            words.extend(msg.split(":")[1].lower().split())
    if not words:
        return f"No messages from {username}"
    from collections import Counter
    word, freq = Counter(words).most_common(1)[0]
    return f"Most frequent word used by {username}: '{word}' ({freq} times)"

def first_and_last_message(messages, username):
    user_msgs = [msg for msg in messages if msg.startswith(username + ":")]
    if not user_msgs:
        return f"No messages from {username}"
    return f"First: {user_msgs[0]}\nLast: {user_msgs[-1]}"

def check_user_presence(messages, username):
    users = {msg.split(":")[0] for msg in messages}
    return f"User '{username}' found" if username in users else f"User '{username}' not found"

def common_repeated_words(messages):
    from collections import Counter
    words = []
    for msg in messages:
        words.extend(msg.split(":")[1].lower().split())
    repeated = {word for word, count in Counter(words).items() if count > 1}
    return f"Common repeated words: {repeated}"

def longest_avg_message_user(messages):
    from collections import defaultdict
    user_lengths = defaultdict(list)
    for msg in messages:
        user, text = msg.split(":", 1)
        user_lengths[user].append(len(text.split()))
    avg_lengths = {u: sum(l)/len(l) for u,l in user_lengths.items()}
    user = max(avg_lengths, key=avg_lengths.get)
    return f"User with longest average message: {user} ({round(avg_lengths[user],2)} words)"

def messages_mentioning_user(messages, username):
    count = sum(1 for msg in messages if username.lower() in msg.lower())
    return f"Messages mentioning '{username}': {count}"

def remove_duplicate_messages(messages):
    unique_msgs = list(dict.fromkeys(messages))
    return f"Unique messages count: {len(unique_msgs)}"

def sort_messages(messages):
    return "\n".join(sorted(messages))

def extract_questions(messages):
    return "\n".join(msg for msg in messages if "?" in msg)

def check_deleted(messages):
    deleted = sum(1 for msg in messages if "This message was deleted" in msg)
    return f"Deleted messages found: {deleted}"

def reply_ratio(messages, user1, user2):
    replies = sum(1 for i in range(1, len(messages))
                  if messages[i].startswith(user2 + ":") and messages[i-1].startswith(user1 + ":"))
    return f"Reply ratio from {user2} to {user1}: {replies} replies"

def longest_streak(messages):
    max_streak, current_streak, current_user = 1, 1, messages[0].split(":")[0]
    best_user = current_user
    for i in range(1, len(messages)):
        user = messages[i].split(":")[0]
        if user == current_user:
            current_streak += 1
            if current_streak > max_streak:
                max_streak, best_user = current_streak, user
        else:
            current_streak, current_user = 1, user
    return f"Longest streak: {best_user} ({max_streak} messages)"

def most_active_hour(messages):
    # Fake time analysis since timestamps not given
    # Assumption: we'll use message index as "time"
    hour_counts = {}
    for i, msg in enumerate(messages):
        hour = i % 24   # simulate hour from index
        hour_counts[hour] = hour_counts.get(hour, 0) + 1
    best_hour = max(hour_counts, key=hour_counts.get)
    return f"Most active hour (simulated): {best_hour}:00 with {hour_counts[best_hour]} messages"


# --------------------------
# Main Menu
# --------------------------

def main():
    messages = []
    n = int(input("Enter number of messages: "))
    for _ in range(n):
        messages.append(input())

    while True:
        print("\n--- WhatsApp Chat Analysis Menu ---")
        print("1. Count total number of messages")
        print("2. Identify unique users")
        print("3. Count total words")
        print("4. Calculate average words per message")
        print("5. Find longest message")
        print("6. Find most active user")
        print("7. Message count for specific user")
        print("8. Most frequent word by specific user")
        print("9. First and last message of a user")
        print("10. Check if user is present")
        print("11. Find common repeated words")
        print("12. User with longest average message")
        print("13. Messages mentioning a user")
        print("14. Remove duplicate messages")
        print("15. Sort messages alphabetically")
        print("16. Extract all questions")
        print("17. Check for deleted messages")
        print("18. Calculate reply ratio between 2 users")
        print("19. Longest streak of a single user")
        print("20. Most active hour (simulated)")
        print("0. Exit")

        choice = int(input("Enter choice: "))
        
        if choice == 0:
            break
        elif choice == 1:
            print(count_total_messages(messages))
        elif choice == 2:
            print(unique_users(messages))
        elif choice == 3:
            print(total_words(messages))
        elif choice == 4:
            print(avg_words_per_message(messages))
        elif choice == 5:
            print(longest_message(messages))
        elif choice == 6:
            print(most_active_user(messages))
        elif choice == 7:
            user = input("Enter username: ")
            print(message_count_for_user(messages, user))
        elif choice == 8:
            user = input("Enter username: ")
            print(most_frequent_word_by_user(messages, user))
        elif choice == 9:
            user = input("Enter username: ")
            print(first_and_last_message(messages, user))
        elif choice == 10:
            user = input("Enter username: ")
            print(check_user_presence(messages, user))
        elif choice == 11:
            print(common_repeated_words(messages))
        elif choice == 12:
            print(longest_avg_message_user(messages))
        elif choice == 13:
            user = input("Enter username: ")
            print(messages_mentioning_user(messages, user))
        elif choice == 14:
            print(remove_duplicate_messages(messages))
        elif choice == 15:
            print(sort_messages(messages))
        elif choice == 16:
            print(extract_questions(messages))
        elif choice == 17:
            print(check_deleted(messages))
        elif choice == 18:
            u1 = input("Enter first user: ")
            u2 = input("Enter second user: ")
            print(reply_ratio(messages, u1, u2))
        elif choice == 19:
            print(longest_streak(messages))
        elif choice == 20:
            print(most_active_hour(messages))
        else:
            print("Invalid choice!")

if __name__ == "__main__":
   main()