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
        renpy.retain_after_load()
        renpy.call(TAB_EMAILS[mail_id]["label"])
    return

## List of E-Mails ###############################################################################

init python:
    ADDR_VIOLET =  _("Violet Sharp <visharp@lmbs.xz>")
    ADDR_KURT =    _("Kurt Bachowski <kurtb@lmbs.xz>")
    ADDR_BORIS =   _("Boris <boris@arch.lmbs.xz>")
    TAB_EMAILS = {
        "violet-1": {
            "from": ADDR_VIOLET,
            "subj": _("Report on the incident"),
            "label": "email_violet_1"
        },
        "kurt-old": {
            "from": ADDR_KURT,
            "subj": _("Congratulations!"),
            "label": "email_kurt_old"
        },
        "boris_hans_nicht": {
            "from": ADDR_BORIS,
            "subj": _("Response for request"),
            "label": "mail_boris_1"
        },
        "boris_layla_file": {
            "from": ADDR_BORIS,
            "subj": _("Anderson profile"),
            "label": "mail_boris_layla_file"
        },
        "boris_violet_file": {
            "from": ADDR_BORIS,
            "subj": _("Sharp profile"),
            "label": "mail_boris_sharp_profile"
        }
    }

## E-Mail Dialogs ###############################################################################

label email_violet_1:
    mail "Greetings Dr. [LAST_NAME],\nI've made a report on the incident for you."
    mail "I'm waiting for your arrival."
    mail "Regards,\nViolet Sharp."
    $ add_doc("report", silent=False)
    mail "Attached Document: Incident Report"
    if THIS_MAIL_FIRST_TIME:
        "All right, let’s see."
    return

label email_kurt_old:
    mail "Hi climber!"
    mail "Heard you are now under Dr. Rabinovich! Congrats! You are in one step from the CIRO’s chair."
    mail "I dont’t know how to write complimentary letters, you know. Hope it’s not very pathetic."
    mail "I’m really happy for you."
    mail "Look, you should come to visit us if you finally get the vacations. Miriam will be glad too."
    mail "There is an eco-zone construction nearby, and they promised us tickets with a corporative discount!"
    mail "I remember you always liked my stories about my father’s farm."
    mail "You should look at the real trees after all."
    mail "Have a nice day!\nKurt"
    if THIS_MAIL_FIRST_TIME:
        "And now it could be no sence in the vacations at all."
        "Hold on, Kurt, I’m coming."
    return

label mail_boris_1:
    mail "Hi!"
    mail "There is something strange with you request."
    mail "Take a look at the attached file. Like a pulp fiction, I swear you."
    mail "Cheers,\nBoris (still the Archivist)"
    $ add_doc("hans_nicht", silent=False)
    mail "Attached Document: Response From Archive"
    return

label mail_boris_layla_file:
    mail "Hi [FIRST_NAME],"
    mail "I’ve heard that you meet a young lady. I don’t believe she is a chosen one, but I thought you will want to know more on her."
    mail "Do not thank."
    mail "Regards,\nBoris,\nfrom the deepest caves of knowlege."
    $ add_doc("layla_profile", silent=False)
    mail "Attached Document: Layla Anderson Profile"
    return

label mail_boris_sharp_profile:
    mail "Hi Dr. Seuss! Oh, I mean, Dr. [LAST_NAME]."
    mail "What do you think about ms. Sharp?"
    mail "Don’t be quick, take a look at this document first."
    mail "Miss you.\nBoris (guess-who?)"
    $ add_doc("violet_profile", silent=False)
    mail "Attached Document: Violet Sharp Profile"
    if THIS_MAIL_FIRST_TIME:
        "Boris is strange."
    return