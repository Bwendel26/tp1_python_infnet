
# 2. Faça uma função em Python que receba do usuário a idade de uma pessoa em anos,
# meses e dias e retorne essa idade expressa em dias. Considere que todos os anos
# têm 365 dias.

def days_age(years, months, days):
    """
    This func returns the age(years, mounths and days) in days.
    :param years:
    :param months:
    :param days:
    :return int total_days:
    """
    total_days_in_years = years * 365
    months_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #Jan to Dec
    total_days_in_months = 0
    #days
    total_days = total_days_in_years + days #don`t miss the months in days.

    for mounth in range(months):
        total_days_in_months += months_list[mounth]

    total_days += total_days_in_months

    return total_days
#MAIN
years = int(input("Please insert your age in years: "))
months = int(input("And the rest in months: "))
days = int(input("Now the rest in days: "))
print(days_age(years, months, days))