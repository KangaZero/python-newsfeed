def format_date(date):
  return date.strftime('%d/%m/%y')

#   returns 16/01/23 for example

def format_url(url):
  return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]

print(format_url('http://google.com/test/'))
print(format_url('https://www.google.com?q=test'))
# returns google.com

def format_plural(amount, word):
  if amount != 1:
    return word + 's'

  return word