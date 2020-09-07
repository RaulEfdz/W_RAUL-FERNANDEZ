# PROYECTO-IA-pasantia-Wisy

Este algoritmo esta escrito en Python
El objetivo es seleccionar potenciales clietes para determinado proceso de marketing que son proporcionados por un archivo People_In.txt
Los resultados son mostrados el en archivo People_Out.txt, en el cual solo se muestra el ID de los clientes con mas patencial de la lista anteri.

El algoritmo utiliza una especie de reaccion  en cascada o domino, lo que hace es tomar un minimo de palabras claves de un tema por ejemplo tecnologia 
y luego  recorre todos los elementos buscando coinsidencia  una vez encontrada una concidencia el algoritmo adquiere nuevas palabras relacionas al tema las cuales
estas dentro del elemento encontrado, esto provoca que entre mas coinsidencia encuetre el algoritmo mas preciso sera en las siguiete busqueda la cual la hace automaticamente
esto lo hace posible que el algoritmo  pueda iniciar con un minimo de 5 palabras claves al recorrer x cantidad de elementos guarde  un valor exponencial del iniciado, 
toda estas nuevas palabras que por decirlo de alguna manera "aprende" el algoritmo, se guadan en  Memory.txt, que funciona como almacenamiento para el algoritmo.
Tambien el algoritmo al final pide un valor de cantidad  numerica para establecer la cantidad de ID que el usuario desee veer, estos puedes ser desde 1>
Tambien se debe tomar encuenta que la cantidad de ID en la salida debe ser relacinada a los elementos de entrada.
el algoritmo tambien lo diseñe para que  si se desea aregen palabras claves de forma manual.


Para mejorar:
El algoritmo analiza las palabras claves y crea una reaccion en cascada, esto implica que luego de analizar miles de elementos se necesitaran mas recursos computacionales
para que este llevo su trabajo, pero es posible modificarlo y hacerlo mas eficiente.
Un ejemplo de esto seria  programarlo para  reducir palabras usando antonimos y sinonimos.

Datos para Mejorar el Algoritmo: 
Es necesario agregar datos como las edades de los clientes ya que el mercado de la tecnologia tiene diferentes segmentacios las cuales nos pueden brindar datos 
mas detallados de los clientes, y hacerles llegar una  publisidad precisa. Datos como  gustos o pasatiempos ejemplo: Vieojuegos, Vieobloger, diseador ...

Considero ue este algoritmo sera muy util en el campo del mrketin perzonalisado agregando mas datos y entrenado mas la memoria con palabras claves.

