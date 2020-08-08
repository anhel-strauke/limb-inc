default TAB_CONTACTS_AVAIL = {"bella",}

init python:
    TAB_CONTACTS = {
        "bella": {
            "name": "Bella Rabinovich",
            "image": "bella on tablet.png",
            "descr": "CIRO Eastern Branch Limbus inc."
        },
        "boris": {
            "name": "Boris (Archivist)",
            "image": ""
        },
        "dummy": {
            "name": "Dummy",
        }
    }

label tablet_app_contacts_make_call(who):
    show screen tablet_iface_outgoing_call(TAB_CONTACTS[who].get("name"), TAB_CONTACTS[who].get("image"))
    pause 2.0
    show screen tablet_iface_outgoing_call_no_answer(TAB_CONTACTS[who].get("name"), TAB_CONTACTS[who].get("image"))
    if who == "bella":
        "Oh yes, she's on the meeting in the Central Office."
    else:
        "No answer."
label tablet_app_call_cancelled:
    return