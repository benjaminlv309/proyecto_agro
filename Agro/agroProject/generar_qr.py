
from pathlib import Path
import qrcode

# Dirección del formulario público
# Reemplaza la IP por la de tu computador
url = "http://192.168.1.6:8000/registro/"

# Carpeta donde se guardará el QR
carpeta = Path(__file__).resolve().parent / "static" / "img"
carpeta.mkdir(parents=True, exist_ok=True)

# Configuración del QR
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=12,
    border=4
)
qr.add_data(url)
qr.make(fit=True)

imagen = qr.make_image(fill_color="black",back_color="white")

ruta = carpeta / "qr_agroadmin.png"

imagen.save(ruta)

print("Código QR generado correctamente.")
print(f"Ubicación: {ruta}")
print(f"Dirección: {url}")