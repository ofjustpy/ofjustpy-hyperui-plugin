from ofjustpy import icons
from py_tailwind_utils.to_twsty_expr import encode_twstr
import ofjustpy as oj
from py_tailwind_utils import conc_twtags, tstr, pd
from html_writer.macro_module import macros, writer_ctx
def Dropdown(key, title, href="#"):
    def on_menudown_click(dbref, msg, to_ms, ctx=None):
        print ("on menudown click: ", ctx)
        # if hasattr(com, 'is_active'):
        #     pass
        # else:
        #     setattr(root_ms, 'is_active', False)
        # pass
        pass
    with oj.uictx("tlctx") as tlctx:    
        with writer_ctx:
            with HCCMutable_Div(classes="relative") as comp_box:
                with HCCMutable_Div(classes="inline-flex items-center overflow-hidden rounded-md border bg-white"):
                    with A(href=href, classes="border-e px-4 py-2 text-sm/none text-gray-600 hover:bg-gray-50 hover:text-gray-700", text=title):
                        pass
                    with Button(key=key, classes="h-full p-2 text-gray-600 hover:bg-gray-50 hover:text-gray-700", on_click=lambda *args, ctx=tlctx:on_menudown_click(*args, ctx=tlctx)):
                        with Icon_Chevrondown():
                            pass
                with HCCMutable_Div(classes="absolute end-0 z-10 mt-2 w-56 rounded-md border border-gray-100 bg-white shadow-lg", role="menu"):
                    with HCCMutable_Div(key="{key}_items_box", classes="p-2") as items_box:
                        pass
                    pass

    def add_item(label, href="#", items_box=items_box):
        with writer_ctx:
            with A(href=href, classes="block rounded-lg px-4 py-2 text-sm text-gray-500 hover:bg-gray-50 hover:text-gray-700", role="menuitem", text=label) as item_box:
                pass
        items_box.childs.append(item_box)

    comp_box.add_item = add_item

    return comp_box



    
# def Dropdown(menu_title="Edit", href="#", twsty_tags=[]):
  
#     # menu

#     a = oj.PC.A(twsty_tags=encode_twstr("border-e px-4 py-2 text-sm/none text-gray-600 hover:bg-gray-50 hover:text-gray-700"), href=href, text=menu_title)

    
#     # TODO need hooks
#     btn = oj.AD.Button(key="menubtn", twsty_tags=encode_twstr("h-full p-2 text-gray-600 hover:bg-gray-50 hover:text-gray-700"), childs=[icons.chevrondown]
#                        )
#     menu_tlc = oj.PD.Div(twsty_tags=encode_twstr("inline-flex items-center overflow-hidden rounded-md border bg-white"), childs=[a, btn]
#                              )

#     items_container = oj.PC.Div(childs=[], twsty_tags=[pd/2])
#     items_tlc = oj.HCCStatic.Div(twsty_tags=encode_twstr("""absolute end-0 z-10 mt-2 w-56 rounded-md border border-gray-100 bg-white shadow-lg hidden"""),
#                                 role="menu",
#                                 childs = [items_container],
#                                key="menuitem_box"
#                                 )

    
#     root = oj.Mutable.Div(key="menu",
#                           twsty_tags=encode_twstr("relative"),
#                           childs=[menu_tlc, items_tlc])
    
    
#     def on_menudown_click(dbref,msg, to_ms):
#         root_ms = to_ms(root)
#         if hasattr(root_ms, 'is_active'):
#             pass
#         else:
#             setattr(root_ms, 'is_active', False)
            
#         if root.is_active:
#             root.is_active = False
#             items_tlc.add_twsty_tags(hidden)
#         else:
#             root.is_active = True
#             items_tlc.remove_twsty_tags(hidden)
#         print("on menudown called")

#         pass
#     btn.on("click", on_menudown_click)
    
#     on_click = on_menudown_click
#     def add_item(text, href="#", **kwargs):
#         nonlocal items_container
#         twsty_tags = encode_twstr("block rounded-lg px-4 py-2 text-sm text-gray-500 hover:bg-gray-50 hover:text-gray-700")
#         if 'twsty_tags' in kwargs:
#             twsty_tags = conc_twtags(*kwargs.get("twsty_tags"), *twsty_tags)
#         items_container.components.append(oj.PC.A(href=href,
#                                                   twsty_tags=twsty_tags,
#                                                   role="menuitem",
#                                                   text=text,
#                                                   **kwargs
#                                                   )
#                                           )
        
        
#     return root, add_item
