"""
Ejercicio 5: Tabla de clasificación del Campeonato de Fútbol.
Actualiza la tabla luego de una fecha de partidos.
Taller: Vectores y matrices
"""


def crear_equipos():
    """
    Crea los equipos con sus estadísticas iniciales.

    Returns:
        list: Lista de equipos con sus datos.
    """
    equipos_data = [
        {"codigo": 1, "nombre": "Millonarios",    "pj": 5, "pg": 3, "pe": 1, "pp": 1, "gf": 9,  "gc": 5,  "pts": 10},
        {"codigo": 2, "nombre": "Nacional",        "pj": 5, "pg": 3, "pe": 0, "pp": 2, "gf": 8,  "gc": 6,  "pts": 9},
        {"codigo": 3, "nombre": "América",         "pj": 5, "pg": 2, "pe": 2, "pp": 1, "gf": 7,  "gc": 5,  "pts": 8},
        {"codigo": 4, "nombre": "Junior",          "pj": 5, "pg": 2, "pe": 1, "pp": 2, "gf": 6,  "gc": 7,  "pts": 7},
        {"codigo": 5, "nombre": "Santa Fe",        "pj": 5, "pg": 1, "pe": 3, "pp": 1, "gf": 5,  "gc": 5,  "pts": 6},
        {"codigo": 6, "nombre": "Bucaramanga",     "pj": 5, "pg": 1, "pe": 2, "pp": 2, "gf": 4,  "gc": 6,  "pts": 5},
        {"codigo": 7, "nombre": "Tolima",          "pj": 5, "pg": 1, "pe": 1, "pp": 3, "gf": 4,  "gc": 8,  "pts": 4},
        {"codigo": 8, "nombre": "Peñarol FC",      "pj": 5, "pg": 0, "pe": 2, "pp": 3, "gf": 3,  "gc": 8,  "pts": 2},
    ]
    return equipos_data


def crear_partidos():
    """
    Define los partidos de la fecha a jugar.

    Returns:
        list: Lista de partidos con códigos y goles.
    """
    return [
        {"local": 1, "goles_local": 2, "visitante": 2, "goles_visitante": 1},
        {"local": 3, "goles_local": 1, "visitante": 4, "goles_visitante": 1},
        {"local": 5, "goles_local": 0, "visitante": 6, "goles_visitante": 2},
        {"local": 7, "goles_local": 3, "visitante": 8, "goles_visitante": 0},
    ]


def actualizar_tabla(equipos, partidos):
    """
    Actualiza las estadísticas de los equipos según los resultados.

    Args:
        equipos (list): Lista de equipos.
        partidos (list): Lista de partidos jugados.

    Returns:
        list: Equipos con estadísticas actualizadas.
    """
    # Crear índice por código para acceso rápido
    indice = {e["codigo"]: e for e in equipos}

    for partido in partidos:
        local = indice[partido["local"]]
        visitante = indice[partido["visitante"]]
        gl = partido["goles_local"]
        gv = partido["goles_visitante"]

        # Actualizar partidos jugados y goles
        local["pj"] += 1
        visitante["pj"] += 1
        local["gf"] += gl
        local["gc"] += gv
        visitante["gf"] += gv
        visitante["gc"] += gl

        # Determinar resultado
        if gl > gv:           # Gana local
            local["pg"] += 1
            local["pts"] += 3
            visitante["pp"] += 1
        elif gl < gv:         # Gana visitante
            visitante["pg"] += 1
            visitante["pts"] += 3
            local["pp"] += 1
        else:                 # Empate
            local["pe"] += 1
            visitante["pe"] += 1
            local["pts"] += 1
            visitante["pts"] += 1

    # Ordenar por puntos (mayor a menor)
    return sorted(equipos, key=lambda e: e["pts"], reverse=True)


def mostrar_tabla(equipos, titulo="TABLA DE CLASIFICACIÓN"):
    """Muestra la tabla de clasificación formateada."""
    print("\n" + "=" * 70)
    print(f"  {titulo}")
    print("=" * 70)
    print(f"{'#':>3} {'Equipo':<15} {'PJ':>4} {'PG':>4} {'PE':>4} {'PP':>4} "
          f"{'GF':>4} {'GC':>4} {'DIF':>5} {'PTS':>5}")
    print("-" * 70)

    for pos, e in enumerate(equipos, 1):
        dif = e["gf"] - e["gc"]
        signo = "+" if dif > 0 else ""
        print(
            f"{pos:>3} {e['nombre']:<15} {e['pj']:>4} {e['pg']:>4} "
            f"{e['pe']:>4} {e['pp']:>4} {e['gf']:>4} {e['gc']:>4} "
            f"{signo}{dif:>4} {e['pts']:>5}"
        )
    print("=" * 70)


def mostrar_partidos(partidos, equipos):
    """Muestra los resultados de los partidos."""
    indice = {e["codigo"]: e["nombre"] for e in equipos}
    print("\n--- Resultados de la fecha ---")
    for p in partidos:
        local = indice[p["local"]]
        visitante = indice[p["visitante"]]
        print(f"  {local:<15} {p['goles_local']} - {p['goles_visitante']} {visitante}")


def main():
    print("=" * 70)
    print("    CAMPEONATO PROFESIONAL DE FÚTBOL - Actualización de Fecha")
    print("=" * 70)

    equipos = crear_equipos()
    partidos = crear_partidos()

    print("\n📋 Tabla ANTES de la fecha:")
    tabla_antes = sorted(equipos, key=lambda e: e["pts"], reverse=True)
    mostrar_tabla(tabla_antes, "TABLA ANTES DE LA FECHA")

    mostrar_partidos(partidos, equipos)

    equipos_actualizados = actualizar_tabla(equipos, partidos)

    mostrar_tabla(equipos_actualizados, "TABLA DESPUÉS DE LA FECHA")


# ─── Pruebas de escritorio ───────────────────────────────────────────────────

def pruebas_escritorio():
    print("\n" + "=" * 55)
    print("        PRUEBAS DE ESCRITORIO - Ejercicio 5")
    print("=" * 55)

    casos = [
        (3, 1, "Victoria local → local +3pts, visitante +0pts"),
        (1, 3, "Victoria visitante → visitante +3pts, local +0pts"),
        (1, 1, "Empate → ambos +1pt"),
        (0, 0, "Empate en cero → ambos +1pt"),
    ]

    aprobadas = 0
    for gl, gv, descripcion in casos:
        local = {"codigo": 1, "nombre": "A", "pj": 0, "pg": 0, "pe": 0, "pp": 0, "gf": 0, "gc": 0, "pts": 0}
        visitante = {"codigo": 2, "nombre": "B", "pj": 0, "pg": 0, "pe": 0, "pp": 0, "gf": 0, "gc": 0, "pts": 0}
        partido = {"local": 1, "goles_local": gl, "visitante": 2, "goles_visitante": gv}

        actualizar_tabla([local, visitante], [partido])

        if gl > gv:
            ok = local["pts"] == 3 and visitante["pts"] == 0
        elif gl < gv:
            ok = local["pts"] == 0 and visitante["pts"] == 3
        else:
            ok = local["pts"] == 1 and visitante["pts"] == 1

        estado = "✅ PASÓ" if ok else "❌ FALLÓ"
        if ok:
            aprobadas += 1
        print(f"\n{estado} | {descripcion}")
        print(f"       Goles: {gl}-{gv} → Local: {local['pts']}pts, Visitante: {visitante['pts']}pts")

    print(f"\n{'=' * 55}")
    print(f"Resultado: {aprobadas}/{len(casos)} pruebas aprobadas")
    print("=" * 55)


if __name__ == "__main__":
    pruebas_escritorio()
    print()
    main()