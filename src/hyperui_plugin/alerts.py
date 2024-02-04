import ofjustpy as oj
from ofjustpy import icons
from html_writer.macro_module import macros, writer_ctx

def Popup(key, title='', desc=''):
    with writer_ctx:
        with Div(role='alert', classes='rounded-xl border border-gray-100 bg-white p-4 dark:border-gray-800 dark:bg-gray-900') as comp_box:
            with Div(classes='flex items-start gap-4'):
                with Span(classes='text-green-600'):
                    with Icon_EncircledCheckmark():
                        pass
                    pass

                with Div(classes='flex-1'):
                    with Strong(classes='block font-medium text-gray-900 dark:text-white', text=f'{title}'):
                        pass

                    with P(classes='mt-1 text-sm text-gray-700 dark:text-gray-200', text=f'{desc}'):
                        pass

                with Button(key=f"cross_{key}", classes='text-gray-500 transition hover:text-gray-600 dark:text-gray-400 dark:hover:text-gray-500'):
                    with Span(classes='sr-only', text='Dismiss popup'):
                        pass
                    with Icon_Cross():
                        pass

    return comp_box

# Example usage


def PopupWithAction(key, title='', desc=''):
    with writer_ctx:
        with Div(role='alert', classes='rounded-xl border border-gray-100 bg-white p-4 dark:border-gray-800 dark:bg-gray-900') as comp_box:
            with Div(classes='flex items-start gap-4'):
                with Span(classes='text-green-600'):
                    with Icon_EncircledCheckmark():
                        pass
                    pass

                with Div(classes='flex-1'):
                    with Strong(classes='block font-medium text-gray-900 dark:text-white', text=f'{title}'):
                        pass

                    with P(classes='mt-1 text-sm text-gray-700 dark:text-gray-200', text=f'{desc}'):
                        pass

                    with Div(classes='mt-4 flex gap-2'):
                        with A(href='#', classes='inline-flex items-center gap-2 rounded-lg bg-indigo-600 px-4 py-2 text-white hover:bg-indigo-700'):
                            with Span(classes='text-sm', text=' Preview '):
                                pass
                            with Icon_Preview():
                                pass
                    

                        with Button(key="revert_{key}", classes='block rounded-lg px-4 py-2 text-gray-700 transition hover:bg-gray-50'):
                            with Span(classes='text-sm', text='Revert'):
                                pass

                with Button(key=f"cross_{key}", classes='text-gray-500 transition hover:text-gray-600 dark:text-gray-400 dark:hover:text-gray-500'):
                    with Span(classes='sr-only', text='Dismiss popup'):
                        with Icon_Cross():
                            pass
                        pass


    return comp_box

def Content(title='', content=''):
    with writer_ctx:
        with Div(role='alert', classes='rounded border-s-4 border-red-500 bg-red-50 p-4') as alert_div:

            with Strong(classes='block font-medium text-red-800', text=title):
                pass

            with P(classes='mt-2 text-sm text-red-700', text=content):
                pass

    return alert_div

def WarningContent(title='', content=''):
    with writer_ctx:
        with Div(role='alert', classes='rounded border-s-4 border-red-500 bg-red-50 p-4') as alert_div:

            with Div(classes="flex items-center gap-2 text-red-800"):
                with Icon_Warning():
                    pass
                    
                with Strong(classes='block font-medium text-red-800', text=title):
                    pass

            with P(classes='mt-2 text-sm text-red-700', text=content):
                pass

    return alert_div
