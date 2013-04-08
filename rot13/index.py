import webapp2
import cgi

form="""
<form method="post">
  <h2>Enter text here for ROT13 Coversion</h2>
  <br>
  <textarea name="text" cols="45" rows="5">%(textvalue)s</textarea>
	<br>
  <br>
	<input type="submit">
</form>
"""

def escape_html(s):
  return cgi.escape(s, quote = True)

def get_rot13(s):
  text = ''
  for i in s:
    if i.isalpha():
      text = text + getnext(i)
    else:
      text = text + i
  return text

def getnext(i):
  caps = False
  if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    caps = True

  dic = {0:'a', 1:'b', 2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}
  for key in dic:
    if i.lower() == dic[key]:
      key = (key + 13) % 26
      if not caps:
        return dic[key]
      else:
        return dic[key].capitalize()


class MainPage(webapp2.RequestHandler):



  def write_form(self, textvalue=""):
    self.response.out.write(form % ({'textvalue':escape_html(textvalue)}))

  def get(self):
    #self.response.headers['Content-Type'] = 'text/plain'
    self.write_form()

  def post(self):
    user_data = self.request.get('text')
    textvalue = get_rot13(user_data)

    if user_data:
      self.write_form(textvalue)
    
    


app = webapp2.WSGIApplication([('/', MainPage)], debug=True)


