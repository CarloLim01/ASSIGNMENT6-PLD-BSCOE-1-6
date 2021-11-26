# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

first = float(input("\nEnter the first number: "))
second = float(input("Enter the second number: "))
third = float(input("Enter the third number: "))
fourth = float(input("Enter the fourth number: "))

def number_sorter(first, second, third, fourth):
    if first >= second and second >= third and third >= fourth:
        print(f"\nSort from Highest to Lowest: {first}, {second}, {third}, {fourth}")
    elif first >= second and second >= fourth and fourth >= third:
        print(f"\nSort from Highest to Lowest: {first}, {second}, {fourth}, {third}")
    elif first >= third and third >= second and second >= fourth:
        print(f"\nSort from Highest to Lowest: {first}, {third}, {second}, {fourth}")
    elif first >= third and third >= fourth and fourth >= second:
        print(f"\nSort from Highest to Lowest: {first}, {third}, {fourth}, {second}")
    elif first >= fourth and fourth >= second and second >= third:
        print(f"\nSort from Highest to Lowest: {first}, {fourth}, {second}, {third}")
    elif first >= fourth and fourth >= third and third >= second:
        print(f"\nSort from Highest to Lowest: {first}, {fourth}, {third}, {second}")
    elif second >= first and first >= third and third >= fourth:
        print(f"\nSort from Highest to Lowest: {second}, {first}, {third}, {fourth}")
    elif second >= first and first >= fourth and fourth >= third:
        print(f"\nSort from Highest to Lowest : {second}, {first}, {fourth}, {third}")
    elif second >= third and third >= first and first >= fourth:
        print(f"\nSort from Highest to Lowest: {second}, {third}, {first}, {fourth}")
    elif second >= third and third >= fourth and fourth >= first:
        print(f"\nSort from Highest to Lowest: {second}, {third}, {fourth}, {first}")
    elif second >= fourth and fourth >= first and first >= third:
        print(f"\nSort from Highest to Lowest: {second}, {fourth}, {first}, {third}")
    elif second >= fourth and fourth >= third and third >= first:
        print(f"\nSort from Highest to Lowest: {second}, {fourth}, {third}, {first}")
    elif third >= first and first >= second and second >= fourth:
        print(f"\nSort from Highest to Lowest: {third}, {first}, {second}, {fourth}")
    elif third >= first and first >= fourth and fourth >= second:
        print(f"\nSort from Highest to Lowest: {third}, {first}, {fourth}, {second}")
    elif third >= second and second >= first and first >= fourth:
        print(f"\nSort from Highest to Lowest: {third}, {second}, {first}, {fourth}")
    elif third >= second and second >= fourth and fourth >= first:
        print(f"\nSort from Highest to Lowest: {third}, {second}, {fourth}, {first}")
    elif third >= fourth and fourth >= first and first >= second:
        print(f"\nSort from Highest to Lowest: {third}, {fourth}, {first}, {second}")
    elif third >= fourth and fourth >= second and second >= first:
        print(f"\nSort from Highest to Lowest: {third}, {fourth}, {second}, {first}")
