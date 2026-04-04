import csv

def leer_propiedades():
    with open("datos.csv", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)

        for row in reader:

            # FILTRO: solo departamentos
            if row.get("property_type") != "apartment":
                continue

            lugar = row.get("place_with_parent_names", "")
            barrio = lugar.split("|")[-1] if "|" in lugar else lugar

            lat, lng = 0, 0
            latlon = row.get("lat-lon")
            if latlon and "," in latlon:
                try:
                    lat, lng = map(float, latlon.split(","))
                except:
                    pass

            precio = float(row.get("price_aprox_usd") or 0)
            m2 = float(row.get("surface_total_in_m2") or 0)

            # FILTRO CALIDAD (evita basura)
            if precio < 10000 or m2 < 20:
                continue

            yield {
                "titulo": "Depto",
                "barrio": barrio.strip(),
                "tipo": "apartment",
                "lat": lat,
                "lng": lng,
                "m2": m2,
                "precio_usd": precio,
                "precio_m2_usd": float(row.get("price_usd_per_m2") or 0)
            }
