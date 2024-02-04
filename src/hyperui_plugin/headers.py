from ofjustpy import icons
from py_tailwind_utils.to_twsty_expr import encode_twstr
import ofjustpy as oj
from py_tailwind_utils import conc_twtags, tstr, pd, grow

from html_writer.macro_module import macros, writer_ctx

def IntroActions(key, title, subtitle):
    with writer_ctx:
        with Header() as comp_box:
            with Div(classes='mx-auto max-w-screen-xl px-4 py-8 sm:px-6 sm:py-12 lg:px-8') as header_container:
                with Div(classes='sm:flex sm:items-center sm:justify-between'):

                    with Div(classes='text-center sm:text-left') as text_div:
                        with H1(classes='text-2xl font-bold text-gray-900 sm:text-3xl', text=title):
                            pass

                        with P(classes='mt-1.5 text-sm text-gray-500', text=subtitle):
                            pass

                    with Div(classes='mt-4 flex flex-col gap-4 sm:mt-0 sm:flex-row sm:items-center') as button_div:
                        with Button(key=f"{key}_viewWebsite",classes='inline-flex items-center justify-center gap-1.5 rounded-lg border border-gray-200 px-5 py-3 text-gray-500 transition hover:bg-gray-50 hover:text-gray-700 focus:outline-none focus:ring') as view_website_button:
                            with Span(classes='text-sm font-medium', text='View Website'):
                                pass
                            with Icon_Openlink():
                                pass

                        with Button(key="{key}_viewpost", classes='block rounded-lg bg-indigo-600 px-5 py-3 text-sm font-medium text-white transition hover:bg-indigo-700 focus:outline-none focus:ring', text='Create Post'):
                            pass

    return comp_box



# TODO: make texts as arguments
def IntroWithSearchAndMiniNavigation(key):
    with writer_ctx:
        with Header(classes='bg-gray-50') as comp_box:
            with Div(classes='mx-auto max-w-screen-xl px-4 py-8 sm:px-6 lg:px-8') as header_container:
                with Div(classes='flex items-center justify-end gap-4'):

                    with Div(classes='flex items-center gap-4') as search_and_notification_div:
                        with Div(classes='relative') as search_input_container:
                            with Label(classes='sr-only', for_='search', text="Search"):
                                pass

                            with TextInput(classes='h-10 w-full rounded-full border-none bg-white pe-10 ps-4 text-sm shadow-sm sm:w-56', key=f'{key}_search_input',  placeholder='Search website...'):
                                pass

                            with Button(key=f"{key}_search_btn", classes='absolute end-1 top-1/2 -translate-y-1/2 rounded-full bg-gray-50 p-2 text-gray-600 transition hover:text-gray-700', type='button') as search_button:
                                with Span(classes='sr-only', text='Search'):
                                    pass

                                with Icon_Search():
                                    pass

                        with A(href='#', classes='block shrink-0 rounded-full bg-white p-2.5 text-gray-600 shadow-sm hover:text-gray-700') as notification_link:
                            with Span(classes='sr-only', text='Notifications'):
                                pass

                            with Icon_Notification():
                                pass
                    with Span(classes='block h-6 w-px rounded-full bg-gray-200', aria_hidden='true'):
                        pass

                    with A(href='#', classes='block shrink-0') as profile_link:
                        with Span(classes='sr-only', text='Profile'):
                            pass
                        with Img(src='https://images.unsplash.com/photo-1600486913747-55e5470d6f40?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80', alt='Man', classes='h-10 w-10 rounded-full object-cover'):
                            pass

                with Div(classes='mt-8') as text_content_div:
                    with H1(classes='text-2xl font-bold text-gray-900 sm:text-3xl', text='Welcome Back, Barry!'):
                        pass

                    with P(classes='mt-1.5 text-sm text-gray-500', text='Your website has seen a 52% increase in traffic in the last month. Keep it up! 🚀'):
                        pass

    return comp_box
