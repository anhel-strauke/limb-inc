default TAB_CONTACTS_AVAIL = {"bella", "boris"}

init python:
    TAB_CONTACTS = {
        "bella": {
            "name": "Bella Rabinovich",
            "image": "bella on tablet.png",
            "descr": "CIRO Eastern Branch Limbus inc."
        },
        "boris": {
            "name": "Boris (Archivist)",
            "image": "boris on tablet",
            "descr": "Limbus Inc Archive operator"
        },
    }

label tablet_app_contacts_make_call(who):
    if who == "boris":
        if WAITING_FOR_BORIS_RESPONSE:
            "I’ve already requested the information. Boris will send me a response when it’s ready"
        else:
            "I don't have any requests for the Archive."
        jump tablet_app_call_cancelled
    show screen tablet_iface_outgoing_call(TAB_CONTACTS[who].get("name"), TAB_CONTACTS[who].get("image"))
    pause 2.0
    show screen tablet_iface_outgoing_call_no_answer(TAB_CONTACTS[who].get("name"), TAB_CONTACTS[who].get("image"))
    if who == "bella":
        "Oh yes, she's on the meeting in the Central Office. She will call me later."
    else:
        "No answer."

label tablet_app_call_cancelled:
    return