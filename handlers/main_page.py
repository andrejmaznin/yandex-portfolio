from flask_restful import Resource
from flask import render_template
from modules.flask import make_response
from modules import jinja


class MainPageResource(Resource):
    @staticmethod
    def get() -> dict:
        return make_response(
            render_template(
                'main_page.html',
                video_source=jinja.render_template('video_url.txt')

            )
        )
