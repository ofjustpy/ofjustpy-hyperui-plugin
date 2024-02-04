from py_tailwind_utils import *
import ofjustpy as oj
from ofjustpy import icons
from hyperui_plugin.badges import Badge

from ofjustpy.icons import Icon_EuroCurrency
simple_badge = Badge("Live")
icon_badge = Badge( icon = Icon_EuroCurrency)
icon_label_badge = Badge(label = "hello", icon = Icon_EuroCurrency)

label_badge_crossbtn = Badge(label = "hello")
def on_click(dbref, msg, to_ms):
    print ("btn clicked")
    pass
label_badge_crossbtn.add_cross_btn("abtn", on_click=on_click)


# # 1: Simple Badge
# simple_badge = get_component("Badges", "Simple", False, text="Badge title")
# simple_badge_dark = get_component("Badges", "Simple", True, text="Badge title")

# # 2: Simple Badge with Icon (for dark mode)
# simple_badge_with_icon = get_component("Badges",
#                                        "Simple with Icon",
#                                        False,
#                                        text="Badge title with icon",
#                                        badgeIcon=icons.menu)

# simple_badge_with_icon_dark = get_component("Badges", "Simple with Icon", True, text="Badge title with icon")

# # 3: Simple Icon Only Badge (for dark mode)
# simple_icon_only_badge = get_component("Badges", "Simple Icon Only", False,
#                                        badgeIcon=icons.cog)
# simple_icon_only_badge_dark = get_component("Badges",
#                                             "Simple Icon Only",
#                                             True,
#                                             )
# # 3: Simple Icon Only Badge (for dark mode)
# close_icon_badge = get_component("Badges", "Close", False)
# close_icon_badge_dark = get_component("Badges", "Close", True,
#                                       crossIcon = icons.warning)  


app = oj.load_app()
# endpoint = oj.create_endpoint("demo_alert_comp",
#                               childs = [oj.PC.StackV(childs=[oj.PC.Halign(_) for _ in [simple_badge,
#                                                                                              simple_badge_dark,
#                                                                                              simple_badge_with_icon,
#                                                                                              simple_badge_with_icon_dark,
#                                                                                              simple_icon_only_badge,
#                                                                                              simple_icon_only_badge_dark,
#                                                                                              close_icon_badge,
#                                                                                              close_icon_badge_dark
#                                                                                              ]
#                                                              ]
#                                                      , twsty_tags=[space/y/4])],
#                    )

endpoint = oj.create_endpoint("demo_alert_comp",
                              childs = [oj.PC.StackV(childs=[oj.PC.Halign(_) for _ in [simple_badge,
                                                                                       icon_badge, icon_label_badge, label_badge_crossbtn ]],
                                                     twsty_tags=[space/y/4])]
                              )
oj.add_jproute("/", endpoint)
