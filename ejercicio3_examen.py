"""
Ejercicio 3: Examen de admisión universitaria.
Evalúa aptitud matemática (30 preguntas) y verbal (30 preguntas).
Taller: Vectores y matrices
"""

import random


# Respuestas correctas del examen (valores entre 1 y 5)
RESPUESTAS_CORRECTAS = [random.randint(1, 5) for _ in range(60)]


def generar_estudiante(credencial):
    """
    Genera un estudiante con respuestas aleatorias.

    Args:
        credencial (int): Número de identificación del estudiante.

    Returns:
        dict: Datos del estudiante con credencial y respuestas.
    """
    return {
        "credencial": credencial,
        "respuestas": [random.randint(1, 5) for _ in range(60)]
    }


def calificar_estudiante(estudiante, respuestas_correctas):
    """
    Calcula el puntaje de un estudiante en cada prueba.

    Args:
        estudiante (dict): Datos del estudiante.
        respuestas_correctas (list): Lista de 60 respuestas correctas.

    Returns:
        dict: Puntajes del estudiante (matematicas, verbal, total).
    """
    mat = sum(
        1 for i in range(30)
        if estudiante["respuestas"][i] == respuestas_correctas[i]
    )
    ver = sum(
        1 for i in range(30, 60)
        if estudiante["respuestas"][i] == respuestas_correctas[i]
    )
    return {
        "credencial": estudiante["credencial"],
        "matematicas": mat,
        "verbal": ver,
        "total": mat + ver
    }


def analizar_resultados(resultados):
    """
    Calcula promedios, mejores estudiantes y ranking.

    Args:
        resultados (list): Lista de puntajes por estudiante.

    Returns:
        dict: Análisis completo del examen.
    """
    n = len(resultados)
    prom_mat = sum(r["matematicas"] for r in resultados) / n
    prom_ver = sum(r["verbal"] for r in resultados) / n
    prom_total = sum(r["total"] for r in resultados) / n
    mayor = max(r["total"] for r in resultados)

    sobre_promedio = [r for r in resultados if r["total"] >= prom_total]
    mejores = [r for r in resultados if r["total"] == mayor]

    return {
        "prom_mat": prom_mat,
        "prom_ver": prom_ver,
        "prom_total": prom_total,
        "sobre_promedio": sobre_promedio,
        "mayor_puntaje": mayor,
        "mejores": mejores
    }


def mostrar_resultados(resultados, analisis):
    """Muestra todos los resultados del examen."""
    print("\n" + "=" * 55)
    print("         RESULTADOS POR ESTUDIANTE")
    print("=" * 55)
    print(f"{'Credencial':>12} {'Matemáticas':>12} {'Verbal':>8} {'Total':>7}")
    print("-" * 55)
    for r in resultados:
        print(
            f"{r['credencial']:>12} {r['matematicas']:>12} "
            f"{r['verbal']:>8} {r['total']:>7}"
        )

    print("\n" + "=" * 55)
    print("              ANÁLISIS GENERAL")
    print("=" * 55)
    print(f"  Promedio matemáticas : {analisis['prom_mat']:.2f} / 30")
    print(f"  Promedio verbal      : {analisis['prom_ver']:.2f} / 30")
    print(f"  Promedio total       : {analisis['prom_total']:.2f} / 60")

    print(f"\n  Estudiantes con puntaje ≥ promedio ({analisis['prom_total']:.2f}):")
    for r in analisis["sobre_promedio"]:
        print(f"    Credencial {r['credencial']} → {r['total']} puntos")

    print(f"\n  Mayor puntaje: {analisis['mayor_puntaje']} puntos")
    print(f"  Obtenido por:")
    for r in analisis["mejores"]:
        print(f"    Credencial {r['credencial']}")
    print("=" * 55)


def main():
    print("=" * 55)
    print("       EXAMEN DE ADMISIÓN UNIVERSITARIA")
    print("=" * 55)

    while True:
        try:
            n = int(input("\n¿Cuántos estudiantes se presentaron? "))
            if n <= 0:
                print("⚠ Debe haber al menos 1 estudiante.")
                continue
            break
        except ValueError:
            print("⚠ Ingresa un número entero válido.")

    estudiantes = [generar_estudiante(i + 1) for i in range(n)]
    resultados = [
        calificar_estudiante(e, RESPUESTAS_CORRECTAS)
        for e in estudiantes
    ]
    analisis = analizar_resultados(resultados)
    mostrar_resultados(resultados, analisis)


# ─── Pruebas de escritorio ───────────────────────────────────────────────────

def pruebas_escritorio():
    correctas = [1] * 60  # Todas las respuestas correctas son 1

    casos = [
        ([1] * 60, 30, 30, "Todas correctas"),
        ([2] * 60, 0, 0, "Todas incorrectas"),
        ([1] * 30 + [2] * 30, 30, 0, "Solo matemáticas correctas"),
        ([2] * 30 + [1] * 30, 0, 30, "Solo verbal correcta"),
    ]

    print("\n" + "=" * 55)
    print("        PRUEBAS DE ESCRITORIO - Ejercicio 3")
    print("=" * 55)

    aprobadas = 0
    for respuestas, esp_mat, esp_ver, descripcion in casos:
        estudiante = {"credencial": 1, "respuestas": respuestas}
        resultado = calificar_estudiante(estudiante, correctas)
        ok = resultado["matematicas"] == esp_mat and resultado["verbal"] == esp_ver
        estado = "✅ PASÓ" if ok else "❌ FALLÓ"
        if ok:
            aprobadas += 1
        print(f"\n{estado} | {descripcion}")
        print(f"       Matemáticas esperado: {esp_mat} → obtenido: {resultado['matematicas']}")
        print(f"       Verbal esperado:      {esp_ver} → obtenido: {resultado['verbal']}")
        print(f"       Total: {resultado['total']}")

    print(f"\n{'=' * 55}")
    print(f"Resultado: {aprobadas}/{len(casos)} pruebas aprobadas")
    print("=" * 55)


if __name__ == "__main__":
    pruebas_escritorio()
    print()
    main()