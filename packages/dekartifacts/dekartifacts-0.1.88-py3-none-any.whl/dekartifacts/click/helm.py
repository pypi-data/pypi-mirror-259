import typing
import typer
from dektools.yaml import yaml
from dektools.file import read_text
from dektools.cfg import AssignCfg

app = typer.Typer(add_completion=False)


@app.command()
def values(out, env=None, prefix=None, file: typing.Optional[typing.List[str]] = typer.Option(None)):
    if env:
        env = read_text(env)
    data = AssignCfg(prefix=prefix, dotenv=env, *(yaml.load(f) for f in file)).generate()
    yaml.dump(out, data)
