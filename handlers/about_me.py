from flask_restful import Resource
from flask import render_template
from modules.flask import make_response


class AboutMeResource(Resource):
    @staticmethod
    def get() -> dict:
        return make_response(render_template('about-me.html'))
