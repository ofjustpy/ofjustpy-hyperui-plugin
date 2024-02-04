from hyperui_plugin.marketing.sections import  (GridUSP
                                              )
from py_tailwind_utils import *

import ofjustpy as oj
oj.set_style("un")
app = oj.load_app()
gridusp = GridUSP()

endpoint = oj.create_endpoint("Section",
                              childs = [oj.PC.Container(childs=[gridusp
                                                                ],
                                                        twsty_tags=[mr/x/auto]
                                                        )

                                        ],
                              title="Section"
                              )
oj.add_jproute("/", endpoint)

    
