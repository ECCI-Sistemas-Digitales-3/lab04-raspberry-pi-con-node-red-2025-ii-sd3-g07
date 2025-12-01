[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=21897669&assignment_repo_type=AssignmentRepo)
# Lab04: Visualización de Datos en Raspberry Pi con Node-RED 

## Integrantes
PAULA CAÑON

## Documentación
1. Objetivo

Implementar un flujo en Node-RED que permita seleccionar un color mediante un selector, visualizar sus valores RGB y almacenarlos en un archivo. Además, desarrollar un script en Python que procese dichos valores.

2. Requerimientos

Raspberry Pi con Raspberry Pi OS

Node.js / npm

Node-RED

Python 3

Acceso SSH

Red local compartida entre PC y Raspberry Pi

3. Procedimiento
3.1 Instalación y configuración de Node-RED
   
  

sudo apt update
bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)
sudo systemctl enable nodered.service
sudo systemctl start nodered.service

 Acceder vía navegador:
   http://<IP-Raspberry>:1880

   3.2 Desarrollo del flujo en Node-RED

Se crearon los siguientes nodos:

ui_colour_picker – permite seleccionar un color.

Function – extrae los valores RGB del formato rgb(r,g,b).

ui_text – muestra los valores RGB al usuario.

file – almacena los valores en /home/pi/rgb_values.txt.

4. Resultados

Se logró seleccionar colores desde la interfaz web del dashboard.

Los valores RGB se generaron correctamente.

Se almacenaron múltiples líneas en el archivo rgb_values.txt.

El script Python read_rgb.py leyó y procesó correctamente los valores más recientes.

Se validó la comunicación Node-RED → archivo → Python en la Raspberry Pi.



## Conclusiones

Node-RED permite integrar interfaces gráficas rápidas con procesamiento de datos sin necesidad de hardware adicional.

El manejo de archivos en Raspberry Pi facilita la transferencia de datos hacia otros lenguajes como Python.

Este laboratorio demuestra un flujo completo de adquisición → visualización → almacenamiento → procesamiento.

La solución es totalmente escalable para sistemas IoT o aplicaciones de monitoreo.
