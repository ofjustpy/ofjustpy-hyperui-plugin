from py_tailwind_utils import *

import ofjustpy as oj
oj.set_style("un")

from ofjustpy import icons
from py_tailwind_utils import *
from ofjustpy import icons
from hyperui_plugin.marketing.footers import  (CenteredWithBranding
                                          )

app = oj.load_app()
footer_1 = CenteredWithBranding()
                                            
endpoint = oj.create_endpoint("footers",
                              childs = [oj.HCCMutable.Container(childs = [footer_1
                                                                          ],
                                                                twsty_tags=[mr/x/auto, space/y/8]
                                                                )
                                        ],

                              title="Footers"

                   )
oj.add_jproute("/", endpoint)
