from py_tailwind_utils import *

import ofjustpy as oj
oj.set_style("un")

from ofjustpy import icons
from py_tailwind_utils import *
from ofjustpy import icons

from hyperui_plugin.login_forms import  (SplitWithGraphic,
                                         SplitWithContent
                                         )


login_form_type1 = SplitWithGraphic("login_form")
login_form_type2 = SplitWithContent()

app = oj.load_app()
endpoint = oj.create_endpoint("demo_login_forms",
                              childs = [oj.PC.Container(childs=[oj.PC.Halign(login_form_type1),
                                                                oj.PC.Halign(login_form_type2),
                                                                
                                                                ],
                                                        twsty_tags=[mr/x/auto, space/y/8]
                                                        )
                                        ],
                              title="Login forms"
                              
                   )
oj.add_jproute("/", endpoint)

