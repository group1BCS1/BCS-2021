# program asks for billing details and calculates the water bill used in dollars
# main program starts here
while True:
    customer_code = input("Enter customer code:\n")
    initial_reading = input("Enter the beginning meter reading:\n")
    ending_reading = input("Enter the ending meter reading:\n")
    print(f"Customer code: {customer_code}")
    print(f"Beginning meter reading: {initial_reading}")
    print(f"Ending meter reading:{ending_reading}")
