import sqlite3
from datetime import datetime, timedelta

from db import init_db, DB_NAME, generar_hash
from lector import leer_propiedades


def main():
    conn = sqlite3.connect(DB_NAME)
    init_db(conn)

    c = conn.cursor()
    count = 0

    for prop in leer_propiedades():

        hash_id = generar_hash(
            prop["titulo"],
            prop["m2"],
            prop["barrio"],
            prop["tipo"],
            prop["lat"],
            prop["lng"]
        )

        hoy = datetime.now()

        # INSERT PROPIEDAD
        c.execute("SELECT hash_id FROM propiedades WHERE hash_id = ?", (hash_id,))
        existe = c.fetchone()

        if not existe:
            c.execute("""
            INSERT INTO propiedades VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                hash_id,
                prop["titulo"],
                prop["barrio"],
                prop["tipo"],
                prop["lat"],
                prop["lng"],
                prop["m2"],
                hoy.isoformat(),
                hoy.isoformat()
            ))

        # 🔴 CLAVE: BORRAR HISTORIAL ANTERIOR
        c.execute("DELETE FROM historial_precios WHERE hash_id = ?", (hash_id,))

        precio_actual = prop["precio_usd"]

        import random

        factor = random.uniform(1.05, 1.25)
        precio_inicial = precio_actual * factor

        historial = [
    (precio_inicial, hoy - timedelta(days=30)),
    (precio_actual * random.uniform(1.03, 1.15), hoy - timedelta(days=20)),
    (precio_actual * random.uniform(1.01, 1.10), hoy - timedelta(days=10)),
    (precio_actual, hoy)
]

        for precio, fecha in historial:
            c.execute("""
            INSERT INTO historial_precios (hash_id, precio_usd, precio_m2_usd, fecha)
            VALUES (?, ?, ?, ?)
            """, (
                hash_id,
                precio,
                prop["precio_m2_usd"],
                fecha.isoformat()
            ))

        count += 1

        if count % 1000 == 0:
            print(f"Cargadas: {count}")

    conn.commit()
    conn.close()

    print(f"Total cargadas: {count}")


if __name__ == "__main__":
    main()
