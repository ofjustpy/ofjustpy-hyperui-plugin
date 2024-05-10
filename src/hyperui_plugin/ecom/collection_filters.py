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


def InlineDropdown():

    with writer_ctx:
        with Div(classes='flex gap-8') as comp_box:
            # Availability
            with Div(classes='relative'):
                with Details(classes='group', extra_classes="[&_summary::-webkit-details-marker]:hidden"):
                    with Summary(classes='flex cursor-pointer items-center gap-2 border-b border-gray-400 pb-1 text-gray-900 transition hover:border-gray-600'):
                        with Span(classes='text-sm font-medium', text=' Availability '):
                            pass
                        with Span(classes='transition group-open:-rotate-180'):
                            with FontAwesomeIcon(label="faChevronDown",
                                                 classes="w-5 h-5"):
                                pass
                            

                    with Div(classes='z-50 group-open:absolute group-open:start-0 group-open:top-auto group-open:mt-2'):
                        with Div(classes='w-96 rounded border border-gray-200 bg-white'):
                            with Header(classes='flex items-center justify-between p-4'):
                                with Span(classes='text-sm text-gray-700', text=' 0 Selected '):
                                    pass
                                
                                with Button(key="abc", classes='text-sm text-gray-900 underline underline-offset-4', text='Reset'):
                                    pass

                            with Ul(classes='space-y-1 border-t border-gray-200 p-4'):
                                # In Stock
                                with Li():
                                    with Label(for_='FilterInStock', classes='inline-flex items-center gap-2'):
                                        with CheckboxInput(key='FilterInStock', classes='h-5 w-5 rounded border-gray-300'):
                                            pass
                                        with Span(classes='text-sm font-medium text-gray-700', text=' In Stock (5+)'):
                                            pass
                                        

                                # Pre Order
                                with Li():
                                    with Label(for_='FilterPreOrder', classes='inline-flex items-center gap-2'):
                                        with CheckboxInput( key='FilterPreOrder', classes='h-5 w-5 rounded border-gray-300'):
                                            pass
                                        with Span(classes='text-sm font-medium text-gray-700', text=' Pre Order (3+)'):
                                            pass

                                # Out of Stock
                                with Li():
                                    with Label(for_='FilterOutOfStock', classes='inline-flex items-center gap-2'):
                                        with CheckboxInput(key='FilterOutOfStock', classes='h-5 w-5 rounded border-gray-300'):
                                            pass
                                        with Span(classes='text-sm font-medium text-gray-700', text=' Out of Stock (10+)'):
                                            pass

            # Price
            with Div(classes='relative'):
                with Details(classes='group', extra_classes="[&_summary::-webkit-details-marker]:hidden"):
                    with Summary(classes='flex cursor-pointer items-center gap-2 border-b border-gray-400 pb-1 text-gray-900 transition hover:border-gray-600'):
                        with Span(classes='text-sm font-medium', text=' Price '):
                            pass
                        with Span(classes='transition group-open:-rotate-180'):
                            with FontAwesomeIcon(label="faChevronDown"
                                                 classes="w-5 h-5",):
                                pass
                            pass

                    with Div(classes='z-50 group-open:absolute group-open:start-0 group-open:top-auto group-open:mt-2'):
                        with Div(classes='w-96 rounded border border-gray-200 bg-white'):
                            with Header(classes='flex items-center justify-between p-4'):
                                with Span(classes='text-sm text-gray-700', text=' The highest price is $600 '):
                                    pass
                                with Button(key="btn2", classes='text-sm text-gray-900 underline underline-offset-4', text='Reset'):
                                    pass

                            with Div(classes='border-t border-gray-200 p-4'):
                                with Div(classes='flex justify-between gap-4'):
                                    # Price From
                                    with Label(for_='FilterPriceFrom', classes='flex items-center gap-2'):
                                        with Span(classes='text-sm text-gray-600', text='$'):
                                            pass
                                        with TextInput(type='number', key='FilterPriceFrom', placeholder='From', classes='w-full rounded-md border-gray-200 shadow-sm sm:text-sm'):
                                            pass

                                    # Price To
                                    with Label(for_='FilterPriceTo', classes='flex items-center gap-2'):
                                        with Span(classes='text-sm text-gray-600', text='$'):
                                            pass
                                        with TextInput(type='number', key='FilterPriceTo', placeholder='To', classes='w-full rounded-md border-gray-200 shadow-sm sm:text-sm'):
                                            pass
                                        



    return comp_box

from html_writer.macro_module import macros, writer_ctx
def StackedDropdown():

    with writer_ctx:
        with Div(classes='space-y-2') as comp_box:
            # Availability
            with Details(classes='overflow-hidden rounded border border-gray-300',
                         extra_classes = "[&_summary::-webkit-details-marker]:hidden"
                         ):
                with Summary(classes='flex cursor-pointer items-center justify-between gap-2 bg-white p-4 text-gray-900 transition'):
                    with Span(classes='text-sm font-medium', text=' Availability '):
                        pass
                    
                    with Span(classes='transition group-open:-rotate-180'):
                        with FontAwesomeIcon(label="faChevronDown",
                                             classes="w-5 h-5",):
                            pass
                        pass

                with Div(classes='border-t border-gray-200 bg-white'):
                    with Header(classes='flex items-center justify-between p-4'):
                        with Span(classes='text-sm text-gray-700', text=' 0 Selected '):
                            pass
                        with Button(key="abtn", classes='text-sm text-gray-900 underline underline-offset-4', text='Reset'):
                            pass

                    with Ul(classes='space-y-1 border-t border-gray-200 p-4'):
                        # In Stock
                        with Li():
                            with Label(for_='FilterInStock', classes='inline-flex items-center gap-2'):
                                with CheckboxInput(key='FilterInStock', classes='h-5 w-5 rounded border-gray-300'):
                                    pass
                                
                                with Span(classes='text-sm font-medium text-gray-700', text=' In Stock (5+)'):
                                    pass
                                

                        # Pre Order
                        with Li():
                            with Label(for_='FilterPreOrder', classes='inline-flex items-center gap-2'):
                                with CheckboxInput(key='FilterPreOrder', classes='h-5 w-5 rounded border-gray-300'):
                                    pass
                                with Span(classes='text-sm font-medium text-gray-700', text=' Pre Order (3+)'):
                                    pass

                        # Out of Stock
                        with Li():
                            with Label(for_='FilterOutOfStock', classes='inline-flex items-center gap-2'):
                                with CheckboxInput(key='FilterOutOfStock', classes='h-5 w-5 rounded border-gray-300'):
                                    pass
                                with Span(classes='text-sm font-medium text-gray-700', text=' Out of Stock (10+)'):
                                    pass

            # Price
            with Details(classes='overflow-hidden rounded border border-gray-300', extra_classes='[&_summary::-webkit-details-marker]:hidden'):
                with Summary(classes='flex cursor-pointer items-center justify-between gap-2 bg-white p-4 text-gray-900 transition'):
                    with Span(classes='text-sm font-medium', text=' Price '):
                        pass
                    with Span(classes='transition group-open:-rotate-180'):
                        with FontAwesomeIcon(label="faChevronDown",
                                             classes="w-5 h-5",):
                            pass
                        pass

                with Div(classes='border-t border-gray-200 bg-white'):
                    with Header(classes='flex items-center justify-between p-4'):
                        with Span(classes='text-sm text-gray-700', text=' The highest price is $600 '):
                            pass
                        with Button(key="abtn", classes='text-sm text-gray-900 underline underline-offset-4', text='Reset'):
                            pass
                        

                    with Div(classes='border-t border-gray-200 p-4'):
                        with Div(classes='flex justify-between gap-4'):
                            # Price From
                            with Label(for_='FilterPriceFrom', classes='flex items-center gap-2'):
                                with Span(classes='text-sm text-gray-600', text='$'):
                                    pass
                                with TextInput(key='FilterPriceFrom', placeholder='From', classes='w-full rounded-md border-gray-200 shadow-sm sm:text-sm'):
                                    pass

                            # Price To
                            with Label(for_='FilterPriceTo', classes='flex items-center gap-2'):
                                with Span(classes='text-sm text-gray-600', text='$'):
                                    pass
                                
                                with TextInput(key='FilterPriceTo', placeholder='To', classes='w-full rounded-md border-gray-200 shadow-sm sm:text-sm'):
                                    pass
    return comp_box
