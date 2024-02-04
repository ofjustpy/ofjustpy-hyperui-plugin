import ofjustpy as oj
from ofjustpy import icons
from py_tailwind_utils.to_twsty_expr import encode_twstr
from py_tailwind_utils import conc_twtags, tstr, pd, grow, bg, green, W, fc, gray, space, y
from html_writer.macro_module import macros, writer_ctx
def Simple():
    table = oj.PC.Table(twsty_tags=encode_twstr("min-w-full divide-y-2 divide-gray-200 bg-white text-sm"))
    def add_header():
        arow = oj.PC.Tr(childs=[])
        def add_cell(text, arow = arow):
            cell = oj.PC.Th(twsty_tags=encode_twstr("whitespace-nowrap text-left px-4 py-2 font-medium text-gray-900"), text=text)
            arow.components.append(cell)

        thead = oj.PC.Thead(childs = [arow])
        thead.add_cell = add_cell
        table.components.append(thead)
        return thead
    
    tbody = oj.PC.Tbody(twsty_tags=encode_twstr("divide-y divide-gray-200"))
    table.components.append(tbody)
    def add_row(**kwargs):
        tr = oj.PC.Tr(**kwargs)
        font_style = "font-medium"
        def add_cell(text, tr=tr):
            nonlocal font_style
            cell = oj.PC.Td(twsty_tags=encode_twstr(f"whitespace-nowrap px-4 py-2 text-gray-700 {font_style}"), text=text)
            font_style = ""
            tr.components.append(cell)
        tbody.components.append(tr)
        tr.add_cell = add_cell
        return tr

    root = oj.PC.Div(childs=[table])
    root.add_row = add_row
    root.add_header = add_header
    
    
    return root

def SimpleWithBorder():
    with writer_ctx:
        with Div(classes="overflow-x-auto rounded-lg border border-gray-200") as comp_box:
            with Table(classes="min-w-full divide-y-2 divide-gray-200 bg-white text-sm") as table_box:
                pass
            with Tbody(classes="divide-y divide-gray-200") as tbody_box:
                pass
    def add_header(table_box=table_box):
        with writer_ctx:
            with Thead("ltr:text-left rtl:text-right") as header_box:
                with Tr() as row_box:
                    pass
            
        def add_cell(cell_text, row_box=row_box):
            with writer_ctx:
                with Th(classes='whitespace-nowrap px-4 py-2 text-left font-medium text-gray-900', text=cell_text) as cell_box:
                    pass
            row_box.components.append(cell_box)
        
        header_box.add_cell = add_cell
        table_box.components.append(header_box)
        return header_box

    def add_row(tbody_box = tbody_box):
        with writer_ctx:
            with Tr() as tr_box:
                pass
        def add_cell(text, tr_box=tr_box):
            with writer_ctx:
                with Td(classes="whitespace-nowrap px-4 py-2 text-gray-700", text=text) as td_box:
                    pass

            tr_box.components.append(td_box)
        tr_box.add_cell = add_cell
        tbody_box.components.append(tr_box)
        return tr_box
    
    comp_box.add_header = add_header
    comp_box.add_row = add_row
    return comp_box
