# using a function and arguments to calculate overtime pay for work more than forty hours

def compute_pay(hours, rate):
    if hours > 40:
        pay = (hours-40)*rate*0.5 + (hours*rate)  # calculating overtime pay
        return pay
    else:
        pay = hours*rate   # calculating regular pay
        return pay


try:
    hours_worked = float(input("Enter hours worked:\n"))
    hourly_rate = float(input("Enter hourly rate:\n"))
    pay = compute_pay(hours_worked, hourly_rate)
    print('Pay is: ', pay)
except:
    print("Please enter a numeric figure:\n")
