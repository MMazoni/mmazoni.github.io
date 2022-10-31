Title: Utilizando Ansible para automatizar ambiente local
Date: 2022-04-21 11:34
Tags: ansible, programação, environment, crostini
Slug: ansible-local-dev-1
Authors: Matheus Mazoni
Summary: Automatizar a configuração do meu ambiente de Desenvolvimento do Chromebook com Ansible


Se você leu os primeiros posts do meu blog, deve saber que tenho um chromebook. Hoje em dia, a forma mais fácil e nativa de desenvolvimento é utilizando o Crostini. É um LXC (Linux Containers), que vem na distro Debian por padrão, mas dá para mudar para Ubuntu, Arch Linux entre outras. Eu tenho um problema muito grande chamado: *espaço em disco*. Como meu chromebook tem apenas 16Gb de disco, o Crostini consegue alocar no máximo 7Gb, sendo que o sistema do Linux por si só já deve comer uns 2Gb.

Geralmente faço reboot desse container para diferentes setups de desenvolvimento (Node+Docker, Terraform+Kubernetes, PHP+Python+MySQL). E fazer a instalação dos pacotes tudo na mão toda hora que eu troco entre esses setup é um saco. É aí que entra o Ansible. Conheci recentemente por uma indicação de um colega do trabalho. Pesquisei e vi uns vídeos da Alura sobre o assunto e já consegui brincar um pouquinho para automatizar o provisionamento de meu ambiente padrão de desenvolvimento no Crostini.

A ideia era fazer a migração de um script bash para o Ansible. Segue abaixo o meu script:

```sh
#!/bin/bash

echo "Mazoni Environment Script!"

sudo apt update
sudo apt upgrade -y
sudo apt install git curl fish wget -y

# fish
echo "Configuring fish..."
mkdir ~/.config/fish
curl -o ~/.config/fish/config.fish https://raw.githubusercontent.com/MMazoni/configuration-files/master/.config/fish/config.fish
sudo chsh -s $(which fish) $USER

# vim
echo "Configuring vim..."
curl -o ~/.vimrc https://raw.githubusercontent.com/MMazoni/configuration-files/master/.vimrc
curl -o ~/.vim/colors/atlantic-dark.vim https://raw.githubusercurrent.com/MMazoni/configuration-files/master/.vim/colors/atlantic-dark.vim --create-dirs

# github
echo "Configuring git..."
git config --global user.name "Matheus Mazoni"
git config --global user.email "mmazoni.andrade@gmail.com"
git config --global core.editor vim
ssh-keygen -t rsa -b 4096 -C "mmazoni.andrade@gmail.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
sshcode=`cat ~/.ssh/id_rsa.pub`
echo $sshcode
read -p "Press enter to continue"

# docker
echo "Installing docker..."
sudo apt remove docker docker-engine docker.io containerd runc -y
sudo apt install apt-transport-https ca-certificates curl gnupg lsb-release -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io -y
sudo groupadd docker
sudo usermod -aG docker $USER

# docker-compose
echo "Installing docker-compose..."
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# node
echo "Installing node and yarn..."
nodeversion="v14.17.3"
curl -o "$HOME/.node/node-$nodeversion-linux-x64.tar.xz" "https://nodejs.org/dist/$nodeversion/node-$nodeversion-linux-x64.tar.xz" --create-dirs
tar -xvf "$HOME/.node/node-$nodeversion-linux-x64.tar.xz" -C ~/.node/
rm "$HOME/.node/node-$nodeversion-linux-x64.tar.xz"
echo "set -x PATH \$HOME/.node/node-$nodeversion-linux-x64/bin/ \$PATH" >> ~/.config/fish/config.fish
source ~/.config/fish/config.fish
npm i -g yarn
```

O script era bem simples:

* Instalava o fish, meu shell favorito.
* Configurava o git
* Configurava o vim
* Gerava o SSH da máquina (não era tão automatizado, pois tinha que colocar no github)
* Instalava o Docker e o Docker Compose
* Instalava o node

[Ansible](https://github.com/ansible/ansible) é uma ferramenta open-source de automação mais utilizada para gerenciar a configuração de servidores.  Porêm, vou usá-lo com meu ambiente de desenvolvimento local. Ela foi desenvolvida pela Red Hat em python, mas não precisa saber python para usar o ansible.

Geralmente não é comum utilizar no ambiente local, pelo fato ser muito poderoso pra fazer somente isso. Só que fiz para aprender mesmo. Achei a curva de aprendizado bem tranquila.

Algumas vantagens que percebi ao usar o Ansible:

- simplicidade, fácil de aprender
- não precisa instalar agent na máquina que será automatizada
- playbooks escritos em YAML
- utilizar secrets para dados sensíveis

Em um próximo post vou mostrar as formas de instalar o ansible e como fiz a automação e estruturei os playbooks.
