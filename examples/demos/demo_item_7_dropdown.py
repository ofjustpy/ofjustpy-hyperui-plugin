from py_tailwind_utils import *
import ofjustpy as oj
oj.set_style("un")
from hyperui_plugin.dropdown import Dropdown
from ofjustpy import icons
from py_tailwind_utils import *

dropdown_container = Dropdown("dd_key", "Edit")
def on_click(dbref, msg, to_ms):
    print("A clicked")
    
dropdown_container.add_item("View on StoreFront")
dropdown_container.add_item("View Warehouse Info")
dropdown_container.add_item("Duplicate Product")
dropdown_container.add_item("Unpublish Product")

app = oj.load_app()
endpoint = oj.create_endpoint("demo_dropdown",
                              childs = [oj.PC.Halign(dropdown_container)
                                        ]
                   )
oj.add_jproute("/", endpoint)

