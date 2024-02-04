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

def SplitWithImageAndAction(img_src, top_top, top_mid, top_bottom,  link_text, footer_text):
    with writer_ctx:
        with Section(classes="overflow-hidden rounded-lg shadow-2xl md:grid md:grid-cols-3") as comp_box:
            with Img(
                alt="Trainer",
                src=img_src,
                classes="h-32 w-full object-cover md:h-full",
            ):
                pass

            with Div(classes="p-4 text-center sm:p-6 md:col-span-2 lg:p-8"):
                with P(classes="text-sm font-semibold uppercase tracking-widest", text=top_top):
                    pass  # Additional content can be added here

                with H2(classes="mt-6 font-black uppercase"):
                    with Span(classes="text-4xl font-black sm:text-5xl lg:text-6xl", text=top_mid):
                        pass  # Additional content can be added here

                    with Span(classes="mt-2 block text-sm", text=top_bottom):
                        pass  # Additional content can be added here

                with A(
                    text=link_text,
                    classes="mt-8 inline-block w-full bg-black py-4 text-sm font-bold uppercase tracking-widest text-white",
                    href="",
                ):
                    pass

                with P(classes="mt-8 text-xs font-medium uppercase text-gray-400", text=footer_text):
                    pass  # Additional content can be added here

    return comp_box


def MessageNotificationsAndAction(message_title,
                                  message_desc,
                                  action_btn_text1,
                                  action_btn_text2):
    with writer_ctx:
        with Div(classes="rounded-2xl border border-blue-100 bg-white p-4 shadow-lg sm:p-6 lg:p-8", role="alert") as comp_box:
            with Div(classes="flex items-center gap-4"):
                with Span(classes="shrink-0 rounded-full bg-blue-400 p-2 text-white"):
                    with Icon_ShoutOut():
                        pass

                with P(classes="font-medium sm:text-lg", text=message_title):
                    pass
                
            with P(classes="mt-4 text-gray-500", text=message_desc):
                pass

            with Div(classes="mt-6 sm:flex sm:gap-4"):
                with A(classes="inline-block w-full rounded-lg bg-blue-500 px-5 py-3 text-center text-sm font-semibold text-white sm:w-auto", href="", text=action_btn_text1):
                    pass
                with A(classes="mt-2 inline-block w-full rounded-lg bg-gray-50 px-5 py-3 text-center text-sm font-semibold text-gray-500 sm:mt-0 sm:w-auto", href="", text=action_btn_text2):
                    pass


            
    return comp_box



def OrderNotificationsWithAction():
    with writer_ctx:
        with Section(classes="rounded-3xl shadow-2xl") as comp_box:
            with Div(classes="p-8 text-center sm:p-12"):
                with P(classes="text-sm font-semibold uppercase tracking-widest text-pink-500", text="Your order is on the way"):
                    pass

                with H2(classes="mt-6 text-3xl font-bold", text="Thanks for your purchase, we're getting it ready!"):
                    pass

                with A(classes="mt-8 inline-block w-full rounded-full bg-pink-600 py-4 text-sm font-bold text-white shadow-xl", href="", text="Track Order"):
                    pass


    return comp_box

def ContactActions():
    with writer_ctx:
        with Div(classes="rounded-lg border border-gray-100 text-center shadow-xl") as comp_box:
            with Div(classes="px-6 py-5"):
                with P(classes="font-medium", text="Not found your answer?"):
                    pass

                with Div(classes="mt-4 space-y-2"):
                    with A(classes="block rounded-full border border-blue-500 px-8 py-3 text-sm font-medium text-blue-600", href="", text="Message us"):
                        pass
                    with A(classes="block rounded-full border border-gray-500 px-8 py-3 text-sm font-medium text-gray-600", href="", text="Live chat"):
                        pass

                with P(classes="mt-4 inline-flex items-center gap-1.5"):
                    with Span(classes="inline-block h-1.5 w-1.5 rounded-full bg-green-500"):
                        pass
                    with Span(classes="text-xs font-medium text-green-700", text="Chat online"):
                        pass

            with Div(classes="flex justify-center gap-4 border-t border-gray-100 px-6 py-5"):
                with A(classes="rounded-full border border-gray-200 p-2 text-gray-900", href="#"):
                    with Span(classes="sr-only", text="Company Facebook"):
                        pass
                    with Icon_Facebook():
                        pass
                        # Path element and its attributes go here

                with A(classes="rounded-full border border-gray-200 p-2 text-gray-900", href="#"):
                    with Span(classes="sr-only", text="Company Instagram"):
                        pass
                    with Icon_Instagram():
                        pass
                        # Path element and its attributes go here

                with A(classes="rounded-full border border-gray-200 p-2 text-gray-900", href="#"):
                    with Span(classes="sr-only", text="Company Twitter"):
                        pass
                    with Icon_Twitter():
                        pass
                        # Path element and its attributes go here


    return comp_box

def NotificationWithImageAndClose(key):
    with writer_ctx:
        with Div(classes="relative rounded-lg border border-gray-200 shadow-lg") as comp_box:
            with Button(key=key, classes="absolute -end-1 -top-1 rounded-full border border-gray-300 bg-gray-100 p-1"):
                with Span(classes="sr-only", text="Close"):
                    pass
                with Icon_Cross():
                    pass

            with Div(classes="flex items-center gap-4 p-4"):
                with Img(alt="Women", src="https://images.unsplash.com/photo-1611432579699-484f7990b127?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80", classes="h-12 w-12 rounded-lg object-cover"):
                    pass

                with Div():
                    with P(classes="font-medium text-gray-900", text="Carol Daines"):
                        pass

                    with P(classes="line-clamp-1 text-sm text-gray-500", text="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet, laborum?"):
                        pass

    return comp_box

def FloatingSplitWithImageContentClose(key):
    
    with writer_ctx:
        with Div(classes="fixed inset-x-0 bottom-0 p-4") as comp_box:
            with Div(classes="relative max-w-xl rounded-lg bg-gray-100 p-6 shadow-sm"):
                with Button(key=key, classes="absolute -end-1 -top-1 rounded-full border border-gray-200 bg-white p-1 text-gray-400"):
                    with Icon_Cross():
                        pass

                with Div(classes="grid grid-cols-1 gap-4 sm:grid-cols-2"):
                    with Img(alt="Laptop", src="https://images.unsplash.com/photo-1587614382346-4ec70e388b28?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80", classes="h-full w-full rounded-xl object-cover"):
                        pass

                    with Div():
                        with H2(classes="text-lg font-medium", text="Lorem ipsum dolor sit amet consectetur, adipisicing elit."):
                            pass

                        with P(classes="mt-4 text-sm text-gray-500", text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptates, eos. Inventore dolor delectus commodi laudantium adipisci, illum amet itaque optio!"):
                            pass

                        with Div(classes="mt-6 sm:text-right"):
                            with A(href="#", classes="inline-block rounded-lg bg-blue-500 px-5 py-3 text-sm font-medium text-white", text="Find out more"):
                                pass
    return comp_box

def FloatingWithClose(key):
    
    with writer_ctx:
        with Aside(classes="fixed bottom-4 end-4 z-50 flex items-center justify-center gap-4 rounded-lg bg-black px-5 py-3 text-white") as comp_box:
            with A(href="/new-thing", target="_blank", rel="noreferrer", classes="text-sm font-medium hover:opacity-75", text="Hey! Come Check This Out 👋"):
                pass

            with Button(key = key, classes="rounded bg-white/20 p-1 hover:bg-white/10"):
                with Icon_Cross():
                    pass

    return comp_box
