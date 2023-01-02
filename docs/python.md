# Python

## :gear: Requisitos

* python 3.9
* virtualenv

## :tada: Uso

Levantar el ambiente

```bash
virtualenv -p python3.9 env

. env/bin/activate

pip install -r requeriments.txt
```

Ejecutar

```bash
python app.py examples/pipeline_ejemplo.yaml
```

## :tada: Construir el script

Se lo puede usar en modo script ejecutando (se tiene que levantar el ambiente primero):

```bash
make c

./hefesto example/pipeline_ejemplo.yaml
```

---
## :leftwards_arrow_with_hook: Navegar

* [Volver atras](../README.md)