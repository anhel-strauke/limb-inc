init:
    default TAB_EMAIL_RECEIVED = []
    default TAB_EMAIL_READ = set()
    default MAIL_CHARACTER_NAME = ""
    default THIS_MAIL_FIRST_TIME = False

define mail = DynamicCharacter("MAIL_CHARACTER_NAME")

init python:
    ADDR_VIOLET =  _("Violet Sharp <violetsharp@corp.limbus>")
    TAB_EMAILS = {
        "violet-1": {
            "from": ADDR_VIOLET,
            "subj": _("Report on the incident"),
            "label": "email_violet_1"
        }
    }

label tablet_email_read(mail_id):
    show screen tablet_app_email_read(mail_id)
    $ MAIL_CHARACTER_NAME = TAB_EMAILS[mail_id]["from"]
    $ THIS_MAIL_FIRST_TIME = mail_id not in TAB_EMAIL_READ
    $ renpy.pause(delay=0.7, hard=True)
    $ renpy.call(TAB_EMAILS[mail_id]["label"])
    $ TAB_EMAIL_READ = TAB_EMAIL_READ | {mail_id}
    return

label email_violet_1:
    mail "Greetings dr. [LAST_NAME]\n\nI've investigated the incident."
    mail "Complete report on this incident is in the attached document. Please read."
    mail "I'm waiting for your arrival.\n--\nRegards,\nViolet Sharp."
    if THIS_MAIL_FIRST_TIME:
        me "As I thought."
    return