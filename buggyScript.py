# Python script with bugs

import datetme  # Incorrect spelling of datetime

def get_current_date_time():
    return datetme.datetime.now().strftime("%Y-%m-%D %H:%M:%S")

def add_days(n):
    return datetme.datetime.now() + datetime.timedelta(days=n)

def subtract_days(n):
    return datetime.datetime.now() - datetime.timedelta(days=n)

if __name__ == "__main__":
    print(get_current_date_time())
    print(add_days(5))  # There's no date formatting as per the requirements
    print(subtract_days(3))  # There's no date formatting as per the requirements
    print(subtract_days('3'))  # This will throw a TypeError because the argument is a string
