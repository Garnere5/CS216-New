# ** p4.py **
# ** Earl Garner **
# ** 2 - 17 - 2026 **
# sentinel-controlled loop to determine high, low, average
# bowling scores

min = 301
max = -1
numberBowlers = 1
totalScore = 0
score = 0

# Processing using Sentinel loop


while score != -1:
    score = int(input(f"Enter score {numberBowlers} (or -1 to quit): "))
    if score > -1 and score < 301:
        if score > max:
            max = score
        if score < min:
            min = score
        numberBowlers += 1
        totalScore += score
    else:
        print("Error: Invalid score, Expecting 0-300")


# ** add your code here **
if score == -1:
    numberBowlers -= 1  # Subtract 1 to exclude the sentinel value
    avg = totalScore / numberBowlers  # Calculate average score

    
# Output
print()
print(f"Number of Bowlers: {numberBowlers}")
print(f"High Score: {max}")
print(f"Low Score: {min}")
print(f"Avg Score: {avg:.2f}")