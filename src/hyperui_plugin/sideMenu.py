import ofjustpy as oj
from ofjustpy import icons
from ofjustpy.icons import FontAwesomeIcon
from py_tailwind_utils.to_twsty_expr import encode_twstr
from py_tailwind_utils import conc_twtags, tstr, pd, grow, bg, green, W, fc, gray
from html_writer.macro_module import macros, writer_ctx



def Simple(logo=None, twsty_tags=[], **kwargs):

    with writer_ctx:
        with Div(classes=f"flex overflow-y-auto w-80 h-screen flex-col justify-between border-e bg-white {tstr(*twsty_tags)}") as comp_box:
            with Div(classes=" flex justify-center"):
                with Span(classes="px-2 py-6 font-bold text-indigo-700 text-large uppercase leading-normal", text=logo):
                    pass

            with Ul(classes="mt-6 flex-1") as menu_box:
                pass
            
    def add_flat_item(key, label,  menu_box=menu_box, **kwargs):
        with writer_ctx:
            with Li(classes="justify-center px-4 py-2") as item_box:
                with Button(key=key, classes= "rounded-lg border border-2 border-indigo-500/50 px-4 py-1 text-sm font-medium text-indigo-500 uppercase leading-normal hover:bg-gradient-to-bl hover:from-gray-200 hover:to-gray-200 hover:via-gray-100/50 w-52 overflow-x-auto shadow shadow-indigo-200  hover:shadow-md hower:shadow-indigo-300 focus:bg-gradient-to-bl focus:border-indigo-500/50 focus:border ", text=label, **kwargs):
                    pass

        menu_box.components.append(item_box)
        
    def add_group_item(title, menu_box=menu_box):
        with writer_ctx:
            with Li(classes='') as group_box:
                with Details(classes='group', extra_classes="[&_summary::-webkit-details-marker]:hidden"):
                    with Summary(classes='flex cursor-pointer items-center justify-between rounded-lg px-4 py-2 text-gray-500 hover:bg-gray-100 hover:text-gray-700'):
                        with Div(classes = "flex-1 flex justify-center"):
                            with Span(classes='px-4 font-bold text-indigo-500 text-large uppercase leading-normal', text=title):
                                pass
                            pass
                        

                        with Span(classes='shrink-0 transition duration-300 group-open:-rotate-180'):
                            with FontAwesomeIcon(label="faChevronDown"):
                                pass

                        

                    with Ul(classes='mt-3 flex-1 space-y-3') as ul_box:
                        pass

        def add_flat_item(key, label, ul_box=ul_box, **kwargs):
            with writer_ctx:
                with Li(classes="justify-center px-4") as li_box:
                    with Button(key=key, classes='rounded-lg border border-2 border-indigo-500/50 px-4 py-1 text-sm font-medium text-indigo-500 uppercase leading-normal hover:bg-gradient-to-bl hover:from-gray-200 hover:to-gray-200 hover:via-gray-100/50 w-52 overflow-x-auto shadow shadow-indigo-200  hover:shadow-md hower:shadow-indigo-300', text=label, **kwargs):
                                pass

            ul_box.components.append(li_box)
        menu_box.components.append(group_box)
        group_box.add_flat_item = add_flat_item
        return group_box
    
    comp_box.add_flat_item = add_flat_item
    comp_box.add_group_item = add_group_item
    return comp_box

# def IconsWithTiles():
#     with writer_ctx:
#         with Div(classes="flex h-screen w-16 flex-col justify-between border-e bg-white") as comp_box:
#             with Div():
#                 with Div(classes="inline-flex h-16 w-16 items-center justify-center") as top_box:
#                     pass


#     def add_to_(label, top_box=top_box):
#         with writer_ctx:
#             with Span(classes="grid h-10 w-10 place-content-center rounded-lg bg-gray-100 text-xs text-gray-600",  text=label) as item_box:
#                 pass
#         top_box.components.append(item_box)
        

    
#     def add_group():
#         pass
    
#     def add_bottom_group():
#         pass
    
