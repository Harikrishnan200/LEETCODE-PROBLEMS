def find_gcd(a, b):
    # Euclidean algorithm to find GCD
    while b != 0:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    # Formula => LCM(a, b) = abs(a * b) // GCD(a, b)  
    return abs(a * b) // find_gcd(a, b)

# Input two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Find GCD and LCM
gcd = find_gcd(num1, num2)
lcm = find_lcm(num1, num2)

# Print the results
print(f"GCD of {num1} and {num2} is: {gcd}")
print(f"LCM of {num1} and {num2} is: {lcm}")






# int find_gcd(int a, int b) {
#     while (b != 0) {
#         /*
#         int temp = b;
#         b = a % b;
#         a = temp;  
#         */
#       int  temp = a % b;
#         a = b;
#         b = temp;
#     }
#     return a;
# }