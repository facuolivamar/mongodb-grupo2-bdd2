# MongoDB - Informe Grupo 2

**Fecha:** 08.11.2023

**Materia:** Base De Datos 2

**Tema:** MongoDB

**Integrantes:**
- Andino Guillermo
- Galaverna Lorenzo
- Gonzalez Juan Ignacio
- Güell Tomás
- Márquez Lisandro
- Oliva Marchetto Facundo

**Profesores:**
- Frattin Juan
- Reyna Teodoro

## Contenido del Informe

1. [**Introducción a MongoDB**](#1-introducción-a-mongodb) - 2
2. [**MongoDB**](#2-mongodb) - 2
3. [**Profundizando sobre BSON**](#3-profundizando-sobre-bson) - 2
4. [**Usos y características**](#4-usos-y-características) - 2
5. [**Documentos, Colecciones y Bases de Datos**](#5-documentos-colecciones-y-bases-de-datos) - 4
6. [**Comparación entre MongoDB y SQL**](#6-comparación-entre-mongodb-y-sql) - 4
7. [**Comenzando con MongoDB Atlas UI**](#7-comenzando-con-mongodb-atlas-ui) - 6
8. [**Modelo de Documentos en MongoDB**](#8-modelo-de-documentos-en-mongodb) - 7
9. [**Esquema**](#9-esquema) - 7
10. [**Sintaxis**](#10-sintaxis) - 7
11. [**Modelado de Datos en MongoDB**](#11-modelado-de-datos-en-mongodb) - 8
12. [**Diferencias entre bases de datos relacionales y no relacionales**](#12-diferencias-entre-bases-de-datos-relacionales-y-no-relacionales) - 8
13. [**Principios de MongoDB**](#13-principios-de-mongodb) - 9
14. [**Relaciones comunes**](#14-relaciones-comunes) - 9
15. [**Formas de modelar datos (Embedding, Referencing)**](#15-formas-de-modelar-datos-embedding-referencing) - 11
16. [**Escalabilidad de un modelo de datos**](#16-escalabilidad-de-un-modelo-de-datos) - 12
17. [**Conexión a una base de datos MongoDB**](#17-conexión-a-una-base-de-datos-mongodb) - 13
18. [**Implementación de Connection Strings desde Aplicacion Node.js**](#18-implementación-de-connection-strings-desde-aplicacion-nodejs) - 13
19. [**Operaciones CRUD en MongoDB**](#19-operaciones-crud-en-mongodb) - 15
20. [**Inserción de documentos en una colección MongoDB (Create)**](#20-inserción-de-documentos-en-una-colección-mongodb-create) - 15
21. [**Búsqueda de documentos en una colección MongoDB (Read)**](#21-búsqueda-de-documentos-en-una-colección-mongodb-read) - 16
22. [**Actualización de documentos (Update)**](#22-actualización-de-documentos-update) - 17
23. [**Eliminación de documentos (Delete)**](#23-eliminación-de-documentos-delete) - 19
24. [**Transacciones (Transactions)**](#24-transacciones-transactions) - 20
25. [**Aggregation en MongoDB**](#25-aggregation-en-mongodb) - 22
26. [**Definiciones Clave y Estructura**](#26-definiciones-clave-y-estructura) - 22
27. [**Stages más usadas comúnmente y ejemplos**](#27-stages-más-usadas-comúnmente-y-ejemplos) - 22
28. [**Índices en MongoDB en Colecciones**](#28-índices-en-mongodb-en-colecciones) - 25
29. [**Tipos de índices más comunes**](#29-tipos-de-índices-más-comunes) - 26
30. [**Otros métodos para realizar sobre índices**](#30-otros-métodos-para-realizar-sobre-índices) - 27
31. [**Eliminación de índices**](#31-eliminación-de-índices) - 29
32. [**Material de Presentación**](#32-material-de-presentación) - 29
33. [**Bibliografía**](#33-bibliografía) - 30

## Enlaces Útiles

- [Repositorio en GitHub](https://github.com/facuolivamar/mongodb-grupo2-bdd2)
- [Presentación en Genially](https://view.genial.ly/654950d16dfa440011df2a1b/presentation-presentacion-uni-educacion)

## Actividades Realizadas

### Actividad Python
- [Código en GitHub](https://github.com/facuolivamar/mongodb-grupo2-bdd2/blob/main/act-connection.py)

### Kahoot
- [Diapositivas en GitHub](https://github.com/facuolivamar/mongodb-grupo2-bdd2/tree/main/Multimedia%20Actividades/kahoot)

### Informe
- [PDF](https://github.com/facuolivamar/mongodb-grupo2-bdd2/tree/main/Multimedia%20Actividades/kahoot)

## Acreditaciones
- Certificados obtenidos durante la capacitación en [MongoDB University](https://university.mongodb.com/):
  - [Certificado 1](https://ti-user-certificates.s3.amazonaws.com/ae62dcd7-abdc-4e90-a570-83eccba49043/f6d4b15e-2a0e-4632-9af8-d191e936eb99-facundo-oliva-marchetto-4c7a5c46-989f-414a-9ee3-641247900a9d-certificate.pdf)
  - [Certificado 2](https://ti-user-certificates.s3.amazonaws.com/ae62dcd7-abdc-4e90-a570-83eccba49043/f6d4b15e-2a0e-4632-9af8-d191e936eb99-facundo-oliva-marchetto-233581d8-06a4-4eef-a070-5461b902452b-certificate.pdf)
  - [Certificado 3](https://ti-user-certificates.s3.amazonaws.com/ae62dcd7-abdc-4e90-a570-83eccba49043/f6d4b15e-2a0e-4632-9af8-d191e936eb99-facundo-oliva-marchetto-139aaada-91d0-4c19-96bf-6eb2c9a90068-certificate.pdf)
  - [Certificado 4](https://ti-user-certificates.s3.amazonaws.com/ae62dcd7-abdc-4e90-a570-83eccba49043/2f59ca0e-a46b-4ec3-95af-e38007a696ca-llmtech-n-a-3c93076e-9f33-4df5-a6c7-cbd14401ef0d-certificate.pdf)
  - [Certificado 5](https://ti-user-certificates.s3.amazonaws.com/ae62dcd7-abdc-4e90-a570-83eccba49043/2f59ca0e-a46b-4ec3-95af-e38007a696ca-llmtech-n-a-427f2270-22f2-4248-93ed-f1bc57fa2c9e-certificate.pdf)
  - +10 Certificados individuales ...
  - [Final Proof of Completion](https://ti-user-certificates.s3.amazonaws.com/ae62dcd7-abdc-4e90-a570-83eccba49043/f6d4b15e-2a0e-4632-9af8-d191e936eb99-facundo-oliva-marchetto-f8378a30-72ef-4d3f-9f33-01ed410efa2a-certificate.pdf)
