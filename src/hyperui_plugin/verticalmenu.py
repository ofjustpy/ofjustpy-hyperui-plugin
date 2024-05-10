import ofjustpy as oj
from ofjustpy import icons
from py_tailwind_utils.to_twsty_expr import encode_twstr
from py_tailwind_utils import conc_twtags, tstr, pd, grow, bg, green, W, fc, gray, space, y

def Simple(twsty_tags=[], **kwargs):
    twsty_tags = conc_twtags(space/y/1, *twsty_tags)
    container = oj.PD.Ul(childs=[], twsty_tags=twsty_tags)
    bg_color = "bg-gray-100"
    text_color= "text-gray-700"
    def add_item(text, href="#", twsty_tags=[], **kwargs):
        nonlocal bg_color
        nonlocal text_color
        twsty_tags = conc_twtags(*encode_twstr(f"block rounded-lg {bg_color} px-4 py-2 text-sm font-medium {text_color}"), *twsty_tags)
        bg_color = "hover:bg-gray-100 hover:text-gray-700"
        text_color = "text-gray-500"
        container.components.append(oj.PD.Li(childs=[oj.PC.A(text=text,
                                                             href=href,
                                                             twsty_tags=twsty_tags,
                                                             
                                                             )
                                                     ]
                                             )
                                    )
    container.add_item = add_item
    return container


def WithBadge(twsty_tags=[], **kwargs):
    twsty_tags = conc_twtags(space/y/1, *twsty_tags)
    container = oj.PD.Ul(childs=[], twsty_tags=twsty_tags)
    bg_color = "bg-gray-100"
    text_color= "text-gray-700"
    def add_item(text, href="#",
                 badge=None,
                 twsty_tags=[], **kwargs):
        nonlocal bg_color
        nonlocal text_color
        #TODO:
        twsty_tags = conc_twtags(*encode_twstr(f"group flex items-center justify-between rounded-lg {bg_color} px-4 py-2 {text_color}"), *twsty_tags)
        
        bg_color = "hover:bg-gray-100 hover:text-gray-700"
        text_color = "text-gray-500"
        childs = [oj.PC.Span(text=text, twsty_tags=encode_twstr("text-sm font-medium"))]
        if badge:
            childs.append(oj.PC.Span(twsty_tags=encode_twstr("shrink-0 rounded-full bg-gray-100 px-3 py-0.5 text-xs text-gray-600 group-hover:bg-gray-200 group-hover:text-gray-700"), text=badge)
                          )
            
        container.components.append(oj.PD.Li(childs=[oj.PD.A(href=href,
                                                             classes="group flex items-center justify-between rounded-lg px-4 py-2 text-gray-500 hover:bg-gray-100 hover:text-gray-700",
                                                             childs = childs
                                                             
                                                             )
                                                     ]
                                             )
                                    )
    container.add_item = add_item
    return container


def WithIcon(twsty_tags=[], **kwargs):
    twsty_tags = conc_twtags(space/y/1, *twsty_tags)
    container = oj.PD.Ul(childs=[], twsty_tags=twsty_tags)
    bg_color = "bg-gray-100"
    text_color= "text-gray-700"
    def add_item(text, icon, href="#",  twsty_tags=[], **kwargs):
        nonlocal bg_color
        nonlocal text_color
        # TODO: there is bug in conc_twtags followed by encode_twstr
        twsty_tags = conc_twtags(*encode_twstr(f"flex items-center gap-2 rounded-lg {bg_color} px-4 py-2 {text_color}"), *twsty_tags)
        
        bg_color = "hover:bg-gray-100 hover:text-gray-700"
        text_color = "text-gray-500"
        container.components.append(oj.PD.Li(childs=[oj.PD.A(href=href,
                                                             #twsty_tags=twsty_tags,
                                                             classes="flex items-center gap-2 rounded-lg bg-gray-100 px-4 py-2 text-gray-700",
                                                             childs = [icon,
                                                                       oj.PC.Span(text=text, twsty_tags=encode_twstr("text-sm font-medium"))
                                                                       ]
                                                             
                                                             )
                                                     ]
                                             )
                                    )
    container.add_item = add_item
    return container


def WithIconAndBadge(twsty_tags=[], **kwargs):
    twsty_tags = conc_twtags(space/y/1, *twsty_tags)
    container = oj.PD.Ul(childs=[], twsty_tags=twsty_tags)
    bg_color = "bg-gray-100"
    text_color= "text-gray-700"
    def add_item(text, icon, href="#", badge=None, twsty_tags=[], **kwargs):
        nonlocal bg_color
        nonlocal text_color
        for_badge = ""
        if badge:
            for_badge = "group justify-between"
        twsty_tags = conc_twtags(*encode_twstr(f"{for_badge} flex items-center gap-2 rounded-lg {bg_color} px-4 py-2 {text_color}"), *twsty_tags)
        classes="flex items-center gap-2 rounded-lg bg-gray-100 px-4 py-2 text-gray-700"
        
        bg_color = "hover:bg-gray-100 hover:text-gray-700"
        text_color = "text-gray-500"

        childs = [        oj.PC.Div(twsty_tags=encode_twstr("flex items-center gap-2"), childs=[icon, oj.PC.Span(text=text, twsty_tags=encode_twstr("text-sm font-medium"))])]
        
        if badge:
            childs.append(oj.PC.Span(twsty_tags=encode_twstr("shrink-0 rounded-full bg-gray-100 px-3 py-0.5 text-xs text-gray-600 group-hover:bg-gray-200 group-hover:text-gray-700"), text=badge)
                          )

        
        container.components.append(oj.PD.Li(childs=[oj.PD.A(href=href,
                                                             #twsty_tags=twsty_tags,
                                                             classes=classes,
                                                             childs = childs
                                                             
                                                             )
                                                     ]
                                             )
                                    )
    container.add_item = add_item
    return container

def WithIconAndBrandedAccent(twsty_tags=[], **kwargs):
    twsty_tags = conc_twtags(space/y/1, *twsty_tags)
    container = oj.PD.Ul(childs=[], twsty_tags=twsty_tags)
    bg_color = "bg-blue-50"
    text_color= "text-blue-700"
    border_seen = "border-blue-500"
    def add_item(text, icon, href="#",  twsty_tags=[], **kwargs):
        nonlocal bg_color
        nonlocal text_color
        nonlocal border_seen
        # bug in conc_twtags over encode
        twsty_tags = conc_twtags(*encode_twstr(f"flex items-center gap-2 border-s-4 {border_seen} rounded-lg {bg_color} px-4 py-2 {text_color}"), *twsty_tags)
        classes = "flex items-center gap-2 border-s-[3px] border-blue-500 bg-blue-50 px-4 py-3 text-blue-700"
        
        bg_color = "hover:bg-gray-50 hover:text-gray-700"
        text_color = "text-gray-500"
        border_seen = "border-transparent hover:border-gray-100"
        container.components.append(oj.PD.Li(childs=[oj.PD.A(href=href,
                                                             #twsty_tags=twsty_tags,
                                                             classes=classes,
                                                             childs = [icon,
                                                                       oj.PC.Span(text=text, twsty_tags=encode_twstr("text-sm font-medium"))
                                                                       ]
                                                             
                                                             )
                                                     ]
                                             )
                                    )
    container.add_item = add_item
    return container

def menugroups(twsty_tags=[]):
    tlb = oj.PD.Ul(twsty_tags=encode_twstr("-my-2 divide-y divide-gray-100"))
    def add_group():
        group_box = oj.PC.Ul(twsty_tags=[space/y/1])
        
        def add_item(text, href="", group_box=group_box):
            group_box.components.append(oj.PD.Li(childs = [oj.PC.A(href=href, twsty_tags=encode_twstr("block rounded-lg bg-gray-100 px-4 py-2 text-sm font-medium text-gray-700"), text=text)]))
            
            
            pass
        group_box.add_item = add_item
        tlb.components.append(group_box)
        return group_box
    root = oj.PC.Div(twsty_tags=conc_twtags(*encode_twstr("flow-root"), *twsty_tags),
                     childs=[tlb]
                     )
    root.add_group = add_group
    return root


# 7.html
# from html_writer.macro_module import macros, writer_ctx

# with writer_ctx:
#     with Ul(classes='space-y-1'):
#         with Li():
#             with A(href='', classes='flex items-center gap-2 rounded-lg bg-gray-100 px-4 py-2 text-gray-700'):
#                 with Svg(xmlns='http://www.w3.org/2000/svg', classes='h-5 w-5 opacity-75', fill='none', viewBox='0 0 24 24', stroke='currentColor', stroke_width='2'):
#                     with Path(stroke_linecap='round', stroke_linejoin='round', d='M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z'):
#                         pass

#                     with Path(stroke_linecap='round', stroke_linejoin='round', d='M15 12a3 3 0 11-6 0 3 3 0 016 0z'):
#                         pass

#                 with Span(classes='text-sm font-medium', text=' General '):
#                     pass

#         with Li():
#             with Details(classes='group [&_summary::-webkit-details-marker]:hidden'):
#                 with Summary(classes='group flex items-center justify-between rounded-lg px-4 py-2 text-gray-500 hover:bg-gray-100 hover:text-gray-700'):
#                     with Div(classes='flex items-center gap-2'):
#                         with Svg(xmlns='http://www.w3.org/2000/svg', classes='h-5 w-5 opacity-75', fill='none', viewBox='0 0 24 24', stroke='currentColor', stroke_width='2'):
#                             with Path(stroke_linecap='round', stroke_linejoin='round', d='M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z'):
#                                 pass

#                         with Span(classes='text-sm font-medium', text=' Teams '):
#                             pass

#                     with Span(classes='shrink-0 transition duration-300 group-open:-rotate-180'):
#                         with Svg(xmlns='http://www.w3.org/2000/svg', classes='h-5 w-5', viewBox='0 0 20 20', fill='currentColor'):
#                             with Path(fill_rule='evenodd', d='M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z', clip_rule='evenodd'):
#                                 pass

#                 with Ul(classes='mt-2 space-y-1 px-4'):
#                     with Li():
#                         with A(href='', classes='block rounded-lg px-4 py-2 text-sm font-medium text-gray-500 hover:bg-gray-100 hover:text-gray-700', text='Banned Users'):
#                             pass

#                     with Li():
#                         with A(href='', classes='block rounded-lg px-4 py-2 text-sm font-medium text-gray-500 hover:bg-gray-100 hover:text-gray-700', text='Calendar'):
#                             pass

#         with Li():
#             with A(href='', classes='flex items-center gap-2 rounded-lg px-4 py-2 text-gray-500 hover:bg-gray-100 hover:text-gray-700'):
#                 with Svg(xmlns='http://www.w3.org/2000/svg', classes='h-5 w-5 opacity-75', fill='none', viewBox='0 0 24 24', stroke='currentColor', stroke_width='2'):
#                     with Path(stroke_linecap='round', stroke_linejoin='round', d='M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z'):
#                         pass

#                 with Span(classes='text-sm font-medium', text=' Billing '):
#                     pass

#         with Li():
#             with Details(classes='group [&_summary::-webkit-details-marker]:hidden'):
#                 with Summary(classes='group flex items-center justify-between rounded-lg px-4 py-2 text-gray-500 hover:bg-gray-100 hover:text-gray-700'):
#                     with Div(classes='flex items-center gap-2'):
#                         with Svg(xmlns='http://www.w3.org/2000/svg', classes='h-5 w-5 opacity-75', fill='none', viewBox='0 0 24 24', stroke='currentColor', stroke_width='2'):
#                             with Path(stroke_linecap='round', stroke_linejoin='round', d='M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z'):
#                                 pass

#                         with Span(classes='text-sm font-medium', text=' Account '):
#                             pass

#                     with Span(classes='shrink-0 transition duration-300 group-open:-rotate-180'):
#                         with Svg(xmlns='http://www.w3.org/2000/svg', classes='h-5 w-5', viewBox='0 0 20 20', fill='currentColor'):
#                             with Path(fill_rule='evenodd', d='M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z', clip_rule='evenodd'):
#                                 pass

#                 with Ul(classes='mt-2 space-y-1 px-4'):
#                     with Li():
#                         with A(href='', classes='block rounded-lg px-4 py-2 text-sm font-medium text-gray-500 hover:bg-gray-100 hover:text-gray-700', text='Details'):
#                             pass

#                     with Li():
#                         with A(href='', classes='block rounded-lg px-4 py-2 text-sm font-medium text-gray-500 hover:bg-gray-100 hover:text-gray-700', text='Security'):
#                             pass

#                     with Li():
#                         with Form(action='/logout'):
#                             with Button(type='submit', classes='w-full rounded-lg px-4 py-2 text-sm font-medium text-gray-500 [text-align:_inherit] hover:bg-gray-100 hover:text-gray-700', text='Logout'):
#                                 pass


from html_writer.macro_module import macros, writer_ctx

def SplitWithHeading():
    
    with writer_ctx:
        with Div() as comp_box:
            with Ul(classes='flex flex-col space-y-2') as group_box:
                pass

    def add_group(group_title, group_box=group_box):
        with writer_ctx:
            with Li() as group_item_box:
                with Strong(classes='block text-xs font-medium uppercase text-gray-400', text=group_title):
                    pass

                with Ul(classes='mt-2 space-y-1') as ul_box:
                    pass

        def add_item(title, ul_box=ul_box):
            with writer_ctx:
                with Li() as li_box:
                    with A(href='', classes='block rounded-lg  px-4 py-2 text-sm font-medium text-gray-700 text-gray-500 hover:bg-gray-100 hover:text-gray-700', text=title):
                        pass

            ul_box.components.append(li_box)
        
        group_item_box.add_item = add_item
        group_box.components.append(group_item_box)
        return group_item_box
    comp_box.add_group = add_group
    return comp_box
        
         

