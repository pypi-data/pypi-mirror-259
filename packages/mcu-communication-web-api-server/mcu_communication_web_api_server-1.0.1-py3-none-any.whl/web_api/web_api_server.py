from flask import Flask, jsonify
from flask_restx import Api, Resource


schema_file= "/fbs/mcu_communication.fbs"
class WebAPIServer:
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app, version='1.0', title='Joysort MCU API with Swagger', doc='/swagger/')
        self.setup_routes()

    def setup_routes(self):
        mcu_ns = self.api.namespace('routes', description='MCU operations')
        motor_ns = self.api.namespace('motor', description='Motor operations')

        @mcu_ns.route('/ping')
        class Ping(Resource):
            def post(self):
                # Call the function to create a ping request

                return jsonify({'ping': 'pong'})

        # @query_ns.route('/')
        # class QuerySerialNumber(Resource):
        #     def post(self):
        #         # Call the function to create a query serial number request
        #         request = create_query_serial_number_request()
        #         return flatbuffers_to_json_with_flatc(request,schema_file)

    def run(self, host='localhost', port=5000):
        self.app.run(host=host, port=port)