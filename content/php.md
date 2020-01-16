Title: Ambiente de desenvolvimento em PHP
Date: 2019-12-02 21:12
Tags: php, coding, environment 
Slug: php-environment 
Authors: Matheus Mazoni 
Summary: Ambiente de desenvolvimento em PHP no trabalho

## Ambiente Desenvolvimento PHP

Antes eu comecei utilizando Windows com o Xampp(Apache, MySQL e PHP), no entanto sou muito fã do Linux, pedi para meu gerente se eu poderia instalar uma distribuição de meu interesse. Ele também gosta de Linux, então ele autorizou sem problemas. Depois da migração, eu vi que não precisava mais do Xampp(uso bem pouco hoje em dia), ainda mais que o PHP e o Laravel conseguem subir um servidor para testar o código.

Agora vou mostrar o ambiente de desenvolvimento que preparei no Ubuntu 19.10 no trabalho.

### 1 - Oracle Client (oci8)

Faça o download de acordo com sua máquina do [Oracle Instant Client](https://www.oracle.com/database/technologies/instant-client/linux-x86-64-downloads.html) dos arquivos que tiver `basic` e `sdk`.

+ Arquivos de exemplo do linux x64: _instantclient-basic-linux.x64-19.3.0.0.0dbru.zip_ e _instantclient-sdk-linux.x64-19.3.0.0.0dbru.zip_

Na pasta _Downloads_:

``` sh
mkdir oracle
mv instantclient-basic-linux.x64-19.3.0.0.0dbru.zip oracle/
mv instantclient-sdk-linux.x64-19.3.0.0.0dbru.zip oracle/
cd oracle
unzip instantclient-basic-linux.x64-19.3.0.0.0dbru.zip
unzip instantclient-sdk-linux.x64-19.3.0.0.0dbru.zip
cd ..
sudo mv oracle /opt/
```

Adicione a pasta ao __ldconfig__ e use o comando.

	export LD_LIBRARY_PATH=/opt/oracle/instantclient_19_3
	sudo sh -c "echo /opt/oracle/instantclient_19_3 > /etc/ld.so.conf.d/oracle-instantclient.conf"
	sudo ldconfig

Utilizamos o banco Oracle e precisamos da extensão `oci8` no PHP, iremos ativar na compilação dele.

### 2 - PHP (7.3.12)

Há duas formas mais comuns de instalar o PHP no Linux, usar os comandos no terminal e usar a versão do repositório ou compilar o código fonte. Eu prefiro compilar pois eu consigo ter controle de todas as extensões que estou instalando.

Instale as dependências

```
sudo apt install autoconf automake bison build-essential curl flex \
    libtool libssl-dev libcurl4-openssl-dev libxml2-dev libonig-dev \
    libreadline-dev libsqlite3-dev libzip-dev nginx openssl \
    pkg-config re2c sqlite3 zlib1g-dev 
```

[Baixe o PHP](https://www.php.net/downloads.php). Lembrando que utilizei a versão 7.3. Descompacte e entre no diretório pelo terminal.

Crie um diretório para separar de outras versões do PHP e compile

```
mkdir  ~/php7.3/

./configure --prefix=$HOME/php7.3 \
    --enable-mysqlnd \
    --with-pdo-mysql \
    --with-pdo-mysql=mysqlnd \
    --with-mysqli=mysqlnd \
    --enable-bcmath \
    --enable-fpm \
    --with-fpm-user=www-data \
    --with-fpm-group=www-data \
    --enable-mbstring \
    --enable-phpdbg \
    --enable-shmop \
    --enable-sockets \
    --enable-sysvmsg \
    --enable-sysvsem \
    --enable-sysvshm \
    --enable-zip \
    --with-libzip=/usr/lib/x86_64-linux-gnu \
    --with-zlib \
    --with-curl \
    --with-pear \
    --with-openssl \
    --enable-pcntl \
    --with-readline \
    --with-pdo-sqlite \
    --with-oci8=instantclient,/opt/oracle/instantclient_19_3

make
sudo make install
```

4. Agora, algumas modificações para tudo dar certo.

```
cp php.ini-development ~/php7.3/lib/php.ini
cd ~/php7.3/etc/
mv php-fpm.conf.default php-fpm.conf
mv php-fpm.d/www.conf.default php-fpm.d/www.conf
```
Adicione a caminho ~/php7.3/bin [para a variável $PATH](https://gist.github.com/nex3/c395b2f8fd4b02068be37c961301caa7)

Para testar se o PHP está funcionando.

	php --version

O output:

	PHP 7.3.12 (cli) (built: Dec 02 2019 20:55:45) ( NTS )
	Copyright (c) 1997-2019 The PHP Group
	Zend Engine v3.3.11, Copyright (c) 1998-2019 Zend Technologies

## 3 - Composer - Gerenciador de pacotes do PHP

A partir daqui iremos instalar os requisitos para  o __Laravel__, o composer é um deles.

Apenas rode os comandos abaixo para instalar o composer, tirado diretamento do [site oficial](https://getcomposer.org).

	php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
	php -r "if (hash_file('sha384', 'composer-setup.php') === 'a5c698ffe4b8e849a443b120cd5ba38043260d5c4023dbf93e1558871f1f07f58274fc6f4c93bcfd858c6bd0775cd8d1') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
	php composer-setup.php
	php -r "unlink('composer-setup.php');"

Agora precisamos mover o arquivo `composer.phar` para a pasta de binários do sistema(irei renomear para apenas 'composer').

	sudo mv composer.phar /usr/bin/composer

Digite 'composer --version' e o output será parecido com esse:

	Composer version 1.9.0 2019-08-02 20:55:32

## 4 - Node-js e NPM

Instalei o `node` e o `npm` pelo pelo próprio repositório do Ubuntu, mas você também pode instalar uma versão mais recente pelo [site oficial](https://nodejs.org/en/).

	sudo apt install nodejs nodejs-dev node-gyp libssl1.0-dev npm

Para confirmar:

	nodejs -v
	npm -v

Se apareceu o número da versão, está tudo certo.

## 5 - Laravel

Utilize o comando abaixo para o composer instalar o Laravel e depois adicionar no $PATH

	composer global require laravel/installer
	echo 'export PATH="PATH:/$HOME/.config/composer/vendor/bin/"' | sudo tee -a ~/.bashrc

## 6 - Oracle SQL Developer

Um dos pré-requisitos é a instalação do Java 8 para cima, recomendo que instale o [Java da Oracle](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html), pois o OpenJDK não é o suficiente, sendo necessário a instalação de mais bibliotecas por fora para o SQL Developer funcionar corretamente.

Para instalá-lo, apenas baixe o jdk-8 no formato ´tar.gz´ e extraia para a pasta /opt/jdk.
	
	sudo mkdir  -p /opt/jdk
	sudo cp -rf /$HOME/Downloads/jdk-8u231-linux-x64.tar.gz /opt/jdk/
	cd /opt/jdk/
	sudo tar -zxf jdk-8u231-linux-x64.tar.gz

Com o java instalado, agora vamos baixar o [SQL Developer](https://www.oracle.com/tools/downloads/sqldev-v192-downloads.html). Utilizei o "Other Platforms". 

Extraia o zip baixado e siga os passos abaixo para a instalação:

	sudo unzip /$HOME/Downloads/sqldeveloper-*-no-jre.zip -d /opt/
	sudo chmod +x /opt/sqldeveloper/sqldeveloper.sh
	sudo ln -s /opt/sqldeveloper/sqldeveloper.sh /usr/local/bin/sqldeveloper

Edite o script /opt/sqldeveloper/sqldeveloper.sh por:
	
	#!/bin/bash
	unset -v GNOME_DESKTOP_SESSION_ID
	cd /opt/sqldeveloper/sqldeveloper/bin
	./sqldeveloper "$@"

Quando você executar o SQL Developer, vai ser necessário colocar o caminho da pasta do Java, irei colocar o meu como exemplo:

	sqldeveloper
	
	/opt/jdk/jdk1.8.0_231/
	

Com isso finaliza a instalação do meu ambiente de desenvolvimento com PHP no trabalho. Há alguns programas adicionais utilizados por mim, acho bom apenas citar, que são:

+ `Visual Studio Code` - meu editor de código favorito no momento
+ `Postman` - para testar as APIs feitas com Lumen
+ `Filezilla` - um cliente open-source para gerenciar transferência FTP