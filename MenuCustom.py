import pygame_menu


class MenuCustom(pygame_menu.Menu):

    def __init__(self,
                 height,
                 width,
                 title,
                 center_content=True,
                 column_force_fit_text=False,
                 column_max_width=None,
                 columns=1,
                 enabled=True,
                 joystick_enabled=True,
                 menu_id='',
                 menu_position=(50, 50),
                 mouse_enabled=True,
                 mouse_motion_selection=False,
                 mouse_visible=True,
                 onclose=None,
                 rows=None,
                 theme=pygame_menu.themes.THEME_DEFAULT,
                 **kwargs
                 ):
        super().__init__(height, width, title, theme=theme)
