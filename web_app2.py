"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

# DON'T TOUCH THIS CODE!!! 
from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True	# debugger

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app
# END DON'T TOUCH!!!

# import all our routes from routes.py
from route import * 

# LAUNCHING OUR SERVER    
if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5589'))
    except ValueError:
        PORT = 5589
    app.run(HOST, PORT)
    
## Same debug process as the flask step at beginning     
#if __name__ == '__main__':
    #app.debug = True
    #app.run()