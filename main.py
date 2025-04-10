# První projekt v kurzu.
"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Renato Vítek
email: renev6548@gmail.com
"""

import sys # Modul je volán pro možnost ukončení prgramu pomoci sys.exit()

uživatelé = { # Slovník uživatelů a jejich hesel
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
}

řádek = "-" * 90
print(řádek)
print(řádek + "\n  Vítejte v aplikaci pro analýzu textu.\n" + řádek)

jméno = input("  Přihlašovací jméno: ")
heslo = input("  Zadejte heslo: ")
print(řádek)

if jméno in uživatelé and uživatelé[jméno] == heslo:
    print(f"  Vítej uživateli {jméno}.")
    print("  Máme tři texty k analýze.")
    print(řádek)
else:
    print(f"  1  Uživatelské jméno: {jméno}")
    print(f"  2  Heslo: {heslo}")
    print(f"  Nejste registrován, ukončuji program.")
    sys.exit()

TEXTS = [
    '''
    Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''
    At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''
    The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

print("  Máme tři texty k analýze.")
číslo_textu = input("  Zadejte číslo textu (1-3): ")

if číslo_textu.isdigit():   #Ověření zda je číslo_textu číslo
    # Pokud je číslo_textu číslo, převedeme ho na int.
    číslo_textu = int(číslo_textu)
    if 1 <= číslo_textu <= len(TEXTS):
        vybraný_text = TEXTS[číslo_textu - 1]
        slova = vybraný_text.split()  # Rozdělení textu na jednotlivá slova
        počet_slov = len(slova) # Počet slov v textu
        začínající_velkým = sum(1 for slovo in slova if slovo.istitle())# Počet slov začínajících velkým písmenem
        velká_písmena = sum(1 for slovo in slova if slovo.isupper())  # Počet slov psaných velkými písmeny
        malá_písmena = sum(1 for slovo in slova if slovo.islower())  # Počet slov psaných malými písmeny
        čísla = sum(1 for slovo in slova if slovo.isdigit()) # Počet čísel(string) v textu
        součet = sum(int(slovo) for slovo in slova if slovo.isdigit()) # Součet všech čísel v textu, Nutno převést na int.

        print(řádek)
        print("  VÝSLEDKY ANALÝZY:")
        print(f"  Počet slov v textu: {počet_slov}")
        print(f"  Počet slov začínajících velkým písmenem: {začínající_velkým}")
        print(f"  Počet slov psaných velkými písmeny: {velká_písmena}")
        print(f"  Počet slov psaných malými písmeny: {malá_písmena}")
        print(f"  Počet čísel(string) v textu: {čísla}")
        print(f"  Součet všech čísel v textu: {součet}")
        print(řádek)

        print("  GRAF:")
        print(řádek)
        print(f"  {'ŘÁDEK':<6}|{'POČET':<6}|{'VÝSKYT'}")
        print(řádek)
        print(f"  {'1':<6}|{počet_slov:<6}|{'*' * počet_slov}")
        print(f"  {'2':<6}|{začínající_velkým:<6}|{'*' * začínající_velkým}")
        print(f"  {'3':<6}|{velká_písmena:<6}|{'*' * velká_písmena}")
        print(f"  {'4':<6}|{malá_písmena:<6}|{'*' * malá_písmena}")
        print(f"  {'5':<6}|{čísla:<6}|{'*' * čísla}")
        print(řádek)
    else:
        print("  Napsal jste číslo textu, které není v rozsahu 1-3.")
        sys.exit()
else:
    print("  Neplatný vstup! Zadejte číslo.")
    sys.exit()




















