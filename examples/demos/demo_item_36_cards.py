from hyperui_plugin.marketing.cards import  (Card_Type_1,
                                                )

from py_tailwind_utils import *

import ofjustpy as oj
oj.set_style("un")
app = oj.load_app()

href = "#"
title = "Building a SaaS product as a software developer"
author = "John Doe"
image_src = "https://images.unsplash.com/photo-1633332755192-727a05c4013d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1180&q=80"
content = "Lorem ipsum dolor sit, amet consectetur adipisicing elit. At velit illum provident a, ipsa maiores deleniti consectetur nobis et eaque."
published_date = "31st June, 2021"
reading_time = "3 minutes"

# Generate blog card
card_1 = Card_Type_1(href, title, author, image_src, content, published_date, reading_time)
endpoint = oj.create_endpoint("marketing_card",
                              childs = [oj.PC.Container(childs=[card_1],
                                                        twsty_tags=[mr/x/auto]
                                                        )

                                        ],
                              title="Marketing Cards"
                              )
oj.add_jproute("/", endpoint)

