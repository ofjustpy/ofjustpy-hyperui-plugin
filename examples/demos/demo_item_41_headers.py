from py_tailwind_utils import *

import ofjustpy as oj
oj.set_style("un")

from ofjustpy import icons
from py_tailwind_utils import *
from ofjustpy import icons
from hyperui_plugin.marketing.headers import  (LeftAligned
                                          )

app = oj.load_app()
header_1 = LeftAligned()
                                            
endpoint = oj.create_endpoint("headers",
                              childs = [oj.HCCMutable.Container(childs = [header_1
                                                                          ],
                                                                twsty_tags=[mr/x/auto, space/y/8]
                                                                )
                                        ],

                              title="Headers"

                   )
oj.add_jproute("/", endpoint)
