import os
import subprocess

# Configuración
INPUT_DIR = r"C:\Users\Alex\Desktop\Musica"       # Carpeta de entrada default
OUTPUT_DIR = r"C:\Users\Alex\Desktop\MusicaMP3"    # Carpeta de salida default
FFMPEG_PATH = r"C:\Program Files\ffmpeg\bin\ffmpeg.exe"


def convertir_mp4_a_mp3(input_path, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Comando ffmpeg
    cmd = [
        FFMPEG_PATH,
        "-y",
        "-i", input_path,
        "-vn",                   # sin video
        "-ar", "44100",          # frecuencia de muestreo
        "-ac", "2",              # estéreo
        "-b:a", "192k",          # bitrate
        "-map_metadata", "-1",   # eliminar metadatos
        output_path
    ]

    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

def recorrer_directorio(input_dir, output_dir):
    contador = 0
    salt=1
    salteados=[]
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith((".mp4", ".mp3", ".flac", ".m4a", ".webm")):
                input_path = os.path.join(root, file)
                rel_path = os.path.relpath(root, input_dir)
                file_name = os.path.splitext(file)[0] + ".mp3"
                output_path = os.path.join(output_dir, rel_path, file_name)
                if not os.path.exists(output_path):
                    convertir_mp4_a_mp3(input_path, output_path)
                contador = contador+1
                print(f"{contador} archivos convertidos")                    
            else:
                print(f"Salteado n° {salt}: {file}")
                salt+=1
                salteados.append(file)
    salt-=1 #deshacer la ultima suma para que el total sea coherente
    print(f"Convertido un total de {contador} archivos, salteados {salt} archivos. Contenido total={contador+salt}")
    print("")
    print("-----------------SALTEADOS:-------------------------")
    print("")
    for salteado in salteados:
        print(salteado)
    print("")

if __name__ == "__main__":
    #INFO
    print("*****************************************************************")
    print("*-------------------CONVERTIDOR VIDEO A AUDIO-------------------*")
    print("*FORMATOS DE ENTRADA:-------------------------------------------*")
    print("*mp4, mp3, flac, m4a, webm--------------------------------------*")
    print("*FORMATO DE SALIDA:---------------------------------------------*")
    print("*mp3------------------------------------------------------------*")
    print("*****************************************************************")
    print("")
    #print("Arrastre la carpeta a convertir o presione enter para designar:.")
    #print(INPUT_DIR)
    #inn = input()
    #if inn=="":
    #    inn=INPUT_DIR
    #print("")
    #print("Escriba la ruta destino o presione enter para designar:")
    #print(OUTPUT_DIR)
    #outt = input()
    #if outt=="":
    #    outt=OUTPUT_DIR
    #print("")
    recorrer_directorio(INPUT_DIR,OUTPUT_DIR)#(inn, outt)
    print("Proceso terminado. Presione ENTER para salir.")
    input()
