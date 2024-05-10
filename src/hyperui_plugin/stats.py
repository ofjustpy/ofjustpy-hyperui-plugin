import ofjustpy as oj
from ofjustpy.icons import FontAwesomeIcon
from html_writer.macro_module import macros, writer_ctx

#TODO: make it a proper plugabble component: remove hardwiring of values.
def Simple():
    
    with writer_ctx:
        with Article(classes="flex flex-col gap-4 rounded-lg border border-gray-100 bg-white p-6") as comp_1:

            with Div(classes='inline-flex gap-2 self-end rounded bg-green-100 p-1 text-green-600') :
                with FontAwesomeIcon(label="faChartLine"):
                    pass

                with Span(classes='text-xs font-medium', text='67.81%'):
                    pass

            with Div():
                with Strong(classes='block text-sm font-medium text-gray-500', text='Profit'):
                    pass

                with P():
                    with Span(classes='text-2xl font-medium text-gray-900', text='$404.32'):
                        pass

                    with Span(classes='text-xs text-gray-500', text='from $240.94'):
                        pass

    with writer_ctx:
        with Article(classes="flex flex-col gap-4 rounded-lg border border-gray-100 bg-white p-6") as comp_2:
            with Div(classes='inline-flex gap-2 self-end rounded bg-red-100 p-1 text-red-600'):
                with FontAwesomeIcon(label="faCircleQuestion"):
                    pass

                with Span(classes='text-xs font-medium', text='67.81%'):
                    pass

            with Div():
                with Strong(classes='block text-sm font-medium text-gray-500', text='Profit'):
                    pass

                with P():
                    with Span(classes='text-2xl font-medium text-gray-900', text='$240.94'):
                        pass

                    with Span(classes='text-xs text-gray-500', text='from $404.32'):
                        pass


    return oj.PC.Div(childs=[comp_1, comp_2], classes="space-y-2")

def IconStat():
    with writer_ctx:
        with Article(classes='flex items-end justify-between rounded-lg border border-gray-100 bg-white p-6') as comp_1:
            with Div(classes='flex items-center gap-4'):
                with Span(classes='hidden rounded-full bg-gray-100 p-2 text-gray-600 sm:block'):
                    with FontAwesomeIcon(label="faMoneyBill"):
                        pass

                with Div():
                    with P(classes='text-sm text-gray-500', text='Profit'):
                        pass

                    with P():
                        with Span(classes='text-2xl font-medium text-gray-900', text='$240.94'):
                            pass

            with Div(classes='inline-flex gap-2 rounded bg-green-100 p-1 text-green-600'):
                with FontAwesomeIcon(label="faCircleQuestion"):
                    pass

                with Span(classes='text-xs font-medium', text='67.81%'):
                    pass

    with writer_ctx:
        with Article(classes='flex items-end justify-between rounded-lg border border-gray-100 bg-white p-6') as comp_2:
            with Div(classes='flex items-center gap-4'):
                with Span(classes='hidden rounded-full bg-gray-100 p-2 text-gray-600 sm:block'):
                    with FontAwesomeIcon(label="faMoneyBill"):
                        pass

                with Div():
                    with P(classes='text-sm text-gray-500', text='Profit'):
                        pass

                    with P():
                        with Span(classes='text-2xl font-medium text-gray-900', text='$240.94'):
                            pass

            with Div(classes='inline-flex gap-2 rounded bg-red-100 p-1 text-red-600'):
                with FontAwesomeIcon(label="faCircleQuestion"):
                    pass
                with Span(classes='text-xs font-medium', text='67.81%'):
                    pass
    return oj.PC.Div(childs=[comp_1, comp_2], classes="space-y-2")

def SimpleWithStat():
    with writer_ctx:
        with Article(classes='flex items-end justify-between rounded-lg border border-gray-100 bg-white p-6')  as comp_1:
            with Div():
                with P(classes='text-sm text-gray-500', text='Profit'):
                    pass

                with P():
                    with Span(classes='text-2xl font-medium text-gray-900', text='$240.94'):
                        pass

            with Div(classes='inline-flex gap-2 rounded bg-green-100 p-1 text-green-600'):
                with FontAwesomeIcon(label="faCircleQuestion"):
                    pass

                with Span(classes='text-xs font-medium', text='67.81%'):
                    pass

    with writer_ctx:
        with Article(classes='flex items-end justify-between rounded-lg border border-gray-100 bg-white p-6') as comp_2:
            with Div():
                with P(classes='text-sm text-gray-500', text='Profit'):
                    pass

                with P():
                    with Span(classes='text-2xl font-medium text-gray-900', text='$240.94'):
                        pass

            with Div(classes='inline-flex gap-2 rounded bg-red-100 p-1 text-red-600'):
                with FontAwesomeIcon(label="faCircleQuestion"):
                    pass

                with Span(classes='text-xs font-medium', text='67.81%'):
                    pass
    return oj.PC.Div(childs=[comp_1, comp_2], classes="space-y-2")
