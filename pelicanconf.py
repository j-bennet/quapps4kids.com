#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Connie Lee'
SITENAME = u'Quapps 4 Kids'
SITEURL = 'http://www.quapps4kids.com'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('twitter', 'http://twitter.com/quapps4kids'),
#          ('facebook-official', 'http://www.facebook.com/Quapps'),)

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

DIRECT_TEMPLATES = {}

STATIC_PATHS = {'images', 'css', 'extra/CNAME'}
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

THEME = '../pelican-themes/chameleon'
BS3_URL = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css'
BS3_JS = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js'
BS3_THEME = 'http://bootswatch.com/united/bootstrap.min.css'
CSS_OVERWRITE = '/css/quapps.css'

MENUITEMS = [
    ('Home', '/'),
    ('How to', '/howto.html'),
    ('Apps', '/apps.html'),
    ('Contact us', [('Twitter', 'http://twitter.com/quapps4kids'),
                    ('Facebook', 'http://www.facebook.com/Quapps'),
                    ('Gmail', ('https://mail.google.com/mail/?view=cm&fs=1&'
                               'to=admin%40quapps4kids.com&su=Question&'
                               'body=Dear%20Quapps4Kids,')),
                    ('Yahoo mail',
                     ('http://compose.mail.yahoo.com/?'
                      'to=admin%40quapps4kids.com&subj=Question&'
                      'body=Dear%20Quapps4Kids,')),
                    ('Hotmail, Outlook, Live',
                     ('https://mail.live.com/default.aspx?rru=compose&'
                      'to=admin%40quapps4kids.com&subject=Question&'
                      'body=Dear%20Quapps4Kids,')),
                    ('Email', 'mailto:admin@quapps4kids.com')]),
]
