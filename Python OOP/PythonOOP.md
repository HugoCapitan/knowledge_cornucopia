# Programación Orientada a objetos

## Objetos
Hay 3 formas de interactuar un objecto

- Creacion
- Manipulacion
- Destruccion

Ventajas de los objetos

- Descomposicion (Dividir un problema en sus componentes pequeños)
- Abstraccion (Separar los detalles secundarios de la interfaz)
- Encapsulacion (Permite esconder datos para que solo sean usados en donde son necesarios)

### Objetos en Python
el keyword class `<clase>(<super_class>)` se usa para crear una clase, aqui podemos especificar una super clase.

En todas las clases tenemos un constructor que se ejecuta cada vez que se inicializa una instancia de nuestra clase.
Los metodos los definimos usando el keyword `def` y todos los metodos de instancia, reciben como primer parametro a la instancia misma con el nombre `self.`

Al constructor en python se le dice dunder init, dunder significa doble underscore__

``` py
def __init__(self, <params>): 
    # ... implementacion

def <method_name>(self, <params>):
    # ... implementacion

```

Para generar una instancia de nuestra clase se usa la siguiente sintaxis.

``` py
instancia = NombreDeNuestraClase(parametro1, parametro2, parametro3)
```

Despues podemos ya usar los metodos de la clase de nuestra instancia utilizando el dot notation: instancia.nombre_del_metodo()

Como en python no tenemos la palabra private para definir variables o metodos privados usamos la convencion de ponerle un underscore de prefijo a los atributos que querramos sean privados.

``` py
def _mi_metodo_privado(self, params):
    # ...implementacion

_variable_privada = 'valor'
```

>En python para elevar usamos dos asteriscos. \
> `valor**2`
> 
>Para sacar una raiz cuadrada simplemente elevamos al 0.5\
>`valor**0.5`
> El metodo isinstance(una_variable, una_clase) nos permite saber si una_variable es una instancia de una_clase

## Descomposición
La descomposición de un problema significa separarlo en problemas más pequeños.
> Es mucho más simple resolver 100 problemas pequeños que un problema enorme.

Las clases nos ayudan a descomponer problemas en programación, en problemas mas manejables, fáciles de entender y mantener.

Podemos usar el `=` al definir los parametros de una funcion para especificar un valor por default.

``` py
def __init__(self, cilindros, tipo='gasolina'):
```

## Abstracción
La abstracción es sobre separar los detalles secundarios del funcionamiento de algun objeto detras de intefaces claras y sencillas de usar.

> En lugar de preocuparnos por todos los engranes, valvulas y los detalles de como funciona un coche, solo nos preocupamos por interactuar con la interfaz de manejo (el volante, los pedales, la palanca)


## Encapsulación
Nos permite agrupar datos y comportamiento, para controlar el acceso a ellos y evitar modificaciones no deseadas.

Una estrategia que tenemos para evitar estas modificaciones es la programación defensiva, esto lo hacemos definiendo metodos especificos generalmente llamados getters y setters que controlaran la forma en la que modificamos y accedemos a las propiedades de nuestras clases.

En Python usamos los decoradores `@property` y `@<property_name>.setter` para marcar los métodos en los que definimos de que formas podremos acceder y modificar un valor.

En este ejemplo estamos encapsulando la propiedad region, la cual seria desastroso si se modificara sin antes pasar por la validación de si existe o no en las regiones validas para ese país.


``` py
class CasillaDeVotacion:
    def __init__(self, id, pais):
        self._id = id
        self._pais = pais
        self._region = None

    @property
    def region(self):
        return self._region

    @region.setter
    def set_region(self, region):
        if  region in self._pais:
            self._region = region

        raise ValueError(f'La region {region} no es valida en {self._pais}')
```

## Herencia
- Permite modelar una jerarquia de clases
- Permite compartir un comportamiento comun entre diferentes medios de la jerarquia
- Padre: superclase Hijo: subclase

### Sintaxis para herencia en python
La palabra `super` nos permite obtener una referencia directa a la superclase.
Siempre tenemos que inicializar explicitamente las superclase en el constructor de la subclase.

``` py
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)
```

## Polimorfismo
Nos permite modificar comportamientos compartidos. Se define como la habilidad de tomar varias formas.

Por ejemplo tanto los trenes como los aviones y los autos se desplazan, sin embargo cada uno lo hace en medios y de formas diferentes. Los aviones en el aire usando turbinas y alas, los autos en la carretera usando llantas y los trenes en una via.

En python para modificar un metodo de la superclase solamente tenemos que implementarlo  de nuevo en nuestra subclase con los mismos parametros.


# Complejidad algoritmica 
Nos permite comparar la eficiencia entre algoritmos. Cuando trabajamos con datasets enormes una diferencia de milisegundos facilmente puede convertirse en una diferencia de horas, meses, años, decadas, siglos y hasta vidas de un universo.

- Complejidad temporal: cuanto tiempo toma ejecutar un algoritmo
- Complejidad espacial: cuanto espacio en memoria

T(n)
funcion T que recibe input n y que determina el tiempo que tarda un algoritmo

### Aproximaciones a la funcion T
- Cronometrar el tiempo que corre un algoritmo
Esto nos enfrentra  con el problema de que este tiempo es dependiente de muchas variables como la velocidad de nuestro hardware o los procesos que estan corriendo en el momento en que se ejecuta el algoritmo, por lo que es una aproximacion bastante inexacta.

- Contar los pasos con una medida abstracta de operacion.
Es decir contar cada vez que una operacion matematica se realiza. Cuando usamos datasets muy grandes algunas cosas dejan de ser relevantes

- Contar los pasos asintoticamente, es decir conforme nos acercamos al infinito

## Notacion asintotica / BigO notation
Nos permite encuadrar cada algoritmo en una de las clases del BigO notation para compararlo.

- No importan las variaciones pequeñas
- El enfoque es en cuando el tamaño del problema se acerca al infinito

Al intentar calcular la eficiencia de un algoritmo nos podemos centrar, en el mejor de los casos, un caso promedio o el peor de los casos.

Por lo tanto el Big O se centra en el peor de los casos


## Aproximación abstracta
Para hacer un conteo abstracto de la eficiencia de una función vamos a contar cada vez que se tiene que hacer una operación.

Vamos a contar el número de operaciones en el siguiente algoritmo.

``` py
def f(x):
    # 1 operacion
    respuesta = 0

    # 1000 operaciones
    for i in range(1000):
        respuesta += 1

    # x operaciones
    for i in range(x):
        respuesta += x

   
    for i in range(x):
        for i in range(x):
            # Como aquí hay una iteración dentro de otra, esto va a multiplicar las 2 operaciones por  x * x = 2x^2
            respuesta += 1
            respuesta += 1

    # 1 operación
    return respuesta
```

Si sumamos todo al final obtenemos `1002 + x + x^2` lo cual es una buena aproximación, sin embargo cuando nos aproximamos a una x cerca del infinito, los términos que podrían parecer mas afectar a la velocidad de este algoritmo como el 1002, dejan de hacer sentido y nos distraen de lo que en realidad va a ser lo mas pesado como la x cuadrada

### Ley de la suma
``` py
def f(n):
    for i in range(n):
        print(i)

    for i in range(n):
        print(n)
```
> O(n) + O(n) = O(n + n) = O(2n) = O(n)

``` py
def f(n):
    for i in range(n):
        print(i)

    for i in range(n * n):
        print(n)
```
> O(n) + O(n * n) = O(n + n^2) = O(n^2)

### Ley de la multiplicacion
Cuando hay iteraciones dentro de iteraciones, se multiplican
``` py
def f(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
```

> O(n) * O(n) = O(n * n) = O(n^2)

Si tenemos una funcion recursiva que genera dos o mas llamadas recursivas entonces tenemos una complejidad O(2**n) o O(3**n) lo cual no es nada escalable

## Clases de complejidad algoritmica

- **O(1) Constante:** No importa cuanto cresca el dataset, se va a seguir tardando el mismo tiempo.
- **O(n) Lineal:** Si el input crece 100, nuestro crecimiento de tiempo sera de 100, siempre lineal.
- **O(log n) Logaritmico:** La funcion va a crecer de manera logaritmica, al principio mucho pero cada vez va crecer mas lento.
- **O(n log n) log lineal:** Aparte de crecer logaritmicamente tambien va crecer con una constante lineal.
- **O(n**2) Polinominal:** La funcion crece al cuadrado respecto al tamaño del input
- **O(2**n) Exponencial:** El crecimiento exponencial es el mas grave


![alt text](./Images/BigO_complexity_chart.jpeg "State Pattern's Class Diagram")

# Algoritmos de búsqueda y ordenación

## Búsqueda lineal
Busca en todos los elementos de manera secuencial.

> ¿Cual es el peor caso? \
> Que el elemento que estamos buscando este al final de la lista o que no esté

``` py
def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista:
        if elemento == objetivo:
            match = True
            break

    return match
```

## Búsqueda binaria
En esta forma de busqueda nos encargamos de hacer cada vez el problema mas pequeño, especificamente dividiendolo en 2 en cada iteracion para la búsqueda binaria.

> Pocos algoritmos son tan eficientes como la búsqueda binaria.

Es importante tomar en cuenta que este algoritmo asume que la lista en la que estamos buscando es una lista ordenada. Y si pensamos en que no existe un buen algoritmo de ordenación, para saber si vale la pena ordenar la lista hay que considerar cuantas veces vamos a hacer la búsqueda. Si se va a hacer muchas veces entonces si vale la pena ordenar y guardar la lista y despues usar una búsqueda binaria.

> ¿Cual es el peor caso?
> 

``` py
def busqueda_binaria(lista, comienzo, final , objetivo):
    if comienzo > final:
        return False

    medio = (comienzo + final) // 2

    if objetivo == lista[medio]:
        return True
    elif objetivo > lista[medio]:
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo
```

### Tradeoff espacio - tiempo
Cuando queremos optimizar el tiempo, muchas veces podemos sacrificar espacio en memoria y viceversa. Es decir, no podemos tener lo mejor de los dos. Si queremos usar menos memoria, nos tomara mas tiempo y si queremos tomar menos tiempo usaremos mas memoria.

## Ordenamiento de burbuja (Bubble sort)

El primer algoritmo de ordenamiento que veremos es el ordenamiento de burbuja. Es un algoritmo que recorre repetidamente una lista que necesita ordenarse. Compara elementos adyacentes y los intercambia si están en el orden incorrecto. Este procedimiento se repite hasta que no se requiere mas intercambios, lo que indica que la lista se encuentra ordenada.

> Este algoritmo tiene una complejidad de O(n^2)

``` py
def ordenamiento_de_burbuja(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j - 1]:
                # Notacion para hacer swapping 😱
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista
```

## Ordenamiento por inserción

Una de las características del ordenamiento por inserción es que ordena en “su
lugar.” Es decir, no requiere memoria adicional para realizar el ordenamiento
ya que simplemente modifican los valores en memoria.

La definición es simple:

1. Una lista es dividida entre una sublista ordenada y otra sublista desordenada.
> Al principio, la sublista ordenada contiene un solo elemento, por lo que por definición se encuentra ordenada.

2. A continuación se evalua el primer elemento dentro la sublista desordenada para que podamos insertarlo en el lugar correcto dentro de la lista ordenada.

3. La inserción se realiza al mover todos los elementos mayores al elemento que se está evauluando un lugar a la derecha.

4. Continua el proceso hasta que la sublista desordenada quede vacia y, por lotanto, la lista se encontrará ordenada.

```py
def ordenamiento_por_insercion(lista):
    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual
```

## Ordenamiento por mezcla / Merge Sort
El ordenamiento por mezcla es aceptado como el algoritmo de ordenamiento mas eficiente, crece en O(log n) y consiste en:

1. Dividir la lista en dos repetidamente hasta tener listas de uno o cero elementos
    - Una lista de uno o cero elementos esta siempre ordenada
2. Mezclar estas listas de manera ordenada, y seguir mezclando hasta tener una lista ordenada.

```py
def merge_sort(list_a):
    if len(list_a) > 1:
        middle = len(list_a) // 2
        left = list_a[middle:]
        right = list_a[:middle]

        merge_sort(left)
        merge_sort(right)

        pos_a = 0
        pos_b = 0
        pos_c = 0

        while pos_a < len(left) and pos_b < len(right):
            if left[pos_a] < right[pos_b]:
                list_a[pos_c] = left[pos_a]
                pos_a += 1
            else:
                list_a[pos_c] = right[pos_b]
                pos_b += 1

            pos_c += 1

        while pos_a < len(left):
            list_a[pos_c] = left[pos_a]
            pos_a += 1
            pos_c += 1

        while pos_b < len(right):
            list_a[pos_c] = right[pos_b]
            pos_b += 1
            pos_c += 1

    return list_a

```

# Graficado
### Por qué graficar?
- Visualizar grandes cantidades de datos de manera sencilla.
- Fácil comparativa entre datos
- Permite tener una primera imagen global, rápida.
- Facilidad de modificación y filtros de los datos.

## Graficado simple con bokeh
- Bokeh permite exportar a varios formatos como html, notebooks, imagenes, etc.
- Se puede usar en servidor con Flask O Django
> [Bokeh Docs](https://docs.bokeh.org/en/latest/docs/gallery.html)

Las funciones que estamos importando son:
- `figure`: es la ventana en donde vamos a graficar
- `output_file`: nos permite especificar en que archivo vamos a exportar la grafica
- `show`: nos permite crear un servidor para visualizar nuestra gráfica

```py
from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
    output_file('graficado_simple.html')
    fig = figure()

    total_vals = int(input(f'Cuantos calores quieres graficar?'))
    x_vals = list(range(total_vals))
    y_vals = []

    for x in x_vals:
        val = int(input(f'Valor y para {x}'))
        y_vals.append(val)

    fig.line(x_vals, y_vals, line_width=2)
    show(fig) 
```

# Algoritmos de optimización
Los algoritmos de optimización nos permiten encontrar las mejores opciones para algun problema, cual es el vuelo mas barato, la ruta con menos tráfico, etc.

Los algoritmos de optimización se pueden reducir a algoritmos p vs np (polinominiales vs no poliniominales)

## El problema del morral (0-1 knapsack)
Dado una mochila que tiene un limite de pesos y un monton de objetos con diferentes pesos y valor que no se pueden dividir, cual es la mejor combinación de objetos que podemos llevar en la mochila para obtener el mayor valor.

```py
def morral(available_space, weights, values, n):
    if n == 0 or available_space == 0:
        return 0
    
    current_index = n - 1

    if weights[current_index] > available_space:
        return morral(available_space, weights, values, n - 1)

    return max(
        values[current_index] + morral(available_space - weights[current_index], weights, values, n - 1),
        morral(available_space, weights, values, n - 1)
    )

    

if __name__ == '__main__': 
    valores = [60, 100, 120, 480, 230, 50, 900]
    pesos = [10, 20, 30, 20, 30, 40, 60]
    tamano_morral = 60
    n = len(valores)

    resultado = morral(tamano_morral, pesos, valores, n)
    print(resultado)
```

## Recursividad pensando en frames
Cada vez que hacemos una nueva llamada recursiva estamos creando un frame, nos vamos acercando al caso base y cuando le damos hit a ese caso base vamos de regreso.

# Ambientes Virtuales

Nos permiten aislar las herramientas y configuraciones de un proyecto de python para no afectar la instalación global.

> A partit de python 3 se incluye la librería estandar en el módulo venv

Para generar un ambiente virtual :
``` bash
$ python3.7 -m venv env
```
> el `-m` nos permite decirle al comando python3.7 que queremos ejecutar un módulo
Para activar un ambiente virtual:
``` bash
$ source env/bin/activate
```

Ya con ambiente virtual activado, podemos usar pip para instalar librerias como bokeh

``` bash
pip install bokeh
```
