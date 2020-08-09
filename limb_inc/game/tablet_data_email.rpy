init:
    default TAB_EMAIL_RECEIVED = []
    default TAB_EMAIL_READ = set()
    default MAIL_CHARACTER_NAME = ""
    default THIS_MAIL_FIRST_TIME = False
    define mail = DynamicCharacter("MAIL_CHARACTER_NAME")

init python:
    def tab_email_attenion():
        global TAB_EMAIL_RECEIVED, TAB_EMAIL_READ
        for i in TAB_EMAIL_RECEIVED:
            if i not in TAB_EMAIL_READ:
                return True
        return False

label tablet_email_read(mail_id):
    show screen tablet_app_email_read(mail_id)
    python:
        MAIL_CHARACTER_NAME = TAB_EMAILS[mail_id]["from"]
        THIS_MAIL_FIRST_TIME = mail_id not in TAB_EMAIL_READ
        renpy.pause(delay=0.7, hard=True)
        TAB_EMAIL_READ = TAB_EMAIL_READ | {mail_id}
        renpy.call(TAB_EMAILS[mail_id]["label"])
        renpy.pause(delay=1.0, hard=True)
    return

## List of E-Mails ###############################################################################

init python:
    ADDR_VIOLET =  _("Violet Sharp <visharp@lmbs.xz>")
    ADDR_KURT =    _("Kurt Bachowski <kurtb@lmbs.xz>")
    TAB_EMAILS = {
        "violet-1": {
            "from": ADDR_VIOLET,
            "subj": _("Report on the incident"),
            "label": "email_violet_1"
        },
        "kurt-old": {
            "from": ADDR_KURT,
            "subj": _("Letter from Kurt"),
            "label": "email_kurt_old"
        }
    }

## E-Mail Dialogs ###############################################################################

label email_violet_1:
    mail "Greetings dr. [LAST_NAME]\n\nI've investigated the incident."
    mail "Complete report on this incident is in the attached document. Please read."
    mail "I'm waiting for your arrival.\n--\nRegards,\nViolet Sharp."
    $ add_doc("report", silent=False)
    mail "Attached file: Incident Report"
    if THIS_MAIL_FIRST_TIME:
        me "As I thought."
    return

label email_kurt_old:
    mail "Hi [FIRST_NAME]!"
    mail "Long time no see!"
    mail "{b}TO DO:{/b} More text needed."
    mail "Cheers!\nKurt"
    return
