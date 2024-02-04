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

def WithAction():
    with writer_ctx:
        with Div(classes='bg-indigo-600 px-4 py-3 text-white sm:flex sm:items-center sm:justify-between sm:px-6 lg:px-8') as comp_box:
            with Prose(classes='text-center font-medium sm:text-left', text="Love Alpine JS?"):
                
                with Br(classes='sm:hidden', text="Check out this new deep dive course!"):
                    pass
            with A(classes='mt-4 block rounded-lg bg-white px-5 py-3 text-center text-sm font-medium text-indigo-600 transition hover:bg-white/90 focus:outline-none focus:ring active:text-indigo-500 sm:mt-0', href='#', text="Learn More"):
                pass
            
    return comp_box




def BottomWithClose():
    with writer_ctx:
        with Div(classes='fixed inset-x-0 bottom-0 p-4') as comp_box:
            with Div(classes='relative flex items-center justify-between gap-4 rounded-lg bg-indigo-600 px-4 py-3 text-white shadow-lg'):
                with Prose(classes='text-sm font-medium', text="Love Alpine JS?"):
                    
                    with A(classes='inline-block underline', href='#', text="Check out this new course!"):
                        pass
                        

                with Button(key="close", classes='shrink-0 rounded-lg bg-black/10 p-1 transition hover:bg-black/20', aria_label='Close'):
                    with Icon_Cross():
                        pass


    return comp_box

# TODO: incomplete; incorporate swiper js module
# def SwiperSlider():
#     with writer_ctx:
#         with Div(classes='bg-gray-100 px-4 py-3') as comp_box:
#             with Div(classes='mx-auto flex max-w-3xl items-center justify-center'):
#                 with Button(key="abtn", classes='swiper-prev-button hidden hover:text-gray-500 sm:block sm:rounded sm:text-gray-700 sm:transition', aria_label='Previous slide'):
#                     with Icon_Chevronleft():
#                         pass

#                 with Div(classes='swiper'):
#                     with Div(classes='swiper-wrapper'):
#                         # Slide 1
#                         with Div(classes='swiper-slide'):
#                             with Prose(classes='text-center text-sm font-medium text-gray-900', text="Love Alpine JS?"):
                                
#                                 with A(classes='block underline sm:inline-block', href='#', text="Check out this new course!"):
#                                    pass 

#                         # Slide 2
#                         with Div(classes='swiper-slide'):
#                             with Prose(classes='text-center text-sm font-medium text-gray-900', text="Love Tailwind CSS?"):
#                                 with A(classes='block underline sm:inline-block', href='#', text="Check out this new course!"):
#                                     pass

#                         # Slide 3
#                         with Div(classes='swiper-slide'):
#                             with Prose(classes='text-center text-sm font-medium text-gray-900', text="Love Laravel?"):
#                                 with A(classes='block underline sm:inline-block', href='#', text="Check out this new course!"):
#                                     pass
#                 with Button(key="abtn", classes='swiper-next-button hidden hover:text-gray-500 sm:block sm:rounded sm:text-gray-700 sm:transition', aria_label='Next slide'):
#                     with Icon_Chevronright():
#                         pass
                    

                        
#     return comp_box
