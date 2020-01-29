import sys
sys.path.append('./model/')

import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options
from application import application

define("port", default=8008, type=int)

def main():
    http_server = tornado.httpserver.HTTPServer(application)# A http application
    http_server.bind(options.port, '0.0.0.0') # bind to ip:port
    http_server.start(num_processes=1) # multi process
    print("Start server at:http://0.0.0.0:%s"%(options.port))
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
