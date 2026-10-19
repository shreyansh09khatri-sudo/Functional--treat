import math

data = []

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def statistics(data):
    return min(data), max(data), sum(data), sum(data) / len(data)

while True:
    print("\nWelcome to the Data Analyzer and Transformer Program")
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Calculate Factorial")
    print("4. Filter Data by Threshold")
    print("5. Sort Data")
    print("6. Display Dataset Statistics")
    print("7. Exit Program")

    choice = int(input("Please enter your choice: "))

    if choice == 1:
        data = list(map(int, input("Enter data separated by spaces: ").split()))
        print("Data has been stored successfully!")

    elif choice == 2:
        if data:
            print("Total elements:", len(data))
            print("Minimum value:", min(data))
            print("Maximum value:", max(data))
            print("Sum of all values:", sum(data))
            print("Average value:", round(sum(data) / len(data), 2))
        else:
            print("Please input data first.")

    elif choice == 3:
        n = int(input("Enter a number to calculate its factorial: "))
        if n < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print("Factorial of", n, "is:", factorial(n))

    elif choice == 4:
        if data:
            threshold = int(input("Enter threshold value: "))
            result = list(filter(lambda x: x >= threshold, data))
            print("Filtered Data:", result)
        else:
            print("Please input data first.")

    elif choice == 5:
        if data:
            print("1. Ascending")
            print("2. Descending")
            option = int(input("Enter your choice: "))

            if option == 1:
                print("Sorted Data:", sorted(data))
            elif option == 2:
                print("Sorted Data:", sorted(data, reverse=True))
            else:
                print("Invalid sorting choice.")
        else:
            print("Please input data first.")

    elif choice == 6:
        if data:
            minimum, maximum, total, average = statistics(data)
            print("Dataset Statistics:")
            print("Minimum value:", minimum)
            print("Maximum value:", maximum)
            print("Sum of all values:", total)
            print("Average value:", round(average, 2))
        else:
            print("Please input data first.")

    elif choice == 7:
        print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")