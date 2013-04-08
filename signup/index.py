import webapp2
import cgi
import re


USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

form="""
<form method="post">
  <label>Username
    <input type="text" name="username" value="%(username)s">
  </label><label><span style="color : red">%(username_error)s</span></label>
  <br>

  <label>Password
    <input type="text" name="password" value="">
  </label><label><span style="color : red">%(password_error)s</span></label>
  <br>

  <label>Verify Password
    <input type="text" name="verify" value="">
  </label><label><span style="color : red">%(verify_password_error)s</span></label>
  <br>

  <label>Email(optional)
    <input type="text" name="email" value="%(email)s">
  </label>
  <br>

  <br>
	<input type="submit">
</form>
"""

def escape_html(s):
  return cgi.escape(s, quote = True)

def valid_username(username):
  
  return USER_RE.match(username)
  """
  if username:
    return username
  else:
    return ""
  """

def valid_password(password):
  
  return PASSWORD_RE.match(password)
  """
  if password:
    return password
  else:
    return ""
  """

def valid_verify_password(password):
  return PASSWORD_RE.match(password)
  """
  if password:
    return password
  else:
    return ""
  """

def valid_email(s):
  #EMAIL_RE="^[\S]+@[\S]+\.[\S]+$"
  return True

class WelcomeHandler(webapp2.RequestHandler):
  def get(self):
    name = self.request.get('username')
    if not name:
      self.redirect('/')
    else:
      self.response.out.write("Welcome, %s!"%name)

class SignUpPage(webapp2.RequestHandler):

  def write_form(self, username_error="", username="", password_error="", verify_password_error="", email=""):
    self.response.out.write(form % ({'username_error':username_error, 'username': username, 'email':email, \
                                      'password_error':password_error, \
                                      'verify_password_error':verify_password_error}))

  def get(self):
    #self.response.headers['Content-Type'] = 'text/plain'
    self.write_form()

  def post(self):
    user_username = escape_html(self.request.get('username'))
    user_password = escape_html(self.request.get('password'))
    user_verify_password = escape_html(self.request.get('verify'))
    user_email = escape_html(self.request.get('email'))

    username = valid_username(user_username)
    password = valid_password(user_password)
    verify_password = valid_verify_password(user_verify_password)
    email = valid_email(user_email)

    if not username:
      self.write_form("Thats not a valid username!")
    elif not password:
      self.write_form("", user_username , "Thats not a valid password!")
    elif user_password != user_verify_password:
      self.write_form("", user_username, "", "Passwords do not match")
    else:
      self.redirect('/welcome?username=' + user_username)


app = webapp2.WSGIApplication([('/', SignUpPage),
                               ('/welcome', WelcomeHandler)], debug=True)
