"""Leap year: divisible by 4, except centuries unless divisible by 400."""


def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


if __name__ == "__main__":
    for year in (1900, 2000, 2024, 2025):
        print(year, "leap" if is_leap_year(year) else "not leap")
