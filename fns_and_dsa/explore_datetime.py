from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()  # get current date & time
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

# Part 2: Calculate a Future Date
def calculate_future_date():
    # Prompt user for number of days
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    
    # Get today's date
    current_date = datetime.now()
    
    # Add days using timedelta
    future_date = current_date + timedelta(days=days_to_add)
    
    # Print in YYYY-MM-DD format
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date

# Run both parts
display_current_datetime()
calculate_future_date()
