# Programácion dinámica y estocástica

## Objetivos
* Aprender cuando utilizar programación dinámica y sus beneficios.
* Entender la diferencia entre programas deterministas y estocásticos.
* Aprender a utilizar programación estocástica.
* Aprender a crear simulaciones computacionales básicas.

# Programación dinámica
No hay que dejarse confundir por el nombre rimbombante, ya que este es simplemente un nombre de marketing que le dio su creador Richard Bellman para conseguir financiamiento y ofuscar el hecho de que esto son simplemente matemáticas.

### En que problemas se puede utilizar
* **Subestructura óptima**: Es decir que una solución global óptima se puede encontrar al combinar soluciones óptimas de subproblemas locales.
* **Problemas empalmados**: Una solución óptima que involucra resolver el mismo problema en varias ocaciones.

## Memoization:
Es una técnica qué consiste en guardar los cómputos realizados previamente en un resultado para poder consultarlo en lugar de repetir el cómputo. Un diccionario se puede consultar en O(1) (no importa el tamaño del diccionario, las consultas siempre toman lo mismo)