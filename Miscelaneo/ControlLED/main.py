import sys
import time
from machine import Pin

# Configurar los LEDs
leds = [Pin(pin, Pin.OUT) for pin in [16, 17, 18, 19]]

def apagar_todos():
    for l in leds: 
        l.off()

def secuencia_llenado():
    for l in leds:
        l.on()
        time.sleep(0.3)

#def secuencia_borrado():
#    for l in leds: 
#        l.on()
#    time.sleep(0.2)
#    for l in reversed(leds):
#        l.off()
#        time.sleep(0.3)
#Blink NUNCA quiso servir, me rindo


def secuencia_blink():
    for _ in range(2):
        for l in leds:
            l.on()
        time.sleep(0.2)
        for l in leds:
            l.off()
        time.sleep(0.2)
        sys.stdout.flush()  # <-- mantiene vivo el enlace USB


def secuencia_ida_vuelta():
    apagar_todos()
    for _ in range(2):
        for l in leds:
            l.on()
            time.sleep(0.2)
            l.off()
        for l in reversed(leds):
            l.on()
            time.sleep(0.2)
            l.off()


while True:
    try:
        # Lee un byte desde la conexión USB
        cmd = sys.stdin.buffer.read(1)
        if not cmd:
            time.sleep(0.1)
            continue

        cmd = cmd[0]
        print(f"📩 Recibido: 0x{cmd:02X}")

        if cmd == 0x01:
            secuencia_llenado()
        elif cmd == 0x02:
            secuencia_borrado()
        elif cmd == 0x03:
            secuencia_blink()
        elif cmd == 0x04:
            secuencia_ida_vuelta()

        # Confirmación de ejecución al PC
        sys.stdout.buffer.write(b'\xFF')
        sys.stdout.flush()

    except Exception as e:
        print(f"💥 Error: {e}")
        time.sleep(0.2)

