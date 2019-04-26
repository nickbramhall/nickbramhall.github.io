#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Nick Bramhall'
SITENAME = "The Mountain's Silhouette"
SITESUBTITLE = 'Hiking and backpacking in the mountains of Scotland'
SITEURL = ''

HEADER_COVER = '/images/page-header-image.png'

PATH = 'content'

TIMEZONE = 'Europe/London'
DEFAULT_DATE_FORMAT = '%d %B %Y'

DEFAULT_LANG = 'en'

THEME = '/home/nick/apps/tms/themes/octopress'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('57 Degrees North', 'http://gavinmacfie.blogspot.co.uk'),
         ('Benvironment', 'http://benvironment.org.uk/'),
         ('Cairn in the Mist', 'http://cairn-in-the-mist.blogspot.com/'),
         ('Cairngorm Wanderer', 'http://cairngormwanderer.wordpress.com'),
         ('Chris Townsend Outdoors', 'http://www.christownsendoutdoors.com/'),
         ('eBothy Blog', 'http://www.stravaiger.com'),
         ('Footprints Across Scotland', 'http://paulsblog.sammonds.com/'),
         ('Grid North', 'http://gridnorth.blogspot.co.uk/'),
         ('Incompleat', 'http://www.incompleat.com/'),
         ('Luach Mhor', 'http://luachmhor.wordpress.com/'),
         ('McAlisterium', 'http://mcalisterium.wordpress.com/'),
         ('ness64', 'http://ness64.wordpress.com/'),
         ('PTC*', 'http://www.petesy.co.uk'),
         ('Scottish Mountaineer', 'http://scottishmountaineer.com/'),
         ('Self Powered', 'http://www.davidlintern.com/blog/'),
         ('Tramplite', 'http://tramplite.com/'),
         ('Walk With Tookie', 'http://walkwithtookie.com'),
         ('Walkers Anon', 'http://walkers-anon.blogspot.co.uk/'),
         ('Writes of Way', 'http://writesofway.com/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# My Settings
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_FEEDS_ON_MENU = True
SUMMARY_MAX_LENGTH = 50
SEARCH_BOX = True
INDEX_SAVE_AS = 'blog/index.html'
MENUITEMS = (('About', '/'), ('Blog', '/blog/'), ('Trips', '/reports/'),)
MENUITEMS_MIDDLE = (('Archives', '/archives.html'),)

FEED_FEEDBURNER = 'co/syeE'


ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

SLUGIFY_SOURCE = 'basename'

AUTHORS_SAVE_AS = ''

# Plugins

PLUGIN_PATHS = ['plugins/pelican-plugins']
PLUGINS = ['summary', 'pelican-page-hierarchy']

SUMMARY_END_MARKER = '<!--more-->'

# Static Paths

STATIC_PATHS = [
    'images', 'extra',  # this
]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.png': {'path': 'favicon.png'},  # and this
    'extra/CNAME': {'path': 'CNAME'},
    #'extra/LICENSE': {'path': 'LICENSE'},
    'extra/README': {'path': 'README'},
}
