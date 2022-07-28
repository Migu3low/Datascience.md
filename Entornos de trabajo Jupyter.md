# Introducción:
### ***Notebooks origen***

2001 Fernando Pérez Creador de IPython REPL Read Evaluation Print Loop
Presentar hacer prototipado
Google Colab
Uso gratuito de GPU
### _Entornos/Ambientes Virtuales_

Instalando Anaconda Distribution desde terminal:

- Se usa la bandera -O (ojo != 0) para indicar la carpeta y se copia el enlace de la descarga Linux

    ```wget -O anaconda.sh https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh```

- Se revisa el archivo con ls y luego instalar con el comando bash
    ```bash anaconda.sh```
- Se confirma la dirección de descarga:
    ```/home/migu3low/anaconda3```
- Finalizando la instalación para activar tomo la opción [NO] en ese caso para activar se ejucta el comando:
    ```eval "$(/home/migu3low/anaconda3/bin/conda shell.YOUR_SHELL_NAME hook)```
    donde _YOUR_SHELL_NAME == .bash_
- Se valida la activación e instalación con el comando:
    ``` conda info```
- Actualizar conda: 
    ``` conda update -all```
- Para crear nuevos ambientes
     ```$ /home/charlesritchea/anaconda3/bin/conda create -n pv python=3.6 anaconda```

### _Crear Actualizar y Eliminar Ambientes_
- Listar los ambientes creados: ``` conda env list```
- Crear ambiente(incluir libreria _pandas_): ``` conda create --name py35 python pandas```
- Activar ambiente: ``` conda activate py35```
- Ver las versiones instaladas ```conda list```
- Para cambiar el nombre ```conda create --name py310 -- copy --clone py35
- Para eliminar primero desactivar: ```conda deactivate``` luego se remueve: ```conda env remove -n [AMBIENTE]```

Canales para instalar paquetes:
- Instalar con un canal ```conda install --channel conda-forge boltons```
- Ver la revision del ambiente: ```conda list --revision```
- Exportar un ambiente: ```conda env export --no-builds // conda env export --from-history --file environment.yml```
- Instalar el archivo: ```conda install create --file <nombre del archivo>```

### Mamba
-Instalar: ```conda install --channel conda-forge mamba```

