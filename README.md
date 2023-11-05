Para la resolucion de este laboratorio, use los conocimientos adquiridos en la clase de procesamiento de datos.

Lo primero que hice para facilitar la carga del archivo que necesitaba fue descargarlo, y convertirlo a dataframe,
para luego entrar a hacer el request a la API de los datos adicionales que se requerian.

Creé una variable, y iteré los datos correspondientes a ciudades, para obtener 9 elementos.

Despues de eso hice el request a la API y use el protocolo normal para hacerlo, especificando que queria traer datos especificos de esa APi.

Tome los datos de concentracion y ciudades, para añadirlos al dataframe que estaba elaborando, y que trajeran la informacion requerida.

Hice la conversion y ordene los datos que recien extraje del API.

Los converti a diccionario y luego le di formato .csv.

Luego simplemente elimine ciertos datos que me pedian eliminar del dataframe.

Para finalmente hacer un llamado a las funciones que creé y verificar que funcionara correctamente.


#Debo agregar que trate de seguir el test como se indicaba pero me encontre con multiples errores de assertion, debido a que la API se actualizaba constantemente y el test tenia que recibir datos fijos.
