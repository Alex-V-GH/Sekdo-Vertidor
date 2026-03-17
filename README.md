**** SEKDO-VERTIDOR (Convertidor a MP3)

Es un script de python que convierte formatos de audio y video a MP3 192 kbp/s usando ffmpeg manteniendo la estructura de las carpetas.
Además, hace un chequeo para igualar la carpeta de salida a la de entrada, eliminando cualquier sobrante.
Esto último es especialmente útil luego de mover o eliminar algún archivo.

** Características

- Convierte archivos: .mp4; .mp3; .flac; .m4a; .webm --> .mp3 192 kbp/s
- Mantiene la estructura de carpetas original
- Elimina archivos en la carpeta de salida que ya no existen en la de entrada
- Configuración persistente mediante "sv_config.json"
- Uso automático de FFmpeg

** Requisitos

- Python 3.x
- FFmpeg instalado (y ruta configurada) (No es necesario agregar al PATH de windows)

** Configuración

El script usa un archivo "sv_config.json" con las rutas de entrada, salida, y ffmpeg. Estas pueden ser editadas por medio del mismo script,
así que no es necesario modificarlo manualmente.

** Uso

- Ejecutar "python Sekdo-Vertidor.py" en una consola.
- Revisar la configuración mostrada (entrada, salida, FFmpeg).
- Elegir: Y para modificarla o cualquier otra cosa para continuar como está.
- Al finalizar se muestra un resumen con métricas relevantes.
