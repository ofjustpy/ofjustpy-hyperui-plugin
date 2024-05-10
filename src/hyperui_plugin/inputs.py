import ofjustpy as oj
from ofjustpy import icons
from py_tailwind_utils.to_twsty_expr import encode_twstr
from py_tailwind_utils import conc_twtags, tstr, pd, grow

from html_writer.macro_module import macros, writer_ctx

def Simple(key, label, placeholder):
    with writer_ctx:
        with Div() as email_input_container:
            with Label(for_=f'{key}_UserEmail', classes='block text-xs font-medium text-gray-700', text=label):
                pass

            with TextInput(type='email', key=f'{key}_UserEmail', placeholder=placeholder, classes='mt-1 w-full rounded-md border-gray-200 shadow-sm sm:text-sm'):
                pass

    return email_input_container

# def Simple(key, labeltext, placeholder, **kwargs):
#     """
#     add event handler in kwargs
#     """

#     textinput = oj.AC.TextInput(key=key, placeholder=placeholder, twsty_tags=encode_twstr("mt-1 w-full rounded-md border-gray-200 shadow-sm sm:text-sm"), **kwargs)
    
#     tlc = oj.PC.Div(childs = [oj.PC.Label(twsty_tags=encode_twstr("block text-xs font-medium text-gray-700"),
#                                            text=labeltext),
#                                textinput
#                         ]
#               )    
#     return tlc




def WithIcon(key, label, placeholder):
    with writer_ctx:
        with Div(classes='relative') as comp_box:
            with Label(for_='UserEmail', classes='sr-only', text=label):
                pass

            with TextInput(type='email', key=key, placeholder=placeholder, classes='w-full rounded-md border-gray-200 pe-10 shadow-sm sm:text-sm'):
                pass

            with Span(classes='pointer-events-none absolute inset-y-0 end-0 grid w-10 place-content-center text-gray-500'):
                with FontAwesomeIcon(label="faEnvelope", classes="w-5 h-5",):
                    pass
                pass

    return comp_box


# def WithIcon( key, labeltext, placeholder, icon, **kwargs):
#     label = oj.PC.Label(twsty_tags=encode_twstr("sr-only"),
#                                            text=labeltext)
    
#     textinput = oj.AC.TextInput(key=key, placeholder=placeholder, twsty_tags=encode_twstr("w-full rounded-md border-gray-200 pe-10 shadow-sm sm:text-sm"), **kwargs)
    
#     icon_span = oj.PD.Span(twsty_tags=encode_twstr("pointer-events-none absolute inset-y-0 end-0 grid w-10 place-content-center text-gray-500"), childs=[icon])
#     tlc = oj.PC.Div(twsty_tags=encode_twstr("relative"), childs = [label, textinput, icon_span])
#     return tlc
#     pass

def SearchInputWithButton(key, label, placeholder):
    with writer_ctx:
        with Div(classes='relative') as comp_box:
            with Label(for_='Search', classes='sr-only', text=label):
                pass

            with TextInput(type='text',
                       key=f"{key}_input",
                       placeholder=placeholder,
                       classes='w-full rounded-md border-gray-200 py-2.5 pe-10 shadow-sm sm:text-sm'):
                pass

            with Span(classes='absolute inset-y-0 end-0 grid w-10 place-content-center'):
                with Button(key=f"{key}_btn", classes='text-gray-600 hover:text-gray-700') as search_button:
                    with Span(classes='sr-only', text='Search'):
                        pass
                    with FontAwesomeIcon(label="faMagnifyingGlass", classes="w-5 h-5"):
                        pass

    return comp_box


# def WithButton(key, labeltext, placeholder, icon, **kwargs):
#     btn = oj.AD.Button(key=f"btn_{key}",
#                  twsty_tags=encode_twstr("text-gray-600 hover:text-gray-700"),
#                  childs = [oj.PC.Span(twsty_tags=encode_twstr("sr-only"), text=labeltext),
#                            icon,
#                            ]
#                  )
#     btnbox = oj.PD.Span(childs = [btn], twsty_tags=encode_twstr("absolute inset-y-0 end-0 grid w-10 place-content-center")
    
#         )

#     label = oj.PC.Label(twsty_tags=encode_twstr("sr-only"),
#                                            text=labeltext)
#     textinput = oj.AC.TextInput(key=key, placeholder=placeholder, twsty_tags=encode_twstr("w-full rounded-md border-gray-200 pe-10 shadow-sm sm:text-sm"), **kwargs)

#     tlc = oj.PC.Div(twsty_tags=encode_twstr("relative"), childs = [label, textinput, btnbox])
#     return tlc
#     pass


def WithLabel(key, label, placeholder):
    with writer_ctx:
        with Label(for_='UserEmail', classes='block overflow-hidden rounded-md border border-gray-200 px-3 py-2 shadow-sm focus-within:border-blue-600 focus-within:ring-1 focus-within:ring-blue-600') as comp_box:
            with Span(classes='text-xs font-medium text-gray-700', text=label):
                pass

            with TextInput(type='email', key=key, placeholder=placeholder, classes='mt-1 w-full border-none p-0 focus:border-transparent focus:outline-none focus:ring-0 sm:text-sm'):
                pass

    return comp_box

# def WithLabel(key, labeltext, placeholder, **kwargs):
#     textinput = oj.AC.TextInput(key=key, placeholder=placeholder, twsty_tags=encode_twstr("mt-1 w-full border-none p-0 focus:border-transparent focus:outline-none focus:ring-0 sm:text-sm"), **kwargs)
#     label = oj.PD.Label(twsty_tags=encode_twstr("block overflow-hidden rounded-md border border-gray-200 px-3 py-2 shadow-sm focus-within:border-blue-600 focus-within:ring-1 focus-within:ring-blue-600"), childs = [oj.PC.Span(text=labeltext, twsty_tags=encode_twstr("text-xs font-medium text-gray-700")), textinput]
#                         )
#     return label




def FloatingLabel(key, label, placeholder):
    with writer_ctx:
        with Label(for_='Username', classes='relative block rounded-md border border-gray-200 shadow-sm focus-within:border-blue-600 focus-within:ring-1 focus-within:ring-blue-600') as comp_box:
            with TextInput(type='text', key=key, classes='peer border-none bg-transparent placeholder-transparent focus:border-transparent focus:outline-none focus:ring-0', placeholder=placeholder):
                pass

            with Span(classes='pointer-events-none absolute start-2.5 top-0 -translate-y-1/2 bg-white p-0.5 text-xs text-gray-700 transition-all peer-placeholder-shown:top-1/2 peer-placeholder-shown:text-sm peer-focus:top-0 peer-focus:text-xs', text=label):
                pass

    return comp_box


# def FloatingLabel(key, labeltext, placeholder, **kwargs):
#     textinput = oj.AC.TextInput(key=key, placeholder=placeholder, twsty_tags=encode_twstr("peer border-none bg-transparent placeholder-transparent focus:border-transparent focus:outline-none focus:ring-0"), **kwargs)
#     label = oj.PD.Label(twsty_tags=encode_twstr("relative block rounded-md border border-gray-200 shadow-sm focus-within:border-blue-600 focus-within:ring-1 focus-within:ring-blue-600"), childs = [textinput, oj.PC.Span(text=labeltext, twsty_tags=encode_twstr("pointer-events-none absolute start-2.5 top-0 -translate-y-1/2 bg-white p-0.5 text-xs text-gray-700 transition-all peer-placeholder-shown:top-1/2 peer-placeholder-shown:text-sm peer-focus:top-0 peer-focus:text-xs"))]
#                         )
#     return label




def FloatingLabelInside(key, label, placeholder):
    with writer_ctx:
        with Label(for_='UserEmail', classes='relative block overflow-hidden rounded-md border border-gray-200 px-3 pt-3 shadow-sm focus-within:border-blue-600 focus-within:ring-1 focus-within:ring-blue-600') as comp_box:
            with TextInput(type='email', key=key, placeholder=placeholder, classes='peer h-8 w-full border-none bg-transparent p-0 placeholder-transparent focus:border-transparent focus:outline-none focus:ring-0 sm:text-sm'):
                pass

            with Span(classes='absolute start-3 top-3 -translate-y-1/2 text-xs text-gray-700 transition-all peer-placeholder-shown:top-1/2 peer-placeholder-shown:text-sm peer-focus:top-3 peer-focus:text-xs', text=label):
                pass

    return comp_box

# def FloatingLabelInside(key, labeltext, placeholder, **kwargs):
#     textinput = oj.AC.TextInput(key=key, placeholder=placeholder, twsty_tags=encode_twstr("peer h-8 w-full border-none bg-transparent p-0 placeholder-transparent focus:border-transparent focus:outline-none focus:ring-0 sm:text-sm"), **kwargs)
#     label = oj.PD.Label(twsty_tags=encode_twstr("relative block overflow-hidden rounded-md border border-gray-200 px-3 pt-3 shadow-sm focus-within:border-blue-600 focus-within:ring-1 focus-within:ring-blue-600"), childs = [textinput, oj.PC.Span(text=labeltext, twsty_tags=encode_twstr("absolute start-3 top-3 -translate-y-1/2 text-xs text-gray-700 transition-all peer-placeholder-shown:top-1/2 peer-placeholder-shown:text-sm peer-focus:top-3 peer-focus:text-xs"))]
#                         )
#     return label



def FloatingLabelUnderline(key, label, placeholder):
    with writer_ctx:
        with Label(for_='UserEmail', classes='relative block overflow-hidden border-b border-gray-200 bg-transparent pt-3 focus-within:border-blue-600') as comp_box:
            with TextInput(type='email', key=key, placeholder=placeholder, classes='peer h-8 w-full border-none bg-transparent p-0 placeholder-transparent focus:border-transparent focus:outline-none focus:ring-0 sm:text-sm'):
                pass

            with Span(classes='absolute start-0 top-2 -translate-y-1/2 text-xs text-gray-700 transition-all peer-placeholder-shown:top-1/2 peer-placeholder-shown:text-sm peer-focus:top-2 peer-focus:text-xs', text=label):
                pass

    return comp_box


# def FloatingLabelUnderline(key, labeltext, placeholder, **kwargs):
#     textinput = oj.AC.TextInput(key=key, placeholder=placeholder, twsty_tags=encode_twstr("peer h-8 w-full border-none bg-transparent p-0 placeholder-transparent focus:border-transparent focus:outline-none focus:ring-0 sm:text-sm"), **kwargs)
#     label = oj.PD.Label(twsty_tags=encode_twstr("relative block overflow-hidden rounded-md border border-gray-200 px-3 pt-3 shadow-sm focus-within:border-blue-600 focus-within:ring-1 focus-within:ring-blue-600"), childs = [textinput, oj.PC.Span(text=labeltext, twsty_tags=encode_twstr("absolute start-0 top-2 -translate-y-1/2 text-xs text-gray-700 transition-all peer-placeholder-shown:top-1/2 peer-placeholder-shown:text-sm peer-focus:top-2 peer-focus:text-xs"))]
#                         )
#     return label

