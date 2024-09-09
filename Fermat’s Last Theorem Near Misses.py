#!/usr/bin/env python
# coding: utf-8

# In[5]:


import math

# Function to find near misses
def find_near_misses(n, k):
    """
    Purpose: This function searches for near misses in the equation x^n + y^n = z^n.
    
    Parameters:
    - n (int): The exponent value provided by the user.
    - k (int): The upper bound for x and y values (10 <= x, y <= k).

    The function iterates over all combinations of x and y, calculates their powers, and finds the closest z value. 
    It then calculates the absolute miss and relative miss and prints the values when a smaller miss is found.
    """
    
    min_relative_miss = float('inf')  # Initialize the smallest relative miss to infinity
    best_x, best_y, best_z = None, None, None  # Variables to store the best x, y, z values found

    # Iterate over x and y values from 10 to k
    for x in range(10, k + 1):
        for y in range(10, k + 1):
            lhs = x**n + y**n  # Calculate x^n + y^n

            # Find z such that z^n <= lhs < (z+1)^n
            z = int(math.pow(lhs, 1/n))  # Find the closest integer z using the nth root of lhs

            # Calculate the absolute miss for z^n and (z+1)^n
            miss1 = abs(lhs - z**n)
            miss2 = abs((z + 1)**n - lhs)

            # Find the smaller miss and calculate the relative miss
            absolute_miss = min(miss1, miss2)
            relative_miss = absolute_miss / lhs  # Calculate the relative size of the miss

            # If a smaller relative miss is found, update and print the result
            if relative_miss < min_relative_miss:
                min_relative_miss = relative_miss
                best_x, best_y, best_z = x, y, z
                # Output the current best values with labels
                print(f"x={x}, y={y}, z={z}, absolute_miss={absolute_miss}, relative_miss={relative_miss*100:.6f}%")
    
    # Final result: Print the smallest miss found after iterating through all possibilities
    print(f"Smallest miss: x={best_x}, y={best_y}, z={best_z}, relative_miss={min_relative_miss*100:.6f}%")

# Main function to get user input
def main():
    """
    Purpose: This function collects input from the user and initiates the search for near misses.
    
    It ensures that the user enters valid values for n (3 <= n <= 11) and k (k > 10), then calls the 
    find_near_misses function to perform the search and output the results.
    """
    
    print("Welcome to Fermat's Last Theorem Near Miss Finder")
    
    # Print the names of the programmers
    print("Programmed by:")
    print("Kommana Vasundhara and Gopavarapu Ajay\n")

    # Input validation for n and k
    while True:
        try:
            n = int(input("Enter a value for n (3 <= n <= 11): "))  # Input for n
            if 3 <= n <= 11:
                break
            else:
                print("n must be between 3 and 11.")
        except ValueError:
            print("Please enter an integer.")

    while True:
        try:
            k = int(input("Enter a value for k (k > 10): "))  # Input for k
            if k > 10:
                break
            else:
                print("k must be greater than 10.")
        except ValueError:
            print("Please enter an integer.")

    # Call the function to find near misses with the user input values
    find_near_misses(n, k)

# Run the program
if __name__ == "__main__":
    main()  # Main function call to start the program


# In[ ]:




