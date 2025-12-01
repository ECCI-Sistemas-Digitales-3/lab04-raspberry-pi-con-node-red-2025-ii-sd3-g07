
import re

path = "/home/pi/rgb_values.txt"

with open(path, "r") as f:
    lines = f.readlines()

last = lines[-1].strip()

match = re.search(r"R=(\d+), G=(\d+), B=(\d+)", last)

if match:
    r = int(match.group(1))
    g = int(match.group(2))
    b = int(match.group(3))

    print(f"Último valor leído -> R={r}, G={g}, B={b}")

    rn = r / 255
    gn = g / 255
    bn = b / 255

    print("Valores normalizados:")
    print(f"R={rn:.3f}, G={gn:.3f}, B={bn:.3f}")
else:
    print("No se pudieron leer valores RGB")
