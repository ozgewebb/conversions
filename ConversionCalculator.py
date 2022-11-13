"""
conversions between different units of measurement
"""


def convert_kg(value):
    pounds = value * 2.20462
    ounces = value * 35.274
    print(value, "kg =", pounds, "pounds =", ounces, "ounces")


def convert_pounds(value):
    kg = value * 0.453592
    ounces = value * 16
    print(value, "pounds =", kg, "kg =", ounces, "ounces")


def convert_ounces(value):
    kg = value * 0.0283
    pound = value * 0.0625
    print(value, "ounces =", kg, "kg =", pound, "pounds")


def convert_gallon(value):
    pint = value * 8
    f_ounces = value * 128
    liter = value * 3.8
    quart = value * 4
    print(value, "gallon =", pint, "pints =", f_ounces, "fluid ounces =", liter, "liters =", quart,
          "quarts")


if __name__ == "__main__":
    convert_kg(10)
    convert_pounds(10)
    convert_ounces(10)
    convert_gallon(10)
