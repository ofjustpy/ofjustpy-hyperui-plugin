from py_tailwind_utils import *

import ofjustpy as oj
oj.set_style("un")

from ofjustpy import icons
from py_tailwind_utils import *
from ofjustpy import icons
from hyperui_plugin.pagination import  (WithButtons, WithInput, BackgroundWithInput, WithFraction)
pg_nav_buttons = WithButtons("pagination_nav_bar", [4, 5, 6, 8])

pg_nav_input = WithInput("pagination_nav_input")

pg_nav_bginput = BackgroundWithInput("pagination_nav_bginput")

pg_nav_fraction = WithFraction("pagination_nav_fraction")
content = [oj.PC.Halign(pg_nav_buttons),
           oj.PC.Halign(pg_nav_input),
           oj.PC.Halign(pg_nav_bginput),
           oj.PC.Halign(pg_nav_fraction)
           ]


app = oj.load_app()
endpoint = oj.create_endpoint("demo_pagination_nav_bar",
                              childs = [oj.PC.Container(childs=content,
                                                        twsty_tags=[mr/x/auto, space/y/8, W/"1/3"]
                                                        )
                                        ]
                   )
oj.add_jproute("/", endpoint)
