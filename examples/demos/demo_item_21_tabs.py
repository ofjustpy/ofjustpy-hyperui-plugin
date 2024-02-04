from py_tailwind_utils import *

import ofjustpy as oj
oj.set_style("un")

from ofjustpy import icons
from py_tailwind_utils import *
from ofjustpy import icons
from hyperui_plugin.tabs import  (Pills,
                                  Tabbed
                                          )
app = oj.load_app()
def on_change(dbref, msg, to_ms):
    print("On change")
    pass

# pills = Pills("extab", on_change=on_change)
# pills.add_tab("Settings", "Settings")
# pills.add_tab("Messages", "Messages")
# pills.add_tab("Archive", "Archive")
# pills.add_tab("Notifications", "Notifications")
pills = Pills("pillstab")
pills.add_tab("settings", "Settings")
pills.add_tab("messages", "Messages")
pills.add_tab("archive", "Archive")
pills.add_tab("notifications", "Notifications", selected=True)

tabbed = Tabbed("tabbed")
tabbed.add_tab("settings", "Settings")
tabbed.add_tab("messages", "Messages")
tabbed.add_tab("archive", "Archive")
tabbed.add_tab("notifications", "Notifications", selected=True)


endpoint = oj.create_endpoint("demo_tabs",
                              childs = [oj.HCCMutable.Container(childs = [pills,
                                                                          tabbed
                                                                          ],
                                                                twsty_tags=[mr/x/auto, space/y/8]
                                                                )
                                        ],

                              title="Demo tabs"

                   )

oj.add_jproute("/", endpoint)
