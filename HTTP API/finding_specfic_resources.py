import flask
from flask import request,jsonify


app=flask.Flask(__name__)
app.config["DEBUG"]=True

#create something

books =[
    {'id':0,
     'name':'messi',
     'club':'barca'
    },
   {'id':1,
     'name':'ronaldo',
     'club':'juventus'
    },
   {'id':2,
     'name':'debruyne',
     'club':'mci'
    }
]
@app.route('/',methods=['GET'])

def home():
    return "<h1>Distant Reading Archive</h1><p>A prototype API for distant reading of science fiction novels.</p>"

@app.route('/api/v1/resources/books/all',methods=['GET'])

def api_all():
    return jsonify(books)

@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():

    if 'id' in request.args:#checks url for ?id = smthng
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    results = []

    for book in books: # checks id in books
        if book['id'] == id:
            results.append(book)

    return jsonify(results)

app.run()
