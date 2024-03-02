import yaml
from jinja2 import Template


class YAMLTemplate:
    def __init__(self, yaml_string: str):
        self.yaml_string = yaml_string
        self.template = Template(
            yaml_string,
            variable_start_string="${{",
            variable_end_string="}}",
        )

    def render(self, substitutions: dict) -> dict:
        return yaml.safe_load(self.template.render(substitutions))

    @staticmethod
    def load_from_file(file_path: str):
        with open(file_path, "r") as file:
            return YAMLTemplate(file.read())
