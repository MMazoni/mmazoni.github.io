## MMazoni Blog

Um blog feito pelo, gerador de sites estáticos, Pelican - escrito em Python. Desenvolvimento e autoria por mim mesmo, com muito carinho e dedicação. Nada muito elaborado e complexo, tudo é mais uma referência de coisas que aprendi e compartilhamento de experiências que passei.

## Setup

Primeiramente é necessário a instalação do Python e do Pip.

	sudo apt install python3-pip python3-dev
	pip3 install virtualenv

É preciso colocar a pasta do virtualenv no $PATH para funcionar.

	git clone -b dev <remote-repository>
	virtualenv venv
	source venv/bin/activate

Com o ambiente virtual criado e funcionando, vamos instalar os pacotes de Python que estão listados no `requirements.txt`.

	pip3 install -r requirements.txt

## O tema do blog

	git clone git@github.com:gilsondev/pelican-clean-blog.git ~/
	pelican-themes -l
	pelican-themes -i ~/pelican-clean-blog

## Acessar o site via servidor local


	pelican content/
	cd output/
	python3 -m http.server

Esses três comandos faz com que ele gere os HTML a partir do Markdown e você consiga acessar o blog pelo [localhost na porta 8000](http://0.0.0.0:8000/)

## Publicando no GitHub Pages

Primeiramente, mando meus arquivos para a branch `dev`. A `main` irá ter os arquivos da pasta __output__, a view do blog. Lembre-se de commitar as alterações antes desse comando.

	git push origin dev 