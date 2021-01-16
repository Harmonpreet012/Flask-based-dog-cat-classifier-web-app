from flask import Flask
import myroutes 

app = Flask(__name__, static_url_path='/static')

##adding routes
app.add_url_rule('/', view_func=myroutes.home)
app.add_url_rule('/predict', view_func = myroutes.predict, methods = ['GET', 'POST'])

#main
if __name__ == '__main__':
    app.run()