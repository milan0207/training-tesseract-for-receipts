def capitalize_file(file_path):
    # Olvassuk be a fájl tartalmát
    with open(file_path, 'r', encoding='utf-8') as file:
        # Olvassuk be a sorokat, és töröljük az üres sorokat
        content = [line.strip() for line in file if line.strip()]

    # Nagybetűsítjük a tartalmat
    capitalized_content = [line.upper() for line in content]

    # Írjuk vissza a módosított tartalmat a fájlba
    with open(file_path, 'w', encoding='utf-8') as file:
        # A sorokat összefűzve írjuk vissza, új sorral elválasztva
        file.write('\n'.join(capitalized_content) + '\n')

# Példa a fájl elérési útjára
file_path = 'Receipts.txt'
capitalize_file(file_path)
