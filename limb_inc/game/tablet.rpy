# In-game tablet computer of our here

transform trans_tablet_scene_fade:
    on show:
        xpos 0 ypos 0 alpha 0.0
        linear 0.3 alpha 1.0
    on hide:
        xpos 0 ypos 0 alpha 1.0
        time 0.3
        linear 0.3 alpha 0.0

transform trans_tablet_frame:
    on show:
        xpos 0 ypos 1080
        time 0.3
        ease 0.3 ypos 0
    on hide:
        xpos 0 ypos 0
        ease 0.3 ypos 1080

transform trans_tablet_interface:
    on show:
        alpha 0.0
        linear 0.2 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.2 alpha 0.0


screen tablet_frame_image():
    layer "tablet_frame"
    add "tablet/tablet_frame.png" xpos 0 ypos 0

screen tablet_base():
    layer "screens"
    add "tablet/tablet_scene_fade.png" at trans_tablet_scene_fade
    style_prefix "tablet" 
    fixed:
        at trans_tablet_frame
        add "tablet/tablet_bg_off.png" xpos 520 ypos 29
        use tablet_frame_image
        
        # Tablet can be closed by clicking outside it
        # button:
        #     id "tab_close_1"
        #     xpos 0
        #     ypos 0
        #     xsize 520
        #     ysize 1080
        #     keyboard_focus False
        #     action Return(False)
        # button:
        #     id "tab_close_2"
        #     xpos 520
        #     ypos 0
        #     xsize 877
        #     ysize 29
        #     keyboard_focus False
        #     action Return(False)
        # button:
        #     id "tab_close_3"
        #     xpos 520 + 877
        #     ypos 0
        #     xsize 1920 - 520 - 877
        #     ysize 1080
        #     keyboard_focus False
        #     action Return(False)
        # button:
        #     id "tab_close_4"
        #     xpos 520
        #     ypos 29 + 1016
        #     xsize 877
        #     ysize 1080 - 29 - 1016
        #     keyboard_focus False
        #     action Return(False) 


style tablet_text:
    color "#f9bb04"
    font "Exo2"
    size 40


screen tablet_interface():
    layer "screens"
    fixed:
        at trans_tablet_interface
        add "tablet/tablet_bg.png" xpos 520 ypos 29
        fixed:
            xpos 582
            ypos 92
            xmaximum 752
            ymaximum 886
            transclude
    use tablet_frame_image

screen tablet_iface_login:
    style_prefix "tablet"
    tag tablet_interface
    use tablet_interface:
        vbox:
            pos (40, 40) xsize 700
            null height 40
            text _("Wellcome to the\nLIMB, INC Network system") text_align 0.5 xalign 0.5 size 60
            null height 40
            text _("Please Log In") text_align 0.5 xalign 0.5

style tablet_login_text is tablet_text
style tablet_login_button_text is tablet_text
style tablet_login_input:
    #color "#f9bb04"
    color "#ffffff"
    font "Exo2"
    size 40
style tablet_login_button_text:
    color "#f9bb04"
    text_align 0.5
    xalign 0.5
    hover_color "#ffffff"

transform trans_login_ui:
    on show:
        xpos 632 ypos 520 alpha 0.0
        linear 0.3 alpha 1.0
    on hide:
        xpos 632 ypos 520 alpha 1.0
        linear 0.2 alpha 0.0
transform trans_login_ui_confirm:
    on show:
        xpos 602 ypos 520 alpha 0.0
        linear 0.3 alpha 1.0
    on hide:
        xpos 602 ypos 520 alpha 1.0
        linear 0.2 alpha 0.0

screen tablet_login(prompt, input_val):
    style_prefix "tablet_login"
    modal True
    vbox:
        at trans_login_ui            
        text prompt
        input value input_val id "input_data" length 11 allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюя1234567890-'_"
        hbox:
            null width 375
            textbutton _("Continue >>") action Return() text_xalign 1.0 xalign 1.0

screen tablet_yesno(prompt):
    style_prefix "tablet_login"
    modal True
    vbox:
        at trans_login_ui_confirm
        xsize 700
        text prompt xalign 0.5 text_align 0.5
        null height 20
        hbox:
            xalign 0.5
            textbutton _("Yes") xsize 350 text_align 0.5 action Return(True)
            null width 20
            textbutton _("No") xsize 350 text_align 0.5 action Return(False)

screen tablet_iface_login_success:
    style_prefix "tablet"
    tag tablet_interface
    use tablet_interface:
        vbox:
            pos (40, 40) xsize 700
            null height 40
            text _("Wellcome to the\nLIMB, INC Network system") text_align 0.5 xalign 0.5 size 60
            null height 40
            text _("Successfully Logged In") text_align 0.5 xalign 0.5

screen tablet_iface_missed_call(who):
    style_prefix "tablet"
    tag tablet_interface
    use tablet_interface:
        vbox:
            pos (40, 40) xsize 700
            null height 40
            text _("Hello, %s.") % FIRST_NAME text_align 0.5 xalign 0.5 size 60
            null height 40
            text _("You have a missed call from:\n\n[who]") text_align 0.5 xalign 0.5

transform trans_tablet_incoming_call_image:
    alpha 1.0
    ease 0.5 alpha 0.5
    ease 0.5 alpha 1.0
    repeat

screen tablet_iface_incoming_call(who, who_image):
    style_prefix "tablet"
    tag tablet_interface
    use tablet_interface:
        vbox:
            pos (40, 40) xsize 700
            null height 40
            text _("Incoming Call") text_align 0.5 xalign 0.5 size 60
            null height 40
            add who_image xalign 0.5 at trans_tablet_incoming_call_image
            null height 40
            text who text_align 0.5 xalign 0.5 
            null height 40
            hbox:
                xalign 0.5
                spacing 60
                text _("Answer") size 60
                text _("Cancel") size 60

default call_time_int = 0
default call_time = "00:00"

init python:
    def tablet_active_call_increment_time():
        store.call_time_int = store.call_time_int + 1
        secs = store.call_time_int % 60
        mins = store.call_time_int / 60
        store.call_time = "%02d:%02d" % (mins, secs)
    
    def tablet_reset_call_time():
        store.call_time_int = 0
        store.call_time = "00:00"

screen tablet_iface_active_call(who, who_image):
    style_prefix "tablet"
    tag tablet_interface

    use tablet_interface:
        vbox:
            pos (40, 40) xsize 700
            null height 40
            text _("Active Call") text_align 0.5 xalign 0.5 size 60
            null height 40
            add who_image xalign 0.5
            null height 40
            text who text_align 0.5 xalign 0.5 
            null height 20
            text _("Call Time: [call_time]") xalign 0.5 text_align 0.5 size 20
            null height 20
            text _("End Call") xalign 0.5 size 60
    timer 1.0 repeat True action Function(tablet_active_call_increment_time)