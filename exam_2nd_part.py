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

# 5
e: int = int(input("Enter a 4-digit number: "))
num1: int = e % 1000
num2: int = num1 % 100
num3: int = num2 % 10
print(num3)

# 6
f: int = int(input("Enter a number: "))
num1: int = f % 1000
num2: int = f % 100
num3: int = num2 // 10
print(num3)

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

# 10
salary: float = float(input("What is your salary per month? "))
tax: float = 0
if salary <= 6000:
    print("You don't need to pay a tax")
elif 6000 < salary <= 12000:
    tax = salary * 10 / 100
    print(f"You'll pay {tax:.2f} shekels tax")
elif 12000 < salary <= 18000:
    tax = salary * 20 / 100
    print(f"You'll pay {tax:.2f} shekels tax")
elif 18000 < salary <= 25000:
    tax = salary * 30 / 100
    print(f"You'll pay {tax:.2f} shekels tax")
elif 25000 < salary <= 35000:
    tax = salary * 40 / 100
    print(f"You'll pay {tax:.2f} shekels tax")
elif 35000 < salary <= 50000:
    tax = salary * 40 / 100
    print(f"You'll pay {tax:.2f} shekels tax")
else:
    tax = salary * 51 / 100
    print(f"You'll pay {tax:.2f} shekels tax")

# 11
age: int = int(input("Enter your age: "))
height: int = int(input("Enter your height in cm: "))
if 8 <= age <= 18 and height >= 115 or age > 18 and height >= 100:
    print("You can ride a roller-coaster")
else:
    print("You can't ride a roller-coaster")

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

# 3
n: int = int(input("Enter a number: "))
for i in range(0, n + 1):
    print(i if i % 2 == 0 else "", end=" ")
print()

# 4
max_num: int = int(input("Enter a number: "))
den: int = int(input("Enter a number: "))
for i in range(1, max_num + 1):
    print(i if i % den == 0 else "", end=" ")
print()

# DATA PROCESSING

# 1 (this time I tried to do this exercise without using lists)
sum_nums: int = 0
SENTINEL = None
while True:
    num: int = int(input("Enter a number: "))
    if num == -99:
        num = SENTINEL
        print(num)
        break
    else:
        sum_nums += num
print(f"The sum of numbers is {sum_nums}")

# 2 (this time I tried to do this exercise without using lists)
min_num: int = None
max_num: int = None
SENTINEL = None
while True:
    num: int = int(input("Enter a number: "))
    if num == -99:
        num = SENTINEL
        print(num)
        break
    if num <= 0:
        break
    else:
        max_num = num if not max_num or num > max_num else max_num
        min_num = num if not min_num or num < min_num else min_num
print(f"The minimum number is {min_num}\n"
      f"The maximum number is {max_num}")

# 3 (this time I tried to do this exercise without using lists)
max_num: float = 0
place: int = 0
for i in range(1, 6):
    num: int = int(input("Enter a number: "))
    if num > max_num:
        max_num = num
        place = i
print(f"The biggest number is {max_num} and it's on the {place} place")

# 4
x: int = int(input("Enter the first number: "))
y: int = int(input("Enter the second number: "))
for i in range(0, (x * y) + 1, x):
    x += y
    print(i, end=" ")
print()

# 5
number: int = int(input("Enter the number: "))
power: int = int(input("Enter the power: "))
result: int = 1
for _ in range(power):
    result *= number
print(f"The number {number} to the power of {power} is equal to {result}")

# 8
prime: int = int(input("Enter a number: "))
for i in range(2, prime + 1):
    if prime % i == 0:
        print("The number is not prime")
        break
    else:
        print("The number is prime")
        break

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

# 2
topic: str = input("What is the topic of voting? ")
list1: list[int] = []
opinions: list[int] = [0, 0, 0, 0]
opinion: int = None
while True:
    try:
        opinion: int = int(input("What is your opinion? 1. For; 2. Against; 3.Abstained; 4. Veto: "))
        list1.append(opinion)
        if len(opinions) == 44:
            break
        if opinion < 1 or opinion > 4:
            continue
        if opinion == 1:
            opinions[0] += 1
        elif opinion == 2:
            opinions[1] += 1
        elif opinion == 3:
            opinions[2] += 1
        elif opinion == 4:
            print(f"The country number {len(list1)} voted 'Veto'. The voting stopped.")
            break
    except ValueError:
        print("Numbers only are acceptable")
        continue
print(f"Statistics of opinions:\n"
      f"1. For - {opinions[0]}\n"
      f"2. Against - {opinions[1]}\n"
      f"3. Abstained - {opinions[2]}\n"
      f"The number of country that was the first that voted 'For' is {list1.index(1) + 1}")
