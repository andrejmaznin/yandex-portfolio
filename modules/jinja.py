import os.path

from jinja2 import Environment, FileSystemLoader

project_path = '/'.join(os.path.abspath('').split('/'))

env = Environment(loader=FileSystemLoader(project_path + '/static/templates/jinja'))


def render_template(template):
    template = env.get_template(template)

    return template.render(abspath=project_path)
