conversion_rates = {
    "ACB": (420.69, "Acematarian Boner"),
    "BHC": (1.16, "Bloominian Hilch"),
    "KBL": (0.67, "Karbinatedbeanen Larog"),
    "BWK": (1.34, "Bulwickian Krïna"),
    "CMP": (22.6, "Camel Pound"),
    "CDX": (2.01, "Chinadan Xuan"),
    "GGR": (1354.86, "Gingerland Ginger"),
    "VIA": (5.3, "Vian Via"),
    "LRP": (70.2, "Limardan Rupee"),
    "LIN": (9.02, "Lingaland Linga"),
    "NIR": (2.08, "Niroshi Yino"),
    "RAI": (23.54, "Rainiensafra Farat"),
    "RIZZ": (279.13, "Rizzistan Rizzpee"),
    "EVA": (4.13, "Evanovan Dollar"),
    "RUT": (7.34, "Rutavish Ruvet"),
    "SOI": (4.68, "Soisabu Shilling"),
    "STE": (1.03, "Steida Dollar"),
    "TYR": (42309423.5, "Tyroniean Chickennugget"),
    "WAA": (6.87, "Waarnistani Wyf"),
    "ZIM": (192.67, "Zimzamian Zim"),
    "PEL": (6.62, "Pelalan Podzol"),
    "GCR": (1.06, "Garian Coin"),
    "AJM": (21.62, "Airejordan Michael"),
    "AKR": (5.8, "Alkreba Rebani"),
    "ALY": (150.48, "Alukyan Yen"),
    "IRP": (1.21, "Irupi"),
    "ATU": (1.67, "Atakian Underwoodan"),
    "BNB": (902.6, "Bananan Banana"),
    "BKX": (8.74, "Bartixian Klordung"),
    "BSD": (25, "Basdan Obamna"),
    "BLR": (12, "Bellairan Ruble"),
    "COR": (2.13, "Coralian Hilch"),
    "FTK": (7.16, "Frentuckian Kentucky"),
    "GRY": (21.5, "Granatian Yurian"),
    "GUH": (160.7, "Guhow Lamla"),
    "HNL": (7.206, "Honoloan Nuku"),
    "ISA": (23.15, "Isetian Arktikan"),
    "KOH": (11.436, "Konohan Ryō"),
    "MLG": (125.6, "Malagostani Gostaa"),
    "MKR": (5.3, "Maskurgan Krieug"),
    "NWO": (33.12, "Niwovo Wov"),
    "OCW": (15.1326, "Ocewan Ruble"),
    "OHK": (21.277, "Ohekan Dykra"),
    "OPG": (26.85, "Opongian Arktikan"),
    "OSC": (18.04, "Oscarian Arktikan"),
    "RHD": (266.02, "Rhodavian Davirgh"),
    "AUK": (6.7435, "Auntuk Oceancoin"),
    "TSH": (22.06, "Tashirsk Shironsk"),
    "TKR": (41.2, "Tukaragod Tukra"),
    "YFR": (262.162, "Yiphon Riaali"),
    "YGP": (0.79, "Yugolatkian Pound")
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