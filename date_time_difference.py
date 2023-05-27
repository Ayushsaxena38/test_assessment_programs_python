from datetime import datetime, timedelta

def date_difference(from_date, to_date, difference):
    # Convert the date strings to datetime objects
    from_date = datetime.strptime(from_date, '%y-%m-%d')
    to_date = datetime.strptime(to_date, '%y-%m-%d')

    # Calculate the difference in days between the two dates
    delta = to_date - from_date

    # Check if the difference is less than the specified number of days
    if delta < timedelta(days=difference):
        return True
    else:
        return False