Title: Comandos Básicos de Git/Github
Date: 2019-06-09 14:12
Category: Dev
Tags: git, github
Slug: git-github
Authors: Matheus Mazoni
Summary: Alguns comandos básicos para começar a trabalhar com git e participar de projetos open-source.

<!-- ## Comandos Básicos de Git/Github -->


O primeiro comando para iniciar o repositório local:

    git init folder-name

O *git init* sem o nome da pasta faz com que seja inicializado na pasta que está.

### Configurar sua conta

    git config --global user.name "Mazoni"
    git config --global user.email "mazoni@gmail.com"

### Adicionar os arquivos para o repositório local

    git add file-name

Para adicionar todos arquivos de uma vez:

    git add .

### Salva as alterações feitas no repositório local

    git commit -m "Mensagem do commit"

Você pode também usar o comando _git commit_ que irá abrir seu editor de texto padrão para escrever a mensagem do commit. Crie uma mensagem relacionado às alterações feitas.
Para colocar o vim como o editor padrão ao fazer "git commit":

    git config --global core.editor vim

### A situação do repositório

    git status

### Ver os últimos commits do repositório

    git log

### Criar um repositório remoto

    git remote add <remote> <url>
    git remote add origin git@github.com:username/repository-name (SSH)
    git remote add origin https://github.com/username/repository-name.git (HTTPS)

Quando clonado com `ssh` não é necessário logar na conta do GitHub, mas clonando como `https` é preciso.

### Adicionando SSH Key

Para gerar uma nova chave `ssh` é preciso digitar o comando abaixo com seu email do github.

    ssh-keygen -t rsa -b 4096 -C "mazoni@gmail.com"

Pressione `enter` 3x, ele irá criar uma pasta `.ssh/id_rsa` na pasta do seu usuário, e não será preciso utilizar senha para clonar repositórios utilizando o `ssh`(caso você queira colocar senha, adicione uma senha quando o `prompt` perguntar). Para iniciar o ssh-agent em plano de fundo:

    eval "$(ssh-agent -s)"
    > Agent pid 79294
    ssh-add ~/.ssh/id_rsa

Vamos agora adicionar a chave `ssh` a sua conta. Entre no site do GitHub, vá em configurações, clique no `SSH and GPG keys` depois em `New SSH key`.

    cat ~/.ssh/id_rsa.pub

Agora coloque o nome dessa chave SSH, então copie o código que está no arquivo `id_rsa.pub`(retorno do comando acima) e cole no site onde está escrito `key`.

### Enviar as alterações(commits) de uma branch para o repositório remoto

Primeira vez:

    git push -u origin master

Se o envio for rejeitado o repositório local não foi sincronizado:

    git push <remote> <branch>
    git push

Configurar o push padrão:

    git config --global push.default simple

### Criar uma branch(ramificação)

    git branch <branch-name>

Para criar e já mudar para a nova branch:

    git checkout -b <branch_name>

Caso essa branch ja exista, apenas para alterar de branch:

    git checkout <branch_name>

### Navegar no histórico

    git checkout <commit-number>

É necessário o número do commit, não precisa ser todos os números apenas os primeiros números para diferencias dos outros. Ex: commit _cfac2a8b98cef302b697320760ace3b6d88ba1ef_, quando for usar o comando:

    git checkout cfac2

Se apenas esse commit começar com _cfac2_, você irá acessar esse commit. Usando o comando _ls_, os arquivos desse commit aparecerão.

### Mostrar as diferenças entre repositório local e o remoto

    git diff

Quando for alterado algum arquivo e os repositórios local e remoto não estão iguais, aparece exatamente os arquivos e as linhas com as diferenças que precisa adicionar e commitar.

### Desfazendo commit

Deleta um commit feito:

    git revert <commit-number>

Resetar um repositório para um determinado commit:

    git reset <commit-number>
    git reset HEAD~n
    git reset --hard

* `n`: é a quantidade de commits para resetar.
* `--hard`: volta ao estado do commit anterior sem deixar as alterações feitas posteriormente.

<!-- ###### Merge vs Rebase



    git merge <branch>

    git rebase

    git fetch

Pŕoximos assuntos para completar-->


