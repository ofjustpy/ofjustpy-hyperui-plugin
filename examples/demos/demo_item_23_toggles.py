from py_tailwind_utils import *

import kavya as kv
kv.set_style("un")


from py_tailwind_utils import *


app = kv.load_app()

from hyperui_plugin.toggles import  (Simple,
                                     Apple,
                                     Material,
                                     #SimpleWithIcon
                                          )
async def on_checkbox_click(dbref, msg, wp, request):
    print("on checkbox click = ", msg.value)
    
simple_togglebtn = Simple(key="stbtn", on_change = on_checkbox_click)
apple_togglebtn = Apple(key="atbtn")
material_togglebtn = Material(key="mtbtn")
# simpleicon_togglebtn = SimpleWithIcon(key="sitbtn")

endpoint = kv.create_endpoint("demo_toggle",
                              childs = [kv.HM.Container(childs = [simple_togglebtn,
                                                                          material_togglebtn,
                                                                          apple_togglebtn,
                                                                          #simpleicon_togglebtn
                                                                          ],
                                                                twsty_tags=[mr/x/auto, space/y/8]
                                                                )
                                        ],

                              title="Demo toggle",
                   )
kv.add_route("/", endpoint)
