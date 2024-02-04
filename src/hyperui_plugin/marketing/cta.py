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


def ContentAndImage():
    with writer_ctx:
        with Section(classes='overflow-hidden bg-gray-50 sm:grid sm:grid-cols-2') as comp_box:
            # Left Content
            with Div(classes='p-8 md:p-12 lg:px-16 lg:py-24'):
                with Div(classes='mx-auto max-w-xl text-center ltr:sm:text-left rtl:sm:text-right'):
                    with H2(classes='text-2xl font-bold text-gray-900 md:text-3xl', text="Lorem, ipsum dolor sit amet consectetur adipisicing elit"):
                        pass
                        

                    with P(classes='hidden text-gray-500 md:mt-4 md:block', text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Et, egestas tempus tellus etiam sed. Quam a scelerisque amet ullamcorper eu enim et fermentum, augue. Aliquet amet volutpat quisque ut interdum tincidunt duis."):
                        pass
                        
                    with Div(classes='mt-4 md:mt-8'):
                        with A(href='#', classes='inline-block rounded bg-emerald-600 px-12 py-3 text-sm font-medium text-white transition hover:bg-emerald-700 focus:outline-none focus:ring focus:ring-yellow-400', text="Get Started Today"):
                            
                            pass
            # Right Content (Image)
            with Img(alt='Student',
                     src='https://images.unsplash.com/photo-1464582883107-8adf2dca8a9f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80',
                     classes='h-56 w-full object-cover sm:h-full'):
                pass

    return comp_box




def NewsletterSignup():
    with writer_ctx:
        with Section(classes='bg-gray-50') as comp_box:
            with Div(classes='p-8 md:p-12 lg:px-16 lg:py-24'):
                # Text Content
                with Div(classes='mx-auto max-w-lg text-center'):
                    with H2(classes='text-2xl font-bold text-gray-900 md:text-3xl', text="Lorem, ipsum dolor sit amet consectetur adipisicing elit"):
                        pass

                    with P(classes='hidden text-gray-500 sm:mt-4 sm:block', text="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quae dolor officia blanditiis repellat in, vero, aperiam porro ipsum laboriosam consequuntur exercitationem incidunt tempora nisi?"):
                        pass
                        

                # Signup Form
                with Div(classes='mx-auto mt-8 max-w-xl'):
                    with Form(action='#', key="form",  classes='sm:flex sm:gap-4'):
                        with Div(classes='sm:flex-1'):
                            with Label(for_='email', classes='sr-only', text="Email"):
                                pass
                            with TextInput(key='email', placeholder='Email address', classes='w-full rounded-md border-gray-200 bg-white p-3 text-gray-700 shadow-sm transition focus:border-white focus:outline-none focus:ring focus:ring-yellow-400'):
                                pass

                        with Button(key='submit', classes='group mt-4 flex w-full items-center justify-center gap-2 rounded-md bg-rose-600 px-5 py-3 text-white transition focus:outline-none focus:ring focus:ring-yellow-400 sm:mt-0 sm:w-auto'):
                            with Span(classes='text-sm font-medium', text="Sign Up"):
                                pass
                                
    return comp_box

