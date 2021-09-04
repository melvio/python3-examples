import numpy as np
import pyqrcode as qr


def wifiqr(ssid: str, security: str, password: str) -> qr.QRCode:
    return qr.create(f"WIFI:S:{ssid};T:{security};P:{password};;")


def qr2array(qrcode: qr.QRCode) -> np.ndarray:
    return np.vstack([int(line) for line in qrcode.text().split("\n") if line])


def png_base64(qrcode: qr.QRCode, scale: int = 10):
    return qrcode.png_as_base64_str(scale=scale)


