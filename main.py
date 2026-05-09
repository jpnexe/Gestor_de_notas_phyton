# main.py
import json
def menu():
    print("\n--- SISTEMA DE GESTIÓN DE NOTAS ---")
    print("1. Registrar Estudiante")
    print("2. Ingresar Notas")
    print("3. Calcular Promedio")
    print("4. Generar Reporte")
    print("5. Guardar y Salir")
    return input("Seleccione una opción: ")



# --- FUNCIONES DEL DEV BACKEND (Ramas: feat/registro, feat/notas, feat/promedio) ---

def registrar_estudiante(estudiantes):
    """Registra un nuevo estudiante con nombre e ID."""
    nombre = input("Nombre del estudiante: ")
    id_est = input("ID del estudiante: ")
    estudiantes.append({"nombre": nombre, "id": id_est, "notas": [], "promedio": 0.0, "estado": "N/A"})
    print(f"✅ Estudiante {nombre} registrado.")

def ingresar_notas(estudiantes):
    """Ingresa notas de 0 a 5 para un estudiante específico."""
    id_est = input("ID del estudiante: ")
    for est in estudiantes:
        if est["id"] == id_est:
            try:
                nota = float(input("Ingrese nota (0-5): "))
                if 0 <= nota <= 5:
                    est["notas"].append(nota)
                    print("⭐ Nota agregada.")
                else:
                    print("❌ Error: La nota debe estar entre 0 y 5.")
            except ValueError:
                print("❌ Error: Debe ingresar un número.")
            return
    print("⚠️ Estudiante no encontrado.")
    
# se agrego la funcion para agrear notas y calcular el promedio.   
    
def calcular_promedio(estudiantes):
    """Calcula el promedio de notas para cada estudiante y determina su estado."""
    for est in estudiantes:
        if est["notas"]:
            est["promedio"] = sum(est["notas"]) / len(est["notas"])
            est["estado"] = "Aprobado" if est["promedio"] >= 3 else "Reprobado"
        else:
            est["promedio"] = 0.0
            est["estado"] = "Sin notas"
    print("✅ Promedios calculados.")
    
def generar_reporte(estudiantes):
    """Muestra una tabla formateada en consola."""
    print("\n" + "="*60)
    print(f"{'ID':<10} | {'NOMBRE':<20} | {'PROMEDIO':<10} | {'ESTADO':<10}")
    print("-" * 60)
    for est in estudiantes:
        print(f"{est['id']:<10} | {est['nombre']:<20} | {est['promedio']:<10} | {est['estado']:<10}")
    print("="*60 + "\n")
    
# Funcion para guardar los datos en un archivo JSON.
def guardar_datos(estudiantes):
    """Guarda la lista de estudiantes en un archivo JSON."""
    with open("notas.json", "w") as f:
        json.dump(estudiantes, f, indent=4)
    print("💾 Datos guardados en 'notas.json'.")
    
# Funcion para cargar los datos desde un archivo JSON.
def cargar_datos():
    """Carga los datos desde el archivo JSON si existe."""
    try:
        with open("notas.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
# --- ESTRUCTURA PRINCIPAL (MENÚ) ---

def main():
    estudiantes = cargar_datos()

    while True:
        opcion = menu()
        
        if opcion == "1":
            registrar_estudiante(estudiantes)
        elif opcion == "2":
            ingresar_notas(estudiantes)
        elif opcion == "3":
            calcular_promedio(estudiantes)
        elif opcion == "4":
            generar_reporte(estudiantes)
        elif opcion == "5":
            guardar_datos(estudiantes)
            print("👋 Saliendo del sistema...")
            break
        else:
            print("⚠️ Opción no válida.")

if __name__ == "__main__":
    main()