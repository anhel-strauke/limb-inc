label tablet_modal:
    show screen tablet_base
    $ renpy.pause(delay=0.7, hard=True)
    $ tablet_current_app = ""
    call screen tablet_modal_mode
    $ renpy.retain_after_load() 
    hide screen tablet_web_page
    hide screen tablet_app
    $ renpy.pause(delay=0.3, hard=True)
    hide screen tablet_base
    $ renpy.pause(delay=0.3, hard=True)
    return
