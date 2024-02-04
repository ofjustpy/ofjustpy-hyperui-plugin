from py_tailwind_utils import *

import ofjustpy as oj
oj.set_style("un")

from ofjustpy import icons
from py_tailwind_utils import *
from ofjustpy import icons

app = oj.load_app()
from hyperui_plugin.ecom.collection_filters import  (InlineDropdown,
                                                     StackedDropdown
                                                     )

cf_1 = InlineDropdown()
cf_2 = StackedDropdown()

endpoint = oj.create_endpoint("demo_collection_filters",
                              childs = [cf_1,
                                        cf_2],
                              title="Collection Filters"
                              )
oj.add_jproute("/", endpoint)
