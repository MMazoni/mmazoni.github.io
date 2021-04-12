Title: Como criei esse blog com Pelican
Date: 2019-06-09 12:20
Tags: python, vim, pelican
Slug: pelican-blog
Authors: Matheus Mazoni
Summary: Fazendo o setup do Pelican para gerar páginas estáticas de um blog

<!-- ## Como criei esse blog com Pelican -->

Eu precisava de uma plataforma fácil e simples para fazer um blog, enquanto não consigo desenvolver um blog do zero, para detalhar as minhas experiências como estudante de tecnologia. Encontrei o __Pelican__ que é um gerador de sites estáticos, com isso não preciso escrever _HTML_ /_CSS_, apenas fazer algumas alterações.

Vamos começar com o setup do Pelican. A máquina utilizada foi container com Debian 9 e com o Fish como `shell`. Vamos começar com o setup do Pelican.

### Setup inicial

É preciso ter instalado `python3`(pode ser o `python2` mas nesse guia utilizei o 3 e alguns comandos são diferentes), `pip` e o `virtualenv`.

```sh
pip3 install virtualenv --user
echo "set -x PATH /home/mmazoniandrade/.local/bin/ $PATH" >> ~/.config/fish/config.fish
```

Instalamos o `virtualenv` e colocamos na variável PATH do sistema(lembrando que em outros shell como bash e zsh será diferente o comando) para criar um ambiente virtual para instalar o pelican. Agora iremos criar a pasta do projeto e o ambiente virtual.

```sh
mkdir pelican-blog
cd pelican-blog/
virtualenv venv
```

Para ativar o virtualenv em Fish

```sh
.  venv/bin/activate.fish
```

Para ativar o virtualenv em Bash ou Zsh

```sh
source venv/bin/activate
```

Depois para desativar

```sh
deactivate
```

Crie um arquivo de texto com o nome `requirements.txt`, escreva nele as bibliotecas Python que serão instaladas:

    Markdown==2.6.6
    pelican==3.6.3
    jupyter>=1.0
    ipython>=4.0
    nbconvert>=4.0
    beautifulsoup4
    ghp-import==0.4.1
    matplotlib==1.5.1

Em seguida, digite o comando:

```sh
pip3 install -r requirements.txt
```

### Execute o Pelican

Estamos pronto para rodar o pelican:

```sh
pelican-quickstart
```

O pelican irá perguntar algumas informações para configuções, apenas coloque o título do site, o autor do site e o fuso-horário. Aperte `enter` para as outras perguntas.


### Adicionar conteúdo

É necessário colocar os arquivos em formato markdown (.md) na pasta `content`.

Outra coisa bem importante é a criação do `meta`, que são as informações do post.

    Title: Primeiro Post
    Slug: primeiro-post
    Date: 2019-06-09 13:50
    Category: posts
    Tags: pelican, posts, python
    author: Matheus Mazoni
    Summary: Meu primeiro post, leia para descobrir o que te espera.

Para adicionar no arquivo `markdown` é bastante simples, somente escreva o __meta__ nas primeiras linhas. Deixe 2 linhas vazias após o `meta`.

### Gerando as páginas

Mude para a pasta `pelican-blog` e execute o comando abaixo, então entre na pasta `output` para rodar o servidor na sua máquina e conseguir ver como ficou o blog.

```sh
cd pelican-blog
pelican content
cd output
python3 -m http.server
```

Acesse o site por esse link: [http://0.0.0.0:8000/](http://0.0.0.0:8000/){:target="_blank"}

Agora é possível fazer mais coisas, como colocar temas, adicionar o seu blog no `github pages`(como fiz), adicionar comentários entre outros. Espero que esse post tenha mostrado como o python facilita a criação de um blog com o `pelican`.