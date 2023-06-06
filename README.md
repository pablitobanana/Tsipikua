# TSIPIKUA
## Descripción
Este es un proyecto que consiste en la detección de enfermedades por medio de imágenes.

## Dataset
Nuestro dataset se encuentra en la nube en drive, el cual se puede acceder atreves de el siguiente link.
```sh
https://drive.google.com/drive/folders/1DhFeAb_qjpUBuk89VFcVxUUqF_alDXCl?usp=sharing
```
## Modelo
Como el modelo entrenado es muy pesado para subirlo, aquí dejo el link para poder descargarlo.
```sh
https://drive.google.com/file/d/1-9a0RtmZVF2b3KLF1y8Cpief2M5-tfCR/view?usp=sharing
```
Y para **`"instalarlo"`** solo se debe de descargar dentro de la carpeta raíz Tsipikua.

El codigo del modelo se encuentra en el siguiente link.
 ```sh
 https://colab.research.google.com/drive/1xWn3ggyTUZAlc0_EazcrRhJ9ft-NnnDK?usp=sharing
 ```

## Requerimientos

## Python
Dentro de la carpeta Tsipikua ejecutaremos los siguientes comandos para instalar todos los requerimientos del servidor.
 ```sh
 $ pip install -r requeriments.txt
 ```

## VUE
Dentro de la carpeta Tsipikua ejecutaremos los siguientes comandos para instalar todos los requerimientos de la pagina web.
```sh
$ cd Pagina-Tsipikua
$ npm install
```


## Ejecutar
### Inicializar la API

Una vez descargados los requerimientos y el modelo esta colocado dentro de la carpeta Tsipikua, a la misma altura que el archivo **`app.py`** ejecutamos el siguiente comando para levantar el servidor.
```sh
$ py app.py
```
> NOTA: Puede tardar, ya que el modelo es pesado, puede considerarse que esta listo cuando nos muestra el código de debbug.

### Visualizar la pagina y resultados
Para inicializar la pagina web entraremos a la carpeta `Pagina-Tsipikua` y ejecutaremos el siguiente comando.
```sh
$ cd Pagina-Tsipikua
$ npm run dev
```
Vaya a la dirección asignada y seria todo.
