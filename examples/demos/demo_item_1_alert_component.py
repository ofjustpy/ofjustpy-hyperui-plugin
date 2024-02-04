from py_tailwind_utils import *
import ofjustpy as oj
from hyperui_plugin.alerts import Popup, PopupWithAction, Content, WarningContent
from ofjustpy import icons

alert_popup = Popup("popup_alert", title='Your product changes have been saved.', desc='Changes saved')

alert_popupaction = PopupWithAction("popup_alertaction", title='Your product changes have been saved.', desc='Changes saved')

alert_content = Content('Something went wrong',
                        'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nemo quasi assumenda numquam deserunt consectetur autem nihil quos debitis dolor culpa.')

alert_warning_content = WarningContent('Something went wrong',
                        'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nemo quasi assumenda numquam deserunt consectetur autem nihil quos debitis dolor culpa.'
                                       )


# alert_comp = get_component("Alerts",
#                            "Popup",
#                            False,
#                            title="A title",
#                            desc="A desc",
#                            titleIcon = icons.menu,
#                            crossIcon=icons.cog)
# alert_comp_dark = get_component("Alerts",
#                                 "Popup",
#                                 True,
#                                 title="A title",
#                                 desc="A desc",
#                                 titleIcon = icons.encircledCheckmark,
#                                 crossIcon=icons.cross
#                                 )
# popup_with_actions = get_component("Alerts",
#                                    "Popup with Actions",
#                                    False,
#                                    title="A title",
#                                    desc="A desc",
#                                    titleIcon = icons.encircledCheckmark,
#                                    crossIcon=icons.cross,
#                                    previewIcon = icons.preview
#                                    )
# popup_with_actions_dark = get_component("Alerts",
#                                    "Popup with Actions",
#                                    True,
#                                    title="A title",
#                                    desc="A desc",
#                                    titleIcon = icons.encircledCheckmark,
#                                    crossIcon=icons.cross,
#                                    previewIcon = icons.preview
#                                    )

# content = get_component("Alerts", "Content", False, title = "Something went wrong", content="Alert content")
# content_dark = get_component("Alerts",
#                              "Content",
#                              True,
#                              title = "Something went wrong", content="Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nemo quasi assumenda numquam deserunt consectetur autem nihil quos debitis dolor culpa.")

# content_icon = get_component("Alerts",
#                              "Content with Icon",
#                              False,
#                              title = "Something went wrong",
#                              content="Alert content",
#                              )

# content_icon_dark = get_component("Alerts",
#                                   "Content with Icon",
#                                   True,
#                                   title = "Something went wrong", content="Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nemo quasi assumenda numquam deserunt consectetur autem nihil quos debitis dolor culpa.",
#                                   warningIcon=icons.chevronright)


app = oj.load_app()
endpoint = oj.create_endpoint("demo_alert_comp",
                              childs = [oj.PC.Div(childs=[alert_popup,
                                                          alert_popupaction,
                                                          alert_content,
                                                          alert_warning_content
                                                          ], twsty_tags=[space/y/4])
                                        ],
                   )
oj.add_jproute("/", endpoint)
