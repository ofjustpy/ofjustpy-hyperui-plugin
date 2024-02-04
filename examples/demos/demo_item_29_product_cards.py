
from py_tailwind_utils import *
import ofjustpy as oj
oj.set_style("un")
app = oj.load_app()
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

# ====================== Contained with wishlist =====================
# Example usage:
img_src = "https://images.unsplash.com/photo-1599481238640-4c1288750d7a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2664&q=80"
product_name = "Robot Toy"
product_price = "$14.99"

card_containedWishList = ContainedWishList("wished_toy", img_src, product_name, product_price)
    
content = [oj.PC.Halign(card_simple),
                                        oj.PC.Halign(card_withVariant),
                                        oj.PC.Halign(card_withDescription),
                                        oj.PC.Halign(card_containedWishList)
                                        ]
endpoint = oj.create_endpoint("product_cards",
                              childs = [oj.PC.Div(childs=content, twsty_tags=[space/y/8])],
                              title="Product Cards"
                              )
oj.add_jproute("/", endpoint)
