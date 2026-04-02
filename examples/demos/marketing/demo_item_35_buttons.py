from hyperui_plugin.marketing.buttons import  (Simple_Solid,
                                               Simple_Blank,
                                               GradientBorder,
                                               GradientBorder_Oval,
                                               CurtainClose
                                                )

from py_tailwind_utils import *

import ofjustpy as oj
oj.set_style("un")
app = oj.load_app()

ss_btn = Simple_Solid("ss", "Download")
sb_btn = Simple_Blank("sb", "Download")

gb_btn = GradientBorder("gb", "Download")
gbo_btn = GradientBorder_Oval("gbo", "Download")

cc_l = CurtainClose("ccl", "Download")
cc_r = CurtainClose("ccl", "Download", "right")
cc_b = CurtainClose("ccl", "Download", "bottom")
cc_t = CurtainClose("ccl", "Download", "top")

content = [oj.PC.Halign(ss_btn),
                                       oj.PC.Halign(sb_btn),
                                       oj.PC.Halign(gb_btn),
                                       oj.PC.Halign(gbo_btn),
                                       oj.PC.Halign(cc_l),
                                       oj.PC.Halign(cc_r),
                                       oj.PC.Halign(cc_b),
                                       oj.PC.Halign(cc_t),
                                       ]

endpoint = oj.create_endpoint("buttons",
                              childs =[oj.PC.Div(childs = content, twsty_tags=[space/y/8])],
                              title = "Buttons"
                              )
oj.add_jproute("/", endpoint)
