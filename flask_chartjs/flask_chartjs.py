from flask import current_app, Markup, Blueprint, render_template

try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack

class Chart(object):

    def __init__(self,title='No title'):
        self.title = title

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
                "chartjs", __name__, template_folder="templates"
                )
        app.register_blueprint(module)
        return module

