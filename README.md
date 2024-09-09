# Fermat-s-Last-Theorem-Near-Misses
# Fermat's Last Theorem Near Miss Finder

## Description
This Python program helps users search for "near misses" for Fermat's Last Theorem. Fermat's Last Theorem states that there are no natural numbers \( x \), \( y \), and \( z \) such that:

\[ x^n + y^n = z^n \]

for any integer \( n > 2 \). This program systematically looks for combinations of \( x \), \( y \), and \( z \) that are "near misses" to the equation, where the difference between \( x^n + y^n \) and \( z^n \) is relatively small.

### How it works:
- The user provides:
  - \( n \): the power used in the equation, where \( 3 \leq n \leq 11 \).
  - \( k \): the upper limit for \( x \) and \( y \) values, where \( k > 10 \).
- The program searches for all combinations of \( x \), \( y \), and \( z \), computes their respective powers, and identifies where \( x^n + y^n \) is close to \( z^n \), but not equal.
- It calculates the relative miss percentage and prints out the best combinations of \( x \), \( y \), and \( z \) found.

## Features
- **Interactive Input**: The user enters values for \( n \) and \( k \).
- **Near Miss Calculation**: The program finds the smallest relative miss and prints the corresponding values of \( x \), \( y \), and \( z \).
- **Programmed by**: Kommana Vasundhara and Gopavarapu Ajay.

## How to Run
1. **Clone the repository**:
   ```bash
   git clone https://github.com/AjayGopavarapu/Fermat-s-Last-Theorem-Near-Misses.git
   cd Fermat-s-Last-Theorem-Near-Misses
## Run the Python script:

Open a terminal and run
python fermat_near_miss.py
## Follow the prompts:

Enter values for 
𝑛
n and 
𝑘
k when prompted.
# Example Run:
Welcome to Fermat's Last Theorem Near Miss Finder
Programmed by:
Kommana Vasundhara and Gopavarapu Ajay

Enter a value for n (3 <= n <= 11): 3
Enter a value for k (k > 10): 15
x=10, y=10, z=14, absolute_miss=91, relative_miss=0.052503%
x=12, y=12, z=17, absolute_miss=211, relative_miss=0.073087%
...
Smallest miss: x=14, y=12, z=18, relative_miss=0.042113%
