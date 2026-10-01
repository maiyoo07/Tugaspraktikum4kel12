import json
import os

from src.models.Anggota import Anggota
from src.models.Tugas import Tugas

DATABASE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    "data",
    "database.json"
)

def load_data():
    if not os.path.exists(DATABASE_PATH):
        return {
            "anggota": [],
            "tugas": [],
            "riwayat_tugas": []
        }
    try:
        with open(DATABASE_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (json.JSONDecodeError, OSError):
        return {
            "anggota": [],
            "tugas": [],
            "riwayat_tugas": []
        }

    daftar_anggota = []
    for data_anggota in data.get("anggota", []):
        anggota = Anggota(
            data_anggota["nama"],
            data_anggota["divisi"]
        )
        anggota.beban = data_anggota.get("beban", 0)
        daftar_anggota.append(anggota)

    daftar_tugas = []
    for data_tugas in data.get("tugas", []):
        tugas = Tugas(
            data_tugas["nama"],
            data_tugas["divisi"],
            data_tugas["beban"],
            data_tugas["prioritas"]
        )
        tugas.status = data_tugas.get("status", "Belum")
        tugas.assigned_to = data_tugas.get("assigned_to")
        daftar_tugas.append(tugas)

    for tugas in daftar_tugas:
        if tugas.assigned_to is not None:
            for anggota in daftar_anggota:
                if anggota.nama == tugas.assigned_to:
                    anggota.tugas.append(tugas)
                    break
    riwayat_tugas = data.get("riwayat_tugas", [])

    return {
        "anggota": daftar_anggota,
        "tugas": daftar_tugas,
        "riwayat_tugas": riwayat_tugas
    }

def save_data(daftar_anggota, daftar_tugas, riwayat_tugas):
    data = {
        "anggota": [],
        "tugas": [],
        "riwayat_tugas": riwayat_tugas
    }

    for anggota in daftar_anggota:
        data["anggota"].append({
            "nama": anggota.nama,
            "divisi": anggota.divisi,
            "beban": anggota.beban
        })

    for tugas in daftar_tugas:
        data["tugas"].append({
            "nama": tugas.nama,
            "divisi": tugas.divisi,
            "beban": tugas.beban,
            "prioritas": tugas.prioritas,
            "status": tugas.status,
            "assigned_to": tugas.assigned_to
        })

    os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)
    with open(DATABASE_PATH, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )