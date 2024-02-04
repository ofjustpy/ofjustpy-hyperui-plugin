from py_tailwind_utils import *
import ofjustpy as oj
oj.set_style("un")
from ofjustpy import icons
from hyperui_plugin.breadcrumbs import  (Simple,
                                         ChevronBackground)


breadcrumbs_component = Simple()
breadcrumbs_component.add_item("Shirt")
breadcrumbs_component.add_item("Plain Tee")


chevrobackground_breadcrumbs_component = ChevronBackground()
chevrobackground_breadcrumbs_component.add_item("Shirt")
chevrobackground_breadcrumbs_component.add_item("Plain Tee")

app = oj.load_app()
endpoint = oj.create_endpoint("demo_alert_comp",
                              childs = [breadcrumbs_component,
                                        chevrobackground_breadcrumbs_component
                                        ]
                   )
oj.add_jproute("/", endpoint)

