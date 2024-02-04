from html_writer.macro_module import macros, writer_ctx
from py_tailwind_utils import *

import ofjustpy as oj
oj.set_style("un")

from py_tailwind_utils.to_twsty_expr import encode_twstr
from ofjustpy import icons
from py_tailwind_utils import *
from ofjustpy import icons

from hyperui_plugin.ecom.carts import  (BottomBanner, Popup,
                                        Contained
                                          )
bb_container = BottomBanner()
bb_container.add_item("view_cart", "View My Cart", href="", styling="outline")
bb_container.add_item("checkout", "Checkout", href="", styling="solid")
bb_container.add_item("continueShopping", "Continue Shopping", href="", styling="underline")

popup_cart = Popup(bb_container)
app = oj.load_app()


with writer_ctx:
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



     
endpoint = oj.create_endpoint("popup_cart",
                              childs = [oj.PC.Halign(popup_cart),
                                        oj.PC.Halign(Contained())
                                        ],
                              title="Demo carts"
                              )
oj.add_jproute("/", endpoint)
