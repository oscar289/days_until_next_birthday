import datetime

x = datetime.datetime.now()


def days_until_next_birthday(birthday_month, birthday_day):
    """
  Calculates the number of days until the user's next birthday.

  Args:
      birthday_month (int): The month of the user's birthday (1-12).
      birthday_day (int): The day of the user's birthday (1-31).

  Returns:
      int: The number of days until the user's next birthday.
  """
    now = datetime.datetime.now()
    nextBirt = datetime.datetime(now.year, birthday_month, birthday_day)
    current_year = now.year
    if nextBirt < now:
      nextBirt = datetime.datetime(now.year + 1, birthday_month, birthday_day)

    daysUntilNextBirthday = nextBirt - now

    return daysUntilNextBirthday


bm = int(input("The number of the month of your birthday : "))
bd = int(input("The number of the day of your birthday : "))


print(days_until_next_birthday(bm, bd))
