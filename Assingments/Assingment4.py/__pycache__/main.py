# main.py

import my_program as mp

def menu():
    while True:
        print("\n------ FUNCTION MENU ------")
        print("1. Swap Two Numbers")
        print("2. Armstrong Number")
        print("3. GCD of Two Numbers")
        print("4. Reverse a Number")
        print("5. Sum of Digits")
        print("6. Count Vowels in String")
        print("7. Count Words in Sentence")
        print("8. Convert Decimal to Binary")
        print("9. Factorial of Number")
        print("10. Fibonacci Series")
        print("11. Palindrome Check")
        print("12. Prime Check")
        print("13. Largest Element in List")
        print("14. Convert String to Title Case")
        print("15. Custom Sort (Descending)")
        print("0. Exit")
        print("----------------------------")
        
        choice = input("Enter your choice: ")
        
        if choice == "1": mp.swap_numbers()
        elif choice == "2": mp.armstrong_number()
        elif choice == "3": mp.gcd_two_numbers()
        elif choice == "4": mp.reverse_number()
        elif choice == "5": mp.sum_of_digits()
        elif choice == "6": mp.count_vowels()
        elif choice == "7": mp.count_words()
        elif choice == "8": mp.decimal_to_binary()
        elif choice == "9": mp.factorial()
        elif choice == "10": mp.fibonacci_series()
        elif choice == "11": mp.palindrome_check()
        elif choice == "12": mp.prime_check()
        elif choice == "13": mp.largest_element()
        elif choice == "14": mp.string_title_case()
        elif choice == "15": mp.custom_sort()
        elif choice == "0":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 0–15.")

if __name__ == "_main_":
    menu()