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
    stride = int(input())
    return stride

def calculate_miles(steps, stride):
    feet = float(steps * stride / 12)
    miles = float(f"{feet / 5280:.2f}")
    return miles

def additional_steps_needed(steps):
    if steps > 10000:
        additional = steps - 10000
    else:
        additional = 10000 - steps
    return additional

def miles_output_line(steps, miles):
    msg = f"You walked {steps} steps which is {miles} miles"
    return msg

def steps_output_line(additional):
    if additional > 10000:
        msg = f"You were {additional} steps over 10,000"
    if additional < 10000:
         msg = f"You need {additional} more steps to reach 10,000"
    else:
       msg = "you walked exactly 10,000 steps"
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
