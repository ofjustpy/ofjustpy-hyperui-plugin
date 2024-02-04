from hyperui_plugin.marketing.popups import  (SplitWithImageAndAction,
                                              MessageNotificationsAndAction,
                                              OrderNotificationsWithAction,
                                              ContactActions,
                                              NotificationWithImageAndClose,
                                              FloatingSplitWithImageContentClose,
                                              FloatingWithClose
                                                )

from py_tailwind_utils import *

import ofjustpy as oj
oj.set_style("un")
app = oj.load_app()

# Example invocation
img_src_example = "https://images.unsplash.com/photo-1611510338559-2f463335092c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=928&q=80"
text_example = "On your next order over $50"

popup_type_1 = SplitWithImageAndAction(img_src_example, "Run with the pack", "Get 20% off", "On your next order over $50", "GET DISCOUNT", "Offer valid until 24th March, 2021 *" )
    


popup_type_2 = MessageNotificationsAndAction("New message!",
                              "Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsam ea quo unde vel adipisci blanditiis voluptates eum. Nam, cum minima?",
                              "Take a Look",
                              "Mark as Read",
                              )
popup_type_3 =  OrderNotificationsWithAction()
popup_type_4 = NotificationWithImageAndClose("akey")

popup_type_5 = ContactActions()

popup_type_6 = FloatingSplitWithImageContentClose("btnkey")
popup_type_7 = FloatingWithClose("btnkey")
endpoint = oj.create_endpoint("marketing_card",
                              childs = [oj.PC.Container(childs=[popup_type_1,
                                                                popup_type_2,
                                                                popup_type_3,
                                                                popup_type_4,
                                                                popup_type_5,
                                                                popup_type_6,
                                                                popup_type_7
                                                                ],
                                                        twsty_tags=[mr/x/auto, space/y/16]
                                                        )

                                        ],
                              title="Marketing Cards"
                              )
oj.add_jproute("/", endpoint)

