def grams_to_ounces(grams):
    """Converts grams to ounces."""
    ounces = grams * 28.3495231
    return ounces
grams = float(input("grams: "))
print("ounces = ", grams_to_ounces(grams))