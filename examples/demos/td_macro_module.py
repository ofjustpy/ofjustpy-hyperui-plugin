from html_writer.macro_module import macros, writer_ctx
import ofjustpy  as oj

# case 1: no childs, outermost context assign
# with writer_ctx:
#     with Div(classes = "bg-blue-100") as tldiv:
#         pass

# print(tldiv)

# ====================================================================
# # case 2: 1 annonymous child
# with writer_ctx:
#     with Div(classes = "bg-blue-100") as tldiv:
#         with Span(classes="bg-green-100", text="hello"):
#             pass
#         pass

# print(tldiv.components[0].html_tag)
# print(tldiv.components[0].domDict)
# print(tldiv.components[0].attrs)

# ============================ done case 2 ===========================

#case 3: named child; need an assign stmt
# with writer_ctx:
#     with Div(classes = "bg-blue-100") as tldiv:
#         with Span(classes="bg-green-100", text="hello") as spanHC:
#             pass
#         pass

# print (spanHC)


# case 4: nested  named and anonymous components
with writer_ctx:
    with Div(classes = "bg-blue-100") as tldiv:
        with Div(classes="bg-green-100") as divl1:
            with Div(classes="bg-green-100"):
                with Div(classes="bg-yellow-100") as divl3:
                    pass
                pass
            pass
        pass
    pass

print("divl1 = ", divl1.domDict)
divl1child = divl1.components[0]
print("divl3: via parent = ", divl1child.components[0].domDict)
print("divl3: direct = ", divl3.domDict)
print (divl3)
