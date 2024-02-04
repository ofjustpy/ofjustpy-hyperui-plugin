import ofjustpy as oj
from ofjustpy import icons
from py_tailwind_utils.to_twsty_expr import encode_twstr
from py_tailwind_utils import conc_twtags, tstr, pd, grow, bg, green, W, fc, gray, space, y


def Simple(key, **kwargs):
    cbtn = oj.AC.CheckboxInput(key=key, checked=False,
                               twsty_tags=encode_twstr("peer sr-only"),
                               **kwargs)
    toggle = oj.PD.Label(twsty_tags=encode_twstr("relative h-8 w-14 cursor-pointer"), childs = [ cbtn, 
    oj.PC.Span(twsty_tags=encode_twstr("absolute inset-0 w-14 rounded-full bg-gray-300 transition peer-checked:bg-green-500")),
oj.PC.Span(twsty_tags=encode_twstr("absolute inset-y-0 start-0 m-1 h-6 w-6 rounded-full bg-white transition-all peer-checked:start-6"))
    ]
            )
    return toggle


def Apple(key, **kwargs):
    cbtn = oj.AC.CheckboxInput(key=key, checked=False,
                               twsty_tags=encode_twstr("peer sr-only"),
                               **kwargs)
    toggle = oj.PD.Label(twsty_tags=encode_twstr("relative h-8 w-14 cursor-pointer"), childs = [ cbtn, 
    oj.PC.Span(twsty_tags=encode_twstr("absolute inset-0 rounded-full bg-gray-300 transition peer-checked:bg-blue-500")),
oj.PC.Span(twsty_tags=encode_twstr("absolute inset-y-0 start-0 m-1 h-6 w-6 rounded-full bg-gray-500 ring-4px ring-inset ring-white transition-all peer-checked:start-8 peer-checked:w-2 peer-checked:bg-white peer-checked:ring-transparent"))
    ]
            )
    return oj.PC.Div(childs=[toggle], classes="pt-8")


from html_writer.macro_module import macros, writer_ctx

def Material(key, **kwargs):
    with writer_ctx:
        with Div() as comp_box:
            with Label(for_='AcceptConditions', classes='relative h-8 w-12 cursor-pointer ', extra_classes="[-webkit-tap-highlight-color:_transparent]"):
                with CheckboxInput(key=key,  id='AcceptConditions', classes='peer sr-only', **kwargs):
                    pass

                with Span(classes='absolute inset-0 m-auto w-8 h-2 rounded-full bg-gray-300'):
                    pass

                with Span(classes='absolute inset-y-0 start-0 m-auto h-6 w-6 rounded-full bg-gray-500 transition-all peer-checked:start-6', extra_classes="peer-checked:[&_>_*]:scale-0"):
                    with Span(classes='absolute inset-0 m-auto h-4 w-4 rounded-full bg-gray-200 transition'):
                        pass

    return comp_box


#TODO: toggling data-unchecked-icon, data-checked-icon is essential for this to work
# def SimpleWithIcon(key):
#     with writer_ctx:
#         with Label(for_='AcceptConditions', classes='relative h-8 w-14 cursor-pointer ', extra_classes="[-webkit-tap-highlight-color:_transparent") as comp_box:
#             with CheckboxInput( key=key, classes='peer sr-only', extra_classes="[&:checked_+_span_svg[data-checked-icon]]:block [&:checked_+_span_svg[data-unchecked-icon]]:hidden"):
#                 pass

#             with Span(classes='absolute inset-y-0 start-0 z-10 m-1 inline-flex h-6 w-6 items-center justify-center rounded-full bg-white text-gray-400 transition-all peer-checked:start-6 peer-checked:text-green-600'):
#                 with Icon_Cross():
#                     pass
                

#                 with Icon_EncircledCheckmark():
#                     pass

#             with Span(classes='absolute inset-0 rounded-full bg-gray-300 transition peer-checked:bg-green-500'):
#                 pass



#     return comp_box
