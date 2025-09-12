# WhatsApp Chat Data Analysis Assignment

def average_words(messages):
    return total_words(messages) / len(messages) if messages else 0

def reply_ratio(messages, user1, user2):
    """Count how many times user2 replies immediately after user1"""
    count = 0
    for i in range(1, len(messages)):
        if messages[i-1].lower().startswith(user1.lower() + ":") and messages[i].lower().startswith(user2.lower() + ":"):
            count += 1
    return count

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
        print("12. Identify user with shortest average message length")   # new
        print("13. Identify user with longest average message length")
        print("14. Count messages mentioning a user")
        print("15. Remove duplicate messages")
        print("16. Sort messages alphabetically")
        print("17. Extract all questions")
        print("18. Calculate reply count between two users")
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
        elif choice == 12:
            # new feature: shortest avg message
            user, avg = min(longest_avg_message(messages), key=lambda x: x[1])
            print(f"User with shortest avg message: {user} ({round(avg,2)} words)")
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
            print(f"Replies from {u2} to {u1}: {reply_ratio(messages, u1, u2)}")
        elif choice == 19:
            print("Deleted messages found:", deleted_messages(messages))
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
