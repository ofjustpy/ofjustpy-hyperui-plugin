from py_tailwind_utils import *
import ofjustpy as oj
from hyperui_plugin.hui_components import get_component
from ofjustpy import icons
content_icon = get_component("Alerts",
                             "Content with Icon",
                             False,
                             title = "Something went wrong",
                             content="Alert content",
                             )

content_icon_dark = get_component("Alerts",
                                  "Content with Icon",
                                  True,
                                  title = "Something went wrong", content="Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nemo quasi assumenda numquam deserunt consectetur autem nihil quos debitis dolor culpa.",
                                  warningIcon=icons.chevronright)


app = oj.load_app()
endpoint = oj.create_endpoint("demo_alert_comp",
                              childs = [oj.PC.Div(childs=[
                                                          content_icon,
                                                          content_icon_dark
                                               ])],
                   )
oj.add_jproute("/", endpoint)
