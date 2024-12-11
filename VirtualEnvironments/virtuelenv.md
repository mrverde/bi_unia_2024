# Entornos virtuales de python

Los entornos virtuales son una herramienta de Python que permiten crear entornos aislados y que sirven para gestionar las dependencias y versiones de las bibliotecas que se usan en los proyectos de desarrollo.

Estos entornos permiten crear versiones de Python aisladas para cada proyecto, evitando así que aparezcan conflictos y asegurando la instalación de versiones específicas de las bibliotecas.

## Crear un entorno virtual con anaconda y windows

Podemos acceder a la documentación en el [siguiente enlace:](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment)


Los siguientes elementos están hechos desde la línea de comandos:

Chequear si anaconda está instalado en nuestro sistema
```bash
conda -V
```

Chequear si Anaconda esta actualizado
```bash
conda update conda
```

Crear un entorno virtual
```bash
conda create -n NOMBRE_ENTORNO_VIRTUAL python=x.x anaconda
```

Activar el entorno virtual
```bash
source activate NOMBRE_ENTORNO_VIRTUAL
```

Instalar paquetes adicionales en el entorno virtual
```bash
conda install -n NOMBRE_ENTORNO_VIRTUAL [package]
```

Desactivar el entorno virtual
```bash
source deactivate
```

Borrar el entorno virtual
```bash
conda remove -n NOMBRE_ENTORNO_VIRTUAL --all
```

Ver lista de entornos
```bash
conda env list
```

Listar paquetes instalados en el entorno
```bash
conda list -n myenv
```

Exportar bibliotecas de un entonro
```bash
conda env export > environment_droplet.yml
```

# Crear un entorno virtual con pip y windows

Para crear y gestionar entornos virtuales en Python se utiliza la biblioteca virtualenv.

Para instalar virtualenv desde el gestor de paquetes pip usaremos:

```bash
pip install virtualenv
```

Para crear un entorno virtual
```bash
virtualenv venv
```

O también puede utilizarse
```bash
python -m venv venv
```

Para activar un entorno virtual (desde el directorio base)
```bash
.\venv\Scripts\activate
```

Para desactivar un entorno virtual
```bash
deactivate
```

Una vez activado, para instalar paquetes usaremos pip
```bash
pip install pandas
```

Para desinstalar un paquete
```bash
pip uninstall pandas
```

Para revisar los paquetes que tenemos instalados en el entorno virtual
```bash
pip freeze
```

Para exportar un entorno virtual
```bash
pip freeze > requirements.txt
```

```bash
pip install -r requirements.txt
```

La activación del entorno virtual con Activate puede ser diferente si estás usando un terminal diferente, así que asegúrate de consultar la documentación correspondiente a tu entorno de línea de comandos.
