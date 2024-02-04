from py_tailwind_utils import *

import ofjustpy as oj
oj.set_style("un")

from ofjustpy import icons
from py_tailwind_utils import *
from ofjustpy import icons
from hyperui_plugin.marketing.forms import  (Login,
                                            
                                          )

app = oj.load_app()
form_1 = Login()



endpoint = oj.create_endpoint("footers",
                              childs = [oj.HCCMutable.Container(childs = [form_1,
                                                                          
                                                                          ],
                                                                twsty_tags=[mr/x/auto, space/y/8]
                                                                )
                                        ],

                              title="Footers"

                   )
oj.add_jproute("/", endpoint)
