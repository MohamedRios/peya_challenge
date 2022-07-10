from imp import source_from_cache
from platform import platform
import requests

url = 'http://localhost:5000/api'

r = requests.post(url, json={
        "ano_de_construccion": [1991.0],
        "banos": [1.0],
        "disposicion": ["contrafrente"],
        "dormitorios": [1.0],
        "estado": ["excelente estado"],
        "garajes": [0.0],
        "gastos_comunes": [5000.0],
        "m2_de_la_terraza": [0.0],
        "m2_del_terreno": [45.0],
        "m2_edificados": [45.0],
        "tipo_propiedad": ["apartamentos"],
        "vivienda_social": [0.0],
        "zona": ["punta carretas"]
    })

print(r.json())