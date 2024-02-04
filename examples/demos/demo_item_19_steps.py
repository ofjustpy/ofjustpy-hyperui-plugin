from py_tailwind_utils import *

import ofjustpy as oj
oj.set_style("un")

from ofjustpy import icons
from py_tailwind_utils import *
from ofjustpy import icons
from hyperui_plugin.steps import  (WithTextAndIcon,
                                   WithCheckIcons,
                                   WithChevronTextIcon
                                   
                                   )

steps_type_1, abtn = WithTextAndIcon("pg_1")
steps_type_2 = WithCheckIcons("pg_2")
steps_type_3 = WithChevronTextIcon()

content=[oj.HCCMutable.Div(childs=[oj.HCCMutable.Halign(steps_type_1),
                                   oj.PC.Halign(abtn)], twsty_tags=[space/y/4]),
         oj.PC.Halign(steps_type_2),
         oj.PC.Halign(steps_type_3)
         ]
app= oj.load_app()
endpoint = oj.create_endpoint("steps",
                              childs = [oj.HCCMutable.Container(childs = content,
                                                                twsty_tags=[space/y/16]

                                                                          )
                                        ],

                              title="Steps"
                              )
oj.add_jproute("/", endpoint)
