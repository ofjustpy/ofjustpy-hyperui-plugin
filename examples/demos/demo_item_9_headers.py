from py_tailwind_utils import *

import ofjustpy as oj
oj.set_style("un")

from ofjustpy import icons
from py_tailwind_utils import *
from ofjustpy import icons
from hyperui_plugin.headers import IntroActions, IntroWithSearchAndMiniNavigation
header_introActions = IntroActions("header_intro",
                                         "Welcome Back, Barry!", "Let's write a new blog post! 🎉")
# def on_click(dbref, msg, to_ms):
#     print("A clicked")
    
# nav_item_adder("view_website", "View Website", icons.preview)
# nav_item_adder("post", "Post")
header_IntroWithSearchAndMiniNavigation = IntroWithSearchAndMiniNavigation("header_searchnav")

app = oj.load_app()
endpoint = oj.create_endpoint("demo_button_group",
                              childs = [oj.PC.Container(childs=[oj.PC.Halign(header_introActions),
                                                                oj.PC.Halign(header_IntroWithSearchAndMiniNavigation)
                                                                
                                                                ],
                                                        twsty_tags=[mr/x/auto]
                                                        )
                                        ]
                   )
oj.add_jproute("/", endpoint)

