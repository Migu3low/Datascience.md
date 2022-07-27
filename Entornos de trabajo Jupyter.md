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
