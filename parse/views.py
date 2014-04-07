from django.shortcuts import render
from django.template.loader import get_template 
from django.template import Context
from django.http import HttpResponse
from BeautifulSoup import BeautifulSoup
import urllib2
import urllib

# Create your views here.
def hello(request, message = "HeXA"):
	return HttpResponse("hello, World! Your message is " + message)

	
def me(request, name, group, role):
	t = get_template('index.html')
	context = Context({'first' : name, 'second' : group, 'third' : role,})
	
	html = t.render(context)
	return HttpResponse(html, mimetype = 'text/html;charset=utf-8')
	
	
def htmltest(request):
	t = get_template('main_page.html')
	context = Context({'head_title' : 'aa', 'page_title' : 'bb', 'page_body' : 'cc',})	
	html = t.render(context)
	return HttpResponse(html, mimetype = 'text/html;charset=utf-8')




def soupkeywordView(request, keyword, type = "string"):
	image_url = 'http://www.booksaetong.co.kr'
	url = u'http://booksaetong.co.kr/shop/search.php?sfl=wr_subject%7C%7Cwr_content&sop=and&stx=&search_flag=%BB%F3%C7%B0&search_flag1=it_name&search_str='
	temp = urllib.quote((keyword).encode('euc-kr'), '/:')
	url += temp
	
	http = urllib2.urlopen(url)
	data = http.read()
	
	soup = BeautifulSoup(data, fromEncoding='utf-8')
	html = ""
	filename = ""
	for image in soup.findAll("img"):
		filename = str(image['src'])
		filepath = ""
		if 'http' in filename:
			filepath = filename
			if type == "picture":
				html+="<img src=" + filepath + ">"
			else:
				html+=filepath + "<br>"

	
	return HttpResponse(html, mimetype = 'text/html;charset=utf-8')

	
def soupView(request, type = "string"):
	url = 'http://www.booksaetong.co.kr'
	http = urllib2.urlopen(url)
	data = http.read()
	
	soup = BeautifulSoup(data, fromEncoding='utf-8')
	html = ""
	filename = ""
	for image in soup.findAll("img"):
		filename = str(image['src'])
		filepath = ""
		if not 'http' in filename:
			filepath = url
		filepath += filename;
		
		if type == "picture":
			html+="<img src=" + filepath + ">"
		else:
			html+=filepath + "<br>"

#	t = get_template('main_page.html')
#	context = Context({'head_title' : soup.title.string, 'page_title' : 'bb', 'page_body' : soup.body.string ,})	
#	html = t.render(context)
	return HttpResponse(html, mimetype = 'text/html;charset=utf-8')

def soupgoogleView(request, keyword, type = "string"):

	url = 'http://portal.korea.ac.kr'
	http = urllib2.urlopen(url)
	data = http.read()
	
	soup = BeautifulSoup(data, fromEncoding='utf-8')
	html = ""
	filename = ""
	for image in soup.findAll("img"):
		filename = str(image['src'])
		filepath = ""
		if not 'http' in filename:
			filepath = url
		filepath += filename;
		
		if type == "picture":
			html+="<img src=" + filepath + ">"
		else:
			html+=filepath + "<br>"

	
	return HttpResponse(html, mimetype = 'text/html;charset=utf-8')
	
def download_photo(self, img_url, filename):
    file_path = "%s%s" % (DOWNLOADED_IMAGE_PATH, filename)
    downloaded_image = file(file_path, "wb")

    image_on_web = urllib.urlopen(img_url)
    while True:
        buf = image_on_web.read(65536)
        if len(buf) == 0:
            break
        downloaded_image.write(buf)
    downloaded_image.close()
    image_on_web.close()

    return file_path
