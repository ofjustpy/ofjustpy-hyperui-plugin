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

# ============================ login forms ===========================

from hyperui_plugin.login_forms import  (SplitWithGraphic,
                                         SplitWithContent
                                         )


login_form_type1 = SplitWithGraphic("login_form")
login_form_type2 = SplitWithContent()
content=[kv.PD.Halign(login_form_type1),
         kv.PD.Halign(login_form_type2),
         ]
loginforms_box = kv.HS.StackV(key="LoginForms", childs=content, twsty_tags=[space/y/4])
# ================================ end ===============================

# =========================== media alerts ===========================
from hyperui_plugin.media_alert import  (card)
def cards():
    for _ in ["top", "center", "bottom", "stretch"]:
        yield card(title="Title goes here",
                    text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptates voluptas distinctio nesciunt quas non animi.",
                    img_src = "https://images.unsplash.com/photo-1633332755192-727a05c4013d?q=80&w=2680&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
             align=_
                    )

        yield card(title="Title goes here",
                    text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptates voluptas distinctio nesciunt quas non animi.",
                    img_src = "https://images.unsplash.com/photo-1633332755192-727a05c4013d?q=80&w=2680&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
             align=f"{_}-right"
                    )
content=[kv.PD.Halign(_) for _ in cards()]
mediaalerts_box = kv.HS.StackV(key="MediaAlerts",
                                      childs=content,
                                      twsty_tags=[space/y/8]
                                      )
# ================================ end ===============================

# ============================ pagination ============================
from hyperui_plugin.pagination import  (WithButtons, WithInput, BackgroundWithInput, WithFraction)
pg_nav_buttons = WithButtons("pagination_nav_bar", [4, 5, 6, 8])

pg_nav_input = WithInput("pagination_nav_input")

pg_nav_bginput = BackgroundWithInput("pagination_nav_bginput")

pg_nav_fraction = WithFraction("pagination_nav_fraction")
content = [kv.PD.Halign(pg_nav_buttons),
           kv.PD.Halign(pg_nav_input),
           kv.PD.Halign(pg_nav_bginput),
           kv.PD.Halign(pg_nav_fraction)
           ]

pagination_box = kv.HS.StackV(key="Pagination",
                                      childs=content,
                                      twsty_tags=[space/y/8]
                                      )
# ================================ end ===============================
# ============================== selects =============================
from hyperui_plugin.selects import  (Base, BaseGroup, Datalist)

base_select = Base("base", "Headline")
base_select.add_option("JM", "John Mayer")
base_select.add_option("SRV", "Stevie Ray Vaughn")
base_select.add_option("JH", "Jimi Hendrix")
base_select.add_option("BBK", "B.B King")
base_select.add_option("AK", "Albert King")
base_select.add_option("BG", "Buddy Guy")
base_select.add_option("EC", "Eric Clapton")


basegroup_select = BaseGroup("basegroup", "Headline")
optgroup = basegroup_select.add_optgroup("A")
optgroup.add_option("AK", "Albert King")

optgroup = basegroup_select.add_optgroup("B")
optgroup.add_option("BBK", "B.B King")
optgroup.add_option("BG", "Buddy Guy")


optgroup = basegroup_select.add_optgroup("E")
optgroup.add_option("EC", "Eric Clapton")


optgroup = basegroup_select.add_optgroup("J")
optgroup.add_option("JM", "John Mayer")
optgroup.add_option("JH", "Jimi Hendrix")

optgroup = basegroup_select.add_optgroup("S")
optgroup.add_option("SRV", "Stevie Ray Vaughn")


datalist_select = Datalist("base", "Headline")
datalist_select.add_option("JM", "John Mayer")
datalist_select.add_option("SRV", "Stevie Ray Vaughn")
datalist_select.add_option("JH", "Jimi Hendrix")
datalist_select.add_option("BBK", "B.B King")
datalist_select.add_option("AK", "Albert King")
datalist_select.add_option("BG", "Buddy Guy")
datalist_select.add_option("EC", "Eric Clapton")



content = [base_select,
                                                                        basegroup_select,
                                                                        datalist_select
                                                                        ]
selects_box = kv.HS.StackV(key="Selects",
                                      childs=content,
                                      twsty_tags=[space/y/8]
                                      )
# ================================ end ===============================
