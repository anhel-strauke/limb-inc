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
            "descr": _("Today’s Hot News"),
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
            "title": _("New Cyberdog Model"),
            "text": _("Cyberdyne Systems announces a new model of the cyberdog."),
            "label": "ch_cyberdog"
        },
        "corp_war": {
            "title": _("Corporate War"),
            "text": _("Some details on the ongoing war between corporations."),
            "label": "ch_corp_war"
        },
        "psychic": {
            "title": _("Novel Antipsychotics"),
            "text": _("A novelty on the market among approved antipsychotics!"),
            "label": "ch_psychic"
        },
        "limbus_ai": {
            "title": _(""),
            "text": _(""),
            "label": "ch_limbus_ai"
        }
    }

    TAB_SOCNET_PROFILES = {
        "violet": {

        },
        "kaz": {

        }
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
            text _(":::::::::::::::::::::::::::::::::::: TODAY’S HOT NEWS ::::::::::::::::::::::::::::::::::::") xalign 0.5 size 20
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
            text _(":::::::::::::::::::::::::::::::::::: TODAY’S HOT NEWS ::::::::::::::::::::::::::::::::::::") xalign 0.5 size 20
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



## Cyber Herald Articles ############################################################################

label ch_a1:
    w "New CPU was presented yesterday on the Consumers Electronics Show in the San Francisco."
    w "It has incredible speed and also a low power consumption."
    w "It will be available by the end of the current year."
    return

label ch_landfill:
    w "Heading “Deadly Sin”: Four corporations are still fighting for the right to obtain a license to own a landfill in Zhilmassiv-City."
    w "As a result of the redistribution of the territory, three industrial buildings and one residential structure were blown up."
    w "The number of victims is currently being determined."
    w "The head of security Robotics Inc. has been taken into custody on charges of reckless handling of explosives."
    w "The commercial director of Somnium-N, accused of organizing spontaneous large-scale rallies among the residents of the district, was released on bail."
    w "The chairman of the Natural Life League has announced his willingness to press charges on the warehouse owners on Sixteenth Avenue."
    w "Will we have a place to dump our trash next year?"
    w "Connect to the online broadcast to listen to the comments of the best lawyers in the city!"
    return

label ch_cyberdog:
    w "Cyberdyne Systems announced the tenth version of ITerrier is on sale!"
    w "A new faithful friend and the best we can offer to anyone wishing to upgrade from the ninth model!"
    w "This cybernetic dog with an improved body and a brand-new operating system will become an excellent home companion for you and your children!"
    w "The first thousand customers will receive models with eye lenses in a unique green shade."
    return

label ch_corp_war:
    w "War. War never changes."
    w "{b}TO DO:{/b} The War between corporations? What?"
    return

label ch_psychic:
    w "Somnium-N Society has carried out the final set of clinical trials and launched its latest project on the market — TenebrioSTOP."
    w "This medicine is a real breakthrough for those willing to balance their life and improve the reality they have to face every day."
    w "A simple and reliable tool will guarantee mental peace and save you the pain of having to pay for psychiatric services."
    w "Are you looking for restful sleep and less irritability?"
    w "Are you suffering from alcoholism or drug delirium that you would not dare confessing, even to your best friend?"
    w "Are you experiencing auditory or visual hallucinations?"
    w "There is nothing to be ashamed of, the main thing is to start working on yourself!"
    w "TenebrioSTOP will make your world simple and manageable again!"
    w "TenebrioSTOP - the recommendation of the best psychiatrists! *\nAvailable without a prescription.\n{size=20}* based on the results of the evaluation carried by Vector-Blum company.{/size}"
    return


