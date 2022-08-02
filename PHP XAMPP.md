# 👁️ Intalación Paquete XAMPP

1. Se agrega el repositorio con el instalador
```
sudo add-apt-reposiyoty ppa:ondrej/php
```
2. Se actualiza el apt adgregado
```
sudo apt-update
```
3. Luego se instala el nuevo apt
```
sudo apt upgrade
```
4. Se instala el paaquete
```
sudp apt install pho apache2
```
5. Verificar las versiones instaladas:
```
sudo dpkg --get-selections | grep php
```
6. Habilitar o deshabilitar versiones:
```
sudo a2enmod phpX.X
sudo a2dismod phpX.X
```
7. Revisar que esta corriendo la conexion
```
$ cd /var/wwww/html/
$ sudo rm index.html
sudo touch index.php
sudo nano index.php
<?php
phpinfo();
```
Ctrl + O para guardar luego Ctrl + X para salir de nano
8. Problema:
```
System has not been booted with systemd as init system (PID 1). Can't operate.
```
9. Solución
```
sudo a2enmod php8.1
sudo service apache2 -full-restart
service --status-all
```
10. Nueva libreria 
```
sudo apt install libapache2-mod-phpX.X
```
11. Solución de Retax Master para WSL
```
$ sudo /etc/init.d/apache2 start
```

