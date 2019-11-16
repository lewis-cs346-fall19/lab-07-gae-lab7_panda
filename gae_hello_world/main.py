import webapp2
import passwords
import MySQLdb

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/html"
        self.response.write(("Hello world from GAE")

app = webapp2.WSGIApplication([
    ("/", MainPage),
], debug=True)
