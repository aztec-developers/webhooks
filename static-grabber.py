#!/bin/python
from flask import Flask,request
from flask_restful import Resource, Api,reqparse
from collections import defaultdict
import subprocess

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task')

class GithubHooker(Resource):
	def get(self,req):
		print("get")
		print(req)
		return {"hello":"world"}

	def post(self,req):
		args = parser.parse_args()
		print(args)
		return "this was a post"

#subprocess.call(["git","pull"])
#
#

api.add_resource(GithubHooker, '/webhooks/<req>')

if __name__ == '__main__':
    app.run(debug=True)

