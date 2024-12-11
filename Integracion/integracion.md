# Integración de datos

Es el proceso de combinar y armonizar datos de distintas fuentes en un formato unificado y coherente y que les permitan ser utilizados para fines analíticos.

Las empresas por norma general recopilan datos de múltiples fuentes: bases de datos, aplicaciones, hojas de cálculo, IoT, APIs, páginas web, ... Estos datos suelen estar disponibles de formas distintas, a veces con formatos no compatibles entre sí, con codificaciones distintas en función del país, etc... Lo que da lugar a incoherencias, análisis que no tienen una suficiente calidad y que pueden lastrar la toma de decisiones

Con el proceso de integración se intenta solucionar estos problemas.

## ¿Cómo funciona el proceso de integración de datos?

1. Identificación de las fuentes de datos. Bases de datos, hojas de cálculo, servicios en la nube, APIs...

2. Extracción de datos.

3. Mapeo de datos (Estandarización)

4. Validación.

5. Transformación.

6. Carga

7. Sincronización.

8. Gobierno.

9. Gestión de los metadatos.

10. Acceso y análisis.

## ETLs y ELTs

ETL es el acrónimo de **Extraction**, **Transform** y **Load** (Extracción, transformación y carga) y es un proceso dentro de la integración de datos que se utiliza para mezclar datos provenientes de varias fuentes en un conjunto único y coherente.

En las ELTs la carga de datos se produce antes que su transformación. 

Las ELTs suelen ofrecer más rendimiento que las ETLs, pero estas últimas suelen ofrecer datos de mayor calidad.

Es una parte fundamental dentro del proceso de trabajo de análisis de datos y machine learning.

### Extracción

En este paso se extraen los datos sin procesar. Se pueden extraer de diferentes fuentes, estructurados o sin estructurar. Algunas posibles fuentes de datos pueden ser:

- Bases de datos SQL
- Bases de datos NoSQL
- Archivos
- Páginas web
- APIs

### Transformación

Aquí los datos se procesan y tratan para poder ser utilizados en análisis. Esta fase puede implicar :

- Filtrar, depurar, eliminar duplicados, validar...
- Realizar cálculos, traducir, resumir, conversión, edición de textos...
- Realizar auditorías que garanticen la calidad de los datos...
- Eliminar, cifrar o proteger datos sensibles con protección legal...
- Formatear los datos en tablas para que coincida con los esquemas de dato de destino...

### Carga

En este paso los datos se trasladan a la zona de preparación o almacén de datos de destino.

# Bibliografía
https://es.wikipedia.org/wiki/Extract,_transform_and_load 
https://www.ibm.com/es-es/topics/etl
https://www.ibm.com/es-es/topics/data-integration
https://aws.amazon.com/es/what-is/etl/
https://aws.amazon.com/es/what-is/api/
https://restfulapi.net/http-methods/
https://developer.mozilla.org/es/docs/Web/HTTP/Status
