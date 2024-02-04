from py_tailwind_utils import *

import ofjustpy as oj
oj.set_style("un")

from ofjustpy import icons
from py_tailwind_utils import *
from ofjustpy import icons

from hyperui_plugin.inputs import  (Simple  as SimpleInput,
                                              WithIcon,
                                              SearchInputWithButton,
                                              WithLabel,
                                              FloatingLabel,
                                    FloatingLabelInside,
                                    FloatingLabelUnderline)

ainp = SimpleInput("inp1", "Email", "san@me.com")
ainp2 = WithIcon("inp2", "Email", "san@me.com")
ainp3 = SearchInputWithButton("inp2", "Email", "san@me.com")
ainp4 = WithLabel("inp4", "Email", "san@me.com")
ainp5 = FloatingLabel("inp5", "Email", "san@me.com")
ainp6 = FloatingLabelInside("inp6", "Email", "san@me.com")
ainp7 = FloatingLabelUnderline("inp7", "Email", "san@me.com")

            
app = oj.load_app()
endpoint = oj.create_endpoint("demo_button_group",
                              childs = [oj.PC.Container(childs=[oj.PC.Halign(ainp),
                                                                oj.PC.Halign(ainp2),
                                                                oj.PC.Halign(ainp3),
                                                                oj.PC.Halign(ainp4),
                                                                oj.PC.Halign(ainp5),
                                                                oj.PC.Halign(ainp6),
                                                                oj.PC.Halign(ainp7),
                                                                
                                                                ],
                                                        twsty_tags=[mr/x/auto, space/y/8]
                                                        )
                                        ]
                   )
oj.add_jproute("/", endpoint)

