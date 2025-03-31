import ofjustpy as oj
from ofjustpy.icons import FontAwesomeIcon
from html_writer.macro_module import macros, writer_ctx


# TODO: do we need name argument
def Base(key, title, **kwargs):
    with writer_ctx:
        with Div() as comp_box:
            with Label(for_='HeadlineAct', classes='block text-sm font-medium text-gray-900', text=title):
                pass

            with Select(key=f"{key}_select_box", classes='mt-1.5 p-2 w-full rounded-lg bg-white border border-gray-300 text-gray-700 sm:text-sm', **kwargs) as select_box:
                with Option(value='', text='Please select'):
                    pass

    def add_option(value, text, select_box=select_box):
        with writer_ctx:
            with Option(value=value, text=text) as opt_item:
                    pass

        select_box.components.append(opt_item)

    comp_box.add_option = add_option
    comp_box.select_box = select_box
    return comp_box


def BaseGroup(key, title, **kwargs):
    with oj.uictx(key) as ctx_:
        with writer_ctx:
            with Div(**kwargs) as comp_box:
                with Label(for_=title, classes='block text-sm font-medium text-gray-900', text=title):
                    pass

                with Select(key="select_box",
                            classes='mt-1.5 p-2 w-full rounded-lg bg-white border border-gray-300 text-gray-700 sm:text-sm') as select_box:
                    with Option(value='', text='Please select'):
                        pass

    def add_optgroup(label, select_box=select_box):
        with writer_ctx:
            with Optgroup(label=label) as optgroup_box:
                pass
        
        def add_option(value, text, optgroup_box=optgroup_box):
            with writer_ctx:
                with Option(value=value, text=text) as opt_item:
                        pass

            optgroup_box.components.append(opt_item)

        optgroup_box.add_option = add_option
        select_box.components.append(optgroup_box)
        return optgroup_box
    comp_box.add_optgroup = add_optgroup
    return comp_box



#TODO: Not working; because oj ignores list attribute
#TODO: Icon_IncrementDecrement() is replaced with Question mark circle
def Datalist(key, title):
    with writer_ctx:
        with Div() as comp_box:
            with Label(for_='HeadlineAct', classes='block text-sm font-medium text-gray-900', text=title):
                pass

            with Div(classes="relative mt-1.5"):
                with TextInput(key=key, classes="w-full rounded-lg p-2 border border-gray-300 pe-10 text-gray-700 sm:text-sm", extra_classes="[&::-webkit-calendar-picker-indicator]:opacity-0", placeholder="Please Select", list=f"dl_{key}"):
                    pass
                with Span(classes="absolute inset-y-0 end-0 flex w-8 items-center"):
                    with FontAwesomeIcon(label="faCircleQuestion"): 
                        pass
                    pass
            with Datalist(name="HeadlineAct", key=f"dl_{key}") as dl_box:
                pass
                
    def add_option(value, text, dl_box=dl_box):
        with writer_ctx:
            with Option(value=value, text=text) as opt_item:
                    pass

        dl_box.components.append(opt_item)

    comp_box.add_option = add_option
    return comp_box
