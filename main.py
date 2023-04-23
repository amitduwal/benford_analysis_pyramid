from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config

from benford import calculate_benford_law

import json

@view_config(
    route_name = "benford",
    renderer ="templates/home.jinja2"
)

def home(request):
    if request.method == 'POST' and 'csvfile' in request.POST:
        csvfile = request.POST['csvfile'].file.read().decode('utf-8')
        data = []
        for row in csvfile.split('\n'):
            if row.strip():  # skip empty rows
                value = float(row.split(',')[0])
                data.append(value)
        benford_result = calculate_benford_law(data)
        return {'benford_result': benford_result}
    else:
        return {'error': 'error'}

@view_config(
    route_name="json",
    renderer="json"
)
def json_data(request):
    if request.method == 'POST' and 'csvfile' in request.POST:
        csvfile = request.POST['csvfile'].file.read().decode('utf-8')
        data = []
        for row in csvfile.split('\n'):
            if row.strip():  # skip empty rows
                value = float(row.split(',')[0])
                data.append(value)
        benford_result = calculate_benford_law(data)
        return {'benford_result': benford_result}
    else:
        return {'error': 'error'}


if __name__=="__main__":
    with Configurator() as config:
        config.include("pyramid_jinja2")
        config.add_static_view(name = 'static',path = 'static')
        config.add_route("benford",'/')
        config.add_route("json", "/json")
        config.scan()
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
