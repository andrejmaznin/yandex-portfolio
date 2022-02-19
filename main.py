from flask import Flask
from flask_restful import Api

from handlers.about_me import AboutMeResource
from handlers.info import InfoResource
from handlers.main_page import MainPageResource
from handlers.video import VideoResource

app = Flask(__name__, template_folder='static/templates')
api = Api(app)

api.add_resource(MainPageResource, '/')
api.add_resource(VideoResource, '/video')
api.add_resource(AboutMeResource, '/about-me')
api.add_resource(InfoResource, '/info')

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
