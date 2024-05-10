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


def GridUSP():
    with writer_ctx:
        with Section(classes='bg-gray-900 text-white') as comp_box:
            with Div(classes='max-w-screen-xl px-4 py-8 sm:px-6 sm:py-12 lg:px-8 lg:py-16'):
                with Div(classes='max-w-xl'):
                    with H2(classes='text-3xl font-bold sm:text-4xl', text="What makes us special"):
                        pass
                        

                    with P(classes='mt-4 text-gray-300', text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat dolores iure fugit totam iste obcaecati. Consequatur ipsa quod ipsum sequi culpa delectus, cumque id tenetur quibusdam, quos fuga minima."):
                        pass
                        
                    pass
                
                with Div(classes='mt-8 grid grid-cols-1 gap-8 md:mt-16 md:grid-cols-2 md:gap-12 lg:grid-cols-3'):
                    with Div(classes='flex items-start gap-4'):
                        with Span(classes="shrink-0 rounded-lg bg-gray-800 p-4"):
                            with FontAwesomeIcon(label="faGraduationCap"):
                                pass

                        with Div():
                            with H2(classes='text-lg font-bold', text="Lorem, ipsum dolor."):
                                pass


                            with P(classes='mt-1 text-sm text-gray-300', text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Error cumque tempore est ab possimus quisquam reiciendis tempora animi! Quaerat, saepe."):
                                pass

                    with Div(classes='flex items-start gap-4'):
                        with Span(classes='shrink-0 rounded-lg bg-gray-800 p-4'):
                            with FontAwesomeIcon(label="faGraduationCap"):
                                pass

                        with Div():
                            with H2(classes='text-lg font-bold', text="Lorem, ipsum dolor."):
                                pass


                            with P(classes='mt-1 text-sm text-gray-300', text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Error cumque tempore est ab possimus quisquam reiciendis tempora animi! Quaerat, saepe."):
                                pass
                    with Div(classes='flex items-start gap-4'):
                        with Span(classes='shrink-0 rounded-lg bg-gray-800 p-4'):

                            with FontAwesomeIcon(label="faGraduationCap"):
                                pass

                        with Div():
                            with H2(classes='text-lg font-bold', text="Lorem, ipsum dolor."):
                                pass


                            with P(classes='mt-1 text-sm text-gray-300', text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Error cumque tempore est ab possimus quisquam reiciendis tempora animi! Quaerat, saepe."):
                                pass                            
                    with Div(classes='flex items-start gap-4'):
                        with Span(classes='shrink-0 rounded-lg bg-gray-800 p-4'):
                            with FontAwesomeIcon(label="faGraduationCap"):
                                pass

                        with Div():
                            with H2(classes='text-lg font-bold', text="Lorem, ipsum dolor."):
                                pass


                            with P(classes='mt-1 text-sm text-gray-300', text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Error cumque tempore est ab possimus quisquam reiciendis tempora animi! Quaerat, saepe."):
                                pass


                    with Div(classes='flex items-start gap-4'):
                        with Span(classes='shrink-0 rounded-lg bg-gray-800 p-4'):
                            with FontAwesomeIcon(label="faGraduationCap"):
                                pass

                        with Div():
                            with H2(classes='text-lg font-bold', text="Lorem, ipsum dolor."):
                                pass


                            with P(classes='mt-1 text-sm text-gray-300', text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Error cumque tempore est ab possimus quisquam reiciendis tempora animi! Quaerat, saepe."):
                                pass

                    with Div(classes='flex items-start gap-4'):
                        with Span(classes='shrink-0 rounded-lg bg-gray-800 p-4'):
                            with FontAwesomeIcon(label="faGraduationCap"):
                                pass

                        with Div():
                            with H2(classes='text-lg font-bold', text="Lorem, ipsum dolor."):
                                pass


                            with P(classes='mt-1 text-sm text-gray-300', text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Error cumque tempore est ab possimus quisquam reiciendis tempora animi! Quaerat, saepe."):
                                pass
                            
    return comp_box
