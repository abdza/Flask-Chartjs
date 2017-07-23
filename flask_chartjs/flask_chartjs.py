from flask import current_app, Markup

try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack

class Chart(object):

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.register_blueprint(app)
        self.title = "Chart Title"

    def register_blueprint(self, app):
        module = Blueprint(
                "chartjs", __name__, template_folder="templates"
                )
        app.register_blueprint(module)
        return module

    def render(self, *args, **kwargs):
        return render_template(*args, **kwargs)

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
