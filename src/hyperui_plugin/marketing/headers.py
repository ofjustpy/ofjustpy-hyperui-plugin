import ofjustpy as oj
from ofjustpy import icons
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

def LeftAligned():
    with writer_ctx:
        with Header(classes='bg-white') as comp_box: 
            with Div(classes='mx-auto flex h-16 max-w-screen-xl items-center gap-8 px-4 sm:px-6 lg:px-8'):
                with A(classes='block text-teal-600', href='/'):
                    with Span(classes='sr-only', text="Home"):
                        pass
                    with FontAwesomeIcon(label="faHippo"):
                        pass
                    
                with Div(classes='flex flex-1 items-center justify-end md:justify-between'):
                    with Nav(aria_label='Global', classes='hidden md:block'):
                        with Ul(classes='flex items-center gap-6 text-sm'):
                            with Li():
                                with A(classes='text-gray-500 transition hover:text-gray-500/75', href='/', text='About'):
                                    pass
                            with Li():
                                with A(classes='text-gray-500 transition hover:text-gray-500/75', href='/', text='Careers'):
                                    pass
                            with Li():
                                with A(classes='text-gray-500 transition hover:text-gray-500/75', href='/', text='History'):
                                    pass
                            with Li():
                                with A(classes='text-gray-500 transition hover:text-gray-500/75', href='/', text='Services'):
                                    pass
                            with Li():
                                with A(classes='text-gray-500 transition hover:text-gray-500/75', href='/', text='Projects'):
                                    pass
                            with Li():
                                with A(classes='text-gray-500 transition hover:text-gray-500/75', href='/', text='Blog'):
                                    pass
    
                    with Div(classes='flex items-center gap-4'):
                        with Div(classes='sm:flex sm:gap-4'):
                            # Login Button
                            with A(classes='block rounded-md bg-teal-600 px-5 py-2.5 text-sm font-medium text-white transition hover:bg-teal-700', href='/', text="Login"):
                                pass

                            # Register Button (hidden on small screens)
                            with A(classes='hidden rounded-md bg-gray-100 px-5 py-2.5 text-sm font-medium text-teal-600 transition hover:text-teal-600/75 sm:block', href='/', text="Register"):
                                pass
                        # Mobile Menu Toggle Button
                        with Button(key="btn", classes='block rounded bg-gray-100 p-2.5 text-gray-600 transition hover:text-gray-600/75 md:hidden'):
                            with Span(classes='sr-only', text="Toggle menu"):
                                with FontAwesomeIcon(label="faBars"):
                                    pass


    return comp_box
