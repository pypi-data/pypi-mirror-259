import setuptools
import yaml

with open("setup.yml", 'r') as file:
    config = yaml.safe_load(file)
setuptools.setup(**config)
