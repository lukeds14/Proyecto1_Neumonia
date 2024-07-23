# Proyecto herramienta para la detección rápida de neumonía.

## Presentado por: Luis Eduardo Solarte Riascos.

Aplicación de técnicas de Deep Learning para el análisis de radiografías de tórax en formato DICOM, con el objetivo de clasificarlas en tres categorías distintas:

1. Neumonía Bacteriana
2. Neumonía Viral
3. Ausencia de Neumonía


---

## Uso de la herramienta:

Requerimientos necesarios para el funcionamiento.

  - Guia para la implementación necesaria:
  
   1. Copiar los archivos en una carpeta Neumonia.
  
   2.  Instale Anaconda para Windows siguiendo las siguientes instrucciones:
       https://docs.anaconda.com/anaconda/install/windows/

   3. Abra Anaconda Prompt y ejecute las siguientes instrucciones:

		- conda create -n tf tensorflow

		- conda activate tf

        - cd Neumonia    "Ingresar al directorio donde se copiaron los archivos" 

	4. Ejecute la aplicacion con el siguiente comando:
		
		- docker run -it  -e DISPLAY=host.docker.internal:0.0 detector:neumonia python3 main.py
		
	5. Ejecute las preubas unitarias con los siguientes comandos:
		
		- docker run -it  -e DISPLAY=host.docker.internal:0.0 detector:neumonia python3 test_read_file.py
		- docker run -it  -e DISPLAY=host.docker.internal:0.0 detector:neumonia python3 test_preprocesImagen.py

  

Uso de la Interfaz Gráfica:

- Ingrese la cédula del paciente en la caja de texto
- Presione el botón 'Cargar Imagen', seleccione la imagen del explorador de archivos del computador (Imagenes de prueba en https://drive.google.com/drive/folders/1WOuL0wdVC6aojy8IfssHcqZ4Up14dy0g?usp=drive_link)
- Presione el botón 'Predecir' y espere unos segundos hasta que observe los resultados
- Presione el botón 'Guardar' para almacenar la información del paciente en un archivo excel con extensión .csv
- Presione el botón 'PDF' para descargar un archivo PDF con la información desplegada en la interfaz
- Presión el botón 'Borrar' si desea cargar una nueva imagen

---

## Arquitectura de archivos propuesta.

## main.py

En este código es un punto de entrada simple para una aplicación de detección de neumonía. Al ejecutarlo, se importa la clase NeumoniaDetectorApp y 
se crea una instancia de esta clase, lo que inicia la aplicación y permite al usuario interactuar con ella.

## neumoniaDetectorApp.py

esta aplicación proporciona una interfaz gráfica para cargar imágenes radiográficas, predecir la presencia de neumonía, mostrar los resultados 
y probabilidades, generar informes PDF y guardar los resultados en un archivo CSV. La aplicación utiliza funciones externas para leer y procesar 
las imágenes, y realizar las predicciones.

## leerImagen.py

 este código proporciona funciones para leer y procesar imágenes en formatos DICOM y JPG. Ambas funciones normalizan los datos de píxeles para 
 asegurar que estén en un rango adecuado para su visualización y procesamiento. La función read_dicom_file está especialmente diseñada para trabajar 
 con imágenes médicas, mientras que read_jpg_file se encarga de imágenes estándar. Ambas funciones retornan imágenes que pueden ser utilizadas 
 en aplicaciones de visualización o análisis posterior.

## preprocesImagen.py

La función preprocess realiza un preprocesamiento integral de imágenes, que incluye redimensionamiento, conversión a escala de grises, mejora 
del contraste mediante CLAHE, normalización y ajuste de dimensiones. Este tipo de preprocesamiento es común en aplicaciones de visión por computadora
y aprendizaje automático, especialmente en tareas como la detección de objetos y clasificación de imágenes.

## load_model.py

Este código es un ejemplo de cómo cargar y preparar un modelo de aprendizaje profundo en TensorFlow. Desactiva la ejecución ansiosa para asegurar que 
el modelo funcione en un modo de ejecución por lotes, habilita la salida de intermediarios para facilitar la depuración, y define una función que carga 
un modelo desde un archivo, verifica si necesita ser compilado y, si es necesario, lo compila con una función de pérdida y un optimizador. Este enfoque
es común en aplicaciones de aprendizaje automático donde se requiere reutilizar modelos previamente entrenados.

## grad_cam.py

Este código implementa el algoritmo Grad-CAM para generar un mapa de calor que resalta las regiones más relevantes de una imagen con respecto a la 
predicción de un modelo de aprendizaje profundo. El mapa de calor se superpone sobre la imagen original para visualizar las áreas que más influyen en
la predicción del modelo. Este tipo de técnica de visualización es útil para interpretar y explicar las predicciones de los modelos de aprendizaje 
profundo, especialmente en tareas de clasificación de imágenes.

## PrediccionModelo.py

La función predict implementa un flujo completo para realizar predicciones sobre una imagen utilizando un modelo de aprendizaje profundo.
Incluye el preprocesamiento de la imagen, la carga del modelo, la obtención de la predicción y la probabilidad, la asignación de etiquetas y la 
generación de un mapa de calor Grad-CAM para visualizar las áreas relevantes de la imagen. Este enfoque es útil en aplicaciones de diagnóstico médico
y en cualquier contexto donde se requiera interpretar las decisiones de un modelo de aprendizaje profundo.

## test_read_files.py

Este código proporciona un conjunto de pruebas automatizadas para las funciones read_dicom_file y read_jpg_file. Verifica que estas funciones devuelvan 
los tipos de datos correctos, que las imágenes tengan la forma esperada y que contengan valores de píxel válidos. Las pruebas son una parte esencial del
desarrollo de software, ya que ayudan a garantizar que las funciones se comporten como se espera y a detectar errores de manera temprana.

## test_preprocesImagen

La función test_preprocess es un ejemplo de una prueba automatizada que verifica el correcto funcionamiento de la función preprocess. Asegura que la 
imagen se cargue correctamente, que el preprocesamiento produzca una imagen con la forma y el rango de valores esperados.

## requierements.txt

Archivo en formato txt que contiene las aplicaciones necesarias que se deben instalar para que la aplicación funcione correctamente.

--

Para cargar las imagenes del directorio del contenedor ubicarse en la siguiente ruta: /home/src/





