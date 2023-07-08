from chalice import Chalice

app = Chalice(app_name='chalice_aws_api')


@app.route('/')
def index():
    return {'hello': 'world'}


