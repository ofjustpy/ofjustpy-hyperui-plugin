import ofjustpy as oj
from ofjustpy import icons
from ofjustpy.icons import FontAwesomeIcon
from py_tailwind_utils.to_twsty_expr import encode_twstr
from py_tailwind_utils import (conc_twtags,
                               tstr,
                               pd,
                               grow,
                               bg,
                               green,
                               W,
                               fc,
                               gray,
                               space,
                               y,
                               mr,
                               st,
                               srs,
                               ta)

from html_writer.macro_module import macros, writer_ctx

def BottomBanner():
    container = oj.PC.Div(twsty_tags=[space/y/4, ta.center], childs = [])
    def add_item(key, text, href="", styling="outline", container=container):
        """
        styling: outline, solid, underline
        see https://www.hyperui.dev/components/ecommerce/carts
        
        """
        if styling == "outline":
            twsty_tags = encode_twstr("block rounded border border-gray-600 px-5 py-3 text-sm text-gray-600 transition hover:ring-1 hover:ring-gray-400")
        elif styling == "solid":
            twsty_tags = encode_twstr("block rounded bg-gray-700 px-5 py-3 text-sm text-gray-100 transition hover:bg-gray-600")
        elif styling == "underline":
            twsty_tags = encode_twstr("inline-block text-sm text-gray-500 underline underline-offset-4 transition hover:text-gray-600")
            
            
        rowitem = oj.AC.A(key=key, text=text, href=href, twsty_tags=twsty_tags)
        container.components.append(rowitem)
    container.add_item = add_item
    return container
        
    

    
def Popup(bottom_banner):

    all_items = oj.PC.Ul(twsty_tags=[space/y/4], childs=[])
    def add_item(img_src, desc_title, desc_box, alt="", all_items=all_items):

        img = oj.PC.Img(src=img_src, alt=alt, twsty_tags=encode_twstr("h-16 w-16 rounded object-cover")
                        )


        desc_box = oj.PC.Div(childs = [oj.PC.H3(text=desc_title,
                                     twsty_tags=encode_twstr("text-sm text-gray-900")
                                     ),
                            desc_box

                            ]
                  )
        item_box = oj.PD.Li(twsty_tags=encode_twstr("flex items-center gap-4"), childs = [img, desc_box])
        all_items.components.append(item_box)


    all_items_root = oj.PC.Div(twsty_tags=[mr/st/4, space/y/6], childs = [all_items, bottom_banner])

    close_button = oj.AD.Button(key="close_{key}",
                         childs = [oj.PC.Span(twsty_tags=[srs.only], text="Close cart"), FontAwesomeIcon(label="faCross",
                                                                                                         classes="w-5 h-5",)
                                   ],
                         twsty_tags=encode_twstr("absolute end-4 top-4 text-gray-600 transition hover:scale-110")
                         )
                                   
    root = oj.PC.Div(twsty_tags=encode_twstr("relative w-screen max-w-sm border border-gray-600 bg-gray-100 px-4 py-8 sm:px-6 lg:px-8"),
                     childs = [close_button, all_items_root]
                     )
    root.add_item = add_item

    return root

# TODO: popup(interactive)
# from html_writer.macro_module import macros, writer_ctx

# with writer_ctx:
#     with Div(classes='relative w-screen max-w-sm border border-gray-600 bg-gray-100 px-4 py-8 sm:px-6 lg:px-8', aria_modal='true', role='dialog', tabindex='-1'):
#         with Button(classes='absolute end-4 top-4 text-gray-600 transition hover:scale-110'):
#             Span(classes='sr-only', text='Close cart')

#         with Div(classes='mt-4 space-y-6'):
#             with Ul(classes='space-y-4'):
#                 for i in range(1, 4):
#                     with Li(classes='flex items-center gap-4'):
#                         Img(src='https://images.unsplash.com/photo-1618354691373-d851c5c3a990?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=830&q=80', alt='', classes='h-16 w-16 rounded object-cover')

#                         with Div():
#                             H3(classes='text-sm text-gray-900', text='Basic Tee 6-Pack')

#                             with Dl(classes='mt-0.5 space-y-px text-[10px] text-gray-600'):
#                                 with Div():
#                                     Dt(classes='inline', text='Size:')
#                                     Dd(classes='inline', text='XXS')

#                                 with Div():
#                                     Dt(classes='inline', text='Color:')
#                                     Dd(classes='inline', text='White')

#                         with Div(classes='flex flex-1 items-center justify-end gap-2'):
#                             with Form():
#                                 Label(for_='Line{}Qty'.format(i), classes='sr-only', text='Quantity')

#                                 Input(type='number', min='1', value='1', id='Line{}Qty'.format(i), classes='h-8 w-12 rounded border-gray-200 bg-gray-50 p-0 text-center text-xs text-gray-600 [-moz-appearance:_textfield] focus:outline-none [&::-webkit-inner-spin-button]:m-0 [&::-webkit-inner-spin-button]:appearance-none [&::-webkit-outer-spin-button]:m-0 [&::-webkit-outer-spin-button]:appearance-none')

#                             Button(classes='text-gray-600 transition hover:text-red-600'):
#                                 Span(classes='sr-only', text='Remove item')

#             with Div(classes='space-y-4 text-center'):
#                 A(href='#', classes='block rounded border border-gray-600 px-5 py-3 text-sm text-gray-600 transition hover:ring-1 hover:ring-gray-400', text='View my cart (2)')

#                 A(href='#', classes='block rounded bg-gray-700 px-5 py-3 text-sm text-gray-100 transition hover:bg-gray-600', text='Checkout')

#                 A(href='#', classes='inline-block text-sm text-gray-500 underline underline-offset-4 transition hover:text-gray-600', text='Continue shopping')


def Contained():

    with writer_ctx:
        with Section() as comp_box:
            with Div(classes='mx-auto max-w-screen-xl px-4 py-8 sm:px-6 sm:py-12 lg:px-8'):
                with Div(classes='mx-auto max-w-3xl'):
                    with Header(classes='text-center'):
                        with H1(classes='text-xl font-bold text-gray-900 sm:text-3xl',
                                text='Your Cart'):
                            pass
                        
                    with Div(classes='mt-8'):
                        with Ul(classes='space-y-4'):
                            with Li(classes='flex items-center gap-4'):
                                with Img(src='https://images.unsplash.com/photo-1618354691373-d851c5c3a990?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=830&q=80', alt='', classes='h-16 w-16 rounded object-cover'):
                                    pass

                                with Div():
                                    with H3(classes='text-sm text-gray-900', text='Basic Tee 6-Pack'):
                                        pass

                                    with Dl(classes='mt-0.5 space-y-px text-gray-600', extra_classes="text-[10px]"):
                                        with Div():
                                            with Dt(classes='inline', text='Size:'):
                                                pass
                                            with Dd(classes='inline', text='XXS'):
                                                pass

                                            with Div():
                                                with Dt(classes='inline', text='Color:'):
                                                    pass
                                                with Dd(classes='inline', text='White'):
                                                    pass

                                with Div(classes='flex flex-1 items-center justify-end gap-2'):
                                    with Form(key="abc"):
                                        Label(for_='Line1Qty', classes='sr-only', text='Quantity')

                                        with TextInput(type='number',
                                                       min='1',
                                                       value='1',
                                                       placeholder='1',
                                                       key='Line1Qty',
                                                       classes='h-8 w-12 rounded border-gray-200 bg-gray-50 p-0 text-center text-xs text-gray-600 focus:outline-none',
                                                       extra_classes="[-moz-appearance:_textfield] [&::-webkit-inner-spin-button]:m-0 [&::-webkit-inner-spin-button]:appearance-none [&::-webkit-outer-spin-button]:m-0 [&::-webkit-outer-spin-button]:appearance-none"):
                                            
                                            pass
                                        with Button(key="abtn", classes='text-gray-600 transition hover:text-red-600'):
                                            with Span(classes='sr-only', text='Remove item'):
                                                pass
                                            with FontAwesomeIcon(label="faTrash",classes="w-5 h-5",):
                                                pass

                        with Div(classes='mt-8 flex justify-end border-t border-gray-100 pt-8'):
                            with Div(classes='w-screen max-w-lg space-y-4'):
                                with Dl(classes='space-y-0.5 text-sm text-gray-700'):
                                    with Div(classes='flex justify-between'):
                                        with Dt(text='Subtotal'):
                                            pass
                                        with Dd(text='£250'):
                                            pass

                                    with Div(classes='flex justify-between'):
                                        with Dt(text='VAT'):
                                            pass
                                        with Dd(text='£25'):
                                            pass

                                    with Div(classes='flex justify-between'):
                                        with Dt(text='Discount'):
                                            pass
                                        with Dd(text='-£20'):
                                            pass
                                        

                                    with Div(classes='flex justify-between !text-base font-medium'):
                                        with Dt(text='Total'):
                                            pass
                                        with Dd(text='£200'):
                                            pass

                                with Div(classes='flex justify-end'):
                                    with Span(classes='inline-flex items-center justify-center rounded-full bg-indigo-100 px-2.5 py-0.5 text-indigo-700'):
                                        with P(classes='whitespace-nowrap text-xs', text='2 Discounts Applied'):
                                            pass

                                with Div(classes='flex justify-end'):
                                    with A(href='#', classes='block rounded bg-gray-700 px-5 py-3 text-sm text-gray-100 transition hover:bg-gray-600', text='Checkout'):
                                        pass
                                    
    return comp_box
