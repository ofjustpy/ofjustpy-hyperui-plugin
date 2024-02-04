from hyperui_plugin.marketing.testimonials import  (SplitContentSlider,
                                              )
from py_tailwind_utils import *

import ofjustpy as oj
oj.set_style("un")
app = oj.load_app()
testimonial_1 = SplitContentSlider()

endpoint = oj.create_endpoint("Testimonial",
                              childs = [oj.PC.Container(childs=[testimonial_1
                                                                ],
                                                        twsty_tags=[mr/x/auto]
                                                        )

                                        ],
                              title="Testimonial"
                              )
oj.add_jproute("/", endpoint)
