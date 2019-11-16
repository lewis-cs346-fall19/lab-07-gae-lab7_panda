import webapp2
import passwords
import MySQLdb
import cgi

class MainPage(webapp2.RequestHandler):
    def get(self):
        conn = MySQLdb.connect(unix_socket = passwords.SQL_HOST,
                       user = passwords.SQL_USER,
                       passwd = passwords.SQL_PASSWD,
                       db = "dbtwo")
        cursor = conn.cursor()
        cookie_name = self.request.cookies.get("cookie_name")
        
        if cookie_name == None:
            id = "%032x" % random.getrandbits(128)
            self.response.set_cookie("cookie_name", id, max_age=1800)
            cursor.execute("INSERT INTO sessions (sessionid) VALUES (" + id + ");")
            self.response.headers["Content-Type"] = "text/html"
            self.response.write("""<html><body><form onsubmit= method="POST">
                                <input type="text" name="username">
                                    <input type="submit"></form></body></html>""")
        else:
            form = cgi.FieldStorage()
            cursor.execute("SELECT username FROM sessions WHERE sessionid=" + id + ";")
            results = cursor.fetchall()
            username = '';
            if (results = ''):
                username = form.getvalue("username")
                cursor.execute("UPDATE sessions SET username=" + username + " WHERE sessionid=" + id + ";")
            else:
                
            
        
        cursor.close()
        conn.close()

        self.response.headers["Content-Type"] = "text/html"
        self.response.write(results)

app = webapp2.WSGIApplication([
    ("/", MainPage),
], debug=True)
