
import kavya as kv
from kavya.dsl import macros, MuCtx
from py_tailwind_utils import *

# ======================== Expression helpers ========================
class LMapInitiator:
    def __init__(self) -> None:
        pass
    def __or__(self, iterable):
        return LMapRunner(iterable)

class LMapRunner:
    def __init__(self, iterable):
        self.iterable = iterable

    def __or__(self, func):
        # let the terminal func handle the self.iterable
        if hasattr(func, '__ror__'):
            return func.__ror__(self.iterable)
        
        if not callable(func):
            raise TypeError("The next item in the LMap chain must be a callable function.")
        
        # Update the internal iterable in-place with a lazy generator
        self.iterable = (func(item) for item in self.iterable)
        
        # Return the EXACT SAME instance
        return self

    def __iter__(self):
        # Yield items out one by one when iterated
        for item in self.iterable:
            yield item
        
        # Break reference immediately after exhaustion to free memory
        self.iterable = None

LMap = LMapInitiator()

class ToList:
    @classmethod
    def __ror__(cls, other):
        # 'other' will be the LMapRunner instance passed from the left
        return list(other)
    




# class LMapInitiator:
#     def __or__(self, iterable):
#         # Spawns a temporary runner for this specific operation.
#         # 'LMap' itself stays completely untouched and clean.
#         return LMapRunner(iterable)

# class LMapRunner:
#     def __init__(self, iterable):
#         self.iterable = iterable

#     def __or__(self, func):
#         if not callable(func):
#             raise TypeError("The final item in the LMap chain must be a callable function.")
        
#         # 1. Compute the result
#         result = [func(item) for item in self.iterable]
        
#         # 2. Explicitly break references to the input data to free memory immediately
#         self.iterable = None 
        
#         # 3. Return the native list
#         return result

# The single global instance






# ================================ end ===============================


# ============================== popups ==============================
from hyperui_plugin.alerts import (Popup, PopupWithAction, Content, WarningContent)
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

# ============================= sideMenu =============================
from hyperui_plugin.sideMenu import  (Simple
                                          )

simple_sideMenu = Simple("Wiki Items")
simple_sideMenu.add_flat_item("general", "General")
simple_sideMenu.add_flat_item("more_things","More things")
teams = simple_sideMenu.add_group_item("Teams")
teams.add_flat_item("banned_users", "Banned Users")
teams.add_flat_item("calender", "Calender")


textbox = kv.PC.Prose(text="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ullamcorper accumsan lacus, a condimentum orci auctor ut. Quisque et volutpat elit. Vestibulum id velit vel augue suscipit ultricies. Aenean ultricies, libero eu dignissim interdum, eros dui cursus neque, at feugiat dolor nulla nec arcu. Nam vehicula justo in tincidunt tincidunt. Vivamus accumsan urna ut fringilla commodo. Nulla facilisi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Suspendisse eu tincidunt orci.
Curabitur sed consequat dolor. Nullam eget urna nec nulla sodales posuere. Mauris id metus non ligula venenatis malesuada in id metus. Fusce eu urna ac justo consectetur venenatis vel sit amet libero. Sed euismod nisl vel mi ultrices, at cursus mauris volutpat. Quisque a libero felis. Curabitur laoreet, libero vel scelerisque suscipit, metus est bibendum arcu, id dapibus odio arcu nec libero. Integer convallis eget purus vel luctus. Nulla facilisi. Sed pharetra vel urna vel tempor. Integer et felis sed metus ullamcorper laoreet.

Praesent vel consectetur justo, vel blandit arcu. Vivamus cursus, libero eu tincidunt aliquet, arcu metus commodo justo, eget ultricies ligula lectus vitae lacus. Proin gravida nec metus ut rhoncus. Ut sit amet erat sit amet mi tempor rhoncus eget at neque. Integer sit amet turpis id neque bibendum cursus. Fusce quis enim euismod, suscipit justo vel, commodo mauris. Sed convallis tellus sed risus finibus efficitur. Vivamus vel elit nec odio accumsan cursus eu vel tortor. Vivamus dapibus sem id sapien dignissim cursus.

Quisque eget fermentum tortor, et congue justo. Aliquam erat volutpat. Duis malesuada eleifend orci, in vestibulum lacus suscipit et. Sed interdum laoreet nisi, at ultrices justo auctor at. Integer laoreet felis ut odio euismod eleifend. Vestibulum a feugiat elit. Integer nec fermentum mauris. Fusce bibendum, risus et malesuada ultricies, velit lacus tincidunt odio, id bibendum eros justo vel nisi. Vestibulum auctor dolor vitae sapien bibendum, in sagittis erat ultricies.

Donec eu velit quis nisi pharetra hendrerit. Nullam hendrerit auctor nisi, a euismod orci gravida nec. Proin tincidunt arcu in ligula fermentum, ut pellentesque ex efficitur. Quisque ut metus ac justo bibendum cursus nec sit amet velit. Integer vestibulum augue ut bibendum sagittis. Fusce non dapibus elit. Integer vel arcu ac quam malesuada sagittis. In hac habitasse platea dictumst. Integer elementum, erat id fermentum consequat, lacus velit rhoncus elit, eget sodales turpis elit eu ligula. Nulla facilisi.

Nam vel ullamcorper ligula. Ut suscipit bibendum turpis, vitae vestibulum mi sagittis vel. Curabitur a leo vel est ullamcorper luctus. Nunc sit amet fermentum nulla. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nulla facilisi. Fusce tristique justo et est fermentum, in ullamcorper libero fringilla. Suspendisse potenti. Quisque vel ante nec mi tincidunt eleifend. Vivamus laoreet turpis ac nisi finibus, id efficitur quam egestas. Integer vel tellus urna. Curabitur ut purus vel tellus gravida sodales.""", twsty_tags=[W/"2/3"])

sideMenu_type1 = kv.PD.StackH(childs = [simple_sideMenu, textbox])
sideMenu_box = kv.HS.StackV(key="SideMenu",
                                      childs=[sideMenu_type1],
                                      twsty_tags=[space/y/8]
                                      )

# ================================ end ===============================
# =============================== stats ==============================
from hyperui_plugin.stats import  (Simple,
                                   IconStat,
                                   SimpleWithStat
                                   )

stats_type_1 = Simple()
stats_type_2 = IconStat()
stats_type_3 = SimpleWithStat()
content=[stats_type_1, stats_type_2, stats_type_3]
stats_box = kv.HS.StackV(key="Stats",
                                      childs=content,
                                      twsty_tags=[space/y/8]
                                      )
# ================================ end ===============================
# =============================== steps ==============================
from hyperui_plugin.steps import  (WithTextAndIcon,
                                   WithCheckIcons,
                                   WithChevronTextIcon
                                   
                                   )

steps_type_1, abtn = WithTextAndIcon("pg_1")
steps_type_2 = WithCheckIcons("pg_2")
steps_type_3 = WithChevronTextIcon()

content=[kv.HM.Div(childs=[kv.HM.Halign(steps_type_1),
                                   kv.PD.Halign(abtn)], twsty_tags=[space/y/4]),
         kv.PD.Halign(steps_type_2),
         kv.PD.Halign(steps_type_3)
         ]
steps_box = kv.MD.StackV(key="Steps",
                                      childs=content,
                                      twsty_tags=[space/y/8]
                                      )

# ================================ end ===============================

# ============================== tables ==============================
from hyperui_plugin.tables import  (Simple,
                                    SimpleWithBorder
                                          )
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

content= [kv.PD.Halign(simple_table),
          kv.PD.Halign(simpleWithBorder_table)
          ]
tables_box = kv.HS.StackV(key="Tables",
                                 childs=content,
                                 twsty_tags=[space/y/8]
                                 )
# ================================ end ===============================

# =============================== tabs ===============================
from hyperui_plugin.tabs import  (Pills,
                                  Tabbed
                                          )
def on_change(dbref, msg, to_ms):

    pass

pills = Pills("pillstab")
pills.add_tab("settings", "Settings")
pills.add_tab("messages", "Messages")
pills.add_tab("archive", "Archive")
pills.add_tab("notifications", "Notifications", selected=True)

tabbed = Tabbed("tabbed")
tabbed.add_tab("settings", "Settings")
tabbed.add_tab("messages", "Messages")
tabbed.add_tab("archive", "Archive")
tabbed.add_tab("notifications", "Notifications", selected=True)

content=[kv.PD.Halign(pills),
         kv.PD.Halign(tabbed)
         ]
# Tabs are mutable -- eventullay
tabs_box = kv.MD.StackV(key="Tabs",
                        childs=content,
                        twsty_tags=[space/y/8]
                        )
# ================================ end ===============================
# ============================= textareas ============================
from hyperui_plugin.textareas import  (Simple,
                                       ActionContained,
                                       WithActions
                                          )

simple_ta = Simple("tbtn",
                   "Order notes",
                   "Enter any additional order notes...")

actioncontained_ta = ActionContained("tbtn",
                                     "Order notes",
                   "Enter any additional order notes..."

    )

withaction_ta = WithActions("tawa",
                            "Order notes",
                   "Enter any additional order notes..."

    )
content = [simple_ta,
           actioncontained_ta,
           withaction_ta
           ]

textarea_box = kv.HS.StackV(key="Textarea",
                                 childs=content,
                                 twsty_tags=[space/y/8]
                                 )
# ================================ end ===============================
# ============================== toggles =============================
from hyperui_plugin.toggles import  (Simple,
                                     Apple,
                                     Material,
                                     #SimpleWithIcon
                                          )

simple_togglebtn = Simple(key="stbtn")
apple_togglebtn = Apple(key="atbtn")
material_togglebtn = Material(key="mtbtn")
#simpleicon_togglebtn = SimpleWithIcon(key="sitbtn")

# content = [kv.PD.Halign(simple_togglebtn),
#            kv.PD.Halign(material_togglebtn),
#            kv.PD.Halign(apple_togglebtn),
#            #simpleicon_togglebtn
#            ]

content = LMap | [ simple_togglebtn,
                     material_togglebtn,
                     apple_togglebtn

                    ] | kv.PD.Halign  | ToList
toggles_box = kv.MD.StackV(key="Toggles",
                                      childs=content,
                                      twsty_tags=[space/y/8]
                                      )

# ================================ end ===============================

# =========================== vertical menu ==========================
from hyperui_plugin.verticalmenu import  (Simple,
                                          WithBadge,
                                          WithIcon,
                                          WithIconAndBadge,
                                          WithIconAndBrandedAccent,
                                          menugroups,
                                          SplitWithHeading
                                          )

container = Simple(twsty_tags=[W/32])
container.add_item("General")
container.add_item("Teams")
container.add_item("Billing")

badge_container = WithBadge(twsty_tags=[W/32])
badge_container.add_item("General")
badge_container.add_item("Teams", badge="6")
badge_container.add_item("Billing")
badge_container.add_item("Invoices", badge="3")

mg_container = menugroups(twsty_tags=[W/64])
agroup = mg_container.add_group()
agroup.add_item("Profile")
agroup.add_item("Team")
agroup.add_item("Projects")
agroup = mg_container.add_group()
agroup.add_item("Update")
agroup.add_item("Help")
agroup.add_item("Settings")
agroup = mg_container.add_group()
agroup.add_item("Logout")

splitWithHeading = SplitWithHeading()
group= splitWithHeading.add_group("General")
group.add_item("Profile")
group.add_item("Team")
group.add_item("Projects")
group.add_item("Meeting")
group.add_item("Calender")

group= splitWithHeading.add_group("Support")
group.add_item("Update")
group.add_item("Help")
group.add_item("Settings")

group= splitWithHeading.add_group("Profile")
group.add_item("Details")
group.add_item("Subscription")
group.add_item("Logout")

content = LMap | [ container,
                   badge_container,
                   mg_container,
                   splitWithHeading

                    ] | kv.PD.Halign | ToList


verticalmenu_box = kv.HS.StackV(key="VerticalMenu",
                                 childs=content,
                                 twsty_tags=[space/y/8]
                                 )

# ============================ ecom/carts ============================
from hyperui_plugin.ecom.carts import  (BottomBanner, Popup,
                                        Contained
                                          )
bb_container = BottomBanner()
bb_container.add_item("view_cart", "View My Cart", href="", styling="outline")
bb_container.add_item("checkout", "Checkout", href="", styling="solid")
bb_container.add_item("continueShopping", "Continue Shopping", href="", styling="underline")

popup_cart = Popup(bb_container)

with MuCtx:
    with Dl(classes="mt-0.5 space-y-px text-xs text-gray-600") as card_body:
        with Div:
            with Dt(twsty_tags=[db.i], text="Size:"):
                pass
            with Dd(twsty_tags=[db.i], text="XXS"):
                pass

        with Div:
            with Dt(twsty_tags=[db.i], text="Color:"):
                pass
            with Dd(twsty_tags=[db.i], text="White"):
                pass
            

            
    
popup_cart.add_item(img_src="https://images.unsplash.com/photo-1618354691373-d851c5c3a990?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=830&q=80",
                    desc_title="Basic Tee 6-Pack",
                    
                    desc_box=card_body
                    )

popup_cart.add_item(img_src="https://images.unsplash.com/photo-1618354691373-d851c5c3a990?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=830&q=80",
                    desc_title="Basic Tee 6-Pack",
                    
                    desc_box=card_body
                    )

popup_cart.add_item(img_src="https://images.unsplash.com/photo-1618354691373-d851c5c3a990?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=830&q=80",
                    desc_title="Basic Tee 6-Pack",
                    
                    desc_box=card_body
                    )

content = LMap | [ popup_cart,
                   Contained()

                    ] | kv.PD.Halign | ToList

ecomcarts_box = kv.HS.StackV(key="EcomCarts",
                             childs=content,
                             twsty_tags=[space/y/8]
                             )
# ================================ end ===============================

# ======================== collection filters ========================
from hyperui_plugin.ecom.collection_filters import  (InlineDropdown,
                                                     StackedDropdown
                                                     )

cf_1 = InlineDropdown()
cf_2 = StackedDropdown()
content = LMap | [ cf_1, 
                   cf_2

                    ] | kv.PD.Halign | ToList
ecomcollectionfilters_box = kv.HS.StackV(key="EcomCollectionFilters",
                                 childs=content,
                                 twsty_tags=[space/y/8]
                                 )
# ================================ end ===============================

# ========================= featuredsections =========================
from hyperui_plugin.ecom.featured_sections import  (WithProducts,
                                                    CollectionGrid
                                          )

collection_with_products = WithProducts("Watches", "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Quas rerum quam amet provident nulla error!", "Shop All", )

collection_with_products.add_product("https://images.unsplash.com/photo-1523275335684-37898b6baf30?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1598&q=80", "Simple Watch", "$150")

collection_with_products.add_product("https://images.unsplash.com/photo-1523275335684-37898b6baf30?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1598&q=80", "Simple Watch", "$150")

collection_with_products.add_product("https://images.unsplash.com/photo-1523275335684-37898b6baf30?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1598&q=80", "Simple Watch", "$150")


collection_grid = CollectionGrid("New Collection", "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Itaque praesentium cumque iure dicta incidunt est ipsam, officia dolor fugit natus?")
collection_grid.add_product("https://images.unsplash.com/photo-1618898909019-010e4e234c55?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80",
                            
                            "Casual Trainers",
                            "Shop Now")
collection_grid.add_product("https://images.unsplash.com/photo-1618898909019-010e4e234c55?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80",
                            
                            "Casual Trainers",
                            "Shop Now")

collection_grid.add_product("https://images.unsplash.com/photo-1618898909019-010e4e234c55?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80",
                            
                            "Casual Trainers",
                            "Shop Now")

content = LMap | [collection_with_products,
                                        collection_grid
                                        ] | kv.PD.Halign | ToList

ecomfeaturedsections_box = kv.HS.StackV(key="EconFeaturedSections",
                                 childs=content,
                                 twsty_tags=[space/y/8]
                                 )
# ================================ end ===============================

# =========================== product cards ==========================
from hyperui_plugin.ecom.product_cards import  (Simple,
                                                WithVariant,
                                                WithDescription,
                                                ContainedWishList
                                          )

card_simple = Simple("https://images.unsplash.com/photo-1523381210434-271e8be1f52b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80",
       "https://images.unsplash.com/photo-1523381140794-a1eef18a37c7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwcm9maWxlLXBhZ2V8MjQ2fHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=800&q=60",
       "Limited Edition Sports Trainer",
       "$189.99"
       )

img_src = "https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1450&q=80"
img_src_hover = "https://images.unsplash.com/photo-1600185365926-3a2ce3cdb9eb?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1450&q=80"
desc = "Limited Edition Sports Trainer"
sticker = "$189.99"
variant_text = "6 Colors"

card_withVariant = WithVariant(img_src, img_src_hover, desc, sticker, variant_text)

# Example usage:
img_src = "https://images.unsplash.com/photo-1592921870789-04563d55041c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80"
desc = "Small Headphones"
desc_subtitle = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quasi nobis, quia soluta quisquam voluptatem nemo."
price = "$299"

card_withDescription = WithDescription(img_src, desc, desc_subtitle, price)


# Example usage:
img_src = "https://images.unsplash.com/photo-1599481238640-4c1288750d7a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2664&q=80"
product_name = "Robot Toy"
product_price = "$14.99"

card_containedWishList = ContainedWishList("wished_toy", img_src, product_name, product_price)


content = LMap | [card_simple,
           card_withVariant,
           card_withDescription,
           card_containedWishList
           ] | kv.PD.Halign | ToList

ecomproductcards_box = kv.HS.StackV(key="EcomProductCards",
                                 childs=content,
                                 twsty_tags=[space/y/8]
                                 )
# ================================ end ===============================

# ======================== product collection ========================
from hyperui_plugin.ecom.product_collection import  (Simple,
                                                )

simple_collection = Simple("Product Collection", "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Itaque praesentium cumque iure dicta incidunt est ipsam, officia dolor fugit natus?")

# Example usage:
img_src = "https://images.unsplash.com/photo-1523381210434-271e8be1f52b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80"
product_name = "Basic Tee"

regular_price = "\u00a324.00 GBP"
simple_collection.add_product(img_src, product_name, regular_price)
simple_collection.add_product(img_src, product_name, regular_price)
simple_collection.add_product(img_src, product_name, regular_price)
simple_collection.add_product(img_src, product_name, regular_price)

content = [simple_collection]
ecomproductcollection_box = kv.HS.StackV(key="EcomProductCollection",
                                 childs=content,
                                 twsty_tags=[space/y/8]
                                 )

# ================================ end ===============================

# ========================== quantity_input ==========================
from hyperui_plugin.ecom.quantity_input import  (Simple,
                                                 Contained
                                                )

simple_qinp = Simple("simple")
contained_quinp = Contained("contained")
content = LMap | [simple_qinp,
           contained_quinp
           ]| kv.PD.Halign | ToList
ecomquantinp_box = kv.HS.StackV(key="EcomQuantInp",
                                 childs=content,
                                 twsty_tags=[space/y/8]
                                 )
# ================================ end ===============================
# =========================== announcements ==========================
from hyperui_plugin.marketing.announcements import  (WithAction,
                                                     BottomWithClose,
                                                     #SwiperSlider
                                                     
                                                     )
with_action = WithAction()
bottom_close = BottomWithClose()
content = LMap | [with_action,
                  bottom_close,
                  ] | kv.PD.Halign | ToList

marketingannouncements_box = kv.HS.StackV(key="MarketingAnnouncements",
                                 childs=content,
                                 twsty_tags=[space/y/8]
                                 )
# ================================ end ===============================

# ============================== banners =============================
from hyperui_plugin.marketing.banners import  (CenteredWithAction,
                                               CenteredWithActionGradient
                                                )


title = "Understand User Flow."
sub_title = "Increase Conversion."
description = "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nesciunt illo tenetur fuga ducimus numquam ea!"
button1_text = "Get Started"
button1_link = "/get-started"
button2_text = "Learn More"
button2_link = "/about"

banner_centeredWithAction = CenteredWithAction(title, sub_title, description, button1_text, button1_link, button2_text, button2_link)

# Example usage:
title = "Understand User Flow."
sub_title = "Increase Conversion."
description = "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nesciunt illo tenetur fuga ducimus numquam ea!"
button1_text = "Get Started"
button1_link = "/get-started"
button2_text = "Learn More"
button2_link = "/about"

banner_2 = CenteredWithActionGradient(title, sub_title, description, button1_text, button1_link, button2_text, button2_link)
content = LMap | [banner_centeredWithAction, banner_2] | kv.PD.Halign | ToList
marketingbanner_box = kv.HS.StackV(key="MarketingBanner",
                                 childs=content,
                                 twsty_tags=[space/y/8]
                                 )
# ================================ end ===============================
# ============================ blog cards ============================
from hyperui_plugin.marketing.blog_cards import  (Simple,
                                                  Floating,
                                                  Bordered,
                                                  GradientBorder
                                                  )

# Example usage:
blog_card_simple = Simple(
    image_url="https://images.unsplash.com/photo-1524758631624-e2822e304c36?ixlib=rb-1.2.1&ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2070&q=80",
    date="2022-10-10",
    title="How to position your furniture for positivity",
    content="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Recusandae dolores, possimus pariatur animi temporibus nesciunt praesentium dolore sed nulla ipsum eveniet corporis quidem, mollitia itaque minus soluta, voluptates neque explicabo tempora nisi culpa eius atque dignissimos. Molestias explicabo corporis voluptatem?",
    link="#",
)

# Example usage:
blog_card_floating = Floating(
    image_url="https://images.unsplash.com/photo-1631451095765-2c91616fc9e6?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80",
    alt_text="Lava",
    title="Finding the Journey to Mordor",
    content="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Recusandae dolores, possimus pariatur animi temporibus nesciunt praesentium dolore sed nulla ipsum eveniet corporis quidem, mollitia itaque minus soluta, voluptates neque explicabo tempora nisi culpa eius atque dignissimos. Molestias explicabo corporis voluptatem?",
    link="#",
)

blog_card_bordered = Bordered(
    image_url="https://images.unsplash.com/photo-1600880292203-757bb62b4baf?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80",
    alt_text="Office",
    title="Lorem ipsum dolor sit amet consectetur adipisicing elit.",
    content="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Recusandae dolores, possimus pariatur animi temporibus nesciunt praesentium dolore sed nulla ipsum eveniet corporis quidem, mollitia itaque minus soluta, voluptates neque explicabo tempora nisi culpa eius atque dignissimos. Molestias explicabo corporis voluptatem?",
    link="#",
)

blog_card_gradientBorder = GradientBorder(
    date="2022-10-10",
    title="How to center an element using JavaScript and jQuery",
    tags=["Snippet", "JavaScript"]
)
content = LMap | [blog_card_simple, 
                  blog_card_floating,
                  blog_card_bordered,
                  blog_card_gradientBorder ] | kv.PD.Halign | ToList

marketingblogcards_box = kv.HS.StackV(key="MarketingBlogCards",
                                      childs=content,
                                      twsty_tags=[space/y/8]
                                      )


# ================================ end ===============================
# ============================== buttons =============================
from hyperui_plugin.marketing.buttons import  (Simple_Solid,
                                               Simple_Blank,
                                               GradientBorder,
                                               GradientBorder_Oval,
                                               CurtainClose
                                                )

ss_btn = Simple_Solid("ss", "Download")
sb_btn = Simple_Blank("sb", "Download")

gb_btn = GradientBorder("gb", "Download")
gbo_btn = GradientBorder_Oval("gbo", "Download")

cc_l = CurtainClose("ccl", "Download")
cc_r = CurtainClose("ccl", "Download", "right")
cc_b = CurtainClose("ccl", "Download", "bottom")
cc_t = CurtainClose("ccl", "Download", "top")

content = LMap | [ss_btn,
           sb_btn,
           gb_btn,
           gbo_btn,
           cc_l,
           cc_r,
           cc_b,
           cc_t,
           ] | kv.PD.Halign | ToList
buttons_box = kv.HS.StackV(key="Buttons",
                                 childs=content,
                                 twsty_tags=[space/y/8]
                                 )
# ================================ end ===============================
# ========================== marketing cards =========================
from hyperui_plugin.marketing.cards import  (Card_Type_1,
                                                )

href = "#"
title = "Building a SaaS product as a software developer"
author = "John Doe"
image_src = "https://images.unsplash.com/photo-1633332755192-727a05c4013d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1180&q=80"
content = "Lorem ipsum dolor sit, amet consectetur adipisicing elit. At velit illum provident a, ipsa maiores deleniti consectetur nobis et eaque."
published_date = "31st June, 2021"
reading_time = "3 minutes"

# Generate blog card
card_1 = Card_Type_1(href, title, author, image_src, content, published_date, reading_time)
content = [card_1]
marketingcard_box = kv.HS.StackV(key="MarketingCards",
                                 childs=content,
                                 twsty_tags=[space/y/8]
                                 )


# ================================ end ===============================
# ================================ cta ===============================
from hyperui_plugin.marketing.cta import  (ContentAndImage,
                                           NewsletterSignup
                                                )

cta_1 = ContentAndImage()
cta_2 = NewsletterSignup()

content = LMap | [cta_1, cta_2]| kv.PD.Halign | ToList
marketingcta_box = kv.HS.StackV(key="MarketingCTA",
                                 childs=content,
                                 twsty_tags=[space/y/8]
                                 )
# ================================ end ===============================

# =============================== faqs ===============================

from hyperui_plugin.marketing.faqs import  (BackgroundAccentBorder
                                                )

faq_1 = BackgroundAccentBorder()
faq_1.add_faq_item("Lorem ipsum dolor sit amet consectetur adipisicing?",
                  "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ab hic veritatis molestias culpa in, recusandae laboriosam neque aliquid libero nesciunt voluptate dicta quo officiis explicabo consequuntur distinctio corporis earum similique! "
                  )

content = [faq_1]
marketingfaq_box = kv.HS.StackV(key="MarketingFAQ",
                                 childs=content,
                                 twsty_tags=[space/y/8]
                                 )
# ================================ end ===============================
# ============================== footers =============================
from hyperui_plugin.marketing.footers import  (CenteredWithBranding
                                          )
footer_1 = CenteredWithBranding()
content= [footer_1]
marketingfooter_box = kv.HS.StackV(key="MarketingFooter",
                                   childs=content,
                                   twsty_tags=[space/y/8]
                                   )
# ================================ end ===============================
from hyperui_plugin.marketing.forms import  (Login,
                                          )

form_1 = Login()

content= [footer_1]
marketingform_box = kv.HS.StackV(key="MarketingForm",
                                        childs=content,
                                        twsty_tags=[space/y/8]
                                        )
# ================================ end ===============================
# ============================== headers =============================
from hyperui_plugin.marketing.headers import  (LeftAligned
                                          )

header_1 = LeftAligned()
content = [header_1]
marketingheader_box = kv.HS.StackV(key="MarketingHeader",
                                        childs=content,
                                        twsty_tags=[space/y/8]
                                        )
# ================================ end ===============================
# =============================== popus ==============================
from hyperui_plugin.marketing.popups import  (SplitWithImageAndAction,
                                              MessageNotificationsAndAction,
                                              OrderNotificationsWithAction,
                                              ContactActions,
                                              NotificationWithImageAndClose,
                                              FloatingSplitWithImageContentClose,
                                              FloatingWithClose
                                                )


# Example invocation
img_src_example = "https://images.unsplash.com/photo-1611510338559-2f463335092c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=928&q=80"
text_example = "On your next order over $50"

popup_type_1 = SplitWithImageAndAction(img_src_example, "Run with the pack", "Get 20% off", "On your next order over $50", "GET DISCOUNT", "Offer valid until 24th March, 2021 *" )
    


popup_type_2 = MessageNotificationsAndAction("New message!",
                              "Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsam ea quo unde vel adipisci blanditiis voluptates eum. Nam, cum minima?",
                              "Take a Look",
                              "Mark as Read",
                              )
popup_type_3 =  OrderNotificationsWithAction()
popup_type_4 = NotificationWithImageAndClose("akey")

popup_type_5 = ContactActions()

popup_type_6 = FloatingSplitWithImageContentClose("btnkey")
popup_type_7 = FloatingWithClose("btnkey")

content = LMap | [popup_type_1,
           popup_type_2,
           popup_type_3,
           popup_type_4,
           popup_type_5,
           popup_type_6,
           popup_type_7
           ] | kv.PD.Halign | ToList 


marketingpopus_box = kv.HS.StackV(key="MarketingPopup",
                                        childs=content,
                                        twsty_tags=[space/y/8]
                                        )

# ================================ end ===============================
# ============================= pricings =============================
from hyperui_plugin.marketing.pricings import  (HighlightOption,
                                              )
highlightOption = HighlightOption()
content = [highlightOption]
marketingpricings_box = kv.HS.StackV(key="MarketingPricings",
                                        childs=content,
                                        twsty_tags=[space/y/8]
                                        )
# ================================ end ===============================
# ============================== section =============================
from hyperui_plugin.marketing.sections import  (GridUSP
                                              )
gridusp = GridUSP()
content = [gridusp]

marketingsections_box = kv.HS.StackV(key="MarketingSections",
                                        childs=content,
                                        twsty_tags=[space/y/8]
                                        )

# ================================ end ===============================
# =========================== testimonials ===========================
from hyperui_plugin.marketing.testimonials import  (SplitContentSlider,
                                              )
testimonial_1 = SplitContentSlider()

content = [testimonial_1]
marketingtestimonial_box = kv.HS.StackV(key="MarketingTestimonal",
                                        childs=content,
                                        twsty_tags=[space/y/8]
                                        )

