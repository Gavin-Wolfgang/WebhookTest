from flask import Flask, make_response, request, current_app, Request, jsonify

app = Flask(__name__)
app.debug = True

# will be handling payloads
@app.route("/payload", methods=['POST'])
def handlePost():
	print(request)
	print(request.json)
	return "success"

def main():
	app.run(port=4567, debug=True)

if __name__ == '__main__':
	main()