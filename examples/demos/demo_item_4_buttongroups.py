from py_tailwind_utils import *
import ofjustpy as oj
from ofjustpy.icons import FontAwesomeIcon
oj.set_style("un")
from ofjustpy import icons
from py_tailwind_utils import *
from ofjustpy import icons
from hyperui_plugin import buttongroups
btn_container = buttongroups.Simple()
btn_container.add_button(key="abtn", text="Click me")
btn_container.add_button(key="bbtn", text="Click me 2")
btn_container.add_button(key="cbtn", text="Click me 3")

btn_container_icon =  buttongroups.WithIcons()
btn_container_icon.add_button("iabtn",
                              "Edit",
                              FontAwesomeIcon(label="faEdit"))
btn_container_icon.add_button("ibbtn", "View", FontAwesomeIcon(label="faEye"))
btn_container_icon.add_button("icbtn",
                              "Delete",
                              FontAwesomeIcon(label="faTrashAlt")
                              )

tlc = oj.PC.StackV(childs = [oj.PC.Halign(btn_container),
                             oj.PC.Halign(btn_container_icon)],
                   twsty_tags=[space/y/4]
             )

app = oj.load_app()
endpoint = oj.create_endpoint("demo_button_group",
                              childs = [tlc
                                        ]
                   )
oj.add_jproute("/", endpoint)
