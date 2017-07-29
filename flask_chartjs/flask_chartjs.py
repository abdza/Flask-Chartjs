from flask import current_app, Markup, Blueprint, render_template, g
import re

try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack

class Chart(object):

    def __init__(self,title='No title',chart_type='bar',slug=None,click=None):
        self.title = title
        if slug:
            self.slug = slug
        else:
            self.slug = re.sub(r'\W+','_',str(title))
        self.type = chart_type
        self.click = click
        self.datasets = {
                }

    @property
    def js(self):
        return Markup(
                self.render(
                    'chartjs/chartjs.js',
                    chart=self,
                    )
                )

    @property
    def html(self):
        return Markup(
                self.render(
                    'chartjs/chartjs.html',
                    chart=self,
                    )
                )

    def render(self, *args, **kwargs):
        return render_template(*args, **kwargs)

def set_chartjs_loaded():
    g.chartjs_loaded = True
    return ''

def is_chartjs_loaded():
    return getattr(g, 'chartjs_loaded', False)

class ChartJs(object):

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        self.register_blueprint(app)
        self.title = "Chart Title"

    def register_blueprint(self, app):
        module = Blueprint(
                "chartjs", __name__, template_folder="templates", static_folder="static"
                )
        app.register_blueprint(module)
        app.add_template_global(is_chartjs_loaded)
        app.add_template_global(set_chartjs_loaded)
        return module

