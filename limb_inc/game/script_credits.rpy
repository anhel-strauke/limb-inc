init:
    define CREDITS_STRINGS = (
            (
                _("Idea"),
                (
                    _("{size=60}Dina Griko{/size}"),
                ),
            ),
            (
                _("Scenario"),
                (
                    _("{size=60}Timirlan Kenjibaev{/size}"),
                ),
            ),
            (
                _("Special Guest"),
                (
                    _("{size=60}Andrey Zykin{/size}{p}{i}as Boris the Archivist{/i}"),
                )
            ),
            (
                _("Narrative"),
                (
                    _("Timirlan Kenjibaev"),
                    _("Dina Griko"),
                    _("Alexandra Pikarevskaya"),
                )
            ),
            (
                _("English Translation"),
                (
                    _("Alexandra Kanapina"),
                    _("Naina Kovyazina"),
                    _("Sergei Reischel"),
                    _("Darya Bocharova"),
                    _("V.M.A."),
                    _("Timirlan Kenjibaev"),
                    _("Anatoly Griko"),
                    _("Dina Griko"),
                )
            ),
            (
                _("Backgrounds Art"),
                (
                    (_("Bravo"), "artstation.com/nadezhdarunova"), # ← ?
                    _("Anatoly Griko"),
                )
            ),
            (
                _("Limbo Backgrounds Art"),
                (
                    (_("Vadim Zalepaev"), "vk.com/3wy3wy"),
                )
            ),
            (
                _("Characters Art"),
                (
                    (_("Taya Chugainova"), "vk.com/thekingdomofkai"),
                )
            ),
            (
                _("Limbo Characters Art"),
                (
                    (_("Margarita Kamushek"), "vk.com/teamochi"),
                    (_("Vadim Zalepaev"), "vk.com/3wy3wy"),
                )
            ),
            (
                _("Animations"),
                (
                    _("Anatoly Griko"),
                )
            ),
            (
                _("Programming"),
                (
                    _("Anatoly Griko"),
                )
            ),
            (
                _("Scripting"),
                (
                    _("Anatoly Griko"),
                    _("Dina Griko"),
                )
            ),
            (
                _("Sound Design"),
                (
                    (_("Vlad Ulrich"), "github.com/Wedmer"),
                    _("Anatoly Griko"),
                )
            ),
            (
                _("Special Thanks"),
                (
                    _("Anna Bolshakova"),
                    _("Anna Kovalenko"),
                    (_("Giglemash"), "github.com/Giglemash"),
                    _("Phil Michalski"),
                    _("Blazze Di"),
                )
            ),
        )

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
    credits_time = 66.0
    cr_credits_height = 0

    def build_credits():
        cr_credits_height = 0
        cr_y = 0
        objects = []
        
        for sindex, sect in enumerate(CREDITS_STRINGS):
            if type(sect[0]) is not tuple:
                sect_displayable = Text("[CREDITS_STRINGS[%d][0]!t]" % sindex, slow=False, style="cr_style_section", pos=(cr_max_w / 2, cr_y))
                objects.append(sect_displayable)
                cr_y += cr_section_height
            items = tuple() if len(sect) <= 1 or type(sect[1]) is not tuple else sect[1]
            if items:
                cr_y += cr_section_space
                for item_index, item in enumerate(items):
                    if type(item) is unicode or type(item) is str:
                        item_displayable = Text("[CREDITS_STRINGS[%d][1][%d]!t]" % (sindex, item_index), slow=False, style="cr_style_item", pos=(cr_max_w / 2, cr_y))
                        objects.append(item_displayable)
                        cr_y += (cr_item_height + cr_item_space)
                    else:
                        left_displayable = Text("[CREDITS_STRINGS[%d][1][%d][0]!t]" % (sindex, item_index), slow=False, style="cr_style_item_left", pos=(cr_max_w / 2, cr_y))
                        cr_y += (cr_item_height + cr_subitem_space)
                        right_displayable = Text("[CREDITS_STRINGS[%d][1][%d][1]!t]" % (sindex, item_index), slow=False, style="cr_style_item_right", pos=(cr_max_w / 2, cr_y))
                        cr_y += (cr_subitem_height + cr_item_space)
                        objects.append(left_displayable)
                        objects.append(right_displayable)
                cr_y -= cr_item_space
            if type(sect[0]) is not tuple or items:
                cr_y += cr_section_margin
        
        objects.append(Text(__("Made with Ren’Py %d.%d") % (renpy.version_tuple[0], renpy.version_tuple[1]), slow=False, style="cr_style_section", pos=(cr_max_w / 2, cr_y)))
        cr_y += cr_section_height + cr_subitem_space
        objects.append(Text("https://www.renpy.org/", slow=False, style="cr_style_item", pos=(cr_max_w / 2, cr_y)))
        cr_y += cr_item_height + cr_section_margin
        cr_credits_height = cr_y
        return (cr_credits_height, objects)

init:
    style cr_style_base:
        font "Exo2" color "#ffffff" xanchor 0.5 yanchor 0.5
    style cr_style_game_subtitle is cr_style_base
    style cr_style_game_subtitle:
        size 60
    style cr_style_game_title is cr_style_base
    style cr_style_game_title:
        size 120
    style cr_style_game_ending is cr_style_base
    style cr_style_game_ending:
        size 40
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


init python:
    def regenerate_credits(t1, t2):
        global cr_credits_height, cr_max_w
        cr_credits_height, cr_objects = build_credits()
        return (Fixed(*cr_objects, xysize=(cr_max_w, cr_credits_height), xanchor=0.5), None)
    
    def regenerate_game_subtitle(t1, t2):
        return (Text(_("Thanks for playing"), slow=False, style="cr_style_game_subtitle"), None)
    
    def regenerate_final_message(t1, t2):
        return (Fixed(VBox(
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
        ), xysize=(cr_last_max_w, 515), xanchor=0.5), None)
    
    def regenerate_msg_good_ending(t1, t2):
        return (Text(_("You have reached a good ending"), slow=False, style="cr_style_game_ending"), None)

    def regenerate_msg_neutral_ending(t1, t2):
        return (Text(_("You have reached a neutral ending"), slow=False, style="cr_style_game_ending"), None)
    
    def regenerate_msg_bad_ending(t1, t2):
        return (Text(_("You have reached a bad ending"), slow=False, style="cr_style_game_ending"), None)

init:
    image cr_game_subtitle = DynamicDisplayable(regenerate_game_subtitle)
    image cr_game_title = Text("LIMBUS INC", slow=False, style="cr_style_game_title")
    image cr_final = DynamicDisplayable(regenerate_final_message)
    image all_credits = DynamicDisplayable(regenerate_credits)
    image cr_msg_good_ending = DynamicDisplayable(regenerate_msg_good_ending)
    image cr_msg_neutral_ending = DynamicDisplayable(regenerate_msg_neutral_ending)
    image cr_msg_bad_ending = DynamicDisplayable(regenerate_msg_bad_ending)

    transform cr_trans_credits(yfrom, yto, t, wait_t):
        xanchor 0.5 yanchor 0.0
        xpos (1920 / 2) ypos yfrom alpha 1.0
        pause wait_t
        linear t ypos yto

    transform cr_trans_game_title_show(cr_h, wait):
        xpos (1920 / 2) ypos (1080 / 2) alpha 0.0
        (1.0 if wait else 0.0)
        ease 1.0 alpha 1.0
        (4.5 if wait else 2.0)
        linear credits_time ypos (1080 / 2 - cr_h - 1080)

    transform cr_trans_game_subtitle_show(cr_h):
        xpos (1920 / 2) ypos (1080 / 2 - 120) alpha 0.0
        ease 0.5 alpha 1.0
        6.0
        linear credits_time ypos (1080 / 2 - 120 - cr_h - 1080)
    transform cr_trans_game_ending_show(cr_h):
        xpos (1920 / 2) ypos (1080 / 2 + 120) alpha 0.0
        2.5
        ease 1.0 alpha 1.0
        3.0
        linear credits_time ypos (1080 / 2 + 120 - cr_h - 1080)
    
    transform trans_cr_duck_pos:
        xanchor 0.5 yanchor 0.5 xpos 1290 ypos 710
        1.0
        ease 1.0 xpos 1190

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
        $ renpy.music.set_volume(1.0)
        play music credits

    if IS_ENDING_CREDITS:
        show cr_game_subtitle at cr_trans_game_subtitle_show(cr_credits_height)
    show cr_game_title at cr_trans_game_title_show(cr_credits_height, IS_ENDING_CREDITS)
    if IS_ENDING_CREDITS:
        if ENDING_UNLOCKED == "good":
            show cr_msg_good_ending at cr_trans_game_ending_show(cr_credits_height)
        elif ENDING_UNLOCKED == "norm":
            show cr_msg_neutral_ending at cr_trans_game_ending_show(cr_credits_height)
        elif ENDING_UNLOCKED == "bad":
            show cr_msg_bad_ending at cr_trans_game_ending_show(cr_credits_height)
    show all_credits at cr_trans_credits(1080, -cr_credits_height, credits_time, (6.5 if IS_ENDING_CREDITS else 4.0))
    show cr_final at cr_trans_credits(1080 + cr_credits_height + 495, 495, credits_time, (6.5 if IS_ENDING_CREDITS else 4.0))

    if IS_ENDING_CREDITS:
        $ renpy.pause(delay=10.0, hard=True)
        pause credits_time
    else:
        pause (credits_time + 10.0)

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
        play sound quack
        $ duck(_("Quack!"), interact=False, advance=False)
        $ renpy.pause(delay=2.0, hard=True)
        hide window
        $ renpy.pause(delay=0.5, hard=True)
        scene black
        with dissolve
        $ renpy.music.set_volume(0.0, delay=1.0)
        $ renpy.pause(delay=1.0, hard=True)
        stop music
        $ renpy.music.set_volume(1.0)


    $ quick_menu = True
    $ config.rollback_enabled = True
    $ _game_menu_screen = old_game_menu_screen
    return
