# Program: p2.py
# Date: 1-28-2026
# Author: Earl Garner
# Description: Calculates miles walked from steps and stride length,
# and reports how far over or under 10,000 steps. Demonstrates use of return functions.


#Function

def get_steps():
    steps = int(input())
    return steps

def get_stride_inches():
    stride_inches = int(input())
    return stride_inches

def calculate_miles(steps, stride_inches):
    feet = (steps * stride_inches) / 12
    miles = feet / 5280
    return miles

def additional_steps_needed(steps):
    additional = steps
    return additional

def miles_output_line(steps, miles):
    msg = f"You walked {steps:,} steps which is {miles:.2f} miles"
    return msg

def steps_output_line(additional):
    if additional > 0:
        msg = f"You need {additional:,} more steps to reach 10,000"
    elif additional < 0:
        msg = f"You were {abs(additional):,} steps over 10,000"
    else:
        msg = "You walked exactly 10,000 steps"
    
    return msg

# +-----do not modify this section-----+
# main program
def main():

    #input
    steps = get_steps()
    stride_inches = get_stride_inches()

    #processing
    miles = calculate_miles(steps, stride_inches)
    additional = additional_steps_needed(steps)

    #output
    print( miles_output_line(steps, miles) )
    print( steps_output_line(additional) )

    if __name__ == "__main__":
        main()

# ------do not modify this section-----+
