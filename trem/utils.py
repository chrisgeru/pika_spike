from jinja2 import Environment, PackageLoader
from sanic.response import html

# Jinja Environment
env = Environment(loader=PackageLoader('app', 'templates'))


def render_template(context, file):
    template = env.get_template(file)
    html_content = template.render(**context)
    return html(html_content)
