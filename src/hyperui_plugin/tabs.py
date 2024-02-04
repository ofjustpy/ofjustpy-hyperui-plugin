import ofjustpy as oj
from ofjustpy import icons
from py_tailwind_utils.to_twsty_expr import encode_twstr
from py_tailwind_utils import conc_twtags, tstr, pd, grow, bg, green, W, fc, gray, space, y
from html_writer.macro_module import macros, writer_ctx

                    # with A(href='#', classes='shrink-0 rounded-lg p-2 text-sm font-medium text-gray-500 hover:bg-gray-50 hover:text-gray-700', text='Messages'):
                    #     pass

                    # with A(href='#', classes='shrink-0 rounded-lg p-2 text-sm font-medium text-gray-500 hover:bg-gray-50 hover:text-gray-700', text='Archive'):
                    #     pass

                    # with A(href='#', classes='shrink-0 rounded-lg bg-gray-100 p-2 text-sm font-medium text-gray-700', aria_current='page', text='Notifications'):
                    #     pass
                    
def Pills(key):
    with writer_ctx:
        with Div() as comp_box:
            with Div(classes='sm:hidden'):
                with Label(for_='Tab', classes='sr-only', text='Tab'):
                    pass

                with Select(key=key, classes='w-full rounded-md border-gray-200') as select_box:
                    pass

            with Div(classes='hidden sm:block'):
                with Nav(classes='flex gap-6', aria_label='Tabs') as nav_box:
                    pass

    def add_tab(key, label, selected=False, nav_box=nav_box):
        with writer_ctx:
            with Button(key=key, classes='shrink-0 rounded-lg p-2 text-sm font-medium text-gray-500 hover:bg-gray-50 hover:text-gray-700', text=label) as tab_btn:
                
                pass
        nav_box.components.append(tab_btn)
        select_box.components.append(oj.PC.Option(text=label, selected=selected))

                    
    comp_box.add_tab = add_tab
    
    return comp_box



def Tabbed(key):
    with writer_ctx:
        with Div() as comp_box:
            with Div(classes='sm:hidden'):
                with Label(for_='Tab', classes='sr-only', text='Tab'):
                    pass

                with Select(key=key, classes='w-full rounded-md border-gray-200') as select_box:
                    pass
                

            with Div(classes='hidden sm:block'):
                with Div(classes='border-b border-gray-200'):
                    with Nav(classes='-mb-px flex gap-6') as nav_box:
                        pass

    def add_tab(key, label, selected=False, nav_box=nav_box):
        with writer_ctx:
            # TODO: when selected
            # remove border-transparent
            # add/overwrite: rounded-t-lg  border-gray-300 border-b-white  text-sky-600
            with Button(key=key, classes='shrink-0 border border-transparent p-3 text-sm font-medium text-gray-500 hover:text-gray-700', text=label) as tab_btn:
                pass

        nav_box.components.append(tab_btn)
        select_box.components.append(oj.PC.Option(text=label, selected = selected))

    comp_box.add_tab = add_tab
    return comp_box
# def Pills(key,  **kwargs):
#     tab_nav_bar = oj.PD.Nav(twsty_tags=encode_twstr("flex gap-6"))
#     select_comp = oj.AC.Select(key=f"{key}_select",
#                                childs = [],
#                                **kwargs
#                  )
    
#     def add_tab(key, text, href="#"):
#         tab = oj.AC.A(key=key, href=href, text=text, twsty_tags=encode_twstr("shrink-0 rounded-lg p-2 text-sm font-medium text-gray-500 hover:bg-gray-50 hover:text-gray-700"))
#         tab_nav_bar.components.append(tab)
#         select_comp.components.append(oj.PC.Option(text=text))
        



#     sr_label = oj.PC.Label(#for="Tab",
#         twsty_tags=encode_twstr("sr-only"), text="Tab"
#         )
#     print(encode_twstr("hidden sm:block"))
    
#     root = oj.PD.Div(childs = [oj.PC.Div(childs=[sr_label, select_comp],
#                                          twsty_tags=encode_twstr("sm:hidden")
#                                          ),
#                                oj.PC.Div(childs=[tab_nav_bar],
#                                          twsty_tags=encode_twstr("hidden sm:block")
#                                    )
#                                ]
#                      )
#     root.add_tab = add_tab
#     return root


# def PillsBranded(key, **kwargs):
#     tab_nav_bar = oj.PD.Nav(twsty_tags=encode_twstr("flex gap-6"))
#     select_comp = oj.AC.Select(key=f"{key}_select",
#                                childs = [],
#                                twsty_tags=encode_twstr("w-full rounded-md border-gray-200")
#                                **kwargs
#                  )
    
#     def add_tab(key, text, href="#"):
#         tab = oj.AC.A(key=key, href=href, text=text, twsty_tags=encode_twstr("shrink-0 rounded-lg p-2 text-sm font-medium text-gray-500 hover:bg-gray-50 hover:text-gray-700"))
#         tab_nav_bar.components.append(tab)
#         select_comp.components.append(oj.PC.Option(text=text))
        



#     sr_label = oj.PC.Label(#for="Tab",
#         twsty_tags=encode_twstr("sr-only"), text="Tab"
#         )
    
#     root = oj.PD.Div(childs = [oj.PC.Div(childs=[sr_label, select_comp],
#                                          twsty_tags=encode_twstr("sm:hidden")
#                                          ),
#                                oj.PC.Div(childs=[tab_nav_bar],
#                                          twsty_tags=encode_twstr("hidden sm:block")
#                                    )
#                                ]
#                      )
#     root.add_tab = add_tab
#     return root
