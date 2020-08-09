transform trans_accessing_mail_archive:
    alpha 1.0
    ease 0.3 alpha 0.2
    ease 0.3 alpha 1.0
    repeat

screen tablet_mail_archive_entrance():
    tag tablet_app
    style_prefix "tablet"
    use tablet_desktop_base:
        vbox:
            xfill True
            null height 240
            vbox:
                at trans_accessing_mail_archive
                xfill True
                text _("Accessing") xalign 0.5 size 60
                text _("Mail Server") xalign 0.5 size 60
                text _("Archive...") xalign 0.5 size 60

screen tablet_mail_archive_granted():
    tag tablet_app
    style_prefix "tablet"
    use tablet_desktop_base:
        vbox:
            xfill True
            null height 240
            text _("Access") xalign 0.5 size 60
            text _("Granted") xalign 0.5 size 60

transform trans_hilight_search_menu:
    alpha 0.5
    pause 0.1
    alpha 1.0
    pause 0.1
    alpha 0.5
    pause 0.1
    alpha 1.0
    pause 0.1
    alpha 0.5
    pause 0.1
    alpha 1.0

screen tablet_mail_archive_home():
    tag tablet_app
    style_prefix "tablet"
    use tablet_desktop_base:
        vbox:
            xfill True
            null height 20
            text _("Limbus Inc Mail Server Archive")
            null height 20
            text _("Account: %s %s") % (FIRST_NAME, LAST_NAME) size 40
            null height 10
            text _("12’842 archived messages") size 20
            null height 20
            hbox:
                spacing 20
                text _("{u}s{/u}earch") size 40
                text _("{u}c{/u}leanup") size 40
                text _("{u}r{/u}eport") size 40
                text _("{u}m{/u}ore") size 40
            null height 20
            vbox:
                xfill True
                spacing 5
                for (m, s) in [("human.resources@lmbs.xz", "30"), ("bella.rabinovich@lmbs.xz", "15"), ("contacts@cncurr.rf", "28"),
                               ("dr.strange@mrvll.wow", "112"), ("victor.green@umd.yt", "15"), ("greenwas@assert.corp", "65"), 
                               ("bella.rabinovich@lmbs.xz", "98"), ("bella.rabinovich@lmbs.xz", "7"), ("human.resources@lmbs.xz", "23"), 
                               ("bella.rabinovich@lmbs.xz", "17"), ("bella.rabinovich@lmbs.xz", "7"), ("human.resources@lmbs.xz", "23")]:
                    hbox:
                        spacing 20
                        add "tablet/mail_icon.png" yoffset 4
                        vbox:
                            xsize 520
                            text m size 30 
                        text "%s Kb" % s size 30


screen tablet_mail_archive_home_search():
    tag tablet_app
    style_prefix "tablet"
    use tablet_desktop_base:
        vbox:
            xfill True
            null height 20
            text _("Limbus Inc Mail Server Archive")
            null height 20
            text _("Account: %s %s") % (FIRST_NAME, LAST_NAME) size 40
            null height 10
            text _("12’842 archived messages") size 20
            null height 20
            hbox:
                spacing 20
                text _("{u}s{/u}earch") size 40 color "#ffffff" at trans_hilight_search_menu
                text _("{u}c{/u}leanup") size 40
                text _("{u}r{/u}eport") size 40
                text _("{u}m{/u}ore") size 40
            null height 20
            vbox:
                xfill True
                spacing 5
                for (m, s) in [("human.resources@lmbs.xz", "30"), ("bella.rabinovich@lmbs.xz", "15"), ("contacts@cncurr.rf", "28"),
                               ("dr.strange@mrvll.wow", "112"), ("victor.green@umd.yt", "15"), ("greenwas@assert.corp", "65"), 
                               ("bella.rabinovich@lmbs.xz", "98"), ("bella.rabinovich@lmbs.xz", "7"), ("human.resources@lmbs.xz", "23"), 
                               ("bella.rabinovich@lmbs.xz", "17"), ("bella.rabinovich@lmbs.xz", "7"), ("human.resources@lmbs.xz", "23")]:
                    hbox:
                        spacing 20
                        add "tablet/mail_icon.png" yoffset 4
                        vbox:
                            xsize 520
                            text m size 30 
                        text "%s Kb" % s size 30


default search_time_limit = "|"
default search_text = ""
default search_phase = 0
default search_time_limit_pos = 0
default search_text_pos = 0

init python:
    def tablet_ch2_update_search():
        global search_time_limit, search_text, search_phase, search_time_limit_pos, search_text_pos
        time_lim = _("3 years ago")
        search_txt = _("Kurt Bachowski")
        if search_phase == 0:
            timer_delay = 0.1 + renpy.random.random() * 0.2
            if search_time_limit_pos == len(time_lim):
                search_phase = 1
                search_time_limit = time_lim
            else:
                search_time_limit_pos += 1
                search_time_limit = time_lim[:search_time_limit_pos] + "|"
        elif search_phase < 4:
            search_text = "|"
            search_phase += 1
        elif search_phase == 4:
            timer_delay = 0.1 + renpy.random.random() * 0.2
            if search_text_pos == len(search_txt):
                search_phase = 5
                search_text = search_txt
            else:
                search_text_pos += 1
                search_text = search_txt[:search_text_pos] + "|"
        if search_phase == 5:
            return True
        renpy.restart_interaction()

screen tablet_mail_archive_search():
    tag tablet_app
    style_prefix "tablet"
    use tablet_desktop_base:
        vbox:
            xfill True
            null height 20
            text _("Limbus Inc Mail Server Archive")
            null height 20
            text _("Search") size 60
            null height 20
            text _("Set Time Limitation:")
            text _(search_time_limit) color gui.tablet_text_hover_color
            null height 20
            text _("Search For:")
            text _(search_text) color gui.tablet_text_hover_color
    timer 0.15 action Function(tablet_ch2_update_search) repeat True
    
screen tablet_mail_archive_searching():
    tag tablet_app
    style_prefix "tablet"
    use tablet_desktop_base:
        vbox:
            xfill True
            null height 20
            text _("Limbus Inc Mail Server Archive")
            null height 20
            text _("Search") size 60
            null height 20
            text _("Searching...") xalign 0.5:
                at transform:
                    alpha 1.0
                    ease 0.3 alpha 0.2
                    ease 0.3 alpha 1.0
                    repeat
    timer 2.0 action Return()

screen tablet_mail_archive_search_result():
    tag tablet_app
    style_prefix "tablet"
    use tablet_desktop_base:
        vbox:
            xfill True
            null height 20
            text _("Limbus Inc Mail Server Archive")
            null height 60
            text _("Search Result") size 60
            null height 80
            hbox:
                spacing 20
                add "tablet/mail_icon.png" yoffset 4
                vbox:
                    xsize 520
                    text ADDR_KURT size 30 
                text "3 Kb" size 30
            null height 80
            text _("Restore?") size 60 xalign 0.5
            null height 40
            grid 2 1:
                xfill True
                text _("Yes") xalign 0.5 size 60
                text _("No") xalign 0.5 size 60
                
screen tablet_mail_archive_search_result_yes():
    tag tablet_app
    style_prefix "tablet"
    use tablet_desktop_base:
        vbox:
            xfill True
            null height 20
            text _("Limbus Inc Mail Server Archive")
            null height 60
            text _("Search Result") size 60
            null height 80
            hbox:
                spacing 20
                add "tablet/mail_icon.png" yoffset 4
                vbox:
                    xsize 520
                    text ADDR_KURT size 30 
                text "3 Kb" size 30
            null height 80
            text _("Restore?") size 60 xalign 0.5
            null height 40
            grid 2 1:
                xfill True
                text _("Yes") xalign 0.5 size 60 at trans_hilight_search_menu
                text _("No") xalign 0.5 size 60

screen tablet_receive_file():
    tag tablet_app
    style_prefix "tablet"
    use tablet_desktop_base:
        vbox:
            xfill True
            null height 120
            text _("File Direct Transmission Request") size 60 xalign 0.5 text_align 0.5
            null height 40
            text _("Source: Device in 77 cm") xalign 0.5
            null height 40
            text _("Accept Transmission?") xalign 0.5
            null height 40
            grid 2 1:
                xfill True
                textbutton _("Yes") action Return(True) xalign 0.5 text_size 60
                textbutton _("No") action Return(False) xalign 0.5 text_size 60


style download_bar_left:
    ysize 40
    xsize 1
    background "#c0c0c0"
style download_bar_left_full:
    ysize 40
    xsize 600
    background "#c0c0c0"
style download_bar_right:
    ysize 40
    xsize 1
    background "#303030"

transform trans_bar_left:
    size (0, 40)
    linear 2.0 size (600, 40)
transform trans_bar_right:
    size (600, 40)
    linear 2.0 size (0, 40)

screen tablet_receive_file_process():
    tag tablet_app
    style_prefix "tablet"
    use tablet_desktop_base:
        vbox:
            xfill True
            null height 120
            text _("File Direct Transmission") size 60 xalign 0.5 text_align 0.5
            null height 60
            text _("Downloading File...") xalign 0.5
            null height 40
            hbox:
                xsize 680
                null width 40
                window style "download_bar_left" at trans_bar_left
                window style "download_bar_right" at trans_bar_right
                null width 40
    timer 2.0 action Return()

transform blinking:
    alpha 1.0
    ease 0.3 alpha 0.2
    ease 0.3 alpha 1.0
    repeat

screen tablet_receive_file_process_complete():
    tag tablet_app
    style_prefix "tablet"
    use tablet_desktop_base:
        vbox:
            xfill True
            null height 120
            text _("File Direct Transmission") size 60 xalign 0.5 text_align 0.5
            null height 60
            text _("Download Finished") xalign 0.5 at blinking
            null height 40
            hbox:
                xsize 680
                null width 40
                window style "download_bar_left_full"
                null width 40
    timer 1.8 action Return()

screen tablet_file_destroyed():
    style_prefix "tablet"
    tag tablet_app
    use tablet_interface:
        vbox:
            pos (40, 40) xsize 700
            text _("Reading Document")
            null height 160
            text _("File Deleted") xalign 0.5 size 60

            