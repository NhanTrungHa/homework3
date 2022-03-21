# include Flask class from file flask
from flask import Flask

# create an instance of Flask class
# __name__ is a predefined setup variable
myapp_obj = Flask(__name__)


# different URL the app will implement
@myapp_obj.route("/")
# called view function
def home():
    name = 'Nhan'
    city_names = ['San Jose', 'Los Angeles', 'Tokyo']
    return '''
    <html>
    <head>
        <title>Home Page - my blog</title>
    </head>
    <body>
        <h1>Welcome ''' + name + '''</h1>

        <a href="https://www.google.com">not google</a>

        <ul> 
            <li>''' + city_names[0] + '''</li>
            <li>''' + city_names[1] + '''</li>
             <li>''' + city_names[2] + '''</li>
         </ul>
    </body>
    </html>'''


#myapp_obj.run()
