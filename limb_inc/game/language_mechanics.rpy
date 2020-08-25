init:
    ## TODO: Add more messages when needed:
    define LANGUAGE_SELECT_MESSAGES = ["Please choose a preferred language", "Пожалуйста, выберите предпочитаемый язык"]
    default CHARACTER_GENDER = 0

init python:
    CURRENT_LANGUAGE_NEEDS_GENDER = False # English is default and it does not need a gender of main character

    if persistent.language_was_selected is None:
        persistent.language_was_selected = False

    def merge_lang_sel(old, new, current):
        current = bool(old) or bool(new)
        return current
    renpy.register_persistent("language_was_selected", merge_lang_sel)

    def language_is_selected():
        persistent.language_was_selected = True
        renpy.save_persistent()

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

    def current_language_needs_gender_selection():
        ## TODO: Add more languages when needed
        return _preferences.language in ("russian", )

    def gender_tag(tag, argument, contents):
        global CHARACTER_GENDER
        results = [[]]
        current_index = 0
        for kind, txt in contents:
            if kind == renpy.TEXT_TEXT:
                bar_pos = txt.index("/")
                if bar_pos >= 0:
                    curr_txt = txt[:bar_pos]
                    next_txt = txt[bar_pos + 1:]
                    results[current_index].append((kind, curr_txt))
                    results.append([(kind, next_txt)])
                    current_index += 1
                    continue
            results[current_index].append((kind, txt))
        if CHARACTER_GENDER < len(results):
            return results[CHARACTER_GENDER]
        else:
            return results[-1]
    
    config.custom_text_tags["g"] = gender_tag

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
                textbutton lang_name action [Language(lang_id), Function(language_is_selected, _update_screens=False), Return()]
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
    xalign 1.0 yalign 1.0 xoffset -10 yoffset -10

label main_menu:
    if not persistent.language_was_selected:
        scene black
        with dissolve
        call screen first_time_choose_language with dissolve

    $ renpy.transition(dissolve)
    jump main_menu_screen