#!/usr/bin/python

import os
import tornado
from urls import urls

application = tornado.web.Application(
              handlers=urls,
              settings=dict(template_path='./templates'),
              static_path= os.path.join(os.path.dirname(__file__), "static"),
              debug=True
              )
