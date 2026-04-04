import sqlite3
import hashlib

DB_NAME = "realestate.db"


def generar_hash(titulo, m2, barrio, tipo, lat, lng):
    base = f"{titulo}_{m2}_{barrio}_{tipo}_{lat}_{lng}"
    return hashlib.sha256(base.encode()).hexdigest()


def init_db(conn):
    c = conn.cursor()

    # TABLA PROPIEDADES
    c.execute("""
    CREATE TABLE IF NOT EXISTS propiedades (
        hash_id TEXT PRIMARY KEY,
        titulo TEXT,
        barrio TEXT,
        tipo TEXT,
        lat REAL,
        lng REAL,
        m2 REAL,
        fecha_detectada TEXT,
        fecha_actualizacion TEXT
    )
    """)

    # TABLA HISTORIAL PRECIOS
    c.execute("""
    CREATE TABLE IF NOT EXISTS historial_precios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        hash_id TEXT,
        precio_usd REAL,
        precio_m2_usd REAL,
        fecha TEXT
    )
    """)

    # ÍNDICES (MEJORA DE PERFORMANCE)
    c.execute("""
    CREATE INDEX IF NOT EXISTS idx_propiedades_hash 
    ON propiedades(hash_id)
    """)

    c.execute("""
    CREATE INDEX IF NOT EXISTS idx_historial_hash 
    ON historial_precios(hash_id)
    """)

    c.execute("""
    CREATE INDEX IF NOT EXISTS idx_historial_fecha 
    ON historial_precios(fecha)
    """)

    conn.commit()
