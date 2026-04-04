import sqlite3

DB_NAME = "realestate.db"


def analizar():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # obtener último precio y precio inicial
    c.execute("""
    SELECT 
        p.titulo,
        p.barrio,
        (
            SELECT precio_usd 
            FROM historial_precios 
            WHERE hash_id = p.hash_id 
            ORDER BY fecha ASC LIMIT 1
        ) as precio_inicial,

        (
            SELECT precio_usd 
            FROM historial_precios 
            WHERE hash_id = p.hash_id 
            ORDER BY fecha DESC LIMIT 1
        ) as precio_actual

    FROM propiedades p
    """)

    resultados = []

    for titulo, barrio, precio_inicial, precio_actual in c.fetchall():

        if not precio_inicial or not precio_actual:
            continue

        if precio_inicial == 0:
            continue

        caida = ((precio_inicial - precio_actual) / precio_inicial) * 100

        if caida > 5:  # filtro realista
            resultados.append((titulo, barrio, precio_actual, caida))

    resultados.sort(key=lambda x: x[3], reverse=True)

    print("\nTOP OPORTUNIDADES\n")

    for r in resultados[:10]:
        print(f"{r[0]} | {r[1]}")
        print(f"Precio actual: {int(r[2])}")
        print(f"Caída: {round(r[3],2)}%")
        print("-" * 30)

    conn.close()


if __name__ == "__main__":
    analizar()
