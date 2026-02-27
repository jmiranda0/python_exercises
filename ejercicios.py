"""
#1 Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

#2 Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
    - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

#3 Crea una agenda de contactos por terminal.
    - Debes implementar funcionalidades de búsqueda, inserción, actualización
      y eliminación de contactos.
    - Cada contacto debe tener un nombre y un número de teléfono.
    - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
      y a continuación los datos necesarios para llevarla a cabo.
    - El programa no puede dejar introducir números de teléfono no numéricos y con más
      de 11 dígitos (o el número de dígitos que quieras).
    - También se debe proponer una operación de finalización del programa.

#4 Crea un programa que analice dos palabras diferentes y realice comprobaciones para descubrir si son:
    - Palíndromos
    - Anagramas
    - Isogramas

#5 Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
    - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
      Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
      se asigna a dos variables diferentes a las originales. A continuación, imprime
      el valor de las variables originales y las nuevas, comprobando que se ha invertido
      su valor en las segundas.
      Comprueba también que se ha conservado el valor original en las primeras.

#6 Utiliza el concepto de recursividad para:
    - Calcular el factorial de un número concreto (la función recibe ese número).
    - Calcular el valor de un elemento concreto (según su posición) en la 
      sucesión de Fibonacci (la función recibe la posición).

#7 - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
     de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
     que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
     Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
     el nombre de una nueva web.
   - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
     impresora compartida que recibe documentos y los imprime cuando así se le indica.
     La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
     interpretan como nombres de documentos.

#8 Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
   en el ejercicio número 7 de la ruta de estudio)
   - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
     retornar el número de elementos e imprimir todo su contenido.

#9 Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
   pueden ser Gerentes, Gerentes de Proyectos o Programadores.
   Cada empleado tiene un identificador y un nombre.
   Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
   actividad, y almacenan los empleados a su cargo.

#10 Crea una función que sea capaz de procesar parámetros, pero que también
   pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
   corresponderse con un tipo de excepción creada por nosotros de manera
   personalizada, y debe ser lanzada de manera manual) en caso de error.
    - Captura todas las excepciones desde el lugar donde llamas a la función.
    - Imprime el tipo de error.
    - Imprime si no se ha producido ningún error.
    - Imprime que la ejecución ha finalizado.
"""