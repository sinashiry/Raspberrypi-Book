from bottle import route, run, template
from datetime import datetime

@route('/')

def index(name='time'):
	dt = datetime.now()
	time = "{:%Y-%m-%d %H:%M:%S}".format(dt)
	return template('<b>Pi date/time is: {{t}}</b>', t=time)
	
run(host='192.168.137.239', port=80)