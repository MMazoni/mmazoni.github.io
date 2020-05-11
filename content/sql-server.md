Title: Instalando o SQL Server no Ubuntu 18.04 via Docker
Date: 2020-05-06 17:55
Tags: sql, docker, ubuntu, server 
Slug: docker-sql-server
Authors: Matheus Mazoni 
Summary: Tutorial para instalar o Docker, SQL Server e utilizar com o DBeaver

A maneira mais fácil que encontrei de usar o SQL Server no Linux, algo necessário para minha aula de banco de dados na faculdade. Vou dividir esse guia em três partes: instalação do Docker, criar a imagem SQL Server(docker)  e configurá-la, usar o DBeaver para gerenciar o banco.

## Parte 1 - Docker

Vamos instalar o docker utilizando o repositório, primeiramente precisamos configurá-lo:

```
$ sudo apt-get update

$ sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

$ sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```

Agora, iremos atualizar o repositório e instalar o docker:

```
$ sudo apt-get update
$ sudo apt-get install docker-ce docker-ce-cli containerd.io

$ sudo docker run hello-world
```
Se instalou e rodou a imagem docker do "Hello World", então está tudo perfeito. 

Para não precisar sempre utilizar o `sudo`, iremos adicionar o docker ao grupo de usuário.

```
$ sudo usermod -aG docker $USER
```
 
Agora é necessário deslogar e logar novamente para ativar as alterações.

Caso queira que o docker inicie no boot:

```
$ sudo systemctl enable docker
```

Para desabilitar:

```
$ sudo systemctl disable docker
```

## Parte 2 - Imagem SQL Server Docker

A partir daqui vou instalar a imagem do SQL Server, não utilizarei o sudo, pois adicionei o docker ao grupo de usuário. Para baixar e executar a imagem, utilize os comandos abaixo:

```
$ docker pull mcr.microsoft.com/mssql/server:2019-CU3-ubuntu-18.04

$ docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=UmaSenhaForte" \
   -p 1433:1433 --name sql1 \
   -d mcr.microsoft.com/mssql/server:2019-CU3-ubuntu-18.04
```
Os parâmetros passados:

+ **-e "ACCEPT_EULA=Y"** - Aqui é para definir a variável que irá aceitar os termos de licença.

+ **-e "SA_PASSWORD=UmaSenhaForte"** - Define a varíavel da senha do SA

+ **-p 1433:1433** - Mapeia a porta 1433 para o host e o container

+ **--name sqli** - O nome do container

+ **-d mcr.microsoft.com/mssql/server:2019-CU3-ubuntu-18.04** - O nome da imagem


Para exibir os containers do docker utilize o comando:

```
$ docker ps -a
```

![comando-docker](https://trello-attachments.s3.amazonaws.com/5a9ad7ae3d56417005320ecd/5eb92a44f4a2f55fbe5aee93/d3b4f8c81aeed408e399af55be521eb1/terminal-docker.png "Terminal com comando 'docker ps -a'")

Como você pode ver na imagem acima, no campo status todo estão como `Exited`, pois os containers estão destivados, quando ficarem Up é porque subiu o container. É necessário o comando:

```
$ docker start sql1
```

### Conectando no SQL Server via linha de comando

1. Execute o container com o bash

```
$ docker exec -it sql1 "bash"
```

2. Agora dê o comando do SQL Server com os parâmetros da senha

```
$ /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P "<UmaSenhaForte>"
```

Se tudo ocorreu bem, você estará no SQL Server, no prompt de comando. Agora já pode usar os comandos SQL para manipular dados, mas vou mostrar como instalar e se conectar com o DBeaver.

## Parte 3 - Conectando no SQL Server via DBeaver

Para instalar, baixe o instalador `.deb` no [site deles](https://dbeaver.io/download/) e clique duplo para instalar.

Abra o DBeaver e clique no ícone de criar uma conexão de banco:

![conexao-dbeaver](https://trello-attachments.s3.amazonaws.com/5a9ad7ae3d56417005320ecd/5eb92a44f4a2f55fbe5aee93/a8cc1a49b8b35887e91858ecb0447f12/database-connection.png "Ícone de criar conexão")

Escolha o SQL Server e clique em `Next`:

![sql-server](https://trello-attachments.s3.amazonaws.com/5a9ad7ae3d56417005320ecd/5eb92a44f4a2f55fbe5aee93/8105d0cb761d9af25644eefedf949a14/sql-server.png "SQL Server")

Apenas coloque SA no nome de usuário e a senha do SA e clique em `Finish`:

![criando-conexao](https://trello-attachments.s3.amazonaws.com/5a9ad7ae3d56417005320ecd/5eb92a44f4a2f55fbe5aee93/b476c7a2b7d9994432ac70bcc10804b0/conectar-sql.png "Criando conexão")

Após isso ele irá pedir para instalar um plugin para utilizar o SQL Server, que é necessário apenas confirmar que ele já baixa e instala. Depois disso é só começar a manipular os dados com o DBeaver utilizando o SQL Server. Lembrando que quando você desligar ou reiniciar o computador, será necessário subir o container do SQL Server novamente.

![conexoes](https://trello-attachments.s3.amazonaws.com/5a9ad7ae3d56417005320ecd/5eb92a44f4a2f55fbe5aee93/09f0ac6c7440c078b31a86cb1745c6c7/conexoes.png "DBeaver")


