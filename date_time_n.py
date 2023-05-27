from datetime import datetime, timedelta

def calculate_previous_date(date, n):
    # Convert the date string to a datetime object
    date_obj = datetime.strptime(date, '%y-%m-%d')

    # Calculate the previous date by subtracting n days
    previous_date = date_obj - timedelta(days=n)

    # Convert the previous date back to a string representation
    previous_date_str = previous_date.strftime('%y-%m-%d')

    return previous_date_str