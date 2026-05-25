"""
Ejercicio 2: Determinante de una matriz NxN.
La clase Matriz incluye fill_matrix() para llenar con números aleatorios.
Taller: Vectores y matrices
"""

import random


class Matriz:
    def __init__(self, n):
        """
        Inicializa una matriz cuadrada de tamaño NxN.

        Args:
            n (int): Tamaño de la matriz.
        """
        self.n = n
        self.datos = [[0] * n for _ in range(n)]

    def fill_matrix(self):
        """Llena la matriz con números aleatorios entre 1 y 20."""
        self.datos = [
            [random.randint(1, 20) for _ in range(self.n)]
            for _ in range(self.n)
        ]

    def mostrar(self):
        """Muestra la matriz en pantalla de forma legible."""
        print()
        for fila in self.datos:
            print("  " + "  ".join(f"{val:3}" for val in fila))
        print()

    def calcular_determinante(self, matriz=None):
        """
        Calcula el determinante usando expansión por cofactores.

        Args:
            matriz (list): Submatriz a evaluar (usa self.datos si es None).

        Returns:
            float: El determinante de la matriz.
        """
        if matriz is None:
            matriz = self.datos

        n = len(matriz)

        # Caso base: matriz 1x1
        if n == 1:
            return matriz[0][0]

        # Caso base: matriz 2x2
        if n == 2:
            return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

        determinante = 0
        for col in range(n):
            # Construir submatriz eliminando fila 0 y columna col
            submatriz = [
                [matriz[fila][j] for j in range(n) if j != col]
                for fila in range(1, n)
            ]
            cofactor = ((-1) ** col) * matriz[0][col]
            determinante += cofactor * self.calcular_determinante(submatriz)

        return determinante


def main():
    print("=" * 45)
    print("     DETERMINANTE DE MATRIZ NxN")
    print("=" * 45)

    while True:
        try:
            n = int(input("\n¿De qué tamaño será la matriz? (N): "))
            if n <= 0:
                print("⚠ El tamaño debe ser mayor a 0.")
                continue
            break
        except ValueError:
            print("⚠ Ingresa un número entero válido.")

    matriz = Matriz(n)
    matriz.fill_matrix()

    print(f"\nMatriz {n}x{n} generada aleatoriamente:")
    matriz.mostrar()

    det = matriz.calcular_determinante()
    print(f"Determinante = {det:.2f}")
    print("=" * 45)


# ─── Pruebas de escritorio ───────────────────────────────────────────────────

def pruebas_escritorio():
    casos = [
        ([[5]], 5, "Matriz 1x1"),
        ([[1, 2], [3, 4]], -2, "Matriz 2x2 normal"),
        ([[2, 2], [2, 2]], 0, "Matriz 2x2 todos iguales (det=0)"),
        ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 1, "Identidad 3x3"),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, "Matriz singular 3x3"),
    ]

    print("\n" + "=" * 55)
    print("        PRUEBAS DE ESCRITORIO - Ejercicio 2")
    print("=" * 55)

    m = Matriz(1)
    aprobadas = 0

    for datos, esperado, descripcion in casos:
        m.datos = datos
        m.n = len(datos)
        resultado = round(m.calcular_determinante(), 6)
        estado = "✅ PASÓ" if resultado == esperado else "❌ FALLÓ"
        if resultado == esperado:
            aprobadas += 1
        print(f"\n{estado} | {descripcion}")
        print(f"       Esperado:  {esperado}")
        print(f"       Obtenido:  {resultado}")

    print(f"\n{'=' * 55}")
    print(f"Resultado: {aprobadas}/{len(casos)} pruebas aprobadas")
    print("=" * 55)


if __name__ == "__main__":
    pruebas_escritorio()
    print()
    main()