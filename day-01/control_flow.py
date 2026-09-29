# Write day-01/control_flow.py that does all of this:
# Part A — Grading (uses if/elif/else)
# Ask for a marks value (inline int cast). Print the grade:

# >= 90 → "A"
# >= 80 → "B"
# >= 70 → "C"
# >= 60 → "D"
# otherwise → "F"

# Part B — Even numbers (uses for)
# Loop from 1 to 20 (inclusive) and print only the even numbers. Use % 2 == 0 inside an if.

# Part C — Countdown (uses while)
# Ask for a number, then count down to 0 printing each value, then print "Liftoff!".

# Part D — Multiples
# Ask for a number n, then use a for loop to print the first 5 multiples of n (i.e. n*1 through n*5).

# Rules:
# Inline casts, snake_case, f-strings where it helps.
# No break/continue needed yet.


marks = int(input("Enter your marks: "))
if marks >=90:
    print("A")
elif marks >=80:
    print("B")
elif marks >=70:
    print("C")
elif marks >=60:
    print("D")
else:
    print("F")


for num in range(1, 21):
    if num%2==0:
        print(num)

ask_num= int(input("Enter a number to countdown from: "))
while ask_num>=0:
    print(ask_num)
    ask_num-=1
print("Liftoff!")


num_multiples= int(input("Enter a number to print its first 5 multiples: "))
for i in range(1,6):
    print(f"{num_multiples} * {i} = {num_multiples * i}")
