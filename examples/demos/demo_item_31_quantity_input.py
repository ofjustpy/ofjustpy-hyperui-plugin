

import ofjustpy as oj
oj.set_style("un")
app = oj.load_app()
from hyperui_plugin.ecom.quantity_input import  (Simple,
                                                 Contained,
                                                )

simple_qinp = Simple("simple")
contained_quinp = Contained("contained")


endpoint = oj.create_endpoint("quantity_input",
                              childs = [simple_qinp,
                                        contained_quinp

                                        ],
                              title="Quantity Input"
                              )
oj.add_jproute("/", endpoint)

