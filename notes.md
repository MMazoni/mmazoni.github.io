## Initial project

mkdir mazoni-blog
cd mazoni-blog/

https://github.com/github/gitignore/blob/master/Python.gitignore

vim .gitignore

virtualenv venv

source venv/bin/activate

vim requirements.txt

Markdown==2.6.6
pelican==3.6.3
jupyter>=1.0
ipython>=4.0
nbconvert>=4.0
beautifulsoup4
ghp-import==0.4.1
matplotlib==1.5.1

pip install -r requirements.txt

## Pelican

pelican-quickstart

git init
git submodule add git://github.com/danielfrg/pelican-ipynb.git plugins/ipynb

cd content/
mkdir CromeOS
mkdir Dev
mkdir Linux
mkdir Math

pelican content

cd output

python -m http.server

## Pelican Themes

git clone git@github.com:gilsondev/pelican-clean-blog.git

pelican-themes -l

pelican-themes -i ~/pelican-clean-blog

## Publish

pelican content -s publishconf.py

git checkout -b dev

ghp-import output -b master

git push origin master

## MISC

git remote add origin git@github.com:MMazoni/MMazoni.github.io.git

'sha1:8f394f2e3e1d:5d2194a0e11b9b7d25fff01988667ec7ee98e296'

ssh -i "mazoni.pem" ubuntu@ec2-3-16-112-133.us-east-2.compute.amazonaws.com

ssh -i "mazonis.pem" -L 8110:localhost:8000 ubuntu@ec2-18-217-236-3.us-east-2.compute.amazonaws.com
