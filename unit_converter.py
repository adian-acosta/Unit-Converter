CONVERSION_RATES = {
    ("Miles", "Kilometers"): 1.609344,
    ("Miles", "Inches"): 63360,
    ("Miles", "Centimeters"): 160934.4,
    ("Kilometers", "Miles"): 0.6213711922,
    ("Kilometers", "Inches"): 39370.1,
    ("Kilometers", "Centimeters"): 100000,
    ("Kilogram", "Pound"): 2.2046226218,
    ("Pound", "Kilogram"): 0.45359237,
    ("Inches", "Centimeters"): 2.54,
    ("Inches", "Miles"): 0.000015782828283,
    ("Inches", "Kilometer"): 39370.1,
    ("Centimeters", "Inches"): 0.3937007874,
    ("Centimeters", "Miles"): 0.0006213711,
    ("Centimeters", "Kilometer"): 100000
}

def convert_units(value, from_units, to_units):
    if (from_units, to_units) in CONVERSION_RATES:
        return value * CONVERSION_RATES[(from_units, to_units)]
    else:
        raise ValueError(f"Conversion from {from_units} to {to_units} not supported")