#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para gestionar commits del repositorio Git
Hace un commit del estado actual y luego pregunta qué cambios se hicieron
"""

import subprocess
import sys
from datetime import datetime


def ejecutar_comando(comando):
    """
    Ejecuta un comando en la terminal y retorna el resultado
    """
    try:
        resultado = subprocess.run(
            comando,
            shell=True,
            capture_output=True,
            text=True,
            check=False
        )
        return resultado.stdout.strip(), resultado.stderr.strip(), resultado.returncode
    except subprocess.CalledProcessError as e:
        return "", e.stderr.strip(), e.returncode


def verificar_git_config():
    """
    Verifica que Git esté configurado correctamente
    """
    print("[*] Verificando configuración de Git...")
    
    # Verificar nombre de usuario
    salida_nombre, _, codigo_nombre = ejecutar_comando("git config --global user.name")
    
    if codigo_nombre != 0 or not salida_nombre:
        print("✗ Git no está configurado correctamente")
        print("\nConfigurando Git automáticamente...")
        
        # Configurar nombre
        nombre = input("Ingresa tu nombre de usuario: ").strip()
        if nombre:
            ejecutar_comando(f'git config --global user.name "{nombre}"')
            print(f"✓ Nombre configurado: {nombre}")
        
        # Configurar email
        email = input("Ingresa tu email: ").strip()
        if email:
            ejecutar_comando(f'git config --global user.email "{email}"')
            print(f"✓ Email configurado: {email}")
    else:
        print(f"✓ Git configurado como: {salida_nombre}")
    
    return True


def mostrar_menu():
    """
    Muestra el menú principal
    """
    print("\n" + "="*50)
    print("   GESTOR DE COMMITS - GIT")
    print("="*50)
    print("\nEste script realizará un commit automático")
    print("del estado actual del repositorio.\n")


def commit_estado_actual():
    """
    Hace un commit del estado actual con timestamp
    """
    print("[*] Haciendo commit del estado actual...")
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mensaje_auto = f"[AUTO] Estado actual: {timestamp}"
    
    # Agregar todos los cambios
    stdout, stderr, _ = ejecutar_comando("git add .")
    
    # Hacer el commit con shell=True para mejor compatibilidad en Windows
    stdout, stderr, codigo = ejecutar_comando(f'git commit -m "{mensaje_auto}"')
    
    if codigo == 0:
        print(f"✓ Commit automático realizado: {mensaje_auto}")
        return True
    else:
        if "nothing to commit" in stderr.lower() or "nothing to commit" in stdout.lower():
            print("ℹ No hay cambios para hacer commit")
            return True
        else:
            print(f"✗ Error al hacer commit")
            if stderr:
                print(f"   Error: {stderr}")
            if stdout:
                print(f"   Salida: {stdout}")
            return False


def solicitar_mensaje_commit():
    """
    Solicita al usuario que ingrese el mensaje del commit
    """
    print("\n" + "-"*50)
    print("Ingrese el mensaje del commit:")
    print("-"*50)
    print()
    
    mensaje = input("Mensaje: ").strip()
    return mensaje


def hacer_commit_usuario(mensaje):
    """
    Hace un commit con el mensaje proporcionado por el usuario
    """
    if not mensaje:
        print("\n✗ El mensaje de commit no puede estar vacío")
        return False
    
    print(f"\n[*] Haciendo commit con mensaje: '{mensaje}'")
    
    # Agregar todos los cambios
    stdout, stderr, _ = ejecutar_comando("git add .")
    
    # Hacer el commit con shell=True para mejor compatibilidad en Windows
    stdout, stderr, codigo = ejecutar_comando(f'git commit -m "{mensaje}"')
    
    if codigo == 0:
        print(f"✓ Commit realizado exitosamente")
        print(f"   Mensaje: {mensaje}")
        return True
    else:
        if "nothing to commit" in stderr.lower() or "nothing to commit" in stdout.lower():
            print("ℹ No hay nuevos cambios para hacer commit")
            return True
        else:
            print(f"✗ Error al hacer commit")
            if stderr:
                print(f"   Error: {stderr}")
            if stdout:
                print(f"   Salida: {stdout}")
            return False


def mostrar_ultimo_commit():
    """
    Muestra información del último commit
    """
    salida, _, _ = ejecutar_comando("git log -1 --pretty=format:%H%n%an%n%ae%n%ai%n%s")
    
    if salida:
        lineas = salida.split('\n')
        print("\n" + "="*50)
        print("ÚLTIMO COMMIT")
        print("="*50)
        print(f"Hash:    {lineas[0]}")
        print(f"Autor:   {lineas[1]} ({lineas[2]})")
        print(f"Fecha:   {lineas[3]}")
        print(f"Mensaje: {lineas[4] if len(lineas) > 4 else 'Sin mensaje'}")
        print("="*50)


def hacer_push():
    """
    Hace push del repositorio a GitHub
    """
    print("\n[*] Enviando cambios a GitHub...")
    
    stdout, stderr, codigo = ejecutar_comando("git push origin main")
    
    if codigo == 0:
        print("✓ Push completado exitosamente")
        print(f"   {stdout}")
        return True
    else:
        print("✗ Error al hacer push a GitHub")
        if stderr:
            print(f"   Error: {stderr}")
        if stdout:
            print(f"   Salida: {stdout}")
        return False


def main():
    """
    Función principal
    """
    mostrar_menu()
    
    # Verificar configuración de Git
    verificar_git_config()
    
    # Paso 1: Commit del estado actual
    if not commit_estado_actual():
        print("\n✗ Error en el proceso. Abortando...")
        sys.exit(1)
    
    # Paso 2: Solicitar mensaje del nuevo commit
    mensaje = solicitar_mensaje_commit()
    
    # Paso 3: Hacer el commit con el mensaje del usuario
    if mensaje:
        if hacer_commit_usuario(mensaje):
            mostrar_ultimo_commit()
            print("\n✓ Commit realizado exitosamente")
            
            # Paso 4: Hacer push automático a GitHub
            print("\n" + "="*50)
            if hacer_push():
                print("\n✓ ¡Proceso completado exitosamente!")
                print("   Los cambios han sido enviados a GitHub")
            else:
                print("\n⚠ El commit se realizó pero hubo error al enviar a GitHub")
                print("   Puedes intentar manualmente con: git push origin main")
            print("="*50)
        else:
            print("\n✗ Error al hacer el commit")
            sys.exit(1)
    else:
        print("\n[*] Commit cancelado por el usuario")
        mostrar_ultimo_commit()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n✗ Proceso interrumpido por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Error inesperado: {e}")
        sys.exit(1)
