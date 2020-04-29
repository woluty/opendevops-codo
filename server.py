import tornado.web
import tornado.ioloop
import tornado.httpserver
import config

class Indexhandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        self.write("good is luck")


if __name__=="__main__":
    app = tornado.web.Application([
        (r'/',Indexhandler)
    ])

    httpserver=tornado.httpserver.HTTPServer(app)
    httpserver.bind(config.options["port"])
    httpserver.start(1)
    tornado.ioloop.IOLoop.current().start()