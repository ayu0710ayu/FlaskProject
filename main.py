from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Helloworld(Resource):
    def get(self):
        return {"data": "Helloworld"}
    def post(self):
        return {"data": "HelloCoder"}
api.add_resource(Helloworld,"/helloworld")

if __name__ == "__main__":
    app.run(debug=True)
