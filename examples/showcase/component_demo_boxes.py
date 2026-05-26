from hyperui_plugin.alerts import (Popup, PopupWithAction, Content, WarningContent)
import kavya as kv

from py_tailwind_utils import *

# ============================== popups ==============================
alert_popup = Popup("popup_alert", title='Your product changes have been saved.', desc='Changes saved')

alert_popupaction = PopupWithAction("popup_alertaction", title='Your product changes have been saved.', desc='Changes saved')

alert_content = Content('Something went wrong',
                        'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nemo quasi assumenda numquam deserunt consectetur autem nihil quos debitis dolor culpa.')

alert_warning_content = WarningContent('Something went wrong',
                        'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nemo quasi assumenda numquam deserunt consectetur autem nihil quos debitis dolor culpa.'
                                       )

alert_box = kv.HS.Div(key="Alerts", childs=[alert_popup,
                                                          alert_popupaction,
                                                          alert_content,
                                                          alert_warning_content
                                                          ], twsty_tags=[space/y/4])



# ============================== badges ==============================
from hyperui_plugin.badges import Badge

simple_badge = Badge("Live")
icon_badge = Badge( icon = kv.PC.FontAwesomeIcon(label="faEuroSign",
                                                 size="1x",
                                                 fixedWidth=True,
                                                 classes="w-5 h-5",
                                                 )
                   )
icon_label_badge = Badge(label = "hello", icon = kv.PC.FontAwesomeIcon(label="faEuroSign",
                                                                       size="1x",
                                                                       fixedWidth=True,
                                                                       classes="w-5 h-5",),
                         
                         )

label_badge_crossbtn = Badge(label = "hello")
def on_click(dbref, msg, to_ms):
    print ("btn clicked")
    pass
label_badge_crossbtn.add_cross_btn("abtn", on_click=on_click)
badges_box = kv.HS.StackV(key="Badges", childs=[kv.PD.Halign(_) for _ in [simple_badge,
                                                                          icon_badge,
                                                                          icon_label_badge,
                                                                          label_badge_crossbtn ]
                                                ],
                          twsty_tags=[space/y/4]
                          )

# ================================ end ===============================

# ============================ breadcrumbs ===========================
from hyperui_plugin.breadcrumbs import  (Simple,
                                         ChevronBackground)


breadcrumbs_component = Simple()
breadcrumbs_component.add_item("Shirt")
breadcrumbs_component.add_item("Plain Tee")


chevrobackground_breadcrumbs_component = ChevronBackground()
chevrobackground_breadcrumbs_component.add_item("Shirt")
chevrobackground_breadcrumbs_component.add_item("Plain Tee")
breadcrumbs_box = kv.HS.StackV(key="Breadcrumbs",
                               childs=[kv.PD.Halign(_) for _ in [breadcrumbs_component,
                                                                 chevrobackground_breadcrumbs_component
                                                                 ]
                                       ],
             twsty_tags=[space/y/4]
             )

# =========================== buttongroups ===========================

from hyperui_plugin import buttongroups
btn_container = buttongroups.Simple()
btn_container.add_button(key="abtn", text="Click me")
btn_container.add_button(key="bbtn", text="Click me 2")
btn_container.add_button(key="cbtn", text="Click me 3")

btn_container_icon =  buttongroups.WithIcons()

btn_container_icon.add_button("iabtn",
                              "Edit",
                              kv.PC.FontAwesomeIcon(label="faEdit", mdi_label='note-edit', classes="w-5 h-5")

                              )
btn_container_icon.add_button("ibbtn", "View", kv.PC.FontAwesomeIcon(label="faEye", classes="w-5 h-5")
                              )
btn_container_icon.add_button("icbtn", "Delete", kv.PC.FontAwesomeIcon(label="faTrash", classes="w-5 h-5")
                              )


buttongroups_box = kv.HS.StackV(key="Buttongroups", childs = [kv.PD.Halign(btn_container),
                                                                     kv.PD.Halign(btn_container_icon)],
                                       twsty_tags=[space/y/4]
                                       )

# ================================ end ===============================


# ============================ detailslist ===========================
from hyperui_plugin.detailslist import Detailslist

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

detailslist_box = kv.PD.StackV(key="Detailslist",
                                      childs = [kv.PD.Halign(list_container, twsty_tags=[bg/white]),
                                                kv.PD.Halign(list_container_striped, twsty_tags=[bg/white]),
                                                kv.PD.Halign(list_container_contained, twsty_tags=[bg/white]),
                                                kv.PD.Halign(list_container_contained_striped, twsty_tags=[bg/white])
                                                ],
                   twsty_tags=[space/y/4]
             )

# ================================ end ===============================

# ============================= dividers =============================
from hyperui_plugin import dividers
more_divider = dividers.More(text="Lorem, ipsum dolor")
blurry_divider = dividers.Blurry(text="Lorem, ipsum dolor")
left_align_divider = dividers.AlignLeft(text="Lorem, ipsum dolor")
right_align_divider = dividers.AlignLeft(text="Lorem, ipsum dolor")

content = [kv.PD.Halign(_) for _ in [more_divider, blurry_divider, left_align_divider, right_align_divider
                                     ]
           ]
dividers_box = kv.HS.StackV(key="Dividers", childs=content, twsty_tags=[space/y/4])

# ================================ end ===============================

# ============================== dropdow =============================
#TBD
# ================================ end ===============================

# ============================ errorpages ============================
from hyperui_plugin import errorpages

notfoundpage = errorpages.NotFoundPage()
error404page = errorpages.Error404Page()
notFoundPageWithImage = errorpages.NotFoundPageWithImage()
content = [notfoundpage, error404page, notFoundPageWithImage
           ]
errorpages_box = kv.HS.StackV(key="Errorpages", childs=content, twsty_tags=[space/y/4])

# ================================ end ===============================

# ============================== inputs =============================
from hyperui_plugin.inputs import  (Simple  as SimpleInput,
                                              WithIcon,
                                              SearchInputWithButton,
                                              WithLabel,
                                              FloatingLabel,
                                    FloatingLabelInside,
                                    FloatingLabelUnderline)

ainp = SimpleInput("inp1", "Email", "san@me.com")
ainp2 = WithIcon("inp2", "Email", "san@me.com")
ainp3 = SearchInputWithButton("inp2", "Email", "san@me.com")
ainp4 = WithLabel("inp4", "Email", "san@me.com")
ainp5 = FloatingLabel("inp5", "Email", "san@me.com")
ainp6 = FloatingLabelInside("inp6", "Email", "san@me.com")
ainp7 = FloatingLabelUnderline("inp7", "Email", "san@me.com")

content = [kv.PD.Halign(ainp),
                                                                kv.PD.Halign(ainp2),
                                                                kv.PD.Halign(ainp3),
                                                                kv.PD.Halign(ainp4),
                                                                kv.PD.Halign(ainp5),
                                                                kv.PD.Halign(ainp6),
                                                                kv.PD.Halign(ainp7),]
inputs_box = kv.HS.StackV(key="Inputs", childs=content, twsty_tags=[space/y/4])
# ================================ end ===============================

