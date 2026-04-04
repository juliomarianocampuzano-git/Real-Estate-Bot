import csv

def leer_propiedades():
    with open("Data/datos.csv", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)

        for row in reader:

            if row.get("property_type") != "apartment":
                continue

            try:
                precio = float(row.get("price_aprox_usd") or 0)
                m2 = float(row.get("surface_total_in_m2") or 0)
            except:
                continue

            # FILTROS CRÍTICOS (ESTO ARREGLA TODO)
            if precio < 30000 or precio > 500000:
                continue

            if m2 < 20 or m2 > 500:
                continue

            lugar = row.get("place_with_parent_names", "")
            barrio = lugar.split("|")[-1].strip()

            yield {
                "titulo": "Depto",
                "barrio": barrio,
                "tipo": "apartment",
                "lat": 0,
                "lng": 0,
                "m2": m2,
                "precio_usd": precio,
                "precio_m2_usd": precio / m2 if m2 else 0
            }
