label main_menu:
    $ renpy.transition(dissolve)
    jump main_menu_screen

screen no_interaction():
    button action NullAction() xpos 0 ypos 0 xsize 1920 ysize 1080 keyboard_focus False

init -1000 python:
    class FunctionIfNoSay(Action, DictEquality):
        def __init__(self, callback, *args, **kwargs):
            self._callable = callback
            self._args = args
            self._update_screens = kwargs.pop("_update_screens", True)
            self._kwargs = kwargs
        
        def __call__(self):
            rv = self._callable(*self._args, **self._kwargs)
            if self._update_screens:
                renpy.restart_interaction()
            return rv
        
        def get_sensitive(self):
            return not renpy.get_screen("say")