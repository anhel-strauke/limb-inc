##############################################################################
## In-game tablet computer
##############################################################################

define gui.tablet_text_color = "#c0c0c0"
define gui.tablet_text_hover_color = "#ffffff"

## Author of the source tablet image is „千图网”, free background photos from pngtree.com <https://pngtree.com/free-backgrounds>
## <div>Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

##############################################################################
## Tablet button in the game UI

transform trans_attenion:
    alpha 1.0
    ease 0.3 alpha 0.6
    ease 0.3 alpha 1.0
    repeat

style tablet_icon_button:
    background "tablet/tablet_icon_idle.png"
    hover_background "tablet/tablet_icon_hover.png"
    selected_idle_background "tablet/tablet_icon_hover.png"
    selected_hover_background "tablet/tablet_icon_hover.png"
    xsize 138
    ysize (160 + 5 + 30)

style tablet_icon_button_text:
    size 30
    #font "Exo2"
    #outlines [(absolute(2), "#000000", absolute(2), absolute(2))]
    color "#101010"
    hover_color gui.accent_color
    xalign 0.5
    yalign 1.0
    text_align 0.5
    xsize 138
    yoffset 5

transform trans_tablet_button:
    ypos (1080 - 49 - 160 - 5 - 30) # 160 is a tablet icon height, 30 is size of text label
    xpos 40
    on show:
        xpos (-138 - 10)
        ease 0.3 xpos 40
    on hide:
        ease 0.3 xpos (-138 - 10)

init python:
    def show_tablet_modal():
        renpy.hide_screen("tablet_button") 
        renpy.log("Before tablet: %s" % str(TAB_EMAIL_READ))
        renpy.call_in_new_context("tablet_modal")
        renpy.log("After tablet: %s" % str(TAB_EMAIL_READ))
        renpy.show_screen("tablet_button")

screen tablet_button():
    style_prefix "tablet_icon"
    fixed:
        at trans_tablet_button
        button action Function(show_tablet_modal):
            text _("Tablet") style "tablet_icon_button_text"
        if (len(TAB_EMAIL_RECEIVED) - len(TAB_EMAIL_READ) > 0):
            add "tablet/attenion.png" at trans_attenion xpos (138 / 2 - 16) ypos (160 / 2 - 16)

##############################################################################
## Tablet frame and interface

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
    on show, replace:
        alpha 0.0
        linear 0.1 alpha 1.0
    on hide, replaced:
        alpha 1.0
        linear 0.1 alpha 0.0

transform trans_tablet_wallpaper:
    on show:
        alpha 0.0
        time 0.1
        alpha 1.0
    on hide:
        alpha 0.0

transform trans_tablet_interface_frame:
    xpos 0 ypos 0
    on show, replace:
        alpha 1.0
    on hide, replaced:
        alpha 1.0
        time 0.1
        alpha 0.0


screen tablet_frame_image_base():
    layer "tablet_frame"
    add "tablet/tablet_frame.png" xpos 0 ypos 0

screen tablet_frame_image():
    layer "tablet_frame"
    add "tablet/tablet_frame.png" at trans_tablet_interface_frame 


screen tablet_base():
    layer "screens"
    add "tablet/tablet_scene_fade.png" at trans_tablet_scene_fade
    style_prefix "tablet" 
    fixed:
        at trans_tablet_frame
        add "tablet/tablet_off.png" xpos 520 ypos 29


style tablet_text:
    color gui.tablet_text_color
    font "Exo2"
    size 40

screen tablet_interface():
    layer "screens"
    fixed:
        at trans_tablet_wallpaper
        add "tablet/tablet_bg.png" xpos 520 ypos 29
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


## First Log In ####################################################################################

screen tablet_iface_login():
    style_prefix "tablet"
    tag tablet_interface
    use tablet_interface:
        vbox:
            pos (40, 40) xsize 700
            null height 40
            text _("Wellcome to the\nLIMBUS INC Network system") text_align 0.5 xalign 0.5 size 60
            null height 40
            text _("Please Log In") text_align 0.5 xalign 0.5

style tablet_login_text is tablet_text
style tablet_login_button_text is tablet_text
style tablet_login_input:
    #color gui.tablet_text_color
    color "#ffffff"
    font "Exo2"
    size 40
style tablet_login_button_text:
    color gui.tablet_text_color
    text_align 0.5
    xalign 0.5
    hover_color gui.tablet_text_hover_color

transform trans_login_ui:
    on show:
        xpos 632 ypos 520 alpha 0.0
        linear 0.2 alpha 1.0
    on hide:
        xpos 632 ypos 520 alpha 1.0
        linear 0.1 alpha 0.0
transform trans_login_ui_confirm:
    on show:
        xpos 602 ypos 520 alpha 0.0
        linear 0.2 alpha 1.0
    on hide:
        xpos 602 ypos 520 alpha 1.0
        linear 0.1 alpha 0.0

screen tablet_login(prompt, input_val):
    style_prefix "tablet_login"
    modal True
    vbox:
        at trans_login_ui            
        text prompt
        input value input_val id "input_data" length 11 allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюя1234567890-‘’`'_ӲӳÁáÀàȂȃÂâÄäA̋a̋ÃãĆćČčĎďÉéȆȇȆȇÈèÊêËëẼẽÍíȊȋÎîÏïÌìÑñŇňǸǹÓóÒòȎȏÔôÖöÕõŐőŰűȒȓŘřŠšŤťÚúȖȗÛûÜüÙùŸÿŽžǍǎĚěǏǐǑǒǓǔĂăĔĕĬĭŎŏŬŭĞğ"
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

screen tablet_iface_login_success():
    style_prefix "tablet"
    tag tablet_interface
    use tablet_interface:
        vbox:
            pos (40, 40) xsize 700
            null height 40
            text _("Wellcome to the\nLIMBUS INC Network system") text_align 0.5 xalign 0.5 size 60
            null height 40
            text _("Successfully Logged In") text_align 0.5 xalign 0.5


## Missed Call cutscene ##################################################################

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

## Active Call Interface ####################################################################

default call_time_int = 0
default call_time = "00:00"

init python:
    def tablet_active_call_increment_time():
        global call_time_int, call_time
        call_time_int = call_time_int + 1
        secs = call_time_int % 60
        mins = call_time_int / 60
        call_time = "%02d:%02d" % (mins, secs)
    
    def tablet_reset_call_time():
        global call_time_int, call_time
        call_time_int = 0
        call_time = "00:00"

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


#############################################################################################
## Tablet in modal mode (when activated using tablet icon on the screen)

screen tablet_modal_mode:
    timer 0.01 action Function(tablet_run)

init python:
    tablet_current_app = ""

    def tablet_close_mask(x, y):
        return not (520 <= x <= 520 + 877 and 29 <= y <= 29 + 1016)

    def tablet_run():
        global tablet_current_app
        tablet_run_app(tablet_current_app)

    def tablet_run_app(app_name):
        global tablet_current_app
        tablet_current_app = app_name
        if not app_name:
            renpy.show_screen("tablet_desktop")
        else:
            renpy.show_screen(app_name)

    def tablet_end_app():
        tablet_run_app("")

style tablet_desktop_text is tablet_text
style tablet_desktop_text:
    hover_color gui.tablet_text_hover_color
    text_align 0.0

style tablet_button_text is tablet_text
style tablet_button_text:
    hover_color gui.tablet_text_hover_color

screen tablet_desktop_base():
    style_prefix "tablet"
    use tablet_interface:
        vbox:
            pos (40, 6) xsize 700
            hbox:
                xfill True
                text _("LIMBUS INC NETWORK SYSTEM") size 20 xalign 0.0 xoffset 10
                textbutton _("POWER OFF") action Return() xalign 1.0 text_size 20 top_padding 0 xoffset 8 yoffset 27
            transclude
    fixed:
        # Tablet can be closed by clicking outside it
        button action Return() pos (0, 0) xysize (1920, 1080) keyboard_focus False keysym "K_ESCAPE" focus_mask tablet_close_mask 



## Desktop App ###############################################################################

style desktop_icon is tablet_text
style desktop_icon:
    ysize 128
    xsize 128
    xalign 0.5
style desktop_icon_contacts is desktop_icon
style desktop_icon_web is desktop_icon
style desktop_icon_documents is desktop_icon
style desktop_icon_email is desktop_icon
style desktop_icon_contacts:
    background "tablet/contacts.png"
    hover_background "tablet/contacts_hover.png"
style desktop_icon_web:
    background "tablet/web.png"
    hover_background "tablet/web_hover.png"
style desktop_icon_documents:
    background "tablet/documents.png"
    hover_background "tablet/documents_hover.png"
style desktop_icon_email:
    background "tablet/email.png"
    hover_background "tablet/email_hover.png"

screen tablet_desktop():
    style_prefix "tablet"
    tag tablet_app
    use tablet_desktop_base:
        null height 40
        grid 3 2:
            xsize 680
            style_prefix "tablet_desktop"
            yoffset 30
            xspacing 10
            yspacing 30
            button action Function(tablet_run_app, "tablet_app_contacts"):
                vbox:
                    window style "desktop_icon_contacts"
                    null height 10
                    text _("Contacts")
            button action NullAction():
                vbox:
                    window style "desktop_icon_web"
                    null height 10
                    text _("Browser")
            button action NullAction():
                vbox:
                    window style "desktop_icon_documents"
                    null height 10
                    text _("Documents")
            button action Function(tablet_run_app, "tablet_app_email"):
                vbox:
                    window style "desktop_icon_email":
                        if len(TAB_EMAIL_RECEIVED) - len(TAB_EMAIL_READ) > 0:
                                at trans_attenion
                                add "tablet/attenion.png" xalign 1.0 yalign 0.0
                    null height 10
                    text _("E-Mail")
            null
            null

## Contacts App ###############################################################################

style tablet_app_contacts_button_text is tablet_text
style tablet_app_contacts_button_text:
    hover_color gui.tablet_text_hover_color

screen tablet_app_contacts():
    style_prefix "tablet"
    tag tablet_app
    use tablet_desktop_base:
        vbox:
            null height 10
            textbutton _("<< Contacts") action Function(tablet_end_app)
            null height 40
            vbox:
                xoffset 20
                style_prefix "tablet_app_contacts"
                for name_id in sorted(list(TAB_CONTACTS_AVAIL)):
                    button action Call("tablet_app_contacts_make_call", name_id, from_current=True):
                        style_prefix "tablet_app_contacts_button"
                        hbox:
                            add TAB_CONTACTS[name_id].get("image", "") xalign 0.0 size (90, 104) 
                            null width 40
                            vbox:
                                text TAB_CONTACTS[name_id].get("name", "???")
                                text TAB_CONTACTS[name_id].get("descr", "") size 20

screen tablet_iface_outgoing_call(who, who_image):
    style_prefix "tablet"
    tag tablet_app
    use tablet_interface:
        vbox:
            pos (40, 40) xsize 700
            null height 40
            text _("Calling") text_align 0.5 xalign 0.5 size 60
            null height 40
            add who_image xalign 0.5 at trans_tablet_incoming_call_image
            null height 40
            text who text_align 0.5 xalign 0.5 
            null height 40
            textbutton _("Cancel") action Jump("tablet_app_call_cancelled") text_size 60 xalign 0.5

screen tablet_iface_outgoing_call_no_answer(who, who_image):
    style_prefix "tablet"
    tag tablet_app
    use tablet_interface:
        vbox:
            pos (40, 40) xsize 700
            null height 40
            text _("Call Ended") text_align 0.5 xalign 0.5 size 60
            null height 40
            add who_image xalign 0.5
            null height 40
            text who text_align 0.5 xalign 0.5 
            null height 40
            text _("No Answer") size 40 xalign 0.5



## E-Mail App ###############################################################################

style mail_icon_base:
    xsize 32
    ysize 32

style mail_icon is mail_icon_base
style mail_icon:
    background "tablet/mail_icon_hover.png"
    hover_background "tablet/mail_icon_hover.png"

style mail_icon_open is mail_icon_base
style mail_icon_open:
    background "tablet/mail_open_icon.png"
    hover_background "tablet/mail_open_icon_hover.png"

transform trans_unread_mail_icon:
    alpha 1.0
    ease 0.3 alpha 0.6
    ease 0.3 alpha 1.0
    repeat

screen tablet_app_email():
    style_prefix "tablet"
    tag tablet_app
    use tablet_desktop_base:
        vbox:
            null height 10
            textbutton _("<< E-Mail") action Function(tablet_end_app)
            text _("Inbox for %s %s") % (FIRST_NAME, LAST_NAME) size 26
            text _("%d unread") % (len(TAB_EMAIL_RECEIVED) - len(TAB_EMAIL_READ)) size 20
            null height 20
            viewport:
                ysize 690
                mousewheel True draggable True
                vbox:
                    for mail_id in reversed(TAB_EMAIL_RECEIVED):
                        button action Call("tablet_email_read", mail_id, from_current=True):
                            style_prefix "tablet_app_contacts_button"
                            hbox:
                                if mail_id in TAB_EMAIL_READ:
                                    window style "mail_icon_open"
                                else:
                                    window style "mail_icon" at trans_unread_mail_icon
                                null width 40
                                vbox:
                                    text _("From: %s") % TAB_EMAILS[mail_id]["from"] size 20 bold (mail_id not in TAB_EMAIL_READ)
                                    text TAB_EMAILS[mail_id]["subj"] size 40 #bold (mail_id not in TAB_EMAIL_READ)
                    if not TAB_EMAIL_RECEIVED:
                        null width 700 height 230
                        text _("Mail Inbox is Empty") size 40 xalign 0.5

screen tablet_app_email_read(mail_id):
    style_prefix "tablet"
    tag tablet_app
    use tablet_interface:
        vbox:
            pos (40, 40) xsize 700
            text _("Reading Mail")
            null height 40
            text _("From:") size 60
            text TAB_EMAILS[mail_id]["from"] xoffset 20
            null height 40
            text _("Subject:") size 60
            text TAB_EMAILS[mail_id]["subj"] xoffset 20



## Browser App #####################################################################################

screen tablet_app_browser():
    style_prefix "tablet"
    tag tablet_app
    use tablet_desktop_base:
        vbox:
            null height 10
            textbutton _("<< Browser") action Function(tablet_end_app)