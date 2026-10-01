def input_teks(prompt):
    while True:
        nilai = input(prompt).lower().strip()
        if nilai:
            return nilai
        print("Input Tidak Boleh Kosong.")


def input_angka(prompt, minimum=None, maksimum=None):
    while True:
        try:
            nilai = int(input(prompt))
            if minimum is not None and nilai < minimum:
                print(f"Nilai Minimal Adalah {minimum}.")
                continue
            if maksimum is not None and nilai > maksimum:
                print(f"Nilai Maksimal Adalah {maksimum}.")
                continue
            return nilai

        except ValueError:
            print("Input Harus Berupa Angka.")

def input_pilihan(prompt, pilihan_valid):
    while True:
        pilihan = input(prompt).strip().lower()
        if pilihan in pilihan_valid:
            return pilihan
        print(
            "Pilihan Tidak Valid."
            f" Pilih Salah Satu: {', '.join(pilihan_valid)}"
        )

def input_divisi(prompt="Divisi : "):
    return input_teks(prompt)

def input_prioritas():
    print("\nPrioritas:")
    print("1. Rendah")
    print("2. Sedang")
    print("3. Tinggi")
    return input_angka(
        "Pilih prioritas: ",
        minimum=1,
        maksimum=3
    )

def konfirmasi(prompt):
    pilihan = input_pilihan(
        f"{prompt} (y/n): ",
        ["y", "n"]
    )
    return pilihan == "y"