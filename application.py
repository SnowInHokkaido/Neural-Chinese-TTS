#!/usr/bin/python

import tornado
from urls import urls

application = tornado.web.Application(
              handlers=urls,
              settings=dict(template_path='./templates', static_path='./static'),
              debug=True
              )
