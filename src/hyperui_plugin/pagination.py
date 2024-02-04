import ofjustpy as oj
from ofjustpy import icons
from py_tailwind_utils.to_twsty_expr import encode_twstr
from py_tailwind_utils import conc_twtags, tstr, pd, grow

from html_writer.macro_module import macros, writer_ctx

def WithButtons(key, page_numbers, href_begin="#", href_end="#"):
    with writer_ctx:
        with Ol(classes='flex justify-center gap-1 text-xs font-medium') as comp_box:
            with Li():
                with A(key=f"begin_{key}", href=href_begin, classes='inline-flex h-8 w-8 items-center justify-center rounded border border-gray-100 bg-white text-gray-900 rtl:rotate-180'):
                    with Span(classes='sr-only', text='Prev Page'):
                        pass
                    with Icon_PaginationLeft():
                        pass
                    


    for i in page_numbers:
        with writer_ctx:
            with Li() as li_item:
                with A(key=f"pn_{i}_{key}", href='#', classes='block h-8 w-8 rounded border border-gray-100 bg-white text-center leading-8 text-gray-900', text=str(i)) as item_box:
                    pass
        comp_box.components.append(li_item)
        

    with writer_ctx:
        with Li() as li_item:
            with A(key=f"last_{key}", classes="inline-flex h-8 w-8 items-center justify-center rounded border border-gray-100 bg-white text-gray-900 rtl:rotate-180", href=href_end):
                with Span(classes="sr-only", text="Next Page"):
                    pass
                with Icon_PaginationRight():
                    pass
    comp_box.components.append(li_item)

    return comp_box



def WithInput(key):
    with writer_ctx:
        with Div(classes='inline-flex justify-center gap-1') as comp_box:
            with A(href='#', classes='inline-flex h-8 w-8 items-center justify-center rounded border border-gray-100 bg-white text-gray-900 rtl:rotate-180', key=f"pno_prev_{key}"):
                with Span(classes='sr-only', text='Prev Page'):
                    pass
                with Icon_PaginationLeft():
                    pass

            with Div():
                with Label(for_='PaginationPage', classes='sr-only', text='Page'):
                    pass

                with TextInput(type='number', key=f"pno_{key}",
                               classes='h-8 w-12 rounded border border-gray-100 bg-white p-0 text-center text-xs font-medium text-gray-900', min='1', placeholder='2',
                               extra_classes="[-moz-appearance:_textfield] [&::-webkit-inner-spin-button]:m-0 [&::-webkit-inner-spin-button]:appearance-none [&::-webkit-outer-spin-button]:m-0 [&::-webkit-outer-spin-button]:appearance-none"):
                    pass

            with A(href='#', classes='inline-flex h-8 w-8 items-center justify-center rounded border border-gray-100 bg-white text-gray-900 rtl:rotate-180', key=f"pno_next_{key}"):
                with Span(classes='sr-only', text='Next Page'):
                    pass
                with Icon_PaginationRight():
                    pass

    return comp_box


def BackgroundWithInput(key):
    # attrs={'aria-hidden': 'true'}c
    with writer_ctx:
        with Div(classes='inline-flex items-center justify-center rounded bg-blue-600 py-1 text-white') as comp_box:
            with A(href='#', classes='inline-flex h-8 w-8 items-center justify-center rtl:rotate-180'):
                with Span(classes='sr-only', text='Prev Page'):
                    pass

                with Icon_PaginationLeft():
                    pass
                
            with Span(classes='h-4 w-px bg-white/25'):
                pass

            with Div():
                with Label(for_='PaginationPage', classes='sr-only', text='Page'):
                    pass

                with TextInput(key=key,  classes='h-8 w-12 rounded border-none bg-transparent p-0 text-center text-xs font-medium focus:outline-none focus:ring-inset focus:ring-white', min='1', value='2', extra_classes="[-moz-appearance:_textfield] [&::-webkit-inner-spin-button]:m-0 [&::-webkit-inner-spin-button]:appearance-none [&::-webkit-outer-spin-button]:m-0 [&::-webkit-outer-spin-button]:appearance-none", placeholder=2):
                    pass

            with Span(classes='h-4 w-px bg-white/25'):
                pass

            with A(href='#', classes='inline-flex h-8 w-8 items-center justify-center rtl:rotate-180'):
                with Span(classes='sr-only', text='Next Page'):
                    pass
                
                with Icon_PaginationRight():
                    pass

    return comp_box

def WithFraction(key):
    with writer_ctx:
        with Div(classes='inline-flex items-center justify-center gap-3') as comp_box:
            with A(href='#', classes='inline-flex h-8 w-8 items-center justify-center rounded border border-gray-100 bg-white text-gray-900 rtl:rotate-180'):
                with Span(classes='sr-only', text='Next Page'):
                    pass

                with Icon_PaginationLeft():
                    pass
                
            with P(classes='text-xs text-gray-900', text='3'):
                with Span(classes='mx-0.25', text='/12'):
                    pass


            with A(href='#', classes='inline-flex h-8 w-8 items-center justify-center rounded border border-gray-100 bg-white text-gray-900 rtl:rotate-180'):
                with Span(classes='sr-only', text='Next Page'):
                    pass
                with Icon_PaginationRight():
                    pass

    return comp_box
# def nav_bar(key, page_numbers):


#     right_end_marker = oj.PD.Li(childs = [oj.AD.A(key=f"rightend_{key}",
#                                                  href="#",
#                                                  childs=[icons.pagination_right,
#                                                          oj.PC.Span(text="Next Page",
#                                                                     twsty_tags=encode_twstr("sr-only")
#                                                                     )
#                                                          ],
#                                                  twsty_tags=encode_twstr("inline-flex h-8 w-8 items-center justify-center rounded border border-gray-100 bg-white text-gray-900 rtl:rotate-180")
#                                                  )
#                                          ]
#                                )



#     page_stubs = [oj.PD.Li(childs=[oj.AC.A(key=f"{_}_{key}", href="#", twsty_tags=encode_twstr("block h-8 w-8 rounded border border-gray-100 bg-white text-center leading-8 text-gray-900"),
#                                            text=str(_)
#                                            )
#                                    ]
#                            )
#                   for _ in page_numbers
#                   ]
#     root = oj.PD.Ol(twsty_tags=encode_twstr("flex justify-center gap-1 text-xs font-medium"),
#              childs = [left_end_marker, *page_stubs, right_end_marker]

#              )
#     return root
    
