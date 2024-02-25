conversion_rates = {
    "BWK": (1.34, "Krina"),
    "ACB": (420.69, "Boner"),
    "BHC": (1.16, "Hilch"),
    "KBL": (0.67, "Larog"),
    "CMP": (22.6, "Pound"),
    "CDX": (2.01, "Xuan"),
    "GGR": (1354.86, "Ginger"),
    "VIA": (5.3, "Via"),
    "LRP": (70.2, "Rupee"),
    "LIN": (9.02, "Linga"),
    "NIR": (2.08, "Yino"),
    "RAI": (23.54, "Farat"),
    "RIZZ": (278.80, "Rizzpee"),
    "EVA": (4.13, "eDollar"),
    "RUT": (9.0, "Ruvet"),
    "SOI": (4.68, "Shilling"),
    "STE": (1.03, "sDollar"),
    "TYR": (42309423.5, "Chickennugget"),
    "WAA": (6.87, "Wyf"),
    "ZIM": (4.20, "Zim"),
    "PEL": (6.62, "Podzol"),
}


def print_currency_options():
    print("Please enter which currency you would like to convert to, or type 'EXIT' to quit:")
    for code, details in conversion_rates.items():
        print(f"{code}: {details[1]}")

while True:
    print_currency_options()
    currency = input().upper()

    if currency == 'EXIT':
        print("Exiting the program.")
        break

    if currency in conversion_rates:
        rate, currency_name = conversion_rates[currency]
        print(f"Welcome to the USD to {currency_name} Converter. Enter amount in USD:", end=" ")
        try:
            usd = float(input())
            converted_amount = usd * rate
            print(f"Amount in {currency_name}: {converted_amount:.2f}")
        except ValueError:
            print("Please enter a valid number for the amount.")
    else:
        print("Invalid currency code. Please enter a valid code from the list.")

    print("\n")