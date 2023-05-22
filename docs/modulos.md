# Modulos

Para usar los modulos estos tienen que estar en un formato yaml como el siguiente ejemplo:

```yaml
- module: git_clone
  url: https://github.com/brianwolf/UTN-sensorial-raspberry-deploy.git

- module: workingdir
  path: "UTN-sensorial-raspberry-deploy"

- module: sh
  cmd: "> hola.txt"

- module: new_file
  path: /
  content: |
    soy un archivo muy feliz
```

## copy

> copia un archivo de un origen a un destino

* from: path origen
* to: path destino

## delete

> borra un archivo

* path: path

## git_clone

> hace un git clon de un repositorio de git

* url: url del repo de git
* username: (opcional) nombre de usuario del repo
* password: (opcional) pass del usuario del repo
* branch: (opcional) rama del repo, por default es master o main

## move

> mueve un archivo

* from: path origen
* to: path destino

## new_file

> crea un archivo

* path: path
* content: contenido del archivo

## new_folder

> crea un directorio

* path: path

## replace_content

> reemplaza el contenido de los archivos en un path

* words: lista de palabras a reemplazar, por ejemplo: - README.md: "ASD.md"
* ignore: lista de paths para ignorar a reemplazar el contenido

## replace_dir

> reemplaza el nombre del archivo por otro

* words: lista de palabras a reemplazar, por ejemplo: - README.md: "ASD.md"
* ignore: lista de paths para ignorar a reemplazar

## sh

> Ejecuta comandos con sh

* cmd: comando a ejecutar

## workingdir

> Establece un workingdir

* path: path

## zip

> Genera un archivo zip ejecutando el comando *zip*

* path: path
* output: (opcional) nombre del archivo zip de salida

---

## :leftwards_arrow_with_hook: Navegar

* [Volver atras](../README.md)
