from flask import Flask, jsonify
from flask import make_response
from host import Host
from flask import abort

app = Flask(__name__)

hosts = {"10.0.2.15":{"user": 'vagrant', "passwd":'vagrant'}}

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/', methods=['GET'])
def home():
	abort(404)
	#return jsonify({'tasks': tasks})

@app.route('/api/v1.0/<host>', methods=['GET'])
def get_host(host):
	if host in hosts:
		h = Host(host, hosts[host]['user'], hosts[host]['passwd'])
		return jsonify({'disks': h.disks(), 'os': h.os(), 'memory': h.memory(), 'cpu': h.cpu()})
	else:
		abort(404)

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0',port=8000)
