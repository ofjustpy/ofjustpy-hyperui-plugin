from py_tailwind_utils import *

import ofjustpy as oj
oj.set_style("un")

from ofjustpy import icons
from py_tailwind_utils import *
from ofjustpy import icons
from hyperui_plugin.stats import  (Simple,
                                   IconStat,
                                   SimpleWithStat
                                   )

stats_type_1 = Simple()
stats_type_2 = IconStat()
stats_type_3 = SimpleWithStat()


content=[stats_type_1, stats_type_2, stats_type_3]
app= oj.load_app()
endpoint = oj.create_endpoint("Stats",
                              childs = [oj.HCCMutable.Container(childs = content

                                                                          )
                                        ],
                              title="Stats"
                              )
oj.add_jproute("/", endpoint)
