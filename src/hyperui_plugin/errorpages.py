from html_writer.macro_module import macros, writer_ctx
import ofjustpy as oj

def NotFoundPage():
    with writer_ctx:
        with Div(classes='grid h-screen place-content-center bg-white px-4') as container_div:
            with H1(classes='uppercase tracking-widest text-gray-500', text='404 | Not Found'):
                pass

    return container_div


def Error404Page(href="#"):
    with writer_ctx:
        with Div(classes='grid h-screen place-content-center bg-white px-4') as container_div:
            with Div(classes='text-center') as content_div:
                with H1(classes='text-9xl font-black text-gray-200', text='404'):
                    pass

                with P(classes='text-2xl font-bold tracking-tight text-gray-900 sm:text-4xl', text='Uh-oh!'):
                    pass

                with P(classes='mt-4 text-gray-500', text="We can't find that page."):
                    pass

                with A(href=href, classes='mt-6 inline-block rounded bg-indigo-600 px-5 py-3 text-sm font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring', text='Go Back Home'):
                    pass

    return container_div



def NotFoundPageWithImage(img_src = 'https://images.unsplash.com/photo-1558769132-cb1aea458c5e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1548&q=80'):
    with writer_ctx:
        with Div(classes='flex h-screen flex-col bg-white') as container_div:
            with Img(src=img_src, alt='', classes='h-64 w-full object-cover'):
                pass

            with Div(classes='flex flex-1 items-center justify-center') as content_div:
                with Div(classes='mx-auto max-w-xl px-4 py-8 text-center') as text_container_div:
                    with H1(classes='text-2xl font-bold tracking-tight text-gray-900 sm:text-4xl', text="We can't find that page."):
                        pass

                    with P(classes='mt-4 text-gray-500', text='Try searching again, or return home to start from the beginning.'):
                        pass

                    with A(href='#', classes='mt-6 inline-block rounded bg-indigo-600 px-5 py-3 text-sm font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring', text='Go Back Home'):
                        pass

    return container_div
