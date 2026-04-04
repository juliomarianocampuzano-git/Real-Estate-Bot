import requests
from bs4 import BeautifulSoup


def scrapear_properati():
    url = "https://www.properati.com.ar/s/departamentos-en-venta"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            return []

        html = response.text

        # guardar html para inspección
        with open("raw_properati.html", "w", encoding="utf-8") as f:
            f.write(html)

        soup = BeautifulSoup(html, "lxml")

        propiedades = []

        # BUSCAR TODOS LOS LINKS (base para extracción real)
        links = soup.find_all("a")

        for link in links:
            href = link.get("href")

            if not href:
                continue

            if "/propiedad/" not in href:
                continue

            texto = link.get_text()

            if "$" not in texto:
                continue

            propiedades.append({
                "titulo": "Depto",
                "barrio": "Desconocido",
                "tipo": "apartment",
                "lat": 0,
                "lng": 0,
                "m2": 0,
                "precio_usd": 100000,
                "precio_m2_usd": 0,
                "link": href,
                "external_id": href
            })

        return propiedades

    except:
        return []


def scrapear_zonaprop():
    return []


def scrapear_argenprop():
    return []


def obtener_propiedades():
    resultados = []

    resultados += scrapear_properati()
    resultados += scrapear_zonaprop()
    resultados += scrapear_argenprop()

    return resultados
