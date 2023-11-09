import random
import time
import os

def generate_arithmetic_expression():
    operators = ['+', '-', '*', '/']
    X = random.randint(1, 9)
    O = random.choice(operators)
    Y = random.randint(1, 9)
    return f"{X} {O} {Y}"

N = random.randint(120, 180)

for _ in range(N):
        expression = generate_arithmetic_expression()
        print(expression, flush = True)
        time.sleep(1)
        
  
