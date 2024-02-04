from py_tailwind_utils import *

import ofjustpy as oj
oj.set_style("un")


from ofjustpy import icons
from py_tailwind_utils import *
from ofjustpy import icons

from hyperui_plugin.radiogroups import  (SimpleStacked)

simpleStacked = SimpleStacked()
simpleStacked.add_item("standard", "Standard", "Free")
simpleStacked.add_item("two_day", "Two Day", "£5.99")
simpleStacked.add_item("next_day", "Next Day", "£9.99")

app = oj.load_app()

endpoint = oj.create_endpoint("demo_radiogroups",
                              childs = [oj.HCCMutable.Container(childs=[simpleStacked
                                                                        ],
                                                        twsty_tags=[mr/x/auto, space/y/8]
                                                        )
                                        ],
                              title="Demo radio groups"

                   )
oj.add_jproute("/", endpoint)
