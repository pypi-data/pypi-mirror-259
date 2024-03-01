import os
from dotenv import load_dotenv
import yaml

def test():
    load_dotenv()
    with open('config/config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    role = os.getenv("role")
    prefix = config["prefix"]
    print(role)
    print(prefix)
