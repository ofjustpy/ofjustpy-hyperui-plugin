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


def SplitContentSlider():
    with writer_ctx:
        with Section(classes='bg-gray-50') as comp_box:
            with Div(classes='mx-auto px-4 py-12 sm:px-6 lg:me-0 lg:py-16 lg:pe-0 lg:ps-8 xl:py-24', extra_classes="max-w-[1340px]"):
                with Div(classes='grid grid-cols-1 gap-8 lg:grid-cols-3 lg:items-center lg:gap-16'):
                    with Div(classes='max-w-xl text-center ltr:sm:text-left rtl:sm:text-right'):
                        with H2(classes='text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl', text="Don't just take our word for it..."):
                            pass
                            

                        with Prose(classes='mt-4 text-gray-700', text="Lorem ipsum, dolor sit amet consectetur adipisicing elit. Voluptas veritatis illo placeat harum porro optio fugit a culpa sunt id!"):
                            pass
                            

                        with Div(classes='hidden lg:mt-8 lg:flex lg:gap-4'):
                            with Button(
                                classes='rounded-full border border-rose-600 p-3 text-rose-600 transition hover:bg-rose-600 hover:text-white',
                                aria_label='Previous slide',
                                key='keen-slider-previous-desktop'
                            ):
                                with Icon_SliderPrev():
                                    pass
                                # Empty button for the visual representation of previous slide
                                pass
                            with Button(
                                classes='rounded-full border border-rose-600 p-3 text-rose-600 transition hover:bg-rose-600 hover:text-white',
                                aria_label='Next slide',
                                key='keen-slider-next-desktop'
                            ):
                                with Icon_SliderNext():
                                    pass
                                # Empty button for the visual representation of next slide
                                pass
                    with Div(classes='-mx-6 lg:col-span-2 lg:mx-0'):
                        with Div(classes='', id='keen-slider'):
                            with Div(classes=''):
                                with Div(
                                    classes='flex h-full flex-col justify-between bg-white p-6 shadow-sm sm:p-8 lg:p-12'
                                ):
                                    with Div():
                                        with Div(classes='flex gap-0.5 text-green-500'):
                                            with Icon_Rated():
                                                pass
                                            
                                            with Icon_Rated():
                                                pass

                                            with Icon_Rated():
                                                pass

                                            with Icon_Rated():
                                                pass
                                            
                                            with Icon_Rated():
                                                pass

                                            with Icon_Rated():
                                                pass                                            
                                           
                                            
                                            
                                        with Div(classes='mt-4'):
                                            with P(classes='text-2xl font-bold text-rose-600 sm:text-3xl', text="Stayin' Alive"):
                                                pass

                                            with P(classes='mt-4 leading-relaxed text-gray-700' , text="No, Rose, they are not breathing. And they have no arms or legs … Where are they? You know what? If we come across somebody with no arms or legs, do we bother resuscitating them? I mean, what quality of life do we have there?"):
                                                pass
                                                

                                    with Footer(classes='mt-4 text-sm font-medium text-gray-700 sm:mt-6', text="Michael Scott"):
                                        pass
                                        

                with Div(classes='mt-8 flex justify-center gap-4 lg:hidden'):
                    with Button(
                        classes='rounded-full border border-rose-600 p-4 text-rose-600 transition hover:bg-rose-600 hover:text-white',
                        aria_label='Previous slide',
                            key='keen-slider-previous'
                    ):
                        # Empty button for the visual representation of previous slide
                        pass
                    with Button(
                        classes='rounded-full border border-rose-600 p-4 text-rose-600 transition hover:bg-rose-600 hover:text-white',
                        aria_label='Next slide',
                        key='keen-slider-next'
                    ):
                        # Empty button for the visual representation of next slide

                        pass
    return comp_box
