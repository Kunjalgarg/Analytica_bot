print("                        ")

###function for gcd calculation
##def gcd(a, b):
##    while b != 0:
##        a, b = b, a % b
##    return a
##
### Input from user
##num1 = int(input("Enter first number: "))
##num2 = int(input("Enter second number: "))
##
### Prints result
##print("The GCD of", num1, "and", num2, "is:", gcd(num1, num2))

### Function to calculate power
##def power(base, exponent):
##    result = 1
##    for _ in range(abs(exponent)):
##        result *= base
##    if exponent < 0:
##        return 1 / result
##    return result
##
##base = float(input("Enter the base number: "))
##exponent = int(input("Enter the exponent: "))
##
##print(f"{base} raised to the power {exponent} is: {power(base, exponent)}")

##numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
##
##maximum = numbers[0]
##for num in numbers:
##    if num > maximum:
##        maximum = num
##
##print("The maximum number is:", maximum)

##def linear_search(arr, target):
##    for i in range(len(arr)):
##        if arr[i] == target:
##            return i  # Return index if found
##    return -1  # Return -1 if not found
##
##arr = list(map(int, input("Enter elements separated by space: ").split()))
##target = int(input("Enter the number to search: "))
##result = linear_search(arr, target)
##
##if result != -1:
##    print(f"Element found at index {result}")
##else:
##    print("Element not found in the list")

##def binary_search(arr, target):
##    low = 0
##    high = len(arr) - 1
##
##    while low <= high:
##        mid = (low + high) // 2
##
##        if arr[mid] == target:
##            return mid
##        elif arr[mid] < target:
##            low = mid + 1
##        else:
##            high = mid - 1
##
##    return -1
##
##arr = sorted(list(map(int, input("Enter sorted elements separated by space: ").split())))
##target = int(input("Enter the number to search: "))
##
##result = binary_search(arr, target)
##
##if result != -1:
##    print(f"Element found at index {result}")
##else:
##    print("Element not found in the list")

##def selection_sort(arr):
##    n = len(arr)
##    for i in range(n):
##        min_index = i
##        for j in range(i + 1, n):
##            if arr[j] < arr[min_index]:
##                min_index = j
##        # Swap the found minimum element with the first element
##        arr[i], arr[min_index] = arr[min_index], arr[i]
##
##arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
##
##selection_sort(arr)
##print("Sorted list using Selection Sort:", arr)

# Insertion Sort in Python

##def insertion_sort(arr):
##    for i in range(1, len(arr)):
##        key = arr[i]
##        j = i - 1
##        while j >= 0 and key < arr[j]:
##            arr[j + 1] = arr[j]
##            j -= 1
##        arr[j + 1] = key
##
##arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
##
##insertion_sort(arr)
##print("Sorted list using Insertion Sort:", arr)

# Merge Sort in Python

##def merge_sort(arr):
##    if len(arr) > 1:
##        # Find the middle point
##        mid = len(arr) // 2
##        
##        # Divide the array elements into 2 halves
##        left_half = arr[:mid]
##        right_half = arr[mid:]
##
##        # Recursively sort both halves
##        merge_sort(left_half)
##        merge_sort(right_half)
##
##        # Merge the sorted halves
##        i = j = k = 0
##
##        # Copy data to temp arrays left_half[] and right_half[]
##        while i < len(left_half) and j < len(right_half):
##            if left_half[i] < right_half[j]:
##                arr[k] = left_half[i]
##                i += 1
##            else:
##                arr[k] = right_half[j]
##                j += 1
##            k += 1
##
##        # Checking for any leftover elements
##        while i < len(left_half):
##            arr[k] = left_half[i]
##            i += 1
##            k += 1
##
##        while j < len(right_half):
##            arr[k] = right_half[j]
##            j += 1
##            k += 1
##
##arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
##
##merge_sort(arr)
##print("Sorted list using Merge Sort:", arr)

# Program to print first n prime numbers

##def is_prime(num):
##    if num < 2:
##        return False
##    for i in range(2, int(num**0.5) + 1):
##        if num % i == 0:
##            return False
##    return True
##
##def first_n_primes(n):
##    primes = []
##    num = 2
##    while len(primes) < n:
##        if is_prime(num):
##            primes.append(num)
##        num += 1
##    return primes
##
##n = int(input("Enter how many prime numbers you want: "))
##
##print(f"The first {n} prime numbers are:")
##print(first_n_primes(n))

# Program to multiply two matrices

##def multiply_matrices(A, B):
##    # Number of rows and columns
##    rows_A, cols_A = len(A), len(A[0])
##    rows_B, cols_B = len(B), len(B[0])
##    # Check if multiplication is possible
##    if cols_A != rows_B:
##        print("Matrix multiplication not possible! (Columns of A ≠ Rows of B)")
##        return None
##    # Initialize result matrix with zeros
##    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
##    # Perform multiplication
##    for i in range(rows_A):
##        for j in range(cols_B):
##            for k in range(cols_A):
##                result[i][j] += A[i][k] * B[k][j]
##
##    return result
##A = [
##    [1, 2, 3],
##    [4, 5, 6]
##]
##B = [
##    [7, 8],
##    [9, 10],
##    [11, 12]
##]
##result = multiply_matrices(A, B)
##if result:
##    print("Resultant Matrix:")
##    for row in result:
##        print(row)

# Word Count Program (for Python IDLE)

##sentence = input("Enter a sentence: ")
##
##words = sentence.split()
##
##print("Sentence:", sentence)
##print("Word count:", len(words))

# Program to find the most frequent words in a given text

text = input("Enter your text: ")

# Convert to lowercase and split into words
words = text.lower().split()

# Create a dictionary to count word frequencies
freq = {}
for word in words:
    # Remove punctuation from each word
    word = word.strip(",.!?;:\"'()[]{}")
    if word:
        freq[word] = freq.get(word, 0) + 1

sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)

print("\nMost Frequent Words:")
for word, count in sorted_words[:5]:  # top 5 frequent words
    print(f"{word} → {count} times")

































