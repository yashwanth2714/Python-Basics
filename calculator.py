# x = int(input("What's x? "))
# y = int(input("What's y? "))

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

# Format the output with commas as thousands separators
# The :, format specifier adds commas as thousands separators
print(f"{z:,}")

a = x / y

# Format the output to 4 decimal places
# The :.4f format specifier formats the number to 4 decimal places
print (f"{a:.4f}")
