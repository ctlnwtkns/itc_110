import web

urls = (
	'/', 'index'
	)
	
app = web.application(urls, globals())

class index:
	def GET(self):
		greeting = 'Hello World'
		return greeting
		
if '_name_' == "_main_":
	app.run()