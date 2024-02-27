import fractions
import re

def make_pretty(numerator, denominator) -> str:
    """
    Returns the prettified version for the specified numerator and denominator.
    """
    numeratorLength = len(str(numerator))
    denominatorLength = len(str(denominator))
    if numeratorLength == denominatorLength:
        seperatorLength = denominatorLength
        return f"{numerator}\n{'-'*seperatorLength}\n{denominator}"
    elif numeratorLength > denominatorLength:
        seperatorLength = numeratorLength
        steps = (seperatorLength - denominatorLength) // 2
        return f"{numerator}\n{'-'*seperatorLength}\n{' '*steps}{denominator}"
    elif numeratorLength < denominatorLength:
        seperatorLength = denominatorLength
        steps = (seperatorLength - numeratorLength) // 2
        return f"{' '*steps}{numerator}\n{'-'*seperatorLength}\n{denominator}"

def display(value: float):
    """
    Visualizes a prettified fraction to a given float value.
    """
    if not isinstance(value, float | int):
        raise ValueError("could not draw fraction: value must be type float")
    valueInt = int(value)
    valueDecimal = value - valueInt
    if valueDecimal == 0:
        print(value)
        return
    valueFraction = fractions.Fraction(valueDecimal).limit_denominator(1_000_000)
    regexFractionSearch = re.search(r"(?P<num>\d+)/(?P<den>\d+)", str(valueFraction))
    if valueInt == 0:
        valuePretty = make_pretty(regexFractionSearch.group("num"), regexFractionSearch.group("den"))
        print(valuePretty)
    if valueInt > 0:
        valuePretty = make_pretty(regexFractionSearch.group("num"), regexFractionSearch.group("den"))
        print(f"{valuePretty} \x1b[1A+ {valueInt}\n")
