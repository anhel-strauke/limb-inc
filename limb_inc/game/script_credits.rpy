init python:
    CREDITS = [
        {
            "title": _("Idea by Dina Griko"),
        },
        {
            "title": _("Scenario by Timirlan Kenjibaev"),
        },
        {
            "title": _("Special Guest"),
            "items": [
                _("{size=60}Andrey Zykin{/size}{p}{i}as Boris the Archivist{/i}")
            ]
        },
        {
            "title": _("Narrative"),
            "items": [
                _("Timirlan Kenjibaev"),
                _("Dina Griko"),
                _("Alexandra Pikarevskaya")
            ]
        },
        {
            "title": _("English Translation"),
            "items": [
                _("Alexandra Kanapina"),
                _("Naina Kovyazina"),
                _("Sergei Reischel"),
                _("Darya Bocharova"),
                _("V.M.A."),
                _("Timirlan Kenjibaev"),
                _("Anatoly Griko"),
                _("Dina Griko"),
            ]
        },
        {
            "title": _("Backgrounds Art"),
            "items": [
                (_("Bravo"), "artstation.com/nadezhdarunova"), # ← ?
                _("Anatoly Griko"),
            ]
        },
        {
            "title": _("Limbo Backgrounds Art"),
            "items": [
                (_("Vadim Zalepaev"), "vk.com/3wy3wy"),
            ]
        },
        {
            "title": _("Characters Art"),
            "items": [
                (_("Taya Chuiganova"), "vk.com/thekingdomofkai")
            ]
        },
        {
            "title": _("Limbo Characters Art"),
            "items": [
                (_("Margarita Kamushek"), "vk.com/teamochi"),
                (_("Vadim Zalepaev"), "vk.com/3wy3wy"),
            ]
        },
        {
            "title": _("Animations"),
            "items": [
                _("Anatoly Griko")
            ]
        },
        {
            "title": _("Programming"),
            "items": [
                _("Anatoly Griko"),
            ]
        },
        {
            "title": _("Scripting"),
            "items": [
                _("Anatoly Griko"),
                _("Dina Griko")
            ]
        },
        {
            "title": _("Sound Design"),
            "items": [
                (_("Vlad Ulrich"), "github.com/Wedmer")
            ]
        },
        {
            "title": _("Special Thanks"),
            "items": [
                _("Anna Bolshakova"),
                _("Anna Kovalenko"),
                (_("Giglemash"), "github.com/Giglemash")
            ]
        },
        {
            "title": _("Made with Ren’Py %d.%d") % (renpy.version_tuple[0], renpy.version_tuple[1]),
            "items": [
                "https://www.renpy.org/"
            ]
        },
    ]

init python:
    cr_max_w = 1300
    cr_last_max_w = 1800
    cr_section_margin = 360
    cr_section_space = 90
    cr_section_height = 60
    cr_item_height = 40
    cr_item_space = 40
    cr_subitem_height = 30
    cr_subitem_space = 5
    cr_item_hspace = 30
    cr_y_start = 1080 + 60 + 60
    credits_time = 60.0

    def build_credits():
        cr_credits_height = 0
        cr_y = 0
        objects = []
        
        for sindex, sect in enumerate(CREDITS):
            title = sect.get("title", "")
            if title:
                sect_displayable = Text(title, slow=False, style="cr_style_section", pos=(cr_max_w / 2, cr_y))
                objects.append(sect_displayable)
                cr_y += cr_section_height
            items = sect.get("items", [])
            if items:
                cr_y += cr_section_space
                for item in items:
                    if type(item) is unicode or type(item) is str:
                        item_displayable = Text(item, slow=False, style="cr_style_item", pos=(cr_max_w / 2, cr_y))
                        objects.append(item_displayable)
                        cr_y += (cr_item_height + cr_item_space)
                    else:
                        left, right = item
                        left_displayable = Text(left, slow=False, style="cr_style_item_left", pos=(cr_max_w / 2, cr_y))
                        cr_y += (cr_item_height + cr_subitem_space)
                        right_displayable = Text("%s" % right, slow=False, style="cr_style_item_right", pos=(cr_max_w / 2, cr_y))
                        cr_y += (cr_subitem_height + cr_item_space)
                        objects.append(left_displayable)
                        objects.append(right_displayable)
                cr_y -= cr_item_space
            if title or items and sindex < (len(CREDITS) - 1):
                cr_y += cr_section_margin
            cr_credits_height = cr_y
        return (cr_credits_height, objects)
    
    cr_credits_height, cr_objects = build_credits()

init:
    style cr_style_base:
        font "Exo2" color "#ffffff" xanchor 0.5 yanchor 0.5
    style cr_style_game_subtitle is cr_style_base
    style cr_style_game_subtitle:
        size 60
    style cr_style_game_title is cr_style_base
    style cr_style_game_title:
        size 120
    style cr_style_section is cr_style_base
    style cr_style_section:
        size cr_section_height yanchor 0.0 text_align 0.5 xfill True
    style cr_style_item is cr_style_base
    style cr_style_item:
        size cr_item_height yalign 0.0 text_align 0.5 xfill True
    style cr_style_item_left is cr_style_item
    style cr_style_item_left:
        xalign 0.5
        text_align 0.5
        xminimum 0
    style cr_style_item_right is cr_style_item
    style cr_style_item_right:
        xalign 0.5
        text_align 0.5
        size cr_subitem_height
        xminimum 0
    style cr_style_item_hbox:
        spacing cr_subitem_space xanchor 0.5 yanchor 0.0 xminimum cr_max_w xfill True
    style cr_style_last is cr_style_base
    style cr_style_last:
        yanchor 0 size 40 xalign 0.5 text_align 0.5 xfill True xminimum cr_last_max_w
    style cr_style_copytight is cr_style_base
    style cr_style_copytight:
        xalign 0 yanchor 0 size 40
    style cr_style_copytight_link is cr_style_base
    style cr_style_copytight_link:
        xalign 0 yanchor 0 size 40 xoffset 50


    image cr_game_subtitle = Text(_("Thanks for playing"), slow=False, style="cr_style_game_subtitle")
    image cr_game_title = Text("LIMBUS INC", slow=False, style="cr_style_game_title")
    image cr_final = Fixed(VBox(
        Text(_("The rules of Limbo works in a real life."), style="cr_style_last"),
        Null(height=5),
        Text(_("Watch yourself and be carefull while breaking someone’s illusions."), style="cr_style_last"),
        Null(height=299),
        Text(_("© 2020 IT Happens"), style="cr_style_copytight"),
        Null(height=5),
        Text(_("© 2020 And Tak Soidet Games"), style="cr_style_copytight"),
        Null(height=5),
        Text(_("https://andtaksoidet.games"), style="cr_style_copytight_link"),
        xfill=True, xminimum=cr_last_max_w
    ), xysize=(cr_last_max_w, 515), xanchor=0.5)

    transform cr_trans_credits(yfrom, yto, t, wait_t):
        xanchor 0.5 yanchor 0.0
        xpos (1920 / 2) ypos yfrom alpha 1.0
        pause wait_t
        linear t ypos yto

    transform cr_trans_game_title_show(cr_h, wait):
        xpos (1920 / 2) ypos (1080 / 2) alpha 0.0
        (1.0 if wait else 0.0)
        ease 1.0 alpha 1.0
        3.0
        linear credits_time ypos (1080 / 2 - cr_h - 1080)
    transform cr_trans_game_subtitle_show(cr_h):
        xpos (1920 / 2) ypos (1080 / 2 - 120) alpha 0.0
        ease 0.5 alpha 1.0
        2.5
        2.0
        linear credits_time ypos (1080 / 2 - 120 - cr_h - 1080)
    
    transform trans_cr_duck_pos:
        xanchor 0.5 yanchor 0.5 xpos 1290 ypos 710
        1.0
        ease 1.0 xpos 1190

    
    image all_credits = Fixed(*cr_objects, xysize=(cr_max_w, cr_credits_height), xanchor=0.5)

    default IS_ENDING_CREDITS = False

label credits:
    $ IS_ENDING_CREDITS = True
    jump show_credits

label menu_credits:
    $ IS_ENDING_CREDITS = False
    jump show_credits

label show_credits:
    $ quick_menu = False
    $ config.rollback_enabled = False
    $ old_game_menu_screen = _game_menu_screen
    $ _game_menu_screen = None
    scene black
    with dissolve

    if IS_ENDING_CREDITS:
        $ renpy.pause(delay=2.0, hard=True)
        if ENDING_UNLOCKED == "good":
            $ renpy.notify(_("Good ending unlocked. Congratulations!"))
        elif ENDING_UNLOCKED == "norm":
            $ renpy.notify(_("Neutral ending unlocked."))
        elif ENDING_UNLOCKED == "bad":
            $ renpy.notify(_("Bad ending unlocked"))

    if IS_ENDING_CREDITS:
        show cr_game_subtitle at cr_trans_game_subtitle_show(cr_credits_height)
    show cr_game_title at cr_trans_game_title_show(cr_credits_height, IS_ENDING_CREDITS)
    show all_credits at cr_trans_credits(1080, -cr_credits_height, credits_time, (6.0 if IS_ENDING_CREDITS else 4.0))
    show cr_final at cr_trans_credits(1080 + cr_credits_height + 495, 495, credits_time, (6.0 if IS_ENDING_CREDITS else 4.0))

    $ renpy.pause(delay=10.0, hard=IS_ENDING_CREDITS)
    pause credits_time #+ (6.0 if IS_ENDING_CREDITS else 4.0)

    scene black
    with dissolve

    $ renpy.pause(delay=0.5, hard=True)

    if IS_ENDING_CREDITS:
        show duck_ovl at truecenter
        show bg limb_cr behind duck_ovl at truecenter with dissolve
        $ renpy.pause(delay=1.0, hard=True)
        show duck silent behind duck_ovl at trans_cr_duck_pos with dissolve
        $ renpy.pause(delay=2.0, hard=True)
        show duck quack with dissolve
        duck "Quack!"
        $ renpy.pause(delay=0.5, hard=True)
        scene black
        with dissolve
        $ renpy.pause(delay=1.0, hard=True)


    $ quick_menu = True
    $ config.rollback_enabled = True
    $ _game_menu_screen = old_game_menu_screen
    return
