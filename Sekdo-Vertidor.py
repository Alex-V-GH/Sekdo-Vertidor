import os
import subprocess
import json         

def convertir_mp4_a_mp3(input_path, output_path,ffmpeg_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Comando ffmpeg
    cmd = [
        ffmpeg_path,
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

def recorrer_directorio(input_dir, output_dir,ffmpeg_path):
    contador = 0
    contador_l = 0
    salt=1
    salteados=[]
    #cleanup
    input_files = {}
    for root, _, files in os.walk(input_dir):
        rel = os.path.relpath(root, input_dir)
        input_files.setdefault(rel, set())
        for f in files:
            input_files[rel].add(os.path.splitext(f)[0])

    for root, _, files in os.walk(output_dir):
        rel = os.path.relpath(root, output_dir)
        for f in files:
            base = os.path.splitext(f)[0]
            if base not in input_files.get(rel, set()):
                os.remove(os.path.join(root, f))
                contador_l += 1
    print(f"{contador_l} archivos limpiados")
                #print(f"**DEBUG**   ", "\n", output_dir, "\n",root, "\n",f)

    #trabajo real
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith((".mp4", ".mp3", ".flac", ".m4a", ".webm")):
                input_path = os.path.join(root, file)
                rel_path = os.path.relpath(root, input_dir)
                file_name = os.path.splitext(file)[0] + ".mp3"
                output_path = os.path.join(output_dir, rel_path, file_name)
                if not os.path.exists(output_path):
                    convertir_mp4_a_mp3(input_path, output_path,ffmpeg_path)
                contador = contador+1
                print(f"{contador} archivos convertidos")                    
            else:
                #print(f"Salteado n° {salt}: {file}")
                salt+=1
                salteados.append(file)
    salt-=1 #deshacer la ultima suma para que el total sea coherente
    
    print(f"Convertido un total de {contador} archivos, salteados {salt} archivos. Contenido total={contador+salt}. Limpiados {contador_l} archivos.")
    print("")
    print("-----------------SALTEADOS:-------------------------")
    print("")
    for salteado in salteados:
        print(salteado)

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
    # Configuración
    with open("sv_config.json", "r+", encoding="utf-8") as f:
        parameters = json.load(f)
        input_dir = parameters["input"]
        output_dir = parameters["output"]
        ffmpeg_path = parameters["ffmpeg"]
        print("Su configuración actual:\nIn: ", input_dir,"\nOut: ", output_dir, "\nFFMPEG: ", ffmpeg_path)
        if input("desea cambiarla? Y/N\n").lower() == "y":
            input_dir = input("Ruta de la carpeta de origen (presione enter para saltear):\n") or input_dir
            print (input_dir)
            output_dir = input("Ruta de la carpeta de origen (presione enter para saltear):\n") or output_dir
            print (output_dir)
            ffmpeg_path = input("Ruta de la carpeta de origen (presione enter para saltear):\n") or ffmpeg_path
            print (ffmpeg_path)
            parameters["input"] = input_dir
            parameters["output"] = output_dir
            parameters["ffmpeg"] = ffmpeg_path
            json.dump(parameters, f, indent=2)
    print("")
    recorrer_directorio(input_dir,output_dir,ffmpeg_path)
    print("")
    print("Proceso terminado. Presione ENTER para salir.")
    input()
