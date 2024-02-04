from hyperui_plugin.marketing.faqs import  (BackgroundAccentBorder
                                                )

from py_tailwind_utils import *

import ofjustpy as oj
oj.set_style("un")
app = oj.load_app()

faq1 = BackgroundAccentBorder()
faq1.add_faq_item("Lorem ipsum dolor sit amet consectetur adipisicing?",
                  "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ab hic veritatis molestias culpa in, recusandae laboriosam neque aliquid libero nesciunt voluptate dicta quo officiis explicabo consequuntur distinctio corporis earum similique! "
                  )

endpoint = oj.create_endpoint("marketing_cta",
                              childs = [oj.PC.Container(childs=[faq1],
                                                        twsty_tags=[mr/x/auto]
                                                        )

                                        ],
                              title="Marketing CTA"
                              )
oj.add_jproute("/", endpoint)

