init:
    ## TODO: Add more messages when needed:
    default LANGUAGE_SELECT_MESSAGES = ["Please choose a preferred language", "Пожалуйста, выберите предпочитаемый язык"]

init python:
    if persistent.language_was_selected is None:
        persistent.language_was_selected = False

    def merge_lang_sel(old, new, current):
        current = bool(old) or bool(new)
        return current
    renpy.register_persistent("language_was_selected", merge_lang_sel)

    def get_languages_list():
        def default_lang_name(n):
            if n:
                return n.capitalize()
            return "???"
        
        LANG_NAMES = {
            None: "English",
            "russian": "Русский",
            ## TODO: Add more language names when needed
        }
        langs = [None] + list(renpy.known_languages())
        return [(LANG_NAMES.get(i, default_lang_name(i)), i) for i in langs]

transform blink_message_delayed(delay_shift, total_length):
    xanchor 0.5 yanchor 0.5 xpos (1920 / 2) ypos (1080 / 4 + 1080 / 8)
    alpha (0.0 if delay_shift > 0.0 else 1.0)
    pause delay_shift
    block:
        ease 0.3 alpha 1.0
        pause 1.4
        ease 0.3 alpha 0.0
        pause (total_length - 2.0)
        repeat

transform language_select_buttons:
    xanchor 0.5 yanchor 0.0 xpos (1920 / 2) ypos (1080 / 2)

screen first_time_choose_language():
    modal True
    fixed:
        style_prefix "first_time_choose_lang_base"
        for i, msg in enumerate(LANGUAGE_SELECT_MESSAGES):
            text msg at blink_message_delayed(i * 2.0, len(LANGUAGE_SELECT_MESSAGES) * 2.0) style "first_time_choose_lang_message"
        vbox:
            at language_select_buttons
            style_prefix "first_time_choose_lang_box"
            for lang_name, lang_id in get_languages_list():
                textbutton lang_name action [Language(lang_id), Return()]
        if renpy.variant("pc"):     
            textbutton _("Quit") at language_select_quit_button action Quit(confirm=False)

style first_time_choose_lang_message:
    font "Exo2" size 60 xalign 0.5 yalign 0.5 color "#ffffff"
style first_time_choose_lang_box_button_text:
    size 60 xalign 0.5 yalign 0.5 color "#a0a0a0" hover_color "#ffffff"
style first_time_choose_lang_base_button:
    xalign 1.0 yalign 1.0 bottom_margin 10 right_margin 20
style first_time_choose_lang_base_button_text:
    font "Exo2" size 40 color "#a0a0a0" hover_color "#ffffff"
transform language_select_quit_button:
    xalign 1.0 yalign 1.0

label main_menu:
    if False and not persistent.language_was_selected:
        scene black
        with dissolve
        call screen first_time_choose_language with dissolve
        $ persistent.language_was_selected = True

    $ renpy.transition(dissolve)
    jump main_menu_screen