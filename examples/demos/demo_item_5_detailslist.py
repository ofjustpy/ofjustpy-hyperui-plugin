from py_tailwind_utils import *
import ofjustpy as oj
oj.set_style("un")
from hyperui_plugin.detailslist import Detailslist
from ofjustpy import icons
from py_tailwind_utils import *
from ofjustpy import icons
list_container = Detailslist()
list_container.add_item("Title", "Mr")
list_container.add_item("Name", "John Frusciante")
list_container.add_item("Occupation", "Guitarist")
list_container.add_item("Salary", "$1,000,000+")
list_container.add_item("Bio", "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Et facilis debitis explicabo doloremque impedit nesciunt dolorem facere, dolor quasi veritatis quia fugit aperiam aspernatur neque molestiae labore aliquam soluta architecto? ")


list_container_striped = Detailslist(striped=True)
list_container_striped.add_item("Title", "Mr")
list_container_striped.add_item("Name", "John Frusciante")
list_container_striped.add_item("Occupation", "Guitarist")
list_container_striped.add_item("Salary", "$1,000,000+")
list_container_striped.add_item("Bio", "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Et facilis debitis explicabo doloremque impedit nesciunt dolorem facere, dolor quasi veritatis quia fugit aperiam aspernatur neque molestiae labore aliquam soluta architecto? ")


list_container_contained = Detailslist(contained=True)
list_container_contained.add_item("Title", "Mr")
list_container_contained.add_item("Name", "John Frusciante")
list_container_contained.add_item("Occupation", "Guitarist")
list_container_contained.add_item("Salary", "$1,000,000+")
list_container_contained.add_item("Bio", "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Et facilis debitis explicabo doloremque impedit nesciunt dolorem facere, dolor quasi veritatis quia fugit aperiam aspernatur neque molestiae labore aliquam soluta architecto? ")


list_container_contained_striped = Detailslist(contained=True, striped=True)
list_container_contained_striped.add_item("Title", "Mr")
list_container_contained_striped.add_item("Name", "John Frusciante")
list_container_contained_striped.add_item("Occupation", "Guitarist")
list_container_contained_striped.add_item("Salary", "$1,000,000+")
list_container_contained_striped.add_item("Bio", "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Et facilis debitis explicabo doloremque impedit nesciunt dolorem facere, dolor quasi veritatis quia fugit aperiam aspernatur neque molestiae labore aliquam soluta architecto? ")


# list_container_striped, key_value_adder = Detailslist(striped=True)
# key_value_adder("Title", "Mr")
# key_value_adder("Name", "John Frusciante")
# key_value_adder("Occupation", "Guitarist")
# key_value_adder("Salary", "$1,000,000+")
# key_value_adder("Bio", "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Et facilis debitis explicabo doloremque impedit nesciunt dolorem facere, dolor quasi veritatis quia fugit aperiam aspernatur neque molestiae labore aliquam soluta architecto? ")




# list_container_contained, key_value_adder = Detailslist(contained=True)
# key_value_adder("Title", "Mr")
# key_value_adder("Name", "John Frusciante")
# key_value_adder("Occupation", "Guitarist")
# key_value_adder("Salary", "$1,000,000+")
# key_value_adder("Bio", "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Et facilis debitis explicabo doloremque impedit nesciunt dolorem facere, dolor quasi veritatis quia fugit aperiam aspernatur neque molestiae labore aliquam soluta architecto? ")


# list_container_striped_contained, key_value_adder = Detailslist(contained=True, striped=True)
# key_value_adder("Title", "Mr")
# key_value_adder("Name", "John Frusciante")
# key_value_adder("Occupation", "Guitarist")
# key_value_adder("Salary", "$1,000,000+")
# key_value_adder("Bio", "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Et facilis debitis explicabo doloremque impedit nesciunt dolorem facere, dolor quasi veritatis quia fugit aperiam aspernatur neque molestiae labore aliquam soluta architecto? ")


tlc = oj.PC.Container(childs = [oj.PC.StackV(childs = [oj.PC.Halign(list_container, twsty_tags=[bg/white]),
                                                       oj.PC.Halign(list_container_striped, twsty_tags=[bg/white]),
                                                       oj.PC.Halign(list_container_contained, twsty_tags=[bg/white]),
                                                       oj.PC.Halign(list_container_contained_striped, twsty_tags=[bg/white])
                                                       ],
                                             twsty_tags=[space/y/16]
                                             )],
                      twsty_tags=[mr/x/auto, bg/pink/"100/50"]
                      )


app = oj.load_app()
endpoint = oj.create_endpoint("demo_button_group",
                              childs = [tlc
                                        ]
                   )
oj.add_jproute("/", endpoint)
