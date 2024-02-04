from py_tailwind_utils import *

import ofjustpy as oj
oj.set_style("un")

from ofjustpy import icons
from py_tailwind_utils import *
from ofjustpy import icons

app = oj.load_app()
from hyperui_plugin.verticalmenu import  (Simple,
                                          WithBadge,
                                          WithIcon,
                                          WithIconAndBadge,
                                          WithIconAndBrandedAccent,
                                          menugroups,
                                          SplitWithHeading
                                          )

container = Simple(twsty_tags=[W/32])
container.add_item("General")
container.add_item("Teams")
container.add_item("Billing")

badge_container = WithBadge(twsty_tags=[W/32])
badge_container.add_item("General")
badge_container.add_item("Teams", badge="6")
badge_container.add_item("Billing")
badge_container.add_item("Invoices", badge="3")


# icon_container = WithIcon(twsty_tags=[W/32])
# icon_container.add_item("General", icons.cog)
# icon_container.add_item("Teams", icons.teams)
# icon_container.add_item("Billing", icons.billing)
# icon_container.add_item("Account", icons.account)




# icon_container = WithIcon(twsty_tags=[W/32])
# icon_container.add_item("General", icons.cog)
# icon_container.add_item("Teams", icons.teams)
# icon_container.add_item("Billing", icons.billing)
# icon_container.add_item("Account", icons.account)

# iconbadge_container = WithIconAndBadge(twsty_tags=[W/64])
# iconbadge_container.add_item("General", icons.cog)
# iconbadge_container.add_item("Teams", icons.teams, badge="5")
# iconbadge_container.add_item("Billing", icons.billing)
# iconbadge_container.add_item("Account", icons.account, badge="6")

# icon_ba_container = WithIconAndBrandedAccent(twsty_tags=[W/64])
# icon_ba_container.add_item("General", icons.cog)
# icon_ba_container.add_item("Teams", icons.teams)
# icon_ba_container.add_item("Billing", icons.billing)
# icon_ba_container.add_item("Account", icons.account)

mg_container = menugroups(twsty_tags=[W/64])
agroup = mg_container.add_group()
agroup.add_item("Profile")
agroup.add_item("Team")
agroup.add_item("Projects")
agroup = mg_container.add_group()
agroup.add_item("Update")
agroup.add_item("Help")
agroup.add_item("Settings")
agroup = mg_container.add_group()
agroup.add_item("Logout")

splitWithHeading = SplitWithHeading()
group= splitWithHeading.add_group("General")
group.add_item("Profile")
group.add_item("Team")
group.add_item("Projects")
group.add_item("Meeting")
group.add_item("Calender")

group= splitWithHeading.add_group("Support")
group.add_item("Update")
group.add_item("Help")
group.add_item("Settings")

group= splitWithHeading.add_group("Profile")
group.add_item("Details")
group.add_item("Subscription")
group.add_item("Logout")


endpoint = oj.create_endpoint("demo_verticalmenu",
                              childs = [oj.HCCMutable.Container(childs=[oj.PC.Halign(container),
                                                                        oj.PC.Halign(badge_container),
                                                                        # oj.PC.Halign(icon_container),
                                                                        # oj.PC.Halign(iconbadge_container),
                                                                        # oj.PC.Halign(icon_ba_container),
                                                                        oj.PC.Halign(mg_container),
                                                                        oj.PC.Halign(splitWithHeading)
                                                                        ],
                                                                twsty_tags=[mr/x/auto, space/y/8]
                                                        )
                                        ],
                              title="Demo vertical menu"

                   )
oj.add_jproute("/", endpoint)
