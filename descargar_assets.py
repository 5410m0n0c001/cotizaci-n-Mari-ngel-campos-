import urllib.request
import os

base_url = "https://raw.githubusercontent.com/5410m0n0c001/antonio-cotizacion/main/"
dest_dir = r"C:\Users\Lenovo\Documents\mariangel-cotizacion"

assets = [
    ("precarga.mp4",                          "precarga.mp4"),
    ("marcasonora.mp3",                       "marcasonora.mp3"),
    ("firma.mp4",                             "firma.mp4"),
    ("hero.png",                              "hero.png"),
    ("jardin%20la%20flor.png",                "jardin_la_flor.png"),
    ("logo%20jardin%20la%20flor.png",         "logo_jardin_la_flor.png"),
    ("imobiliario%20elegante.webp",           "mobiliario.webp"),
    ("manteleria.webp",                       "manteleria.webp"),
    ("vajilla.webp",                          "vajilla.webp"),
    ("margaritas.webp",                       "margaritas.webp"),
    ("cristaleria.webp",                      "cristaleria.webp"),
    ("mezcladores.png",                       "mezcladores.png"),
    ("dj.webp",                               "dj.webp"),
    ("cordinador%20(1).webp",                 "coordinador.webp"),
    ("meseros.webp",                          "meseros.webp"),
    ("letras%20gigantes.webp",                "letras_gigantes.webp"),
    ("hostess.webp",                          "hostess.webp"),
    ("bartender.webp",                        "bartender.webp"),
    ("capitan.webp",                          "capitan.webp"),
    ("crudites.webp",                         "crudites.webp"),
    ("AGUAS_FRESCAS_2.webp",                  "aguas_frescas.webp"),
    ("centro%20de%20mesa%20(1).webp",         "centro_de_mesa.webp"),
    ("tiempodeservicio.webp",                 "tiempo_servicio.webp"),
    ("pistadebaile.jpg",                      "pista.jpg"),
    ("mesa%20principal.webp",                 "mesa_principal.webp"),
]

for filename, localname in assets:
    url = base_url + filename
    dest = os.path.join(dest_dir, localname)
    if os.path.exists(dest):
        print(f"  [SKIP] {localname} ya existe")
        continue
    try:
        print(f"  Descargando {localname}...", end=" ")
        urllib.request.urlretrieve(url, dest)
        size = os.path.getsize(dest)
        print(f"OK ({size:,} bytes)")
    except Exception as e:
        print(f"ERROR: {e}")

print("\nDescarga completada.")
