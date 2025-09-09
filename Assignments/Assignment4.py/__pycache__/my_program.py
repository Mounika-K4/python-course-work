# my_programs.py

def swap_numbers():
    print("Program: Swap Two Numbers")
    print(""" 
def swap(a, b):
    a, b = b, a
    return a, b
    """)
    print("Test Case 1: swap(10, 20) -> (20, 10)")
    print("Test Case 2: swap(5, -1) -> (-1, 5)")
    print("Explanation: This uses tuple unpacking to swap values without a temporary variable.")


def armstrong_number():
    print("Program: Check Armstrong Number")
    print(""" 
def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    return n == sum(int(digit) ** power for digit in num_str)
    """)
    print("Test Case 1: is_armstrong(153) -> True")
    print("Test Case 2: is_armstrong(123) -> False")
    print("Explanation: Each digit is raised to the number of digits and summed. If equal, it's Armstrong.")


def gcd_two_numbers():
    print("Program: GCD of Two Numbers")
    print(""" 
import math
def gcd(a, b):
    return math.gcd(a, b)
    """)
    print("Test Case 1: gcd(48, 18) -> 6")
    print("Test Case 2: gcd(100, 25) -> 25")
    print("Explanation: Uses math.gcd to find the greatest common divisor.")


def reverse_number():
    print("Program: Reverse a Number")
    print(""" 
def reverse_num(n):
    return int(str(n)[::-1])
    """)
    print("Test Case 1: reverse_num(1234) -> 4321")
    print("Test Case 2: reverse_num(500) -> 5")
    print("Explanation: Converts number to string, reverses, then back to int.")


def sum_of_digits():
    print("Program: Sum of Digits")
    print(""" 
def sum_digits(n):
    return sum(int(digit) for digit in str(n))
    """)
    print("Test Case 1: sum_digits(123) -> 6")
    print("Test Case 2: sum_digits(987) -> 24")
    print("Explanation: Loops through digits and sums them.")


def count_vowels():
    print("Program: Count Vowels in String")
    print(""" 
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for ch in s if ch in vowels)
    """)
    print("Test Case 1: count_vowels('hello') -> 2")
    print("Test Case 2: count_vowels('PYTHON') -> 1")
    print("Explanation: Counts characters if they are vowels.")


def count_words():
    print("Program: Count Words in a Sentence")
    print(""" 
def word_count(s):
    return len(s.split())
    """)
    print("Test Case 1: word_count('Hello world') -> 2")
    print("Test Case 2: word_count('Python is fun to learn') -> 5")
    print("Explanation: Splits sentence by spaces and counts words.")


def decimal_to_binary():
    print("Program: Convert Decimal to Binary")
    print(""" 
def dec_to_bin(n):
    return bin(n)[2:]
    """)
    print("Test Case 1: dec_to_bin(10) -> '1010'")
    print("Test Case 2: dec_to_bin(255) -> '11111111'")
    print("Explanation: Uses Python's built-in bin() function and removes prefix '0b'.")


def factorial():
    print("Program: Factorial of a Number")
    print(""" 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
    """)
    print("Test Case 1: factorial(5) -> 120")
    print("Test Case 2: factorial(0) -> 1")
    print("Explanation: Uses recursion to multiply descending numbers.")


def fibonacci_series():
    print("Program: Fibonacci Series")
    print(""" 
def fibonacci(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]
    """)
    print("Test Case 1: fibonacci(5) -> [0, 1, 1, 2, 3]")
    print("Test Case 2: fibonacci(7) -> [0, 1, 1, 2, 3, 5, 8]")
    print("Explanation: Adds previous two numbers to generate series.")


def palindrome_check():
    print("Program: Palindrome Check")
    print(""" 
def is_palindrome(s):
    return s == s[::-1]
    """)
    print("Test Case 1: is_palindrome('madam') -> True")
    print("Test Case 2: is_palindrome('hello') -> False")
    print("Explanation: Compares string with its reverse.")


def prime_check():
    print("Program: Prime Number Check")
    print(""" 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
    """)
    print("Test Case 1: is_prime(7) -> True")
    print("Test Case 2: is_prime(9) -> False")
    print("Explanation: Checks divisibility up to square root of n.")


def largest_element():
    print("Program: Largest Element in a List")
    print(""" 
def largest(lst):
    return max(lst)
    """)
    print("Test Case 1: largest([1, 5, 2, 9]) -> 9")
    print("Test Case 2: largest([-1, -5, -3]) -> -1")
    print("Explanation: Uses max() to find largest element.")


def string_title_case():
    print("Program: Convert String to Title Case")
    print(""" 
def to_title_case(s):
    return s.title()
    """)
    print("Test Case 1: to_title_case('hello world') -> 'Hello World'")
    print("Test Case 2: to_title_case('python PROGRAM') -> 'Python Program'")
    print("Explanation: Uses built-in title() method.")


def custom_sort():
    print("Program: Custom Sort (Descending)")
    print(""" 
def custom_sort(lst):
    return sorted(lst, reverse=True)
    """)
    print("Test Case 1: custom_sort([3, 1, 4]) -> [4, 3, 1]")
    print("Test Case 2: custom_sort(['b','a','c']) -> ['c','b','a']")
    print("Explanation: Uses sorted() with reverse=True for descending order.")