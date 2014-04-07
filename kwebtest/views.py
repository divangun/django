from django.http import HttpResponse
from django.template.loader import get_template 
from django.template import Context

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
	
def main(request):
	t = get_template('main_page.html')
	body = '<a href=\'/parse/soup\'> Soup Test </a>'
	body += '<a href=\'/parse/soup\picture\'> [picture] </a><p> '
	body += '<input type=text id=\'comic\'/><input type=button value=\'검색\' onclick=\"location.href=\'/parse/keyword/\' + document.getElementById(\'comic\').value + \'/picture\'\"'
	context = Context({'head_title' : 'Divangun', 'page_title' : 'Divangun\'s main home', 'page_body' : '어-예', 'link_find' : body,})	
	
	
	html = t.render(context)
	return HttpResponse(html, mimetype = 'text/html;charset=utf-8')
	