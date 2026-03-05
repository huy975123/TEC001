import random

N_str = input("How many random points to generate? ")
N = int(N_str)
n = 0

for i in range(N):
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)
    
    if (x**2 + y**2) < 1:
        n = n + 1

pi_approx = 4 * n / N
print("Approximation of pi:", pi_approx)
