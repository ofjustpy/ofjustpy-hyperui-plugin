from hyperui_plugin.marketing.blog_cards import  (Simple,
                                             Floating,
                                             Bordered,
                                             GradientBorder
                                                )

from py_tailwind_utils import *

import ofjustpy as oj
oj.set_style("un")
app = oj.load_app()

# Example usage:
blog_card_simple = Simple(
    image_url="https://images.unsplash.com/photo-1524758631624-e2822e304c36?ixlib=rb-1.2.1&ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2070&q=80",
    date="2022-10-10",
    title="How to position your furniture for positivity",
    content="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Recusandae dolores, possimus pariatur animi temporibus nesciunt praesentium dolore sed nulla ipsum eveniet corporis quidem, mollitia itaque minus soluta, voluptates neque explicabo tempora nisi culpa eius atque dignissimos. Molestias explicabo corporis voluptatem?",
    link="#",
)

# Example usage:
blog_card_floating = Floating(
    image_url="https://images.unsplash.com/photo-1631451095765-2c91616fc9e6?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80",
    alt_text="Lava",
    title="Finding the Journey to Mordor",
    content="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Recusandae dolores, possimus pariatur animi temporibus nesciunt praesentium dolore sed nulla ipsum eveniet corporis quidem, mollitia itaque minus soluta, voluptates neque explicabo tempora nisi culpa eius atque dignissimos. Molestias explicabo corporis voluptatem?",
    link="#",
)

blog_card_bordered = Bordered(
    image_url="https://images.unsplash.com/photo-1600880292203-757bb62b4baf?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80",
    alt_text="Office",
    title="Lorem ipsum dolor sit amet consectetur adipisicing elit.",
    content="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Recusandae dolores, possimus pariatur animi temporibus nesciunt praesentium dolore sed nulla ipsum eveniet corporis quidem, mollitia itaque minus soluta, voluptates neque explicabo tempora nisi culpa eius atque dignissimos. Molestias explicabo corporis voluptatem?",
    link="#",
)

blog_card_gradientBorder = GradientBorder(
    date="2022-10-10",
    title="How to center an element using JavaScript and jQuery",
    tags=["Snippet", "JavaScript"]
)

endpoint = oj.create_endpoint("blog_card",
                              childs = [oj.PC.Container(childs=[oj.PC.Halign(blog_card_simple),
                                                                oj.PC.Halign(blog_card_floating),
                                                                oj.PC.Halign(blog_card_bordered),
                                                                oj.PC.Halign(blog_card_gradientBorder) ],
                                                        twsty_tags=[mr/x/auto, space/y/8]
                                                        )

                                        ],
                              title="Blog Cards"
                              )
oj.add_jproute("/", endpoint)
