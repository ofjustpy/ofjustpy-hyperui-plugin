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


# def Large_Newsletter():
#     with writer_ctx:
#         with Footer(classes="bg-white") as comp_box:
#             with Div(classes="mx-auto max-w-screen-xl px-4 py-16 sm:px-6 lg:px-8"):
#                 with Div(classes="lg:flex lg:items-start lg:gap-8"):
#                     with Div(classes="text-teal-600"):
#                         with Icon_GenericLogo():
#                             pass
#                     with Div(classes="mt-8 grid grid-cols-2 gap-8 lg:mt-0 lg:grid-cols-5 lg:gap-y-16"):
#                         with Div(classes="col-span-2"):
#                             with Div():
#                                 with Img(src="/img/logo.png", alt="Logo", classes="h-8"):
#                                     pass  # Add other attributes as needed
#                             with Paragraph(classes="mt-2 text-sm text-gray-500"):
#                                 Text("Lorem ipsum dolor sit amet, consectetur adipiscing elit. ")
#                         with Div():
#                             with Heading(3, text="Company", classes="text-sm font-medium text-gray-900"):
#                                 pass  # Add other attributes as needed
#                             with Ul(classes="mt-2 space-y-4"):
#                                 with Li():
#                                     with Link(url="/about", text="About"):
#                                         pass  # Add other attributes as needed
#                                 with Li():
#                                     with Link(url="/contact", text="Contact"):
#                                         pass  # Add other attributes as needed
#                         with Div():
#                             with Heading(3, text="Product", classes="text-sm font-medium text-gray-900"):
#                                 pass  # Add other attributes as needed
#                             with Ul(classes="mt-2 space-y-4"):
#                                 with Li():
#                                     with Link(url="/features", text="Features"):
#                                         pass  # Add other attributes as needed
#                                 with Li():
#                                     with Link(url="/pricing", text="Pricing"):
#                                         pass  # Add other attributes as needed
#                         with Div():
#                             with Heading(3, text="Resources", classes="text-sm font-medium text-gray-900"):
#                                 pass  # Add other attributes as needed
#                             with Ul(classes="mt-2 space-y-4"):
#                                 with Li():
#                                     with Link(url="/blog", text="Blog"):
#                                         pass  # Add other attributes as needed
#                                 with Li():
#                                     with Link(url="/guides", text="Guides"):
#                                         pass  # Add other attributes as needed
#                                 with Li():
#                                     with Link(url="/faq", text="FAQ"):
#                                         pass  # Add other attributes as needed
#                         with Div():
#                             with Heading(3, text="Connect", classes="text-sm font-medium text-gray-900"):
#                                 pass  # Add other attributes as needed
#                             with Ul(classes="mt-2 space-y-4"):
#                                 with Li():
#                                     with Link(url="/community", text="Community"):
#                                         pass  # Add other attributes as needed
#                                 with Li():
#                                     with Link(url="/partners", text="Partners"):
#                                         pass  # Add other attributes as needed
#                                 with Li():
#                                     with Link(url="/events", text="Events"):
#                                         pass  # Add other attributes as needed
#                         with Div(classes="col-span-2"):
#                             with Div(classes="text-sm font-medium text-gray-900"):
#                                 Text("Subscribe to our newsletter")
#                             with Form(classes="mt-4 sm:flex sm:max-w-md"):
#                                 with Label(for_="email", classes="sr-only"):
#                                     Text("Email")
#                                 with TextInput(type="email", key="email", autocomplete="email", required=True, classes="min-w-0 flex-1 h-12 border-#dee2e6 rounded-md sm:px-4 sm:py-2 text-base text-gray-900 placeholder-gray-500 focus:outline-none focus:border-teal-600 focus:ring focus:ring-teal-600 focus:ring-opacity-50"):
#                                     pass  # Add other attributes as needed
#                                 with Button(key="submit",
#                                             classes="mt-3 w-full px-4 py-2 border border-transparent rounded-md shadow-sm text-base font-medium text-white bg-teal-600 hover:bg-teal-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-teal-500 sm:mt-0 sm:ml-3 sm:flex-shrink-0 sm:inline-flex sm:items-center sm:justify-center",
#                                             text="Subscribe"):

#     return comp_box

def CenteredWithBranding():
    with writer_ctx:
        with Footer(classes='bg-gray-100') as comp_box:
            with Div(classes='mx-auto max-w-5xl px-4 py-16 sm:px-6 lg:px-8'):
                with Div(classes='flex justify-center text-teal-600'):
                    with FontAwesomeIcon(label="faHippo"):
                        pass
                    pass

                # Main Text Content
                with P(classes='mx-auto mt-6 max-w-md text-center leading-relaxed text-gray-500', text="Lorem ipsum dolor, sit amet consectetur adipisicing elit. Incidunt consequuntur amet culpa cum itaque neque."):
                    
                    pass
                # Navigation Links
                with Ul(classes='mt-12 flex flex-wrap justify-center gap-6 md:gap-8 lg:gap-12') as nav_box:
                    with Li():
                        with A(href='/', classes='text-gray-700 transition hover:text-gray-700/75', text="About"):
                            pass

                    with Li():
                        with A(href='/', classes='text-gray-700 transition hover:text-gray-700/75', text="Careers"):
                            pass

                    with Li():
                        with A(href='/', classes='text-gray-700 transition hover:text-gray-700/75', text="History"):
                            pass

                    with Li():
                        with A(href='/', classes='text-gray-700 transition hover:text-gray-700/75', text="Services"):
                            pass

                    with Li():
                        with A(href='/', classes='text-gray-700 transition hover:text-gray-700/75', text="Projects"):
                            pass

                    with Li():
                        with A(href='/', classes='text-gray-700 transition hover:text-gray-700/75', text="Blog"):
                            pass                        
                    
                    

                    pass


                with Ul(classes='mt-12 flex justify-center gap-6 md:gap-8'):
                    with Li():
                        with A(href='/', rel='noreferrer', target='_blank', classes='text-gray-700 transition hover:text-gray-700/75'):
                            with Span(classes='sr-only'):
                                with FontAwesomeIcon(label="faFacebook",
                                                     fa_group="brands"):
                                    pass

                    with Li():
                        with A(href='/', rel='noreferrer', target='_blank', classes='text-gray-700 transition hover:text-gray-700/75'):
                            with Span(classes='sr-only'):
                                with FontAwesomeIcon(label="faInstagram",
                                                     fa_group="brands"):
                                    pass

                    with Li():
                        with A(href='/', rel='noreferrer', target='_blank', classes='text-gray-700 transition hover:text-gray-700/75'):
                            with Span(classes='sr-only'):
                                with FontAwesomeIcon(label="faTwitter",
                                                     fa_group="brands"):
                                    pass

                    with Li():
                        with A(href='/', rel='noreferrer', target='_blank', classes='text-gray-700 transition hover:text-gray-700/75'):
                            with Span(classes='sr-only'):
                                with FontAwesomeIcon(label="faGithub",
                                                     fa_group="brands"):
                                    pass
                                
                                

    return comp_box


