from hyperui_plugin.marketing.cta import  (ContentAndImage,
                                           NewsletterSignup
                                                )

from py_tailwind_utils import *

import ofjustpy as oj
oj.set_style("un")
app = oj.load_app()

cta_1 = ContentAndImage()
cta_2 = NewsletterSignup()
endpoint = oj.create_endpoint("marketing_cta",
                              childs = [oj.PC.Container(childs=[cta_1, cta_2],
                                                        twsty_tags=[mr/x/auto]
                                                        )

                                        ],
                              title="Marketing CTA"
                              )
oj.add_jproute("/", endpoint)

