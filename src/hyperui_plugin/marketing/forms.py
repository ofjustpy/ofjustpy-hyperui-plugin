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


def Login():
    
    with writer_ctx:
        with Div(classes='mx-auto max-w-screen-xl px-4 py-16 sm:px-6 lg:px-8') as comp_box:
            with Div(classes='mx-auto max-w-lg text-center'):
                with H1(classes='text-2xl font-bold sm:text-3xl', text="Get started today!"):
                    pass

                with P(classes='mt-4 text-gray-500', text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Et libero nulla eaque error neque ipsa culpa autem, at itaque nostrum!"):
                    pass
                    

            # Form
            with Form(key="form", action='', classes='mx-auto mb-0 mt-8 max-w-md space-y-4'):
                with Div():
                    with Label(for_='email', classes='sr-only', text="Email"):
                        pass
                    with Div(classes='relative'):
                        with TextInput(type='email', key="email", classes='w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm', placeholder='Enter email'):
                            pass

                        with Span(classes='absolute inset-y-0 end-0 grid place-content-center px-4'):
                            with FontAwesomeIcon(label="faAt"):
                                pass
                            pass

                # Password Input
                with Div():
                    with Label(for_='password', classes='sr-only', text="Password"):
                        pass
                    with Div(classes='relative'):
                        with TextInput(type='password', key="password", classes='w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm', placeholder='Enter password'):
                            pass

                        with Span(classes='absolute inset-y-0 end-0 grid place-content-center px-4'):
                            with FontAwesomeIcon(label="faAt"):
                                pass
                            pass

                # Sign Up Link and Sign In Button
                with Div(classes='flex items-center justify-between'):
                    with P(classes='text-sm text-gray-500', text="No account?"):
                        with A(classes='underline', href='', text="Sign up"):
                            pass

                    with Button(type='submit',
                                classes='inline-block rounded-lg bg-blue-500 px-5 py-3 text-sm font-medium text-white', key="submit"):
                        pass
                        

    return comp_box

