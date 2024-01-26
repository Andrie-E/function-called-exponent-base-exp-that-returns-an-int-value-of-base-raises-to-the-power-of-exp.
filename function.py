# Write a function-called-exponent-base-exp-that-returns-an-int-value-of-base-raises-to-the-power-of-exp

# Pseudocode
    
# Function
def exponents(base, exp):
    result = 1
# Multiply base by itself exp times
    for _ in range(exp):
        result *= base
    
    return result
base_1, exp_1 = 2, 5
base_2, exp_2 = 5, 4

result_number1 = exponents(base_1, exp_1)
result_number2 = exponents(base_2, exp_2)
# Print result
print (f" base is = {base_1}")
print (f"exponent is = {exp_1}")
print(f"{base_1} raises to the power of {exp_1} is: {result_number1}")
print (f" base is = {base_2}")
print (f"exponent is = {exp_2}")
print(f"{base_2} raises to the power of {exp_2} is: {result_number2}")