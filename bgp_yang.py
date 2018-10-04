from builtins import input
from consolemenu import ConsoleMenu, SelectionMenu
from consolemenu.items import FunctionItem, SubmenuItem, CommandItem
import json
import napalm_yang
import yaml

def pretty_print(dictionary):
    print(json.dumps(dictionary, sort_keys=True, indent=4))

with open("intf.yml") as f:
    temp = yaml.load(f)

config = napalm_yang.base.Root()
config.add_model(napalm_yang.models.openconfig_interfaces())
config.load_dict(temp)

def show_data(args):
    if "yaml" in args:
        print(stream)
    elif "dict" in args:
        pretty_print(temp)
    elif "yang" in args:
        pretty_print(napalm_yang.utils.model_to_dict(config))
    elif "gen" in args:
        pretty_print(config.get(filter=True))
    elif "junos" in args:
        print(config.translate_config(profile=["junos"]))
    elif "ios" in args:
        print(config.translate_config(profile=["ios"]))
    else:
        return
    input("Press Enter")

menu = ConsoleMenu("Menu")
menu_dict = {"yaml":"YAML data model", "dict": "python dictionary", "yang": "YANG model.  Warning: long output.", "gen": "generated YANG data", "junos":"JunOS config", "ios":"IOS config"}
for key, value in menu_dict.items():
    function_item = FunctionItem("View the " + value, show_data, [key])
    menu.append_item(function_item)
menu.show()
