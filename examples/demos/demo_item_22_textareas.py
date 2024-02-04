from py_tailwind_utils import *

import ofjustpy as oj
oj.set_style("un")

from ofjustpy import icons
from py_tailwind_utils import *
from ofjustpy import icons
from hyperui_plugin.textareas import  (Simple,
                                       ActionContained,
                                       WithActions
                                          )

app = oj.load_app()
simple_ta = Simple("tbtn",
                   "Order notes",
                   "Enter any additional order notes...")

actioncontained_ta = ActionContained("tbtn",
                                     "Order notes",
                   "Enter any additional order notes..."

    )

withaction_ta = WithActions("tawa",
                            "Order notes",
                   "Enter any additional order notes..."

    )

endpoint = oj.create_endpoint("textareas",
                              childs = [oj.HCCMutable.Container(childs = [simple_ta,
                                                                          actioncontained_ta,
                                                                          withaction_ta
                                                                          ],
                                                                twsty_tags=[mr/x/auto, space/y/8]
                                                                )
                                        ],

                              title="Textareas"

                   )
oj.add_jproute("/", endpoint)
