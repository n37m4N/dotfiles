## My Config ##
## n37m4n    ##
config.load_autoconfig()
## Load .Xresources 
import subprocess
def read_xresources(prefix):
    props = {}
    x = subprocess.run(['xrdb', '-query'], stdout=subprocess.PIPE)
    lines = x.stdout.decode().split('\n')
    for line in filter(lambda l : l.startswith(prefix), lines):
        prop, _, value = line.partition(':\t')
        props[prop] = value
    return props
xresources = read_xresources('*')
#### Status Bar 
### MODES
c.statusbar.padding = {'bottom': 2, 'left':0, 'right':0, 'top':5}
#c.statusbar.widgets = ['text:foo',"keypress","url"]
#Normal
c.colors.statusbar.normal.bg = xresources['*.background']
c.colors.statusbar.normal.fg = xresources['*.color7']
c.colors.statusbar.progress.bg = xresources['*.color11']
#Private
c.colors.statusbar.private.bg = xresources['*.background']
c.colors.statusbar.private.fg = xresources['*.color1']
#Caret
c.colors.statusbar.caret.bg = xresources['*.color5']
c.colors.statusbar.caret.fg = xresources['*.color0']
#Selection
c.colors.statusbar.caret.selection.bg = xresources['*.color13']
c.colors.statusbar.caret.selection.fg = xresources['*.color0']
#NormalBrowsing Command
c.colors.statusbar.command.bg = xresources['*.background']
c.colors.statusbar.command.fg = xresources['*.foreground']
#Private Browsing Command
c.colors.statusbar.command.private.bg = xresources['*.background']
c.colors.statusbar.command.private.fg = xresources['*.foreground']
#Insert
c.colors.statusbar.insert.bg = xresources['*.color10']
c.colors.statusbar.insert.fg = xresources['*.color0']
#Passthrough/CTRL-V
c.colors.statusbar.passthrough.bg = xresources['*.color4']
c.colors.statusbar.passthrough.fg = xresources['*.color0']
#HTTP/S_Handling
c.colors.statusbar.url.fg = xresources['*.color15']
c.colors.statusbar.url.error.fg = xresources['*.color1']
c.colors.statusbar.url.hover.fg = xresources['*.color15']
c.colors.statusbar.url.warn.fg = xresources['*.color11']
c.colors.statusbar.url.success.http.fg = xresources['*.color1']
c.colors.statusbar.url.success.https.fg = xresources['*.color2']

####Completion
#Category
c.colors.completion.category.bg = xresources['*.background']
c.colors.completion.category.fg = xresources['*.foreground']
c.colors.completion.category.border.bottom = xresources['*.color6']
c.colors.completion.category.border.top = xresources['*.background']
#Completion
c.colors.completion.even.bg = xresources['*.color0']
c.colors.completion.odd.bg = xresources['*.color8']
c.colors.completion.fg = xresources['*.color15']
c.colors.completion.match.fg= xresources['*.color6']
c.completion.web_history.max_items = 5
c.completion.cmd_history_max_items = 0
c.completion.height = '35%'
c.completion.open_categories = ['bookmarks', 'history', 'searchengines']
##Item
c.colors.completion.item.selected.bg = xresources['*.color6']
c.colors.completion.item.selected.fg = xresources['*.color0']
c.colors.completion.item.selected.border.top = xresources['*.background']
c.colors.completion.item.selected.border.bottom = xresources['*.background']
##Scrollbar
c.scrolling.bar = 'never'
c.colors.completion.scrollbar.bg= xresources['*.color1']
c.colors.completion.scrollbar.fg = xresources['*.color1']
c.completion.scrollbar.padding = 0
c.completion.scrollbar.width = 0

####Downloads
c.colors.downloads.bar.bg = xresources['*.background']
#Start
c.colors.downloads.start.bg = xresources['*.background']
c.colors.downloads.start.fg = xresources['*.color7']
#Stop
c.colors.downloads.stop.bg = xresources['*.background']
c.colors.downloads.stop.fg = xresources['*.color2']
#Error
c.colors.downloads.error.bg = xresources['*.background']
c.colors.downloads.error.fg = xresources['*.color1']

####Hints
c.colors.hints.bg = xresources['*.background']
c.colors.hints.fg = xresources['*.foreground']
c.colors.hints.match.fg = xresources['*.background']
c.colors.keyhint.bg = xresources['*.background']
c.colors.keyhint.fg = xresources['*.color1']
c.colors.keyhint.suffix.fg = xresources['*.foreground']
c.hints.border = '2px outset #5e9d87'
c.keyhint.radius = 10
c.hints.chars = 'asfghjkl'
#c.hints.dictionary = /usr/share/dict/words
#c.hints.leave_on_load = True

####Messages
#Info
c.colors.messages.info.bg = xresources['*.background']
c.colors.messages.info.fg = xresources['*.color14']
c.colors.messages.info.border = xresources['*.background']
#Warning
c.colors.messages.warning.bg = xresources['*.background']
c.colors.messages.warning.fg = xresources['*.color3']
c.colors.messages.warning.border = xresources['*.background']
#Error
c.colors.messages.error.bg = xresources['*.background']
c.colors.messages.error.fg = xresources['*.color1']
c.colors.messages.error.border = xresources['*.background']

####Prompts
c.colors.prompts.bg = xresources['*.background']
c.colors.prompts.fg = xresources['*.foreground']
c.colors.prompts.border = xresources['*.foreground']
c.colors.prompts.selected.bg = xresources['*.color8']
c.prompt.radius = 10
####TABS
c.colors.tabs.bar.bg = xresources['*.background']
c.colors.tabs.even.bg = xresources['*.color8']
c.colors.tabs.even.fg = xresources['*.color15']
c.colors.tabs.odd.bg = xresources['*.color8']
c.colors.tabs.odd.fg = xresources['*.color15']
c.tabs.favicons.show = "never"
###Selected
c.colors.tabs.selected.even.bg = xresources['*.color0']
c.colors.tabs.selected.odd.bg = xresources['*.color0']
c.colors.tabs.selected.even.fg = xresources['*.color15']
c.colors.tabs.selected.odd.fg = xresources['*.color15']
#Indicator is far right within the tab
c.colors.tabs.indicator.error = xresources['*.color1']
c.colors.tabs.indicator.start = xresources['*.color0']
c.colors.tabs.indicator.stop = xresources['*.color5']
#c.colors.tabs.indicator.system = rgb
#c.tabs.indicator.padding = {'top':5, 'bottom':0, 'left':0, 'right':4}
c.tabs.indicator.width = 0
c.tabs.padding = {'bottom': 0, 'left':5, 'right':5, 'top':0}
c.tabs.title.alignment = "center"
c.tabs.title.format = "{index}:{id}{title_sep}| {title} :{protocol}"


#### Webpage
c.colors.webpage.bg = xresources['*.color0']
#c.colors.webpage.preferred_color_scheme = "dark"
c.url.auto_search = "never"
c.url.default_page = "about:blank:"
c.url.searchengines = {
        "DEFAULT"   : "https://duckduckgo.com/?q={}",
        "du"        : "https://duckduckgo.com/?q={}",
        "cve"       : "https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword={}",
        "tr"        : "https://russiandict.net/translate/{}"
        }
#auto-saves of config/cookies/etc within millisceonds
c.auto_save.interval = 15000
c.auto_save.session = False
#alt 'webkit'(similar to safari) -- current based on Chromium
c.backend = 'webengine'
#c.changelog_after_upgrade = 'patch'
c.messages.timeout = 120000
c.window.hide_decoration = True

####Content Handling
c.content.autoplay = False
c.content.cookies.accept = 'no-unknown-3rdparty'
#c.content.cookies.store = False
c.content.desktop_capture = False
c.content.geolocation = False
c.content.hyperlink_auditing = True
c.content.images = True 
#c.content.mouse_lock =
#c.content.notifications.enabled = False
#c.content.notifications.presenter = 'qt'
c.content.pdfjs = True
c.content.plugins = True
#c.content.prefers_reduced_motion = True
#c.content.print_element_backgrounds
#c.content.unknown_url_scheme_policy = 'disallow'
#c.content.webrtc_ip_handling_policy = 'disable-non-proxied-upd'
c.content.xss_auditing = True
#c.input.mouse.back_forward_buttons = False
##Headers
#c.content.headers.accept_language = en-US,en;q-0.9
#c.content.headers.custom = TYPE Dict
#c.content.headers.user_agent =
#c.content.netrc_file
##Javascript
c.content.javascript.can_access_clipboard = False
#c.content.javascript.can_close_tabs= False
c.content.javascript.can_open_tabs_automatically = False
#c.content.javascript.enabled = False
#c.content.javascript.log = 'warning'
##Local
c.content.local_content_can_access_file_urls = False
c.content.local_content_can_access_remote_urls = False
#c.content.local_storage = False
##Media
#c.content.media.audio_capture = ask
#c.content.media.audio_video_capture = ask
##Logging
#c.logging.console = 'error'
#c.logging.ram = 'error'
##Content Blocking
#c.content.blocking.adblock.lists =
#c.content.blocking.method = str(both)
#c.content.blocking.enabled = True
#c.content.blocking.hosts.block_subdomains = True
#c.content.blocking.host.lists = '~/.config/qutebrowser/blocked-hosts'
#c.content.blocking.blocking.whitelist =
#c.content.cache.size = in bytes max is 2gb
##Downloads
#c.downloads.location.remember = False
#c.downloads.open_dispatch =' {/usr/share/}opener'


##set fonts.default literation
#### QT
#c.qt.args = addition arguments to pass to Qt, without leading --
#c.qt.force_software_rendering = "chromium"
#c.qt.low_end_device_mode = "always"
#c.qt.process_model = "single-process" for debugging
#c.spellcheck.languages = "en-US, ru-RU"
#### Aliases ####
c.aliases = {
        'src': 'config-source'
        }
