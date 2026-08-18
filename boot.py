
# ==========================================
# boot.py - Configuración Access Point (ESP32)
# ==========================================
import network
import gc

# Liberar memoria RAM antes de levantar la interfaz
gc.collect()

# Apagar cualquier estación previa para evitar conflictos
sta_if = network.WLAN(network.STA_IF)
if sta_if.active():
    sta_if.active(False)

# Iniciar interfaz en modo Access Point (AP)
ap = network.WLAN(network.AP_IF)
ap.active(True)

# Configuración del Nombre de Red (SSID) y Clave WPA2
SSID_NOMBRE = 'Smart-UIP-Lab'
SSID_CLAVE  = '12345678'  # Nota: WPA2 exige mínimo 8 caracteres para que la clave sea aceptada por los celulares

ap.config(essid=SSID_NOMBRE, password=SSID_CLAVE, authmode=3)

print("=" * 60)
print(" SERVIDOR AUTÓNOMO ESP32 - SMART UIP LAB")
print(f" Red Wi-Fi SSID : {SSID_NOMBRE}")
print(f" Contraseña     : {SSID_CLAVE}")
print(f" Dirección IP   : {ap.ifconfig()[0]}")
print("=" * 60)
