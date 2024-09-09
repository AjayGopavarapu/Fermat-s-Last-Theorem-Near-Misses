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
Welcome to Fermat's Last Theorem Near Miss Finder
Programmed by:
Kommana Vasundhara and Gopavarapu Ajay
''' bash
Enter a value for n (3 <= n <= 11): 5
Enter a value for k (k > 10): 45
x=10, y=10, z=11, absolute_miss=38949, relative_miss=19.474500%
x=10, y=11, z=12, absolute_miss=12219, relative_miss=4.680695%
x=10, y=19, z=19, absolute_miss=100000, relative_miss=3.881838%
x=10, y=20, z=20, absolute_miss=100000, relative_miss=3.030303%
x=10, y=21, z=21, absolute_miss=100000, relative_miss=2.390000%
x=10, y=22, z=22, absolute_miss=100000, relative_miss=1.903445%
x=10, y=23, z=23, absolute_miss=100000, relative_miss=1.529907%
x=10, y=24, z=24, absolute_miss=100000, relative_miss=1.240291%
x=10, y=25, z=25, absolute_miss=100000, relative_miss=1.013621%
x=10, y=26, z=26, absolute_miss=100000, relative_miss=0.834629%
x=10, y=27, z=27, absolute_miss=100000, relative_miss=0.692094%
x=10, y=28, z=28, absolute_miss=100000, relative_miss=0.577688%
x=10, y=29, z=29, absolute_miss=100000, relative_miss=0.485174%
x=10, y=30, z=30, absolute_miss=100000, relative_miss=0.409836%
x=10, y=31, z=31, absolute_miss=100000, relative_miss=0.348079%
x=10, y=32, z=32, absolute_miss=100000, relative_miss=0.297138%
x=10, y=33, z=33, absolute_miss=100000, relative_miss=0.254872%
x=10, y=34, z=34, absolute_miss=100000, relative_miss=0.219609%
x=10, y=35, z=35, absolute_miss=100000, relative_miss=0.190035%
x=10, y=36, z=36, absolute_miss=100000, relative_miss=0.165109%
x=10, y=37, z=37, absolute_miss=100000, relative_miss=0.144001%
x=10, y=38, z=38, absolute_miss=100000, relative_miss=0.126048%
x=10, y=39, z=39, absolute_miss=100000, relative_miss=0.110712%
x=10, y=40, z=40, absolute_miss=100000, relative_miss=0.097561%
x=10, y=41, z=41, absolute_miss=100000, relative_miss=0.086239%
x=10, y=42, z=42, absolute_miss=100000, relative_miss=0.076458%
x=10, y=43, z=43, absolute_miss=100000, relative_miss=0.067977%
x=10, y=44, z=44, absolute_miss=100000, relative_miss=0.060600%
x=10, y=45, z=45, absolute_miss=100000, relative_miss=0.054163%
x=13, y=16, z=17, absolute_miss=12, relative_miss=0.000845%
Smallest miss: x=13, y=16, z=17, relative_miss=0.000845%
