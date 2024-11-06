# CONDITIONS
# 1
a: float = float(input("Enter the first number: "))
b: float = float(input("Enter the second number: "))
if a < b:
    print(a)
    print(a)
    print(a)
else:
    print(b)
    print(b)
    print(b)

# 2
c: int = int(input("Enter the first number: "))
d: int = int(input("Enter the second number: "))
print((c + d) / 2)

# 3
num1: int = int(input("Enter a number: "))
num2: int = int(input("Enter a number: "))
num3: int = int(input("Enter a number: "))
if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num3:
    print(num2)
else:
    print(num3)

# 4
movie: int = int(input("What is the length of movie in minutes? "))
hours: int = movie // 60
minutes: int = movie % 60
print(f"The length of movie is {hours} hour(s) and {minutes} minute(s)")

# 7
g: int = int(input("Enter a 2-digit number: "))
tens: int = g // 10
units: int = g % 10
print(f"The sum of units and tens is {tens + units}")

# 8
h: int = int(input("Enter a 2-digit number: "))
tens: int = h // 10
units: int = h % 10
new_h: int = units * 10 + tens
print(f"The new number is {new_h}")

# 9
i: int = int(input("Enter a number: "))
print("Even" if i % 2 == 0 else "Odd")

# LOOPS
# 1
top: int = int(input("Enter a number: "))
while True:
    if top < 0:
        print("The number must be positive")
        continue
    else:
        for n in range(1, top + 1):
            print(n, end=" ")
        break
print()

# 2
a: int = int(input("Enter the first number: "))
b: int = int(input("Enter the second number: "))
if a < b:
    for n in range(a, b + 1):
        print(n, end=" ")
else:
    for n in range(b, a + 1):
        print(n, end=" ")
print()

# DATA PROCESSING
# 1
nums: list[int] = []
while True:
    num: int = int(input("Enter the number: "))
    if num == -99:
        print("None")
        break
    nums.append(num)
print(f"The sum of the numbers is {sum(nums)}")

# 2
SENTINEL: int = -99
nums: list[int] = []
while True:
    num: int = int(input("Enter a number: "))
    if num < 0 or num == 0:
        break
    if num == SENTINEL:
        print(None)
        break
    nums.append(num)
print(f"The maximum number is {max(nums)}, the minimum number is {min(nums)}")

# 3
nums: list[int] = []
for i in range(1, 5 + 1):
    num: int = int(input("Enter a number: "))
    nums.append(num)
print(f"The biggest number is on the {nums.index(max(nums))} place")

# COMPLEX LOOPS
# 1
min_temp: int = -5
max_temp: int = 40
temperatures: list[int] = []
temperature: int = None
counter: int = 0
while True:
    try:
        temperature: int = int(input("Enter a temperature in Tel Aviv this month: "))
        counter += 1
        if not min_temp <= temperature <= max_temp:
            print("Wrong data")
            break
        if counter == 12:
            break
        else:
            print("Correct data")
        temperatures.append(temperature)
        if temperature == 0 and temperatures[-1] == 0:
            continue
    except ValueError as e:
        print("Only numbers are acceptable")
        break
print(f"The average temperature of the 2023 is {sum(temperatures) / len(temperatures):.2f}")
print(f"The highest temperature was {max(temperatures)}, the lowest temperature was {min(temperatures)}")
