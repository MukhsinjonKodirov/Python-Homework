from datetime import datetime, timedelta
import re
import time
import pytz

def age_calculator():
    birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    today = datetime.today()
    years = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    months = (today.month - birthdate.month) % 12
    days = (today - birthdate.replace(year=today.year)).days if today.day >= birthdate.day else (today - birthdate.replace(year=today.year, month=today.month-1)).days
    print(f"Age: {years} years, {months} months, {days} days")

def days_until_next_birthday():
    birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    today = datetime.today()
    next_birthday = birthdate.replace(year=today.year)
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)
    days_remaining = (next_birthday - today).days
    print(f"Days until next birthday: {days_remaining}")

def meeting_scheduler():
    current_date_time = input("Enter the current date and time (YYYY-MM-DD HH:MM): ")
    duration_hours = int(input("Enter meeting duration (hours): "))
    duration_minutes = int(input("Enter meeting duration (minutes): "))
    current_datetime = datetime.strptime(current_date_time, "%Y-%m-%d %H:%M")
    meeting_end = current_datetime + timedelta(hours=duration_hours, minutes=duration_minutes)
    print(f"Meeting ends at: {meeting_end}")

def timezone_converter():
    date_time = input("Enter date and time (YYYY-MM-DD HH:MM): ")
    from_tz = input("Enter your current timezone (e.g., UTC, US/Eastern): ")
    to_tz = input("Enter the target timezone: ")
    from_timezone = pytz.timezone(from_tz)
    to_timezone = pytz.timezone(to_tz)
    datetime_obj = from_timezone.localize(datetime.strptime(date_time, "%Y-%m-%d %H:%M"))
    converted_time = datetime_obj.astimezone(to_timezone)
    print(f"Converted time: {converted_time}")

def countdown_timer():
    future_datetime = input("Enter future date and time (YYYY-MM-DD HH:MM:SS): ")
    future_time = datetime.strptime(future_datetime, "%Y-%m-%d %H:%M:%S")
    while True:
        remaining_time = future_time - datetime.now()
        if remaining_time.total_seconds() <= 0:
            print("Time's up!")
            break
        print(f"Time remaining: {remaining_time}")
        time.sleep(1)

def email_validator():
    email = input("Enter an email address: ")
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    print("Valid email" if re.match(pattern, email) else "Invalid email")

def phone_number_formatter():
    phone = input("Enter a phone number: ")
    cleaned = re.sub(r"\D", "", phone)
    formatted = f"({cleaned[:3]}) {cleaned[3:6]}-{cleaned[6:]}" if len(cleaned) == 10 else "Invalid number"
    print(formatted)

def password_strength_checker():
    password = input("Enter a password: ")
    length = len(password) >= 8
    upper = any(c.isupper() for c in password)
    lower = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)
    print("Strong password" if all([length, upper, lower, digit]) else "Weak password")

def word_finder():
    text = input("Enter text: ")
    word = input("Enter the word to find: ")
    occurrences = [m.start() for m in re.finditer(rf"\b{word}\b", text)]
    print(f"Occurrences at positions: {occurrences}" if occurrences else "Word not found")

def date_extractor():
    text = input("Enter text: ")
    dates = re.findall(r"\b\d{4}-\d{2}-\d{2}\b", text)
    print("Extracted dates:", dates if dates else "No dates found")

