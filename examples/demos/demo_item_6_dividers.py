from py_tailwind_utils import *
import ofjustpy as oj
oj.set_style("un")


from ofjustpy import icons
from py_tailwind_utils import *
from ofjustpy import icons
from hyperui_plugin import dividers
more_divider = dividers.More(text="Lorem, ipsum dolor")
blurry_divider = dividers.Blurry(text="Lorem, ipsum dolor")
left_align_divider = dividers.AlignLeft(text="Lorem, ipsum dolor")
right_align_divider = dividers.AlignLeft(text="Lorem, ipsum dolor")

content = [oj.PC.Halign(_) for _ in [more_divider, blurry_divider, left_align_divider, right_align_divider
                                     ]
           ]
container = oj.PC.StackV(childs=content
                                             , twsty_tags=[space/y/4])

tlc = oj.PC.Container(childs = [container

                                ],
                      twsty_tags=[mr/x/auto]
                      )
                      


app = oj.load_app()
endpoint = oj.create_endpoint("demo_alert_comp",
                              childs = [tlc],
                   )
oj.add_jproute("/", endpoint)
