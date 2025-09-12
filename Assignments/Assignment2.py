# WhatsApp Chat Data Analysis Assignment

def count_messages(messages):
    return len(messages)

def unique_users(messages):
    return {msg.split(":")[0] for msg in messages}

def total_words(messages):
    return sum(len(msg.split()) - 1 for msg in messages)  # exclude name

def average_words(messages):
    return total_words(messages) / len(messages)

def longest_message(messages):
    return max(messages, key=lambda x: len(x))

def most_active_user(messages):
    from collections import Counter
    users = [msg.split(":")[0] for msg in messages]
    user_count = Counter(users)
    user, count = user_count.most_common(1)[0]
    return user, count

def message_count_user(messages, user):
    return sum(1 for msg in messages if msg.startswith(user + ":"))

def frequent_word_user(messages, user):
    from collections import Counter
    words = []
    for msg in messages:
        if msg.startswith(user + ":"):
            words.extend(msg.split()[1:])  # exclude name
    return Counter(words).most_common(1)[0] if words else None

def first_last_message(messages, user):
    user_msgs = [msg for msg in messages if msg.startswith(user + ":")]
    if user_msgs:
        return user_msgs[0], user_msgs[-1]
    return None, None

def check_user_present(messages, user):
    users = unique_users(messages)
    return user in users

def common_repeated_words(messages):
    from collections import Counter
    words = []
    for msg in messages:
        words.extend(msg.split()[1:])  # exclude name
    return {word for word, count in Counter(words).items() if count > 1}

def longest_avg_message(messages):
    from collections import defaultdict
    word_counts = defaultdict(list)
    for msg in messages:
        user, text = msg.split(":", 1)
        word_counts[user].append(len(text.split()))
    avg_lengths = {user: sum(lengths)/len(lengths) for user, lengths in word_counts.items()}
    return max(avg_lengths.items(), key=lambda x: x[1])

def mentions_of_user(messages, user):
    return sum(1 for msg in messages if user in msg.split()[1:])

def remove_duplicates(messages):
    return list(set(messages))

def sort_messages(messages):
    return sorted(messages)

def extract_questions(messages):
    return [msg for msg in messages if "?" in msg]

def reply_ratio(messages, user1, user2):
    count = 0
    for i in range(1, len(messages)):
        if messages[i-1].startswith(user1 + ":") and messages[i].startswith(user2 + ":"):
            count += 1
    return count

def deleted_messages(messages):
    return sum(1 for msg in messages if "This message was deleted" in msg)


# ---------------- MAIN PROGRAM ----------------

def main():
    n = int(input("Enter the number of messages: "))
    messages = [input() for _ in range(n)]

    while True:
        print("\nAnalysis Options:")
        print("1. Count total number of messages")
        print("2. Identify unique users in the chat")
        print("3. Count total words in the chat")
        print("4. Calculate average words per message")
        print("5. Find the longest message sent")
        print("6. Find the most active user")
        print("7. Get message count for a specific user")
        print("8. Find most frequently used word by a specific user")
        print("9. Retrieve first and last message by a user")
        print("10. Check if a user is present")
        print("11. Find commonly repeated words")
        print("13. Identify user with longest average message length")
        print("14. Count messages mentioning a user")
        print("15. Remove duplicate messages")
        print("16. Sort messages alphabetically")
        print("17. Extract all questions")
        print("18. Calculate reply ratio between two users")
        print("19. Check for deleted messages")
        print("0. Exit")

        choice = int(input("Choose an option: "))

        if choice == 0:
            print("Exiting...")
            break
        elif choice == 1:
            print("Total messages:", count_messages(messages))
        elif choice == 2:
            print("Unique users:", unique_users(messages))
        elif choice == 3:
            print("Total words:", total_words(messages))
        elif choice == 4:
            print("Average words per message:", round(average_words(messages), 2))
        elif choice == 5:
            print("Longest message:", longest_message(messages))
        elif choice == 6:
            user, count = most_active_user(messages)
            print(f"Most active user: {user} ({count} messages)")
        elif choice == 7:
            user = input("Enter user name: ")
            print(f"Messages sent by {user}:", message_count_user(messages, user))
        elif choice == 8:
            user = input("Enter user name: ")
            result = frequent_word_user(messages, user)
            if result:
                print(f"Most frequent word used by {user}: {result[0]}")
            else:
                print(f"No words found for {user}")
        elif choice == 9:
            user = input("Enter user name: ")
            first, last = first_last_message(messages, user)
            if first:
                print("First message:", first)
                print("Last message:", last)
            else:
                print(f"No messages found for {user}")
        elif choice == 10:
            user = input("Enter user name: ")
            print(f"User '{user}' present:", check_user_present(messages, user))
        elif choice == 11:
            print("Common repeated words:", common_repeated_words(messages))
        elif choice == 13:
            user, avg = longest_avg_message(messages)
            print(f"User with longest avg message: {user} ({round(avg,2)} words)")
        elif choice == 14:
            user = input("Enter user name: ")
            print(f"Messages mentioning '{user}':", mentions_of_user(messages, user))
        elif choice == 15:
            unique_msgs = remove_duplicates(messages)
            print("Unique messages count:", len(unique_msgs))
        elif choice == 16:
            print("Messages sorted alphabetically:", sort_messages(messages))
        elif choice == 17:
            print("Questions in chat:", extract_questions(messages))
        elif choice == 18:
            u1 = input("Enter first user: ")
            u2 = input("Enter second user: ")
            print(f"Reply ratio from {u2} to {u1}: {reply_ratio(messages, u1, u2)} replies")
        elif choice == 19:
            print("Deleted messages found:", deleted_messages(messages))
        else:
            print("Invalid choice!")

if __name__ == "_main_":
    main()