"""
Ejercicio 4: Matriz de ventas de N vendedores en M años.
Calcula totales por vendedor, por año y gran total.
Taller: Vectores y matrices
"""

import random


def generar_matriz_ventas(n_vendedores, m_años):
    """
    Genera una matriz NxM con ventas aleatorias.

    Args:
        n_vendedores (int): Número de vendedores.
        m_años (int): Número de años.

    Returns:
        list: Matriz de ventas (valores entre 1000 y 50000).
    """
    return [
        [random.randint(1000, 50000) for _ in range(m_años)]
        for _ in range(n_vendedores)
    ]


def calcular_totales(matriz, n_vendedores, m_años):
    """
    Calcula totales por vendedor, por año y gran total.

    Args:
        matriz (list): Matriz de ventas NxM.
        n_vendedores (int): Número de vendedores.
        m_años (int): Número de años.

    Returns:
        tuple: (totales_vendedor, totales_año, gran_total)
    """
    totales_vendedor = [sum(matriz[i]) for i in range(n_vendedores)]
    totales_año = [sum(matriz[i][j] for i in range(n_vendedores)) for j in range(m_años)]
    gran_total = sum(totales_vendedor)

    return totales_vendedor, totales_año, gran_total


def mostrar_resultados(matriz, n_vendedores, m_años, totales_vendedor, totales_año, gran_total):
    """Muestra la matriz de ventas y todos los totales."""
    print("\n" + "=" * 60)
    print("            MATRIZ DE VENTAS")
    print("=" * 60)

    # Encabezado de años
    encabezado = f"{'Vendedor':>10}"
    for j in range(m_años):
        encabezado += f"  {'Año ' + str(j + 1):>10}"
    encabezado += f"  {'TOTAL':>12}"
    print(encabezado)
    print("-" * 60)

    # Filas de vendedores
    for i in range(n_vendedores):
        fila = f"{'V' + str(i + 1):>10}"
        for j in range(m_años):
            fila += f"  {matriz[i][j]:>10,.0f}"
        fila += f"  {totales_vendedor[i]:>12,.0f}"
        print(fila)

    print("-" * 60)

    # Fila de totales por año
    fila_total = f"{'TOTAL':>10}"
    for j in range(m_años):
        fila_total += f"  {totales_año[j]:>10,.0f}"
    fila_total += f"  {gran_total:>12,.0f}"
    print(fila_total)

    print("=" * 60)
    print(f"\n  Gran total de ventas: ${gran_total:,.0f}")
    print("=" * 60)


def main():
    print("=" * 60)
    print("       VENTAS DE VENDEDORES POR AÑOS")
    print("=" * 60)

    while True:
        try:
            n = int(input("\n¿Cuántos vendedores tiene la empresa? "))
            if n <= 0:
                print("⚠ Debe haber al menos 1 vendedor.")
                continue
            break
        except ValueError:
            print("⚠ Ingresa un número entero válido.")

    while True:
        try:
            m = int(input("¿Cuántos años de operación? "))
            if m <= 0:
                print("⚠ Debe haber al menos 1 año.")
                continue
            break
        except ValueError:
            print("⚠ Ingresa un número entero válido.")

    matriz = generar_matriz_ventas(n, m)
    totales_vendedor, totales_año, gran_total = calcular_totales(matriz, n, m)
    mostrar_resultados(matriz, n, m, totales_vendedor, totales_año, gran_total)


# ─── Pruebas de escritorio ───────────────────────────────────────────────────

def pruebas_escritorio():
    casos = [
        ([[1000]], 1, 1, [1000], [1000], 1000, "Matriz 1x1"),
        ([[0, 0], [0, 0]], 2, 2, [0, 0], [0, 0], 0, "Todas en cero"),
        (
            [[1000, 2000], [3000, 4000]], 2, 2,
            [3000, 7000], [4000, 6000], 10000,
            "Matriz 2x2 conocida"
        ),
        ([[5000, 3000, 2000]], 1, 3, [10000], [5000, 3000, 2000], 10000, "1 vendedor 3 años"),
    ]

    print("\n" + "=" * 55)
    print("        PRUEBAS DE ESCRITORIO - Ejercicio 4")
    print("=" * 55)

    aprobadas = 0
    for matriz, n, m, esp_vend, esp_año, esp_total, descripcion in casos:
        tv, ta, gt = calcular_totales(matriz, n, m)
        ok = tv == esp_vend and ta == esp_año and gt == esp_total
        estado = "✅ PASÓ" if ok else "❌ FALLÓ"
        if ok:
            aprobadas += 1
        print(f"\n{estado} | {descripcion}")
        print(f"       Total vendedores esperado: {esp_vend} → obtenido: {tv}")
        print(f"       Total años esperado:       {esp_año} → obtenido: {ta}")
        print(f"       Gran total esperado:       {esp_total} → obtenido: {gt}")

    print(f"\n{'=' * 55}")
    print(f"Resultado: {aprobadas}/{len(casos)} pruebas aprobadas")
    print("=" * 55)


if __name__ == "__main__":
    pruebas_escritorio()
    print()
    main()