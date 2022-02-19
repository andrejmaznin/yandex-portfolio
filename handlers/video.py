from flask_restful import Resource
from flask import send_file


class VideoResource(Resource):
    @staticmethod
    def get() -> dict:
        return send_file('./video/main_page.mp4')
