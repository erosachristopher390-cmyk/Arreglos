import random
import time

# =====================================================
# CONFIGURACIÓN
# =====================================================

alumnos = 100000
materias = 10

# Alumno y materia que queremos buscar
alumno_buscar = 32
materia_buscar = 5

# Número de veces que repetiremos la búsqueda
# para obtener un tiempo más fácil de medir
repeticiones = 1_000_000


# =====================================================
# CREAR MATRIZ
# =====================================================

matriz = []

for alumno in range(alumnos):

    fila = []

    for materia in range(materias):

        # Generar calificación aleatoria
        calificacion = random.randint(0, 100)

        fila.append(calificacion)

    matriz.append(fila)


# =====================================================
# MOSTRAR TABLA
# =====================================================

print("\n" + "=" * 75)
print("                    CALIFICACIONES")
print("=" * 75)

# Encabezados
print(f"{'Alumno':<15}", end="")

for materia in range(materias):
    print(f"{'Materia' + str(materia + 1):>10}", end="")

print()

print("-" * 75)


# Mostrar los 100 alumnos
for alumno in range(alumnos):

    print(f"{'Alumno' + str(alumno + 1):<15}", end="")

    for materia in range(materias):

        print(
            f"{matriz[alumno][materia]:>10}",
            end=""
        )

    print()

print("-" * 75)


# =====================================================
# BUSCAR ALUMNO Y MATERIA
# =====================================================

print("\n" + "=" * 75)
print("                    BÚSQUEDA")
print("=" * 75)

print("Alumno buscado :", alumno_buscar)
print("Materia buscada:", materia_buscar)


# Obtener la calificación
calificacion = matriz[
    alumno_buscar - 1
][
    materia_buscar - 1
]

print("Calificación    :", calificacion)


# =====================================================
# MEDIR TIEMPO
# =====================================================

print("\n" + "=" * 75)
print("                 MEDICIÓN DE TIEMPO")
print("=" * 75)

print(
    f"\nRealizando {repeticiones:,} búsquedas..."
)


# Comenzar cronómetro
inicio = time.perf_counter()


# Repetir la búsqueda muchas veces
for i in range(repeticiones):

    resultado = matriz[
        alumno_buscar - 1
    ][
        materia_buscar - 1
    ]


# Detener cronómetro
fin = time.perf_counter()


# Calcular tiempo total
tiempo_total = fin - inicio


# Tiempo promedio por búsqueda
tiempo_promedio = tiempo_total / repeticiones


# =====================================================
# MOSTRAR RESULTADOS
# =====================================================

print("\n" + "=" * 75)
print("                    RESULTADOS")
print("=" * 75)

print(
    f"\nAlumno: {alumno_buscar}"
)

print(
    f"Materia: {materia_buscar}"
)

print(
    f"Calificación: {calificacion}"
)

print(
    f"\nNúmero de búsquedas: {repeticiones:,}"
)

print(
    f"Tiempo total: {tiempo_total:.9f} segundos"
)

print(
    f"Tiempo promedio por búsqueda: "
    f"{tiempo_promedio:.12f} segundos"
)

print("\n" + "=" * 75)
