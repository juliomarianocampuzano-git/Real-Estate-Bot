🏠 Real Estate Lead Scoring Automation

Sistema que detecta oportunidades inmobiliarias analizando caídas de precio.

---

📌 Problema

Encontrar buenas oportunidades inmobiliarias es difícil.

Hay miles de propiedades, pero no es claro:
- cuáles bajaron de precio
- cuáles tienen margen de negociación
- cuáles son realmente una oportunidad

---

🚀 Solución

Este proyecto analiza propiedades y detecta automáticamente oportunidades.

Hace lo siguiente:
- procesa datos de propiedades
- genera historial de precios
- calcula caídas de precio
- muestra las mejores oportunidades

---

⚙️ Cómo funciona

Pipeline:

datos.csv → lector.py → main.py → base de datos → analisis.py

---

▶️ Cómo ejecutarlo

1. Ejecutar:

python main.py

2. Luego:

python analisis.py

---

📊 Resultado

El sistema muestra algo como:

TOP OPORTUNIDADES

Depto | Palermo  
Precio actual: 120000  
Caída: 18.7%

---

🧠 Lógica

Caída (%) = (precio inicial - precio actual) / precio inicial

---

🗂️ Archivos

- main.py → genera datos
- analisis.py → analiza oportunidades
- db.py → base de datos
- lector.py → limpia datos
- datos.csv → dataset

---

💡 Valor

Este proyecto demuestra:

- manejo de datos
- uso de base de datos
- lógica de negocio real
- construcción de un sistema completo

---

⚠️ Limitaciones

- usa CSV (no scraping real)
- histórico simulado
- no tiene interfaz visual

---

🔜 Próximo paso

- agregar scraping real
- agregar dashboard
- automatizar alertas

---

👨‍💻 Autor: Julio Mariano Campuzano 

Proyecto de automatización aplicado a Real Estate.