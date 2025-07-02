# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 18:11:37 2025

@author: repau
"""


import random
print("BIENVENIDOS AL MEJOR JUEGO DE PIEDRA, PAPEL O TIJERA DEL MUNDO")
# Opciones disponibles del juego
MOVIMIENTOS = ["piedra", "papel", "tijera"]

# Historial de partidas (solo ganadas y perdidas)
historial_partidas = []

# Resultados acumulados
registro_resultados = {}

# Menú principal
def menu_inicio():
    print("\nMENÚ PRINCIPAL")
    print("1. Jugar")
    print("2. Reglas del juego")
    print("3. Salir")

# Mostrar reglas del juego
def mostrar_reglas():
    print("\nREGLAS DEL JUEGO")
    print("Se permiten las siguientes selecciones entre los jugadores")
    print("- Piedra vence a Tijera")
    print("- Tijera vence a Papel")
    print("- Papel vence a Piedra")
    print("- Si los jugadores eligen el mismo objeto, es un empate y podrán volver a jugar la ronda en cuestión o no, el resultado solo se mostrara en caso de que exista un ganador mas no si se elige saltar la ronda.")
    input("\nPresiona ENTER para regresar al menú...")

# Elegir modo de juego
def seleccionar_modo():
    while True:
        print("\n¿Contra quién deseas jugar?")
        print("1. Contra la computadora")
        print("2. Contra jugador humano")
        opcion = input("Selecciona (1 o 2): ").strip()
        if opcion in ["1", "2"]:
            return opcion
        print("Opción inválida. Selecciona nuevamente.")

# Obtener nombre del jugador
def ingresar_nombre(numero):
    while True:
        nombre = input(f"Ingrese el nombre del jugador {numero}: ").strip()
        if nombre:
            return nombre
        print("El nombre no puede estar vacío.")

# Preguntar por número de partidas
def obtener_numero_rondas():
    while True:
        valor = input("¿Cuántas partidas deseas jugar?: ").strip()
        if valor.isdigit() and int(valor) > 0:
            return int(valor)
        print("Debes ingresar un número entero positivo.")

# Obtener jugada del jugador
def jugada_valida(nombre):
    while True:
        movimiento = input(f"{nombre}, elige piedra, papel o tijera: ").strip().lower()
        if movimiento in MOVIMIENTOS:
            return movimiento
        print("Entrada inválida. Intenta nuevamente.")

# Validar respuesta de sí/no
def confirmar_accion(pregunta):
    while True:
        respuesta = input(f"{pregunta} (s/n): ").strip().lower()
        if respuesta in ["s", "n"]:
            return respuesta
        print("Por favor responde solo con 's' o 'n'.")

# Determinar ganador de una ronda
def determinar_ganador(j1, j2, mov1, mov2):
    if mov1 == mov2:
        return "Empate"
    elif (mov1 == "piedra" and mov2 == "tijera") or \
         (mov1 == "tijera" and mov2 == "papel") or \
         (mov1 == "papel" and mov2 == "piedra"):
        return j1
    else:
        return j2

# Registrar resultado solo si no fue empate
def registrar_partida(j1, j2, mov1, mov2, resultado):
    if resultado != "Empate":
        historial_partidas.append({
            "jugador1": j1,
            "mov1": mov1,
            "jugador2": j2,
            "mov2": mov2,
            "ganador": resultado
        })
        for jugador in [j1, j2]:
            if jugador not in registro_resultados:
                registro_resultados[jugador] = {"ganadas": 0, "perdidas": 0}
        if resultado == j1:
            registro_resultados[j1]["ganadas"] += 1
            registro_resultados[j2]["perdidas"] += 1
        else:
            registro_resultados[j2]["ganadas"] += 1
            registro_resultados[j1]["perdidas"] += 1

# Mostrar historial de partidas jugadas (sin empates)
def mostrar_historial():
    print("\nHISTORIAL DE PARTIDAS")
    if not historial_partidas:
        print("No hay partidas registradas.")
        return
    for i, partida in enumerate(historial_partidas, start=1):
        print(f"{i}. {partida['jugador1']} ({partida['mov1']}) vs {partida['jugador2']} ({partida['mov2']}) - Ganador: {partida['ganador']}")

# Mostrar resumen de resultados
def mostrar_resumen_final():
    print("\nRESULTADOS FINALES")
    for jugador, stats in registro_resultados.items():
        print(f"{jugador}: {stats['ganadas']} ganadas | {stats['perdidas']} perdidas")

# Lógica principal del juego
def jugar():
    modo = seleccionar_modo()
    jugador1 = ingresar_nombre(1)
    jugador2 = "Computadora" if modo == "1" else ingresar_nombre(2)

    total_partidas = obtener_numero_rondas()
    partidas_realizadas = 0

    while partidas_realizadas < total_partidas:
        print(f"\n--- Partida {partidas_realizadas + 1} ---")

        mov1 = jugada_valida(jugador1)
        mov2 = random.choice(MOVIMIENTOS) if jugador2 == "Computadora" else jugada_valida(jugador2)

        print(f"{jugador1} eligió: {mov1}")
        print(f"{jugador2} eligió: {mov2}")

        resultado = determinar_ganador(jugador1, jugador2, mov1, mov2)

        if resultado == "Empate":
            print("Resultado: ¡Empate!")
            repetir = confirmar_accion("¿Desean volver a jugar esta ronda?")
            if repetir == "s":
                continue  # No cuenta la partida
        else:
            print(f"Ganador: {resultado}")
            registrar_partida(jugador1, jugador2, mov1, mov2, resultado)

        partidas_realizadas += 1

        if partidas_realizadas < total_partidas:
            continuar = confirmar_accion("¿Desean seguir jugando?")
            if continuar != "s":
                break

    mostrar_historial()
    mostrar_resumen_final()

# Programa principal
def iniciar_juego():
    while True:
        menu_inicio()
        opcion = input("Selecciona una opción: ").strip()
        if opcion == "1":
            jugar()
        elif opcion == "2":
            mostrar_reglas()
        elif opcion == "3":
            print("¡Gracias por jugar! Hasta luego.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    iniciar_juego()