from py_tailwind_utils import *

import kavya as kv
kv.set_style("un")

from py_tailwind_utils import *


from hyperui_plugin.tables import  (Simple,
                                    SimpleWithBorder
                                    )
app = kv.load_app()
simple_table = Simple()

# Add header
header = simple_table.add_header()
header.add_cell("Name")
header.add_cell("Date of Birth")
header.add_cell("Role")
header.add_cell("Salary")

# Add rows
row1 = simple_table.add_row()
row1.add_cell("John Doe")
row1.add_cell("24/05/1995")
row1.add_cell("Web Developer")
row1.add_cell("$120,000")

row2 = simple_table.add_row()
row2.add_cell("Jane Doe")
row2.add_cell("04/11/1980")
row2.add_cell("Web Designer")
row2.add_cell("$100,000")

row3 = simple_table.add_row()
row3.add_cell("Gary Barlow")
row3.add_cell("24/05/1995")
row3.add_cell("Singer")
row3.add_cell("$20,000")


simpleWithBorder_table = SimpleWithBorder()

# Add header
header = simpleWithBorder_table.add_header()
header.add_cell("Name")
header.add_cell("Date of Birth")
header.add_cell("Role")
header.add_cell("Salary")

# Add rows
row1 = simpleWithBorder_table.add_row()
row1.add_cell("John Doe")
row1.add_cell("24/05/1995")
row1.add_cell("Web Developer")
row1.add_cell("$120,000")

row2 = simpleWithBorder_table.add_row()
row2.add_cell("Jane Doe")
row2.add_cell("04/11/1980")
row2.add_cell("Web Designer")
row2.add_cell("$100,000")

row3 = simpleWithBorder_table.add_row()
row3.add_cell("Gary Barlow")
row3.add_cell("24/05/1995")
row3.add_cell("Singer")
row3.add_cell("$20,000")

endpoint = kv.create_endpoint("demo_tables",
                              childs = [kv.PD.Container(childs = [simple_table,
                                                                          simpleWithBorder_table
                                                                          ],
                                                                twsty_tags=[space/y/16]
                                                                )
                                        ],
                              title="Demo tables",
                              )
kv.add_route("/", endpoint)

