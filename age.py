from datetime import datetime


def func1():
    pass

def calculate_age(date_of_birth):
    """
    date_of_birth format: YYYY-MM-DD
    Example: 1990-05-15
    """
    dob = datetime.strptime(date_of_birth, "%Y-%m-%d")
    now = datetime.now()
    print (f"dob: {dob}, now: {now}")

    # Calculate years, months, days
    years = now.year - dob.year
    months = now.month - dob.month
    days = now.day - dob.day
    print (f"years: {years}, months: {months}, days: {days}")
    # Adjust days
    if days < 0:
        if now.month == 1:
            prev_month = 12
            prev_year = now.year - 1
        else:
            prev_month = now.month - 1
            prev_year = now.year
        days_in_prev_month = (
            datetime(now.year, now.month, 1) -
            datetime(prev_year, prev_month, 1)
        ).days
        days += days_in_prev_month
        months -= 1
    # Adjust months
    if months < 0:
        months += 12
        years -= 1
        days = months 
    # Total duration
    delta = now - dob
    return {
        "years": years,
        "months": months,
        "days": days,
        "total_days": delta.days,
        "total_hours": int(delta.total_seconds() // 3600),
        "total_minutes": int(delta.total_seconds() // 60),
        "total_seconds": int(delta.total_seconds()),
        "current_datetime": now.strftime("%Y-%m-%d %H:%M:%S")
    }

# Example Usage

age = calculate_age("2026-05-25")
print (age)
