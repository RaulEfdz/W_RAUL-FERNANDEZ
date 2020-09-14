PROYECTO  Alg_IA_W.py

Este proyecto tiene el objetivo de identificar de una lista de mas de 2000 usuarios los cuales tienen un formato de datos separados por "|" ,los usuarios que tienen mas posivilidades de ser clientes para determinada empresa, para cumplir con este objetivo el algoritmo trabaja en 3 fases secuenciales las cuales dependen una de la otra:

Fase 1:
-----ENTRENAMIENTO DEL ALGORITMO---------
En esta Fase se divide en 2 partes:
   1- En la primera parte el algoritmo requiere la introduccion de almenos una palabra clave relaciona al area profecional de los usuarios requeridos: 
       Ejemplo: engineering  developers sistems ..
   2- En la segunda parte el algoritmo escoge 2 usuarios aletoriamente de la lista de entrada en este caso people.in, a continuacion los presenta en la terminal estos requieren una confirmacion la cual sera "S" para afirmar que el usuario coincide con el resultado final esperado y "N" para negar , esto se repite con 2 usuarios diferentes. Todas la palabras aprenddas por el algoritmo en esta fase se guardan en el archivo Memory.txt para su posterior uso.
  La Fase 1 le brinda al algoritmo una ruta por la cual debe moverse y buscar usuarios en la Fase 2. Antes de terminar la fase 1 el algoritmo elimina todas las palabras irelevantes como "de, el, ., ..." palabras que no aportan mucho al sistema de busqueda.  
  
 Fase 2:
 ------FILTRO Y CLASIFICACION DE USUARIOS---- 
 Esta fase se divide en 2 partes:
 
1- Esta parte se encarga de filtrar por medio de comparacion las palabras aprendidas y guardadas en Memory.txt:

 En esta  fase  se empieza por leer  Memory.txt y crear una lista con las palabras aprendidas, luego se hace un recorrido por cada uo de los usuarios en el archivo people.in y se separan por "|"  luego se comparan las palabras claves en la Memory.txt con las correspondientes entre profesion y industria de los usuarios en busca de coincidencias. Ejemplo de coincidencia ==> Engineering [ingeniero, ingineer] estas coincidecias se pueden clasificar en tres tipos correspondiete al valor de coincidecia que puede ser  >0.7  >0.8 >0.9 con maximo de 1.0, esto valores de coincidencia los utiliza el algorimo en la segsion de clasificacion. 

2- Esta segunda parte de la fase 2, se enacarga de  clasificar los uasuarios agregando los ID a people.out por medio del valor de coincidencia, tomando en cuenta que se requieren 100 usuarios procesasdos en el resultado final, esta fase toma todos los usarios procesados con una valor de concidecia > 0.9. Sí estos no son sufientes procede agregar los ID de los usuarios con valor de coincidencia > 0.8  <0.9 a la lista de los ID que ya estaban agregados en people.out que es el resultado final, la condicion se repite si aun el resulatdo no cumple con la demanda de 100 ID , repiteindo en proceso anterios con los usarios con  valor de concidencia >0.7 <0.8...
 Si despues de esta clasificacion el resultado final cumple con la demanda de los 100 ID´s se procede a la entrega del resultado final el cual hace la Fase 3.. se resalta que si la demanda de ID´s es completada en la clasificacion >0.9 el algorito pasa a la Fase 3, lo mismo paara las otras dos clasificaciones.
 
 Fase 3:
 -------PRESENTACION DE USUARIOS POTENCIALES----------
 Esta fase se encarga de  escribir y guardar el resultado final en  people.out....  Y listo los 100 ID´s estan completados.
