import random
from datetime import datetime, timedelta

def citeste_produse(denumire_fisier):
    # Citim lista de produse dintr-un fișier text
    with open(denumire_fisier, 'r', encoding='utf-8') as file:
        produse = [linie.strip() for linie in file.readlines() if linie.strip()]
    return produse

def genereaza_bon_fiscal(lista_produse):
    produse = []
    total_fara_tva = 0
    judete = ["Cluj", "București", "Iași", "Timiș", "Brașov"]

    # Generăm 20 de produse aleatorii pentru fiecare bon fiscal
    for _ in range(20):
        produs = random.choice(lista_produse)
        cantitate = random.randint(1, 5)
        pret_unitar = round(random.uniform(1.5, 30.0), 2)
        pret_total = round(cantitate * pret_unitar, 2)
        produse.append({
            "nume_produs": produs,
            "cantitate": cantitate,
            "pret_unitar": pret_unitar,
            "pret_total": pret_total
        })
        total_fara_tva += pret_total

    tva = round(total_fara_tva * 0.19, 2)
    total_final = round(total_fara_tva + tva, 2)

    bon = {
        "id_bon": f"BON-{random.randint(100000, 999999)}",
        "data_ora": (datetime.now() - timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d %H:%M:%S"),
        "judet": random.choice(judete),
        "magazin": "Magazin Fictiv SRL",
        "produse": produse,
        "total_fara_tva": total_fara_tva,
        "tva": tva,
        "total_final": total_final,
        "metoda_plata": random.choice(["Cash", "Card"]),
    }
    return bon

def scrie_bonuri_fiscale(bonuri, denumire_fisier):
    # Scriem datele într-un format text simplu
    with open(denumire_fisier, 'w', encoding='utf-8') as file:
        for bon in bonuri:
            file.write(f"ID Bon: {bon['id_bon']}\n")
            file.write(f"Data și ora: {bon['data_ora']}\n")
            file.write(f"Județ: {bon['judet']}\n")
            file.write(f"Magazin: {bon['magazin']}\n")
            file.write(f"Metoda de plată: {bon['metoda_plata']}\n")
            file.write(f"Total fără TVA: {bon['total_fara_tva']:.2f} RON\n")
            file.write(f"TVA: {bon['tva']:.2f} RON\n")
            file.write(f"Total bon: {bon['total_final']:.2f} RON\n")
            file.write("Produse:\n")
            for produs in bon['produse']:
                file.write(f"  - {produs['nume_produs']} | Cantitate: {produs['cantitate']} | "
                           f"Preț unitar: {produs['pret_unitar']:.2f} RON | "
                           f"Preț total: {produs['pret_total']:.2f} RON\n")
            file.write("\n" + "="*40 + "\n\n")

# Citim lista de produse din fișierul "produse.txt"
lista_produse = citeste_produse("produse.txt")

# Generăm 100 de bonuri fiscale folosind lista de produse
bonuri = [genereaza_bon_fiscal(lista_produse) for _ in range(300)]

# Scriem bonurile fiscale într-un fișier text simplu
scrie_bonuri_fiscale(bonuri, """Receipts.txt""")

print("Bonurile fiscale au fost generate și scrise în fișierul 'bonuri_fiscale.txt'")
