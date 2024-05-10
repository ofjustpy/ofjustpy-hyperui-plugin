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

app = oj.load_app()
endpoint = oj.create_endpoint("demo_alert_comp",
                              childs = [oj.PC.Div(childs=[alert_popup,
                                                          alert_popupaction,
                                                          alert_content,
                                                          alert_warning_content
                                                          ], twsty_tags=[space/y/4])
                                        ],
                              body_classes="font-geist",
                              skeleton_data_theme="modern"
                   )
oj.add_jproute("/", endpoint)
