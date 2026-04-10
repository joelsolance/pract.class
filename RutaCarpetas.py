estoy modificando tu codigo 
import os
import pyperclip

def escanerDisco(rutaDisco):
    print(f"\n Escaneando disco: {rutaDisco}\n")
    carpetas = []

    for raiz, dirs,  _ in os.walk(rutaDisco):
        for dir in dirs:
            carpetas.append(os.path.join(raiz, dir))

    return sorted(carpetas)

def buscarCarpeta(carpetas, busqueda):
    resultados = [c for c in carpetas if busqueda.lower() in os.path.basename(c).lower()]
    return resultados

def main():
    disco = input("¿Cual es la letra de tu disco externo? (ejemplo: E): ").strip().upper()
    rutaDisco = f"{disco}:\\"

    if not os.path.exists(rutaDisco):
        print(f"No se encontro el disco {rutaDisco}")
        return

    carpetas = escanerDisco(rutaDisco)
    print(f"Se encontraron {len(carpetas)} carpetas\n")

    while True:
        busqueda = input("Escribe el nombre de la carpeta (o 'salir' para terminar): ").strip()

        if busqueda.lower() == "salir":
            break

        resultados = buscarCarpeta(carpetas, busqueda)

        if not resultados:
            print("No se encontro ninguna carpeta con ese nombre\n")
        elif len(resultados) == 1:
            ruta = resultados[0]
            pyperclip.copy(ruta)
            os.startfile(ruta)
            print(f"Carpeta encontrada: {ruta}")
            print(f"Ruta copiada al portapapeles!\n")
        else:
            print(f"Se encontraron {len(resultados)} carpetas:")
            for i, r in enumerate(resultados, 1):
                print(f"  {i}. {r}")
            numero = input("¿Cual quieres? (Escribe el numero): ").strip()
            if numero.isdigit() and 1 <= int(numero) <= len(resultados):
                ruta = resultados[int(numero) - 1]
                pyperclip.copy(ruta)
                os.startfile(ruta)
                print(f"Abriendo carpeta y ruta copiada: {ruta}\n")

if __name__ == "__main__":
    main()
