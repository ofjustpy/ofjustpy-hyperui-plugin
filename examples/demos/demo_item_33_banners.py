from hyperui_plugin.marketing.banners import  (CenteredWithAction,
                                          CenteredWithActionGradient
                                                )

import ofjustpy as oj
oj.set_style("un")
app = oj.load_app()
# Example usage:
title = "Understand User Flow."
sub_title = "Increase Conversion."
description = "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nesciunt illo tenetur fuga ducimus numquam ea!"
button1_text = "Get Started"
button1_link = "/get-started"
button2_text = "Learn More"
button2_link = "/about"

banner_centeredWithAction = CenteredWithAction(title, sub_title, description, button1_text, button1_link, button2_text, button2_link)

# Example usage:
title = "Understand User Flow."
sub_title = "Increase Conversion."
description = "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nesciunt illo tenetur fuga ducimus numquam ea!"
button1_text = "Get Started"
button1_link = "/get-started"
button2_text = "Learn More"
button2_link = "/about"

banner_2 = CenteredWithActionGradient(title, sub_title, description, button1_text, button1_link, button2_text, button2_link)

endpoint = oj.create_endpoint("banners",
                              childs = [banner_centeredWithAction,
                                        banner_2

                                        ],
                              title="Banners"
                              )
oj.add_jproute("/", endpoint)
