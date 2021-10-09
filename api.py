from flask import Flask
from flask_restx import Api, Resource, fields
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(
    app,
    version='1.0',
    title='Temperature observation',
    description='A simple TodoMVC API', prefix='/api/v1'
)

ns = api.namespace('temperature_observations', description='Temperature observations')

todo = api.model('TemperatureObservation', {
    'id': fields.Integer(readonly=True, description='The task unique identifier'),
    'temperature': fields.Integer(required=True, description='The task details')
})


class TemperatureObservationDAO(object):
    def __init__(self):
        self.counter = 0
        self.observations = []

    def get(self, observation_id):
        for observation in self.observations:
            if observation['id'] == observation_id:
                return observation
        api.abort(404, "Observation {} doesn't exist".format(id))

    def create(self, data):
        observation = data
        observation['id'] = self.counter = self.counter + 1
        self.observations.append(observation)
        return observation

    def update(self, observation_id, data):
        observation = self.get(observation_id)
        observation.update(data)
        return observation

    def delete(self, observation_id):
        observation = self.get(observation_id)
        self.observations.remove(observation)


# set up some dummy data
DAO = TemperatureObservationDAO()
DAO.create({'temperature': 15})
DAO.create({'temperature': 18})
DAO.create({'temperature': 32})


@ns.route('/')
class TodoList(Resource):
    @ns.doc('list_todos')
    @ns.marshal_list_with(todo)
    def get(self):
        return DAO.observations

    @ns.doc('add_temperature_observation')
    @ns.expect(todo)
    @ns.marshal_with(todo, code=201)
    def post(self):
        return DAO.create(api.payload), 201


if __name__ == '__main__':
    app.run(debug=True)
