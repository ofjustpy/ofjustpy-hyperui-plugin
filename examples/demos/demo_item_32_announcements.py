import ofjustpy as oj
oj.set_style("un")
app = oj.load_app()
from hyperui_plugin.marketing.announcements import  (WithAction,
                                                     BottomWithClose,
                                                     #SwiperSlider
                                                     
                                                     )
with_action = WithAction()
bottom_close = BottomWithClose()
#swiperSlider = SwiperSlider()
endpoint = oj.create_endpoint("announcements",
                              childs = [with_action,
                                        bottom_close,
                                        #swiperSlider

                                        ],
                              title="Announcements"
                              )
oj.add_jproute("/", endpoint)

