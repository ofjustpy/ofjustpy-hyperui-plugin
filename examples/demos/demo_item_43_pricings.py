from hyperui_plugin.marketing.pricings import  (HighlightOption,
                                              )
from py_tailwind_utils import *

import ofjustpy as oj
oj.set_style("un")
app = oj.load_app()
highlightOption = HighlightOption()

endpoint = oj.create_endpoint("pricing",
                              childs = [oj.PC.Container(childs=[highlightOption
                                                                ],
                                                        twsty_tags=[mr/x/auto]
                                                        )

                                        ],
                              title="Pricings"
                              )
oj.add_jproute("/", endpoint)
