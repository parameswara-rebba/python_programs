"""Convert between Celsius and Fahrenheit."""


def celsius_to_fahrenheit(c: float) -> float:
    return c * 9 / 5 + 32


def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5 / 9


if __name__ == "__main__":
    for c in (-40, 0, 37, 100):
        print(f"{c:>5}°C = {celsius_to_fahrenheit(c):.1f}°F")
