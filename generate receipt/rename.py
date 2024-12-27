import os

# Mappa, ahol a fájlok találhatók
folder_path = "data"  # Itt add meg a megfelelő mappát

# Fájlok listázása a mappában
for filename in os.listdir(folder_path):
    # Csak a 'ron_' előtagú fájlokat kezeljük
    if filename.startswith("ron_") and filename.endswith((".tif", ".box", ".txt")):
        # Eltávolítjuk az "ron_" előtagot és a kiterjesztést, hogy csak a számot kezeljük
        name_parts = filename[4:].split(".")
        number = int(name_parts[0])  # Az első rész a szám

        # Csökkentjük a számot 3099-tel
        new_number = number - 3099

        # Az új fájlnév generálása
        if(number<3099):
            new_filename = f"ron_{number}.{name_parts[1]}"
        new_filename = f"ron_{new_number}.{name_parts[1]}"

        # A fájl átnevezése
        old_file_path = os.path.join(folder_path, filename)
        new_file_path = os.path.join(folder_path, new_filename)
        os.rename(old_file_path, new_file_path)

        print(f"Renamed: {filename} -> {new_filename}")
