from py_tailwind_utils import *

import ofjustpy as oj
oj.set_style("un")

from ofjustpy import icons
from py_tailwind_utils import *
from ofjustpy import icons

app = oj.load_app()

from hyperui_plugin.toggles import  (Simple,
                                     Apple,
                                     Material,
                                     #SimpleWithIcon
                                          )
def on_checkbox_click(dbref, msg, to_ms):
    print("on checkbox click = ", msg.value)
    
simple_togglebtn = Simple(key="stbtn", on_change = on_checkbox_click)
apple_togglebtn = Apple(key="atbtn")
material_togglebtn = Material(key="mtbtn")
# simpleicon_togglebtn = SimpleWithIcon(key="sitbtn")

endpoint = oj.create_endpoint("demo_toggle",
                              childs = [oj.HCCMutable.Container(childs = [simple_togglebtn,
                                                                          material_togglebtn,
                                                                          apple_togglebtn,
                                                                          #simpleicon_togglebtn
                                                                          ],
                                                                twsty_tags=[mr/x/auto, space/y/8]
                                                                )
                                        ],

                              title="Demo toggle"

                   )
oj.add_jproute("/", endpoint)
