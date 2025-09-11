#WhatsApp Chat Analysis Program

def get_messages():
    messages = []
    n = int(input("Enter the number of messages: "))
    for _ in range(n):
        messages.append(input())
    return messages

def count_total_messages(messages):
    return len(messages)

def identify_unique_users(messages):
    return set(msg.split(":")[0].strip() for msg in messages)

def count_total_words(messages):
    return sum(len(msg.split(":")[1].strip().split()) for msg in messages)

def average_words_per_message(messages):
    return round(count_total_words(messages) / len(messages), 2)

def find_longest_message(messages):
    return max(messages, key=lambda msg: len(msg.split(":")[1].strip().split()))

def most_active_user(messages):
    from collections import Counter
    users = [msg.split(":")[0].strip() for msg in messages]
    return Counter(users).most_common(1)[0]

def message_count_for_user(messages, username):
    return sum(1 for msg in messages if msg.startswith(username + ":"))

def most_frequent_word_by_user(messages, username):
    from collections import Counter
    words = []
    for msg in messages:
        if msg.startswith(username + ":"):
            words.extend(msg.split(":")[1].strip().lower().split())
    return Counter(words).most_common(1)[0] if words else ("None", 0)

def first_and_last_message_by_user(messages, username):
    user_msgs = [msg for msg in messages if msg.startswith(username + ":")]
    return user_msgs[0], user_msgs[-1] if user_msgs else ("None", "None")

def check_user_presence(messages, username):
    return username in identify_unique_users(messages)

def find_common_words(messages):
    from collections import Counter
    all_words = []
    for msg in messages:
        all_words.extend(msg.split(":")[1].strip().lower().split())
    return {word for word, count in Counter(all_words).items() if count > 1}

def user_with_longest_avg_message(messages):
    from collections import defaultdict
    user_lengths = defaultdict(list)
    for msg in messages:
        user, text = msg.split(":")
        user_lengths[user.strip()].append(len(text.strip().split()))
    avg_lengths = {user: sum(lengths)/len(lengths) for user, lengths in user_lengths.items()}
    max_user = max(avg_lengths, key=avg_lengths.get)
    return max_user, round(avg_lengths[max_user], 2)

def messages_mentioning_user(messages, username):
    return sum(1 for msg in messages if username.lower() in msg.lower())

def remove_duplicate_messages(messages):
    return list(set(messages))

def sort_messages_alphabetically(messages):
    return sorted(messages)

def extract_questions(messages):
    return [msg for msg in messages if "?" in msg]

def reply_ratio(messages, user1, user2):
    replies = 0
    for i in range(1, len(messages)):
        if messages[i].startswith(user2 + ":") and user1 in messages[i - 1]:
            replies += 1
    return replies

def check_deleted_messages(messages):
    return [msg for msg in messages if msg.strip().endswith("This message was deleted")]

def main():
    messages = get_messages()
    while True:
        print("\nWhatsApp Chat Analysis Menu")
        print("1. Count total messages")
        print("2. Identify unique users")
        print("3. Count total words")
        print("4. Average words per message")
        print("5. Find longest message")
        print("6. Most active user")
        print("7. Message count for a user")
        print("8. Most frequent word by user")
        print("9. First and last message by user")
        print("10. Check user presence")
        print("11. Common repeated words")
        print("12. User with longest average message")
        print("13. Messages mentioning a user")
        print("14. Remove duplicate messages")
        print("15. Sort messages alphabetically")
        print("16. Extract questions")
        print("17. Reply ratio between two users")
        print("18. Check for deleted messages")
        print("19. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("Total messages:", count_total_messages(messages))
        elif choice == 2:
            print("Unique users:", identify_unique_users(messages))
        elif choice == 3:
            print("Total words:", count_total_words(messages))
        elif choice == 4:
            print("Average words per message:", average_words_per_message(messages))
        elif choice == 5:
            print("Longest message:", find_longest_message(messages))
        elif choice == 6:
            user, count = most_active_user(messages)
            print(f"Most active user: {user} ({count} messages)")
        elif choice == 7:
            user = input("Enter username: ")
            print(f"Messages sent by {user}:", message_count_for_user(messages, user))
        elif choice == 8:
            user = input("Enter username: ")
            word, count = most_frequent_word_by_user(messages, user)
            print(f"Most frequent word by {user}: '{word}' ({count} times)")
        elif choice == 9:
            user = input("Enter username: ")
            first, last = first_and_last_message_by_user(messages, user)
            print("First message:", first)
            print("Last message:", last)
        elif choice == 10:
            user = input("Enter username: ")
            print("User found:" if check_user_presence(messages, user) else "User not found.")
        elif choice == 11:
            print("Common repeated words:", find_common_words(messages))
        elif choice == 12:
            user, avg = user_with_longest_avg_message(messages)
            print(f"User with longest average message: {user} ({avg} words)")
        elif choice == 13:
            user = input("Enter username to check mentions: ")
            print(f"Messages mentioning '{user}':", messages_mentioning_user(messages, user))
        elif choice == 14:
            unique_msgs = remove_duplicate_messages(messages)
            print("Unique messages count:", len(unique_msgs))
        elif choice == 15:
            print("Sorted messages:")
            for msg in sort_messages_alphabetically(messages):
                print(msg)
        elif choice == 16:
            print("Questions asked:")
            for msg in extract_questions(messages):
                print(msg)
        elif choice == 17:
            u1 = input("Enter first user: ")
            u2 = input("Enter second user: ")
            print(f"Reply ratio from {u2} to {u1}:", reply_ratio(messages, u1, u2))
        elif choice == 18:
            deleted = check_deleted_messages(messages)
            print("Deleted messages found:", len(deleted))
            for msg in deleted:
                print(msg)
        elif choice == 19:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "_main_":
    main()