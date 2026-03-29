from py_tailwind_utils import *

import kavya as kv
kv.set_style("un")

from py_tailwind_utils import *


from hyperui_plugin.selects import  (Base, BaseGroup, Datalist)

base_select = Base("base", "Headline")
base_select.add_option("JM", "John Mayer")
base_select.add_option("SRV", "Stevie Ray Vaughn")
base_select.add_option("JH", "Jimi Hendrix")
base_select.add_option("BBK", "B.B King")
base_select.add_option("AK", "Albert King")
base_select.add_option("BG", "Buddy Guy")
base_select.add_option("EC", "Eric Clapton")


# basegroup_select = BaseGroup("basegroup", "Headline")
# optgroup = basegroup_select.add_optgroup("A")
# optgroup.add_option("AK", "Albert King")

# optgroup = basegroup_select.add_optgroup("B")
# optgroup.add_option("BBK", "B.B King")
# optgroup.add_option("BG", "Buddy Guy")


# optgroup = basegroup_select.add_optgroup("E")
# optgroup.add_option("EC", "Eric Clapton")


# optgroup = basegroup_select.add_optgroup("J")
# optgroup.add_option("JM", "John Mayer")
# optgroup.add_option("JH", "Jimi Hendrix")

# optgroup = basegroup_select.add_optgroup("S")
# optgroup.add_option("SRV", "Stevie Ray Vaughn")


# datalist_select = Datalist("base", "Headline")
# datalist_select.add_option("JM", "John Mayer")
# datalist_select.add_option("SRV", "Stevie Ray Vaughn")
# datalist_select.add_option("JH", "Jimi Hendrix")
# datalist_select.add_option("BBK", "B.B King")
# datalist_select.add_option("AK", "Albert King")
# datalist_select.add_option("BG", "Buddy Guy")
# datalist_select.add_option("EC", "Eric Clapton")







app = kv.load_app()

endpoint = kv.create_endpoint("demo_selects",
                              childs = [kv.PD.Container(childs=[base_select,
                                                                #basegroup_select,
                                                                #datalist_select
                                                                        ],
                                                        twsty_tags=[]
                                                        )
                                        ],
                              title="Demo selects",
                              #skeleton_data_theme="mint",
                              #rendering_type="SSR",

                   )
kv.add_route("/", endpoint)
