import ofjustpy as oj
from html_writer.macro_module import macros, writer_ctx
# TODO: make this mutable with next button
from py_tailwind_utils import W, full

# TODO: make adding steps as member function 
def WithTextAndIcon(key):
    """

    """
    with writer_ctx:
        with HCCMutable_Div() as comp_box:
            with H2(classes='sr-only', text='Steps'):
                pass

            with HCCMutable_Div():
                with HCCMutable_Div(classes='overflow-hidden rounded-full bg-gray-200'):
                    with Mutable_Div(key=key, classes='h-2 w-1/3 rounded-full bg-blue-500') as pb_comp:
                        pass

                with Ol(classes='mt-4 grid grid-cols-3 text-sm space-x-8 font-medium text-gray-500'):
                    with Li(classes='flex items-center justify-start text-blue-600 sm:gap-1.5'):
                        with Span(classes='hidden sm:inline', text='Details'):
                            pass

                        with Icon_IdCard():
                            pass

                    with Li(classes='flex items-center justify-center text-blue-600 sm:gap-1.5'):
                        with Span(classes='hidden sm:inline', text='Address'):
                            pass

                        with Icon_AddressPin():
                            pass


                    with Li(classes='flex items-center justify-end sm:gap-1.5'):
                        with Span(classes='hidden sm:inline', text='Payment'):
                            pass

                        with Icon_PaymentCard():
                            pass

    cur_pos = 2
    def on_next_step_click(dbref, msg, to_ms, pb_comp=pb_comp):
        nonlocal cur_pos
        milestones = [W/"0", W/"1/4", W/"1/3", W/"3/4", W/"full"]
        pb_comp_ms = to_ms(pb_comp)
        pb_comp_ms.add_twsty_tags(milestones[cur_pos])
        cur_pos = (cur_pos + 1)%5
        print (cur_pos)
        
    abtn = oj.AC.Button(key="abtn", text="Next Step",  on_click=on_next_step_click, classes="border border-gray-200 rounded-full text-sm")
    return comp_box, abtn


# TODO: incomplete -- unclear how to incorporate this
# def WithDescription():

#     with writer_ctx:
#         with Div():
#             with H2(classes='sr-only', text='Steps'):
#                 pass

#             with Div():
#                 with Div(classes='overflow-hidden rounded-full bg-gray-200'):
#                     with Div(classes='h-2 w-1/2 rounded-full bg-blue-500'):
#                         pass

#                 with Ol(classes='mt-4 grid grid-cols-3 text-sm font-medium text-gray-500'):
#                     with Li(classes='flex items-center justify-start text-blue-600 sm:gap-1.5'):
#                         with Span(classes='hidden sm:inline', text='Details'):
#                             pass

#                         with Svg(xmlns='http://www.w3.org/2000/svg', classes='h-6 w-6 sm:h-5 sm:w-5', fill='none', viewBox='0 0 24 24', stroke='currentColor', stroke_width='2'):
#                             with Path(stroke_linecap='round', stroke_linejoin='round', d='M10 6H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V8a2 2 0 00-2-2h-5m-4 0V5a2 2 0 114 0v1m-4 0a2 2 0 104 0m-5 8a2 2 0 100-4 2 2 0 000 4zm0 0c1.306 0 2.417.835 2.83 2M9 14a3.001 3.001 0 00-2.83 2M15 11h3m-3 4h2'):
#                                 pass

#                     with Li(classes='flex items-center justify-center text-blue-600 sm:gap-1.5'):
#                         with Span(classes='hidden sm:inline', text='Address'):
#                             pass

#                         with Svg(xmlns='http://www.w3.org/2000/svg', classes='h-6 w-6 sm:h-5 sm:w-5', fill='none', viewBox='0 0 24 24', stroke='currentColor', stroke_width='2'):
#                             with Path(stroke_linecap='round', stroke_linejoin='round', d='M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z'):
#                                 pass

#                             with Path(stroke_linecap='round', stroke_linejoin='round', d='M15 11a3 3 0 11-6 0 3 3 0 016 0z'):
#                                 pass

#                     with Li(classes='flex items-center justify-end sm:gap-1.5'):
#                         with Span(classes='hidden sm:inline', text='Payment'):
#                             pass

#                         with Svg(xmlns='http://www.w3.org/2000/svg', classes='h-6 w-6 sm:h-5 sm:w-5', fill='none', viewBox='0 0 24 24', stroke='currentColor', stroke_width='2'):
#                             with Path(stroke_linecap='round', stroke_linejoin='round', d='M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z'):
#                                 pass

from html_writer.macro_module import macros, writer_ctx

def WithCheckIcons(key):
    
    with writer_ctx:
        with Div() as comp_box:
            with H2(classes='sr-only', text='Steps'):
                pass

            with Div(classes='after:mt-4 after:block after:h-1 after:w-full after:rounded-lg after:bg-gray-200'):
                with Ol(classes='grid grid-cols-3 text-sm space-x-8 font-medium text-gray-500'):
                    with Li(classes='relative flex justify-start text-blue-600'):
                        with Span(classes='absolute -bottom-[1.75rem] start-0 rounded-full bg-blue-600 text-white'):
                            with Icon_EncircledCheckmark():
                                pass

                        with Span(classes='hidden sm:block', text='Details'):
                            pass

                        # with Icon_AddressPin():
                        #     pass

                    with Li(classes='relative flex justify-center text-blue-600'):
                        with Span(classes='absolute -bottom-[1.75rem] left-1/2 -translate-x-1/2 rounded-full bg-blue-600 text-white'):
                            with Icon_EncircledCheckmark():
                                pass

                        with Span(classes='hidden sm:block', text='Address'):
                            pass

                        # with Icon_AddressPin():
                        #     pass



                    with Li(classes='relative flex justify-end'):
                        with Span(classes='absolute -bottom-[1.75rem] end-0 rounded-full bg-gray-600 text-white'):
                            with Icon_EncircledCheckmark():
                                pass
                            

                        with Span(classes='hidden sm:block', text='Payment'):
                            pass

                        # with Icon_AddressPin():
                        #     pass
    return comp_box

def WithChevronTextIcon():
    with writer_ctx:
        with Div() as comp_box:
            with H2(classes='sr-only', text='Steps'):
                pass

            with Div():
                with Ol(classes='grid grid-cols-1 divide-x divide-gray-100 overflow-hidden rounded-lg border border-gray-100 text-sm text-gray-500 sm:grid-cols-3'):
                    with Li(classes='flex items-center justify-center gap-2 p-4'):
                        with Icon_IdCard():
                            pass

                        with P(classes='leading-none'):
                            with Strong(classes='block font-medium', text='Details'):
                                pass

                            with Small(classes='mt-1', text='Some info about you.'):
                                pass

                    with Li(classes='relative flex items-center justify-center gap-2 bg-gray-50 p-4'):
                        with Span(classes='absolute -left-2 top-1/2 hidden h-4 w-4 -translate-y-1/2 rotate-45 border border-gray-100 ltr:border-b-0 ltr:border-s-0 ltr:bg-white rtl:border-e-0 rtl:border-t-0 rtl:bg-gray-50 sm:block'):
                            pass

                        with Span(classes='absolute -right-2 top-1/2 hidden h-4 w-4 -translate-y-1/2 rotate-45 border border-gray-100 ltr:border-b-0 ltr:border-s-0 ltr:bg-gray-50 rtl:border-e-0 rtl:border-t-0 rtl:bg-white sm:block'):
                            pass

                        with Icon_AddressPin():
                                pass

                        with P(classes='leading-none'):
                            with Strong(classes='block font-medium', text='Address'):
                                pass

                            with Small(classes='mt-1', text='Where we sending it?'):
                                pass

                    with Li(classes='flex items-center justify-center gap-2 p-4'):
                        with Icon_PaymentCard():
                            pass

                        with P(classes='leading-none'):
                            with Strong(classes='block font-medium', text='Payment'):
                                pass

                            with Small(classes='mt-1', text='Show us the money.'):
                                pass

    return comp_box
