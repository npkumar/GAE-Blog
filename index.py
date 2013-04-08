import webapp2
import cgi

form="""
<form method="post">
  What is your birthday?
  <br>
  <label> Month
    <input type="text" name="month" value="%(month)s">
  </label>

  <label> Day
    <input type="text" name="day" value="%(day)s">
  </label>

  <label> Year
    <input type="text" name="year" value="%(year)s">
  </label>  
  
  <div style="color : red">%(error)s</div>
	<br>
  <br>
	<input type="submit">
</form>
"""

def escape_html(s):
  return cgi.escape(s, quote = True)

class ThanksHandler(webapp2.RequestHandler):
  def get(self):
    self.response.out.write("Thank you! Valid date!")

class MainPage(webapp2.RequestHandler):


  def valid_month(self, month):
    months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
    month_abbvs = dict((m[:3].lower(), m) for m in months)

    if month:
      short_month = month[:3].lower()
      return month_abbvs.get(short_month)

  def valid_day(self, day):
    if day and day.isdigit():
        day = int(day)
        if day > 0 and day < 32:
            return day
    return None

  def valid_year(self, year):
    if year and year.isdigit():
        year = int(year)
        if year >1899 and year < 2021:
            return year
    return None

  def write_form(self, error="", month="", day="", year=""):
    self.response.out.write(form % ({'error':error, 'month':escape_html(month),\
                                     'year':escape_html(year), 'day':escape_html(day)}))
  """  
  def escape_html(self, s):
    return cgi.escape(s, quote = True)
    
    #&amp; should be first
    for (i,o) in (('>', '&gt;'),('<','&lt;'),('&','&amp;'),('"', '&quot;')):
      s = s.replace(i,o)
    return s
    
    temp = ''
    for i in s:
        if i == '&':
            temp = temp + '&amp;'
        elif i == '<':
            temp = temp + '&lt;'
        elif i == '"':
            temp = temp + '&quot;'
        elif i == '>':
            temp = temp + '&gt;'
        else:
            temp = temp + i
    return temp
    
  """
  def get(self):
    #self.response.headers['Content-Type'] = 'text/plain'
    self.write_form()

  def post(self):
    user_month = self.request.get('month')
    user_day = self.request.get('day')
    user_year = self.request.get('year')

    month = self.valid_month(user_month)
    day = self.valid_day(user_day)
    year = self.valid_year(user_year)

    if not (month and day and year):
      self.write_form("Invalid, friend", user_month, user_day, user_year)
    else:
      self.redirect('/thanks')


app = webapp2.WSGIApplication([('/', MainPage),
                               ('/thanks', ThanksHandler)], debug=True)
