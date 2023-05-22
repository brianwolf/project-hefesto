# :card_index_dividers: Hefesto

> Dios griego herrero usado para forjar tus proyectos

![img](img/hefesto.jpg)

## :tada: Uso

Se puede descargar del siguiente [link](https://github.com/brianwolf/project-hefesto/releases)

1. Si existe un archivo llamado **hefesto.yaml** y **conf.yaml** no se necesitan parametros

    ```bash
    hefesto
    ```

2. Si se tiene un archivo en otro path o con otro nombre

    ```bash
    hefesto -i examples/pipeline.yaml 
    ```

3. Si se tiene un archivo que requiere parametros desde un archivo

    ```bash
    hefesto -i examples/var-pipeline.yaml -f examples/var-conf.yaml 
    ```

4. Si se quiere pasar los parametros por linea de comandos

    ```bash
    hefesto -i examples/params-pipeline.yaml -p content="hola mundo",file=saludo
    ```

5. Si se quiere nombrar el output

    ```bash
    hefesto -i examples/pipeline.yaml -o resultado
    ```

---

## :book: Documentacion

* [Modulos disponibles](docs/modulos.md)
* [Repositorio con ejemplos](https://github.com/brianwolf/repo-hefesto-templates/)
* [Como levantar el ambiente con python](docs/python.md)

---

## :grin: Autor

> **Brian Lobo**

* Github: [brianwolf](https://github.com/brianwolf)
* Docker Hub:  [brianwolf94](https://hub.docker.com/u/brianwolf94)
