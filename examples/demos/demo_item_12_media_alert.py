from py_tailwind_utils import *

import ofjustpy as oj
oj.set_style("un")


from ofjustpy import icons
from py_tailwind_utils import *
from ofjustpy import icons
from hyperui_plugin.media_alert import  (card)
def cards():
    for _ in ["top", "center", "bottom", "stretch"]:
        yield card(title="Title goes here",
                    text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptates voluptas distinctio nesciunt quas non animi.",
                    img_src = "https://images.unsplash.com/photo-1633332755192-727a05c4013d?q=80&w=2680&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
             align=_
                    )

        yield card(title="Title goes here",
                    text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptates voluptas distinctio nesciunt quas non animi.",
                    img_src = "https://images.unsplash.com/photo-1633332755192-727a05c4013d?q=80&w=2680&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
             align=f"{_}-right"
                    )
        
    

app = oj.load_app()
endpoint = oj.create_endpoint("demo_button_group",
                              childs = [oj.PC.Container(childs=[_c for _c in cards()
                                                                
                                                                ],
                                                        twsty_tags=[mr/x/auto, space/y/8, W/"1/3"]
                                                        )
                                        ]
                   )
oj.add_jproute("/", endpoint)

