import napalm_yang
import json
import yaml

def pretty_print(dictionary):
    print(json.dumps(dictionary, sort_keys=True, indent=4))

config = napalm_yang.base.Root()

config.add_model(napalm_yang.models.openconfig_interfaces())

with open("intf.yml") as f:
    stream = f.read()
    temp = yaml.load(stream)

raw_input("View the YAML data model.  Press Enter")
print(stream)

raw_input("View the data model as a python dict.  Press Enter")
pretty_print(temp)

raw_input("View the YANG model.  Warning: long output. Press Enter")
pretty_print(napalm_yang.utils.model_to_dict(config))

raw_input("View the generated YANG data.  Press Enter")
config.load_dict(temp)
pretty_print(config.get(filter=True))

raw_input("View JunOS config.  Press Enter")
print(config.translate_config(profile=["junos"]))

raw_input("View IOS config.  Press Enter")
print(config.translate_config(profile=["ios"]))
