init:
    default TAB_WEB_AVAIL = {"cyberherald", "weather"}
    default TAB_WEB_VISITED = {"cyberherald", "weather"}
    default CYBERHERALD_VISITED = {"a1"}
    default CYBERHERALD_AVAIL = ["a1", "cyberdog", "landfill"]
    default SOCNET_AVAIL = set()
    default SOCNET_VISITED = set()

define w = Character()

init python:
    def tab_websites_ordered():
        global TAB_WEB_SITES, TAB_WEB_AVAIL
        return sorted(list(TAB_WEB_AVAIL), key=lambda x: TAB_WEB_SITES[x]["order"])
    
    def site_need_attenion(site):
        if site not in TAB_WEB_AVAIL:
            return False
        if site not in TAB_WEB_VISITED:
            return True
        if site == "cyberherald":
            for av in CYBERHERALD_AVAIL:
                if av not in CYBERHERALD_VISITED and TAB_CYBERHERALD_ARTICLES[av].get("important", False):
                    return True
        elif site == "socnet":
            for av in SOCNET_AVAIL:
                if av not in SOCNET_VISITED:
                    return True
        return False

    def tab_browser_attenion():
        global TAB_WEB_SITES
        for site_id in TAB_WEB_SITES:
            if site_need_attenion(site_id):
                return True
        return False

label show_web_site(site_id):
    show screen tablet_app_browser_site_title(TAB_WEB_SITES[site_id].get("name", "Web Site"))
    python:
        TAB_WEB_VISITED = TAB_WEB_VISITED | {site_id}
        renpy.call(TAB_WEB_SITES[site_id]["label"])
    return


## Web Sites Data #########################################################################

init python:
    TAB_WEB_SITES = {
        "cyberherald": {
            "order": 0,
            "name": _("The Cyber Herald"),
            "descr": _("News and useful information"),
            "icon": "ch",
            "label": "web_cyberherald"
        },
        "math_university": {
            "order": 10,
            "name": _("Math Analysis Department"),
            "descr": _("Math analysis department of the Academy"),
            "icon": "atomic",
            "label": "web_math"
        },
        "socnet": {
            "order": 20,
            "name": _("LinkTogether"),
            "descr": _("Sociald network"),
            "icon": "soc",
            "label": "web_socnet"
        },
        "weather": {
            "order": 100,
            "name": _("WeatherSite"),
            "descr": _("Weather forecasts"),
            "icon": "web",
            "label": "web_weather"
        }
    }

    TAB_CYBERHERALD_ARTICLES = {
        "a1": {
            "title": _("New CPU from UMD"),
            "text": _("Brand new processor from UMD, the leading silicon company."),
            "label": "ch_a1"
        },
        "landfill": {
            "title": _("A Landfill Debates"),
            "text": _("Debates on the construction of a new landfill continues."),
            "label": "ch_landfill",
        },
        "cyberdog": {
            "title": _("New Cyberdog model"),
            "text": _("Cyberdyne Systems announces a new model of the cyberdog."),
            "label": "ch_cyberdog"
        },
        "corp_war": {
            "title": _("Corporate War"),
            "text": _("Some details on the ongoing war between corporations."),
            "label": "ch_corp_war"
        }
    }

    TAB_SOCNET_PROFILES = {

    }

## Web Site Icons ############################################################

init python:
    # Generate website icon styles
    def web_icon_style(icon):
        return "tablet_web_icon_%s" % icon

    for k in TAB_WEB_SITES:
        icon = TAB_WEB_SITES[k].get("icon", "")
        if not icon:
            icon = "web"
        style_name = web_icon_style(icon)
        stl = Style(style.default)
        stl.xsize = 64
        stl.ysize = 64
        stl.background = "tablet/web/%s.png" % icon
        stl.hover_background = "tablet/web/%s_hover.png" % icon
        setattr(style, style_name, stl)

##############################################################################
## Web Site Labels ###########################################################

## WeatherSite ###############################################################
screen website_weather():
    tag tablet_web_page
    style_prefix "tablet"
    use tablet_app_browser_site:
        vbox:
            text _("WeatherSite") xalign 0.5 size 80
            null height 20
            text _("The most precious forecasts in the world.")
            null height 40
            text _("The weather conditions:") xalign 0.5
            null height 20
            text _("24°C / 75°F") size 100 xalign 0.5
            text _("Sunny and clear") xalign 0.5

label web_weather:
    show screen website_weather
    me "Good news, no rain today."
    return

## The Cyber Herald ##########################################################
screen website_cyberherald():
    tag tablet_web_page
    style_prefix "tablet"
    use tablet_app_browser_site:
        vbox:
            xfill True
            text _("The Cyber Herald") xalign 0.5 size 60
            text _("News and useful information") xalign 0.5 size 20
            null height 20
            text _("Latest Articles")
            for art in reversed(CYBERHERALD_AVAIL):
                hbox:
                    if art in CYBERHERALD_VISITED:
                        text "•":
                            at transform:
                                alpha 0.0
                    else:
                        text "•"
                    null width 20
                    textbutton TAB_CYBERHERALD_ARTICLES[art]["title"] action Call("web_cyberherald_article", art, from_current=True) text_hover_underline True

screen website_cyberherald_read(title, txt):
    tag tablet_web_page
    style_prefix "tablet"
    use tablet_app_browser_site:
        vbox:
            xfill True
            text _("The Cyber Herald") xalign 0.5 size 60
            text _("News and useful information") xalign 0.5 size 20
            null height 40
            text title size 60
            null height 20
            text txt
                    
label web_cyberherald:
    show screen website_cyberherald
    return

label web_cyberherald_article(art_id):
    show screen website_cyberherald_read(TAB_CYBERHERALD_ARTICLES[art_id]["title"], TAB_CYBERHERALD_ARTICLES[art_id]["text"])
    $ CYBERHERALD_VISITED = CYBERHERALD_VISITED | {art_id}
    $ renpy.call(TAB_CYBERHERALD_ARTICLES[art_id]["label"])
    show screen website_cyberherald
    return

label ch_a1:
    w "New CPU was presented yesterday on the Consumers Electronics Show in the San Francisco."
    w "It has incredible speed and also a low power consumption."
    w "It will be available by the end of the current year."
    return

label ch_landfill:
    w "The construction of a new landfill is still causing fierce debate."
    w "Environmentalists warn of serious problems associated with it."
    w "The construction company, in turn, assures that they use the most modern technologies."
    w "The Cyber Herald continues to monitor this debate."
    return

label ch_cyberdog:
    w "Cyberdyne Systems announced a new cyber dog model yesterday."
    w "New model “Milo D12” will replace an old one called “Fido D8”."
    w "Milo D12 has an advanced AI and sensors system."
    w "Store delivery will begin next month."
    return

label ch_corp_war:
    w "War. War never changes."
    w "{b}TO DO:{/b} The War between corporations? What?"
    return