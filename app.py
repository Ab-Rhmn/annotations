from flask import Flask, request, jsonify, json, render_template
from flask_cors import CORS
# from pymongo import MongoClient
import pymongo
from pymongo import MongoClient
client = pymongo.MongoClient("mongodb+srv://abrhmn97:vcri7QMKnW6xaE6z@cluster0.bypte0s.mongodb.net/?retryWrites=true&w=majority")
db = client.NLP
collection = db['TwitterData']
app = Flask(__name__)


# client = MongoClient('mongodb://localhost:xxx/')


def dummy_db():

    return json.dumps([f'Sample Text {x}' for x in range(10)])

@app.route('/')
def index():
    data=collection.find({},{"_id":0}).limit(15)
    # data = json.loads(dummy_db())
    return render_template('index.html', sentences=data)

@app.route('/annotate', methods=['POST'])
def annotate():
    # annotations = {}
    # for sentence in json.loads(dummy_db()):
    #     annotation = request.form[f"{sentence}_annotation"]
    #     print(annotation)
    return jsonify({'status': 200, 'annotation': "annotations"})

if __name__ == '__main__':
    app.run(debug=True)
