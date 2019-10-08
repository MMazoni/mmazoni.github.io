#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Matheus Mazoni'
SITENAME = 'MMazoni Blog'
SITEURL = 'https://mmazoni.github.io'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Linkedin', 'https://www.linkedin.com/in/matheus-mazoni/'),
	  ('twitter', 'https://twitter.com/mazoni_matheus'),
          ('github', 'https://github.com/MMazoni'),
          ('instagram','https://www.instagram.com/mazoni.matheus'),
          ('envelope','mailto:mmazoni.andrade@gmail.com'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
MARKUP = ('md', 'ipynb')
THEME = "pelican-clean-blog"
IGNORE_FILES = [".ipynb_checkpoints"]
GOOGLE_ANALYTICS ='UA-140012978-1' 
