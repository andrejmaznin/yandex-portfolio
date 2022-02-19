import flask


def make_response(*args):
    headers = {'Content-Type': 'text/html'}

    return flask.make_response(*args, 200, headers)
