#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Matheus Mazoni'
SITENAME = 'MMazoni Blog'
SITEURL = 'https://matheusmazoni.com.br'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'
STATIC_PATHS = ['extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }
DEFAULT_LANG = 'pt_BR'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Linkedin', 'https://www.linkedin.com/in/matheus-mazoni/'),
          ('twitter', 'https://twitter.com/mazoni_matheus'),
          ('github', 'https://github.com/MMazoni'),
          ('instagram', 'https://www.instagram.com/mazoni.matheus'),
          ('envelope', 'mailto:mmazoni.andrade@gmail.com'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
THEME = 'clean-blog'
COLOR_SCHEME_CSS = 'github.css'
#HEADER_COLOR = 'black'
