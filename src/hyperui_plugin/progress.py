import ofjustpy as oj
from ofjustpy import icons
from py_tailwind_utils.to_twsty_expr import encode_twstr
from py_tailwind_utils import conc_twtags, tstr, pd, grow, bg, green, W

percentage_values = [8.33,
                     16.66,
                     16.66,
                     20,
                     25,
                     33.33,
                     33.33,
                     40,
                     41.66,
                     50,
                     50,
                     58.33,
                     60,
                     66.66,
                     66.66,
                     75,
                     75,
                     83.33,
                     91.66,
                     100]


fraction_strings = ['1/12',
                           '2/12',
                           '3/12',
                           '1/6',
                           '1/4',
                           '1/3',
                           '2/6',
                           '2/5',
                           '5/12',
                           '1/2',
                           '2/4',
                           '7/12',
                           '3/5',
                           '4/6',
                           '5/6',
                           '3/4',
                           '9/12',
                           '10/12',
                    '11/12',
                    "full"]

def withValue(key, percent_value=50):
    # List of Percentage Values

    position = 5
    
    try:
        position = percentage_values.index(percent_value)
    except:
        pass


    width= fraction_strings[position]

    percent_value_label = oj.Mutable.Span(key="{key}_pclabel", twsty_tags=encode_twstr("font-bold text-white"), text=f"{percent_value}%")
    progress_bar = oj.Mutable.Div(key="{key}_colorbar", twsty_tags=encode_twstr(f"block h-4 rounded-full bg-indigo-600 text-center w-{width}"), childs=[percent_value_label]
                                  )
    ibox = oj.HCCMutable.Div(role="progressbar",
               #aria-labelledby="ProgressLabel",
               #aria-valuenow="50",
               twsty_tags=encode_twstr("block rounded-full bg-gray-200"),
               childs = [progress_bar
                         ]
               )
    
    tlc = oj.HCCMutable.Div(childs = [oj.PC.Span(twsty_tags=encode_twstr("sr-only"), text="Loading"), ibox])

    def update_bar(percent_value, wp, to_ms):
        try:
            position = percentage_values.index(percent_value)
        except:
            return 
            pass


        width= fraction_strings[position]

        progress_bar_ms = to_ms(progress_bar)
        progress_bar_ms.add_twsty_tags(W/width)
        # label_ms = to_ms(percent_value_label)
        # label_ms.text = f"{percent_value}%"
        #oj.run_task(wp.update())
    return tlc, update_bar


def withValueCentered(key, percent_value=50):
    
    position = 5
    try:
        position = percentage_values.index(percent_value)
    except:
        return 
    width= fraction_strings[position]
    color_bar = oj.Mutable.Span(key=f"{key}_colorbar", twsty_tags=encode_twstr(f"block h-4 rounded-full bg-indigo-600 text-center w-{width}"))
    label = oj.Mutable.Span(key=f"{key}_label", twsty_tags=encode_twstr("font-bold text-white"), text=f"{percent_value}%"
                              )
    labelbox = oj.HCCMutable.Div(twsty_tags=encode_twstr("absolute inset-0 flex items-center justify-center"),
                childs = [label
                                        ]
                              )
    root = oj.HCCMutable.Div(twsty_tags=encode_twstr("relative block rounded-full bg-gray-200"),
                             childs = [labelbox, color_bar],
                             role="progressbar"
                             )

    def update_bar(percent_value, wp, to_ms):
        try:
            position = percentage_values.index(percent_value)
        except:
            return 
            pass
        width= fraction_strings[position]
        color_bar_ms = to_ms(color_bar)
        color_bar_ms.add_twsty_tags(W/width)
        # label_ms = to_ms(label)
        # label_ms.text = f"{percent_value}%"
        
    return root, update_bar

