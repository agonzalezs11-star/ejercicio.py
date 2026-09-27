""
20 EJERCICIOS — CLASES Y COLECCIONES (Python)
Solución paso a paso. Cada ejercicio sigue el método de la guía:

  PASO 1  Entender      -> Entrada / Proceso / Salida
  PASO 3  Patrón        -> qué se repite y qué cambia
  PASO 4  Código        -> la clase
  PASO 5  Verificación  -> pruebas con assert (si algo falla, Python avisa)

Cada bloque es independiente: puedes copiar solo el ejercicio que necesites.

# =====================================================================
# EJERCICIO 1 · Validador de notas con promedio (Calificador)
# =====================================================================
# PASO 1 · Entrada: notas sueltas o en lote (*args)
#          Proceso: validar 0-100, guardar solo las válidas, promediar
#          Salida : True/False, lista de válidas, promedio
# PASO 3 · Patrón: cargar_notas REUTILIZA validar_nota dentro de un for.
#          Esa idea (método pequeño + método de lote) se repite en casi
#          todos los ejercicios.
"""

class Calificador:
    def __init__(self):
        self.notas = []                       # lista interna de notas válidas

    def validar_nota(self, nota):
        return 0 <= nota <= 100               # comparación encadenada

    def cargar_notas(self, *args):            # *args -> tupla con todo lo recibido
        for nota in args:
            if self.validar_nota(nota):       # reutilización
                self.notas.append(nota)
        return self.notas

    def promedio(self):
        if not self.notas:                    # evita dividir entre 0
            return 0
        return sum(self.notas) / len(self.notas)


# PASO 5 · Verificación
c = Calificador()
assert c.cargar_notas(85, 92, 110, 78, -5, 88) == [85, 92, 78, 88]
assert c.promedio() == 85.75
print("Ej 1 OK ->", c.notas, c.promedio())


# =====================================================================
# EJERCICIO 2 · Contador de palabras únicas (AnalizadorTexto)
# =====================================================================
# PASO 1 · Entrada: palabras sueltas o en lote
#          Proceso: guardar en un conjunto (sin repetidos) y en una lista (orden)
#          Salida : cantidad de palabras únicas
# PASO 3 · Patrón: dos colecciones para dos propósitos.
#          set  -> unicidad      list -> orden de llegada

class AnalizadorTexto:
    def __init__(self):
        self.unicas = set()                   # conjunto: no admite duplicados
        self.orden = []                       # lista: guarda todo en orden

    def agregar_palabra(self, palabra):
        self.unicas.add(palabra)
        self.orden.append(palabra)

    def contar_palabras(self):
        return len(self.unicas)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)     # reutilización


at = AnalizadorTexto()
at.agregar_multiples("hola", "mundo", "hola")
assert at.contar_palabras() == 2
assert at.orden == ["hola", "mundo", "hola"]
print("Ej 2 OK ->", at.contar_palabras(), at.orden)


# =====================================================================
# EJERCICIO 3 · Gestor de compras con totales (CarroCompras)
# =====================================================================
# PASO 1 · Entrada: nombre y precio de artículos
#          Proceso: guardar {nombre: precio}, sumar, filtrar por rango
#          Salida : total, lista de artículos en rango
# PASO 3 · Patrón: diccionario nombre -> precio.
#          .values() para sumar, .items() para filtrar con la clave.

class CarroCompras:
    def __init__(self):
        self.articulos = {}

    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio

    def total_carrito(self):
 
        return sum(self.articulos.values())

    def articulos_por_rango(self, precio_min, precio_max):
        resultado = []
        for nombre, precio in self.articulos.items():
            if precio_min <= precio <= precio_max:
                resultado.append(nombre)
        return resultado


c = CarroCompras()
c.agregar_articulo("pan", 2.50)
c.agregar_articulo("leche", 3.00)
c.agregar_articulo("queso", 8.00)
assert c.total_carrito() == 13.5
assert c.articulos_por_rango(2, 3) == ["pan", "leche"]
print("Ej 3 OK ->", c.total_carrito(), c.articulos_por_rango(2, 3))


# =====================================================================
# EJERCICIO 4 · Inversor de secuencias (InversorSecuencia)
# =====================================================================
# PASO 1 · Entrada: una lista o varias listas
#          Proceso: invertir SIN reversed(), guardar en diccionario
#          Salida : lista invertida / diccionario
# PASO 3 · Patrón: recorrer de atrás hacia adelante:
#          range(len-1, -1, -1) -> último índice hasta 0.
# OJO    : una lista NO puede ser clave de diccionario (no es hashable).
#          Por eso la convertimos a TUPLA: tuple(lista).

class InversorSecuencia:
    def invertir_lista(self, lista):
        invertida = []
        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])
        return invertida

    def invertir_multiples(self, *listas):
        resultado = {}
        for lista in listas:
            resultado[tuple(lista)] = self.invertir_lista(lista)   # reutilización
        return resultado


inv = InversorSecuencia()
assert inv.invertir_lista([1, 2, 3]) == [3, 2, 1]
assert inv.invertir_multiples([1, 2, 3], [4, 5]) == {(1, 2, 3): [3, 2, 1], (4, 5): [5, 4]}
print("Ej 4 OK ->", inv.invertir_multiples([1, 2, 3], [4, 5]))


# =====================================================================
# EJERCICIO 5 · Detector de pares e impares (AnalizadorNumeros)
# =====================================================================
# PASO 1 · Entrada: números en lote
#          Proceso: clasificar con el operador %
#          Salida : diccionario {'pares': [...], 'impares': [...]} y tupla
# PASO 3 · Patrón: numero % 2 == 0 -> par.
#          cantidad_pares_impares() no recibe datos, así que separar()
#          guarda el resultado en el objeto (self.pares / self.impares).

class AnalizadorNumeros:
    def __init__(self):
        self.pares = []
        self.impares = []

    def es_par(self, numero):
        return numero % 2 == 0

    def separar(self, *numeros):
        self.pares = []                       # reinicia para cada lote nuevo
        self.impares = []
        for n in numeros:
            if self.es_par(n):                # reutilización
                self.pares.append(n)
        else:
                self.impares.append(n)
        return {"pares": self.pares, "impares": self.impares}

    def cantidad_pares_impares(self):
        return (len(self.pares), len(self.impares))   # tupla


an = AnalizadorNumeros()
assert an.separar(1, 2, 3, 4, 5) == {"pares": [2, 4], "impares": [1, 3, 5]}
assert an.cantidad_pares_impares() == (2, 3)
print("Ej 5 OK ->", an.separar(1, 2, 3, 4, 5), an.cantidad_pares_impares())


# =====================================================================
# EJERCICIO 6 · Estadísticas de temperatura (GestorTemperatura)
# =====================================================================
# PASO 1 · Entrada: temperaturas sueltas o en lote
#          Proceso: guardar en lista, calcular mínimo, máximo, promedio
#          Salida : valores estadísticos
# PASO 3 · Patrón: funciones built-in sobre la lista: min(), max(), sum(), len().

class GestorTemperatura:
    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def registrar_multiples(self, *temps):
        for t in temps:
            self.registrar_temperatura(t)     # reutilización

    def minima(self):
        return min(self.temperaturas) if self.temperaturas else None

    def maxima(self):
        return max(self.temperaturas) if self.temperaturas else None

    def promedio(self):
        if not self.temperaturas:
            return None
        return sum(self.temperaturas) / len(self.temperaturas)


gt = GestorTemperatura()
gt.registrar_multiples(20, 25, 18, 30)
assert (gt.minima(), gt.maxima(), gt.promedio()) == (18, 30, 23.25)
print("Ej 6 OK ->", gt.minima(), gt.maxima(), gt.promedio())


# =====================================================================
# EJERCICIO 7 · Mapeador de edades (GestorPersonas)
# =====================================================================
# PASO 1 · Entrada: nombres y edades
#          Proceso: diccionario nombre -> edad, filtrar, promediar
#          Salida : lista de nombres, promedio
# PASO 3 · Patrón: igual que el Ej 3 (dict + items()), pero filtrando con >=.

class GestorPersonas:
    def __init__(self):
        self.personas = {}

    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):
        resultado = []
        for nombre, edad in self.personas.items():
            if edad >= edad_minima:
                resultado.append(nombre)
        return resultado

    def edad_promedio(self):
        if not self.personas:
            return 0
        return sum(self.personas.values()) / len(self.personas)


gp = GestorPersonas()
gp.agregar_persona("Ana", 28)
gp.agregar_persona("Bob", 17)
assert gp.personas_mayores(18) == ["Ana"]
assert gp.edad_promedio() == 22.5
print("Ej 7 OK ->", gp.personas_mayores(18), gp.edad_promedio())


# =====================================================================
# EJERCICIO 8 · Asignador de equipos (Equipos)
# =====================================================================
# PASO 1 · Entrada: nombres de equipos y jugadores
#          Proceso: estructura {equipo: [jugadores]}, contar, comparar
#          Salida : nombre del equipo con más jugadores
# PASO 3 · Patrón: DICCIONARIO DE LISTAS. Cada clave guarda una lista propia.
#          Para buscar el mayor: variable "mejor" + comparación en un for.
# (La guía no da salida esperada: aquí devolvemos el nombre del equipo.)

class Equipos:
    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        if nombre_equipo not in self.equipos:
            self.equipos[nombre_equipo] = []  # lista vacía para el equipo

    def agregar_jugador(self, equipo, jugador):
        if equipo not in self.equipos:
            return False                      # el equipo no existe
        self.equipos[equipo].append(jugador)
        return True

    def equipo_mayor_integrantes(self):
        mejor = None
        for nombre, jugadores in self.equipos.items():
            if mejor is None or len(jugadores) > len(self.equipos[mejor]):
                mejor = nombre
        return mejor


eq = Equipos()
eq.crear_equipo("A")
eq.crear_equipo("B")
eq.agregar_jugador("A", "Juan")
eq.agregar_jugador("A", "Pedro")
eq.agregar_jugador("B", "Luis")
assert eq.equipo_mayor_integrantes() == "A"
print("Ej 8 OK ->", eq.equipos, "| mayor:", eq.equipo_mayor_integrantes())


# =====================================================================
# EJERCICIO 9 · Validador de caracteres (AnalizadorString)
# =====================================================================
# PASO 1 · Entrada: textos
#          Proceso: recorrer carácter a carácter y clasificar
#          Salida : {'vocales': n, 'consonantes': n, 'digitos': n}
# PASO 3 · Patrón: orden de las preguntas -> primero ¿dígito?, luego ¿letra?,
#          y dentro de letra ¿vocal? (si no, consonante).
#          Espacios y signos no cuentan en nada.

class AnalizadorString:
    VOCALES = "aeiouáéíóú"

    def __init__(self):
        self.texto_mas_largo = ""             # atributo que pide el enunciado

    def solo_vocales(self, letra):
        return letra.lower() in self.VOCALES

    def contar_por_tipo(self, texto):
        conteo = {"vocales": 0, "consonantes": 0, "digitos": 0}
        for caracter in texto:
            if caracter.isdigit():
                conteo["digitos"] += 1
            elif caracter.isalpha():
                if self.solo_vocales(caracter):       # reutilización
                    conteo["vocales"] += 1
            else:
                    conteo["consonantes"] += 1
        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto
        return conteo


astr = AnalizadorString()
assert astr.contar_por_tipo("Hola123") == {"vocales": 2, "consonantes": 2, "digitos": 3}
astr.contar_por_tipo("ab")
assert astr.texto_mas_largo == "Hola123"
print("Ej 9 OK ->", astr.contar_por_tipo("Hola123"), "| más largo:", astr.texto_mas_largo)


# =====================================================================
# EJERCICIO 10 · Gestor de tareas con prioridad (Tareas)
# =====================================================================
# PASO 1 · Entrada: descripción y prioridad
#          Proceso: lista de TUPLAS (descripcion, prioridad), filtrar, eliminar
#          Salida : tareas filtradas
# PASO 3 · Patrón: las tuplas son inmutables, así que para "eliminar"
#          reconstruimos la lista SIN la tarea indicada.

class Tareas:
    def __init__(self):
        self.lista = []

    def agregar_tarea(self, descripcion, prioridad):
        self.lista.append((descripcion, prioridad))

    def tareas_prioritarias(self):
        resultado = []
        for tarea in self.lista:
            if tarea[1] == "alta":            # posición 1 de la tupla
                resultado.append(tarea)
        return resultado

    def eliminar_completada(self, descripcion):
        nueva = []
        for tarea in self.lista:
            if tarea[0] != descripcion:
                nueva.append(tarea)
        eliminada = len(nueva) < len(self.lista)
        self.lista = nueva
        return eliminada


t = Tareas()
t.agregar_tarea("Estudiar", "alta")
t.agregar_tarea("Leer", "baja")
assert t.tareas_prioritarias() == [("Estudiar", "alta")]
assert t.eliminar_completada("Estudiar") is True
assert t.lista == [("Leer", "baja")]
print("Ej 10 OK ->", t.lista)


# =====================================================================
# EJERCICIO 11 · Contador de frecuencia (ContadorFrecuencia)
# =====================================================================
# PASO 1 · Entrada: elementos sueltos o en lote
#          Proceso: diccionario elemento -> veces, buscar el máximo
#          Salida : elemento más frecuente, su frecuencia
# PASO 3 · EL patrón clásico de Python para contar:
#          dic[x] = dic.get(x, 0) + 1
#          (.get devuelve 0 si la clave aún no existe)

class ContadorFrecuencia:
    def __init__(self):
        self.frecuencias = {}

    def agregar_elemento(self, elemento):
        self.frecuencias[elemento] = self.frecuencias.get(elemento, 0) + 1

    def agregar_multiples(self, *elementos):
        for e in elementos:
            self.agregar_elemento(e)          # reutilización

    def elemento_mas_frecuente(self):
        mejor = None
        for elemento, veces in self.frecuencias.items():
            if mejor is None or veces > self.frecuencias[mejor]:
                mejor = elemento
        return mejor

    def frecuencia_elemento(self, elemento):
        return self.frecuencias.get(elemento, 0)


cf = ContadorFrecuencia()
cf.agregar_multiples("a", "b", "a")
assert cf.elemento_mas_frecuente() == "a"
assert cf.frecuencia_elemento("a") == 2 and cf.frecuencia_elemento("z") == 0
print("Ej 11 OK ->", cf.frecuencias, "| más frecuente:", cf.elemento_mas_frecuente())


# =====================================================================
# EJERCICIO 12 · Selector de rango con tuplas (SelectorRango)
# =====================================================================
# PASO 1 · Entrada: pares (inicio, fin)
#          Proceso: crear rangos como tuplas, unir sin duplicados
#          Salida : lista de elementos únicos
# PASO 3 · range() excluye el final, pero el ejemplo (1,3) incluye el 3,
#          así que usamos range(inicio, fin + 1).
#          set.update() une colecciones; sorted() devuelve lista ordenada.

class SelectorRango:
    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin + 1))

    def elementos_en_multiples_rangos(self, *rangos):
        unicos = set()
        for inicio, fin in rangos:            # desempaqueta cada tupla
            unicos.update(self.crear_rango(inicio, fin))   # reutilización
        return sorted(unicos)


sr = SelectorRango()
assert sr.crear_rango(1, 3) == (1, 2, 3)
assert sr.elementos_en_multiples_rangos((1, 3), (2, 4)) == [1, 2, 3, 4]
print("Ej 12 OK ->", sr.elementos_en_multiples_rangos((1, 3), (2, 4)))


# =====================================================================
# EJERCICIO 13 · Combinador de listas (CombinadorListas)
# =====================================================================
# PASO 1 · Entrada: dos o más listas
#          Proceso: alternar elementos usando índices
#          Salida : lista intercalada
# PASO 3 · Recorrer hasta la longitud de la lista MÁS LARGA y agregar
#          solo si el índice existe (i < len(lista)).
# NOTA   : intercalar_multiples aplica intercalar() de a pares, tal como
#          pide "reutilice". Con 3+ listas no es un turno rotativo exacto.

class CombinadorListas:
    def intercalar(self, lista1, lista2):
        resultado = []
        for i in range(max(len(lista1), len(lista2))):
            if i < len(lista1):
                resultado.append(lista1[i])
            if i < len(lista2):
                resultado.append(lista2[i])
        return resultado

    def intercalar_multiples(self, *listas):
        resultado = []
        for lista in listas:
            resultado = self.intercalar(resultado, lista)   # reutilización
        return resultado


cl = CombinadorListas()
assert cl.intercalar([1, 2], [3, 4]) == [1, 3, 2, 4]
assert cl.intercalar([1, 2, 3], [9]) == [1, 9, 2, 3]
print("Ej 13 OK ->", cl.intercalar([1, 2], [3, 4]), cl.intercalar_multiples([1, 2], [3, 4], [5, 6]))


# =====================================================================
# EJERCICIO 14 · Mapeo de estudiantes a notas (RegistroNotas)
# =====================================================================
# PASO 1 · Entrada: estudiante -> nota
#          Proceso: guardar, iterar con items(), comparar
#          Salida : lista de aprobados, tupla (nombre, nota)
# PASO 3 · Buscar el mayor: variables "mejor_nombre" y "mejor_nota"
#          que se actualizan cuando aparece una nota superior.

class RegistroNotas:
    def __init__(self):
        self.notas = {}

    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        resultado = []
        for estudiante, nota in self.notas.items():
            if nota >= nota_minima:
                resultado.append(estudiante)
        return resultado

    def mejor_estudiante(self):
        mejor_nombre, mejor_nota = None, None
        for estudiante, nota in self.notas.items():
            if mejor_nota is None or nota > mejor_nota:
                mejor_nombre, mejor_nota = estudiante, nota
        if mejor_nombre is None:
            return None
        return (mejor_nombre, mejor_nota)


rn = RegistroNotas()
rn.registrar("Ana", 95)
rn.registrar("Bob", 70)
assert rn.mejor_estudiante() == ("Ana", 95)
assert rn.estudiantes_aprobados(80) == ["Ana"]
print("Ej 14 OK ->", rn.mejor_estudiante(), rn.estudiantes_aprobados(80))


# =====================================================================
# EJERCICIO 15 · Divisores de un número (DivisorFinder)
# =====================================================================
# PASO 1 · Entrada: uno o varios números
#          Proceso: probar todos los candidatos, sumar divisores
#          Salida : tupla, booleano, diccionario
# PASO 3 · d es divisor de n si n % d == 0. Se prueba de 1 a n.
#          Número perfecto: suma de divisores SIN él mismo == él mismo.
#          Como encontrar_divisores incluye a n, restamos n a la suma.

class DivisorFinder:
    def encontrar_divisores(self, numero):
        divisores = []
        for d in range(1, numero + 1):
            if numero % d == 0:
                divisores.append(d)
        return tuple(divisores)               # se retorna como tupla

    def es_perfecto(self, numero):
        suma_sin_el_mismo = sum(self.encontrar_divisores(numero)) - numero
        return suma_sin_el_mismo == numero

    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}
        for n in numeros:
            resultado[n] = self.encontrar_divisores(n)    # reutilización
        return resultado


df = DivisorFinder()
assert df.encontrar_divisores(12) == (1, 2, 3, 4, 6, 12)
assert df.es_perfecto(6) and df.es_perfecto(28) and not df.es_perfecto(12)
assert df.encontrar_multiples_divisores(6, 7) == {6: (1, 2, 3, 6), 7: (1, 7)}
print("Ej 15 OK ->", df.encontrar_divisores(12), df.es_perfecto(28))


# =====================================================================
# EJERCICIO 16 · Codificador César (CodificadorCesar)
# =====================================================================
# PASO 1 · Entrada: letra/palabra y desplazamiento (1-25)
#          Proceso: ord() -> desplazar con % 26 -> chr(); guardar historial
#          Salida : palabra codificada
# PASO 3 · Fórmula:  chr( (ord(letra) - base + desplazamiento) % 26 + base )
#          base = ord('a') si es minúscula, ord('A') si es mayúscula.
#          El % 26 hace que después de la 'z' se vuelva a la 'a'.
#          Historial: la clave es una TUPLA (palabra, desplazamiento), así la
#          misma palabra con distinto desplazamiento no se sobrescribe.
# NOTA   : "hola" con 3 da "krod" (la guía dice "kroc" y aclara "aprox").

class CodificadorCesar:
    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        if not ("a" <= letra.lower() <= "z"):
            return letra                      # espacios, dígitos, ñ... no cambian
        base = ord("a") if letra.islower() else ord("A")
        return chr((ord(letra) - base + desplazamiento) % 26 + base)

    def codificar_palabra(self, palabra, desplazamiento):
        resultado = ""
        for letra in palabra:
            resultado += self.codificar_letra(letra, desplazamiento)   # reutilización
        self.historial[(palabra, desplazamiento)] = resultado
        return resultado


cc = CodificadorCesar()
assert cc.codificar_letra("a", 3) == "d"
assert cc.codificar_letra("z", 3) == "c"      # da la vuelta al alfabeto
assert cc.codificar_palabra("hola", 3) == "krod"
assert cc.codificar_palabra("Hola", 1) == "Ipmb"
print("Ej 16 OK ->", cc.historial)


# =====================================================================
# EJERCICIO 17 · Grupo de edades (AgrupadorEdades)
# =====================================================================
# PASO 1 · Entrada: edades en lote
#          Proceso: clasificar con if/elif, agrupar en diccionario de listas
#          Salida : {categoría: [edades]}, promedio por categoría
# PASO 3 · Rangos elegidos (la guía no los define):
#          niño < 12 | adolescente 12-17 | adulto 18-59 | mayor >= 60
#          Patrón "agrupar" (igual que Ej 20): si la clave no existe,
#          crear lista vacía; luego append.

class AgrupadorEdades:
    def __init__(self):
        self.grupos = {}

    def clasificar_edad(self, edad):
        if edad < 12:
            return "niño"
        elif edad < 18:
            return "adolescente"
        elif edad < 60:
            return "adulto"
    else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        self.grupos = {}
        for edad in edades:
            categoria = self.clasificar_edad(edad)        # reutilización
            if categoria not in self.grupos:
                self.grupos[categoria] = []
            self.grupos[categoria].append(edad)
        return self.grupos

    def edad_promedio_categoria(self, categoria):
        edades = self.grupos.get(categoria)
        if not edades:
            return None
        return sum(edades) / len(edades)


ae = AgrupadorEdades()
assert ae.agrupar_por_categoria(5, 15, 30, 70) == {
    "niño": [5], "adolescente": [15], "adulto": [30], "mayor": [70]}
ae.agrupar_por_categoria(20, 40, 5)
assert ae.edad_promedio_categoria("adulto") == 30
assert ae.edad_promedio_categoria("mayor") is None
print("Ej 17 OK ->", ae.grupos, ae.edad_promedio_categoria("adulto"))


# =====================================================================
# EJERCICIO 18 · Matriz de distancias (CalculadorDistancia)
# =====================================================================
# PASO 1 · Entrada: puntos como tuplas (x, y)
#          Proceso: fórmula euclidiana, comparar, guardar
#          Salida : distancia, punto más cercano
# PASO 3 · d = raíz( (x2-x1)² + (y2-y1)² ), la raíz es "** 0.5".
#          Punto más cercano = mismo patrón de "buscar el menor".

class CalculadorDistancia:
    def __init__(self):
        self.distancias = []                  # guarda todas las calculadas

    def distancia_euclidiana(self, p1, p2):
        x1, y1 = p1                           # desempaquetar tupla
        x2, y2 = p2
        d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        self.distancias.append(d)
        return d

    def punto_mas_cercano(self, referencia, *puntos):
        mejor_punto, mejor_dist = None, None
        for punto in puntos:
            d = self.distancia_euclidiana(referencia, punto)   # reutilización
            if mejor_dist is None or d < mejor_dist:
                mejor_punto, mejor_dist = punto, d
        return mejor_punto


cd = CalculadorDistancia()
assert cd.distancia_euclidiana((0, 0), (3, 4)) == 5.0
assert cd.punto_mas_cercano((0, 0), (5, 5), (1, 1), (3, 0)) == (1, 1)
print("Ej 18 OK ->", cd.distancias)


# =====================================================================
# EJERCICIO 19 · Inventario de productos (Inventario)
# =====================================================================
# PASO 1 · Entrada: producto y cantidad
#          Proceso: guardar/actualizar, validar que alcance, filtrar
#          Salida : True/False, lista de productos
# PASO 3 · agregar_stock SUMA a lo existente (get con 0 por defecto).
#          restar_stock valida ANTES de restar y devuelve True/False.
# NOTA   : en la guía, "pan" queda con 50-30 = 20 y pide bajo_stock(15) ->
#          ["pan"], pero 20 NO es menor que 15, así que da []. El resultado
#          ["pan"] aparece con un mínimo mayor (ej. 25).

class Inventario:
    def __init__(self):
        self.stock = {}

    def agregar_stock(self, producto, cantidad):
        self.stock[producto] = self.stock.get(producto, 0) + cantidad

    def restar_stock(self, producto, cantidad):
        if self.stock.get(producto, 0) >= cantidad:
            self.stock[producto] -= cantidad
            return True
        return False

    def productos_bajo_stock(self, minimo):
        resultado = []
        for producto, cantidad in self.stock.items():
            if cantidad < minimo:
                resultado.append(producto)
        return resultado


inv = Inventario()
inv.agregar_stock("pan", 50)
assert inv.restar_stock("pan", 30) is True
assert inv.restar_stock("pan", 100) is False  # no alcanza
assert inv.productos_bajo_stock(15) == []
assert inv.productos_bajo_stock(25) == ["pan"]
print("Ej 19 OK ->", inv.stock, inv.productos_bajo_stock(25))


# =====================================================================
# EJERCICIO 20 · Analizador de patrones en textos (AnalizadorPatrones)
# =====================================================================
# PASO 1 · Entrada: texto y patrón
#          Proceso: split(), limpiar, filtrar con startswith, agrupar, set()
#          Salida : lista, diccionario, conjunto
# PASO 3 · palabras_unicas() NO recibe texto -> la clase recuerda las
#          palabras del último análisis en self.palabras.
#          _separar() es un método auxiliar (el "_" indica uso interno).
# NOTA   : la guía muestra {..., 5:['está'], 5:['aquí']}: imposible, un dict
#          no repite claves y "está"/"aquí" tienen 4 letras. La salida
#          correcta es {2: ['el'], 4: ['gato', 'está', 'aquí']}.

class AnalizadorPatrones:
    SIGNOS = ".,;:!?¡¿\"'()"

    def __init__(self):
        self.palabras = []

    def _separar(self, texto):
        limpias = []
        for palabra in texto.lower().split():
            palabra = palabra.strip(self.SIGNOS)
            if palabra:
                limpias.append(palabra)
        self.palabras = limpias
        return limpias

    def encontrar_palabras(self, texto, patron):
        resultado = []
        for palabra in self._separar(texto):
            if palabra.startswith(patron.lower()):
                resultado.append(palabra)
        return resultado

    def agrupar_por_longitud(self, texto):
        grupos = {}
        for palabra in self._separar(texto):
            longitud = len(palabra)
            if longitud not in grupos:
                grupos[longitud] = []
            grupos[longitud].append(palabra)
        return grupos

    def palabras_unicas(self):
        return set(self.palabras)


ap = AnalizadorPatrones()
assert ap.agrupar_por_longitud("el gato está aquí") == {2: ["el"], 4: ["gato", "está", "aquí"]}
assert ap.encontrar_palabras("El perro pasa por la puerta, pero no por la pared", "pa") == ["pasa", "pared"]
ap.encontrar_palabras("hola hola mundo Hola", "h")
assert ap.palabras_unicas() == {"hola", "mundo"}
print("Ej 20 OK ->", ap.agrupar_por_longitud("el gato está aquí"))

print("\n✅ Los 20 ejercicios pasaron todas las verificaciones.")
