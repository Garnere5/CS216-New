#    Program: P1 IPO Steps
#    Date: 1 -15 - 2026
#    Author: Earl Garner
#    Description: Our set variable is 10,000 steps and we need to determine if we're over or under 10,000.
# Once we determine how many steps, we determine the strides of each step in inches and convert them to miles.
# The program will calculate and determine how many miles you walked and will show us the result.

# input
initalsteps = 10000
print("Enter the number of steps you walked today:")
steps = int(input())
print("Enter the length of your stride in inches:")
stride = int(input())

#processing
feet = float(steps * stride / 12)
miles = float(f"{feet / 5280:.2f}")


# output 
if steps > initalsteps:
    total = steps - initalsteps
    print("You walked " + str(total) + " over 10,000 steps.")
elif steps < initalsteps:
    total = initalsteps - steps
    print("You walked " + str(total) + " under 10,000 steps.")
else:
    print("You walked exactly 10,000 steps.")

print("You walked a total of", miles, "miles today.")
