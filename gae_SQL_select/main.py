import webapp2
import passwords
import MySQLdb

class MainPage(webapp2.RequestHandler):
    def get(self):
        conn = MySQLdb.connect(unix_socket = passwords.SQL_HOST,
                       user = passwords.SQL_USER,
                       passwd = passwords.SQL_PASSWD,
                       db = "dbtwo")

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM table_one;")
        results = cursor.fetchall()
        cursor.close()
        conn.close()

        self.response.headers["Content-Type"] = "text/html"
        self.response.write(results)

app = webapp2.WSGIApplication([
    ("/", MainPage),
], debug=True)
