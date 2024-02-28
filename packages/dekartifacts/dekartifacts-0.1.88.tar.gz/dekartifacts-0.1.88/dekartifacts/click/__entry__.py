from . import app
from .image import app as image_app
from .helm import app as helm_app

app.add_typer(image_app, name='image')
app.add_typer(helm_app, name='helm')


def main():
    app()
