init:
    default TAB_DOCS_AVAIL = ["contract"]
    default TAB_DOCS_READ = set()
    default CURRENT_DOC_TITLE = ""
    default THIS_DOC_FIRST_TIME = False
    define doc = DynamicCharacter("CURRENT_DOC_TITLE")

init python:
    def tab_doc_attenion():
        global TAB_DOCS_AVAIL, TAB_DOCS_READ, TAB_DOCS
        for i in TAB_DOCS_AVAIL:
            if i not in TAB_DOCS_READ and TAB_DOCS[i].get("important", False):
                return True
        return False

label tablet_doc_read(doc_id):
    show screen tablet_app_docs_read(doc_id)
    python:
        CURRENT_DOC_TITLE = TAB_DOCS[doc_id]["name"]
        THIS_DOC_FIRST_TIME = doc_id not in TAB_DOCS_READ
        renpy.pause(delay=0.7, hard=True)
        TAB_DOCS_READ = TAB_DOCS_READ | {doc_id}
        renpy.call(TAB_DOCS[doc_id]["label"])
    return

## Documents List ########################################################################
init python:
    TAB_DOCS = {
        "report": {
            "name": _("Incident Report"),
            "descr": _("Report from Violet Sharp on the incident with Kurt Bachowski"),
            "label": "doc_report",
            "important": True
        },
        "secret": {
            "name": _("Transferred File"),
            "descr": _("You're already familiar with the case?"),
            "label": "doc_secret"
        },
        "contract": {
            "name": _("Limbus Inc Contract"),
            "descr": _("Employment Contract between you and Limbus Inc."),
            "label": "doc_contract"
        },
        "kurt_profile": {
            "name": _("Profile of Kurt Bachowski"),
            "descr": _("Full personal information about Kurt Bachowski as employee of the Limbus Inc."),
            "label": "doc_kurt_profile",
            "important": True
        },
        "miriam_profile": {
            "name": _("Profile of Miriam Bachowski"),
            "descr": _("Full personal information about Miriam Bachowski as employee of the Limbus Inc."),
            "label": "doc_miriam_profile",
        },
        "layla_profile": {
            "name": _("Profile of Layla Anderson"),
            "descr": _("Full personal information about Layla Anderson as employee of the Limbus Inc."),
            "label": "doc_layla_profile",
        }
    }

## Documents Contents ####################################################################

label doc_report:
    doc "LIMBUS INC CONFIDENTIAL *** REPORT ON THE INCIDENT XK 3412\nBy Violet Sharp"
    doc "{b}TO DO:{/b} Report contents"
    return

label doc_secret:
    doc "You're already familiar with the case?"
    doc "Take a closer look at the suspected one."
    doc "Hans Fry. Hans that does not exist at all, if you translate from German."
    doc "Look where he still figured, I think you will find a lot of interesting."
    me "Kid, who do you think you..."
    return

label doc_contract:
    doc "LIMBUS INC CONFIDENTIAL *** EMPLOYMENT CONTRACT"
    doc "This agreement was concluded between Limbus Incorporated and [FIRST_NAME] [LAST_NAME]."
    doc "Bla bla bla. Boring legal stuff."
    return

label doc_kurt_profile:
    doc "LIMBUS INC CONFIDENTIAL *** EMPLOYEE PROFILE"
    doc "{b}TO DO:{/b} Content needed."
    if THIS_DOC_FIRST_TIME:
        "Well, well..."
    return

label doc_miriam_profile:
    doc "LIMBUS INC CONFIDENTIAL *** EMPLOYEE PROFILE"
    doc "{b}TO DO:{/b} Content needed."
    return

label doc_layla_profile:
    doc "LIMBUS INC CONFIDENTIAL *** EMPLOYEE PROFILE"
    doc "{b}TO DO:{/b} Content needed."
    return