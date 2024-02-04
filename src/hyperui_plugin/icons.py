"""
list of all the icons in hyperui library
"""

#from .parse_svg_component import parse as parse_svg_component
from ofjustpy import icons
# encircledCheckmark = parse_svg_component("""<svg
#         xmlns="http://www.w3.org/2000/svg"
#         fill="none"
#         viewBox="0 0 24 24"
#         stroke-width="1.5"
#         stroke="currentColor"
#         class="h-6 w-6"
#       >
#         <path
#           stroke-linecap="round"
#           stroke-linejoin="round"
#           d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
#         />
#       </svg>""")

# cross = parse_svg_component("""<svg
#         xmlns="http://www.w3.org/2000/svg"
#         fill="none"
#         viewBox="0 0 24 24"
#         stroke-width="1.5"
#         stroke="currentColor"
#         class="h-6 w-6"
#       >
#         <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
#       </svg>""")


# preview = parse_svg_component("""<svg
#             xmlns="http://www.w3.org/2000/svg"
#             fill="none"
#             viewBox="0 0 24 24"
#             stroke-width="1.5"
#             stroke="currentColor"
#             class="h-4 w-4"
#           >
#             <path
#               stroke-linecap="round"
#               stroke-linejoin="round"
#               d="M13.5 6H5.25A2.25 2.25 0 003 8.25v10.5A2.25 2.25 0 005.25 21h10.5A2.25 2.25 0 0018 18.75V10.5m-10.5 6L21 3m0 0h-5.25M21 3v5.25"
#             />
#           </svg>""")

# warning = parse_svg_component("""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="h-5 w-5">
#       <path
#         fill-rule="evenodd"
#         d="M9.401 3.003c1.155-2 4.043-2 5.197 0l7.355 12.748c1.154 2-.29 4.5-2.599 4.5H4.645c-2.309 0-3.752-2.5-2.598-4.5L9.4 3.003zM12 8.25a.75.75 0 01.75.75v3.75a.75.75 0 01-1.5 0V9a.75.75 0 01.75-.75zm0 8.25a.75.75 0 100-1.5.75.75 0 000 1.5z"
#         clip-rule="evenodd"
#       />
#     </svg>""")

icon_db = {
    "EncircledCheckmark": icons.encircledCheckmark,
    "Cross": icons.cross,
    "Preview": icons.preview,
    "Warning": icons.warning,
    "EuroCurrency": icons.euroCurrency
    }
