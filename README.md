# :card_index_dividers: Hefesto

> Dios herrero griego usado para forjar tus proyectos

![img](img/hefesto.jpg)

## :gear: Requisitos

* python 3.9
* virtualenv

## :tada: Uso con Python

Levantar el ambiente

```bash
virtualenv -p python3.9 env

. env/bin/activate

pip install -r requeriments.txt
```

Ejecutar

```bash
python app.py
```

## :tada: Construir el script

Se lo puede usar en modo script ejecutando (se tiene que levantar el ambiente primero):

```bash
make c

./hefesto example/pipeline_ejemplo.yaml
```
## :tada: Instalar el binario

Se puede descargar el binario y usarlo en un sistema linux

```bash
wget https://github.com/brianwolf/project-hefesto/releases/download/1.0.0/hefesto
sudo chmod +x hefesto
sudo mv hefesto /usr/bin
```

## :books: Referencias

* [Iconos](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md)

## :grin: Autor

> **Brian Lobo**

* Github: [brianwolf](https://github.com/brianwolf)
* Docker Hub:  [brianwolf94](https://hub.docker.com/u/brianwolf94)
