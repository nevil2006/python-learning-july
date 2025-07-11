#   Ask a user for a number. Print whether it's positive, negative, or zero.
n = int(input("Enter a number: "))

if n > 0:
    print(n, "is a positive number")
elif n < 0:
    print(n, "is a negative number")
else:
    print(n, "is zero")

# Take a user's score (0–100) and print their grade: A, B, C, D, or Fail (use multiple elif branches).

score = int(input("Enter your score (0–100): "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: Fail")

# 3. Traffic Light Simulator
light_color = input("Enter the traffic light color (red, yellow, green): ").lower()

if light_color == "red":
    print("Action: Stop")
elif light_color == "yellow":
    print("Action: Wait")
elif light_color == "green":
    print("Action: Go")
else:
    print("Invalid color. Please enter red, yellow, or green.")
