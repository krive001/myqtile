# Copyright (c) 2019 Kriszián Veress (krive)
# https://github.com/krive001/qtile


import os
# import re
# import socket
import subprocess
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook

import memory
import custom
import mpdwidget
import pacman
import wttrweather
import net


# deffinie
mod = "mod4"
home = os.path.expanduser('~')
myTerm = "urxvt"
myBrowser = "chromium"


# @lazy.function
# def window_to_prev_group(qtile):
#     if qtile.currentWindow is not None:
#         i = qtile.groups.index(qtile.currentGroup)
#         qtile.currentWindow.togroup(qtile.groups[i - 1].name)


# @lazy.function
# def window_to_next_group(qtile):
#     if qtile.currentWindow is not None:
#         i = qtile.groups.index(qtile.currentGroup)
#         qtile.currentWindow.togroup(qtile.groups[i + 1].name)


keys = [

    #########################
    # SUPER + ... KEYS      #
    #########################
    Key([mod], "a", lazy.spawn('pamac-manager'), desc="Open pamac manager."),
    Key([mod], "c", lazy.spawn('discord'), desc="Open discord."),
    Key([mod], "d", lazy.spawn("rofi -show run"), desc="Open rofi run."),
    Key([mod], "e", lazy.spawn("subl"), desc="Open subl."),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="fullscreen."),
    Key([mod], "h", lazy.spawn(myTerm + ' -e htop'), desc="Open htop."),
    Key([mod], "m", lazy.layout.maximize(), desc="Bsp layout maximize."),
    Key([mod], "n", lazy.layout.normalize(), desc="Bsp layout normalize."),
    Key([mod], "p", lazy.spawn("rofi-pass"), desc="Open rofi pass."),
    Key([mod], "q", lazy.window.kill(), desc="kill window."),
    Key([mod], "r", lazy.spawn("dmenu_run"), desc="Open dmenu_run."),
    Key([mod], "t", lazy.spawn('termite'), desc="Open termite."),
    Key([mod], "v", lazy.spawn('pavucontrol'), desc="Open pavucontrol."),
    Key([mod], "w", lazy.spawn(myBrowser), desc="Open my browser."),
    Key([mod], "x", lazy.spawn('oblogout'), desc="Open oblogout."),
    Key([mod], "Return", lazy.spawn(myTerm), desc="Open my terminator."),
    Key([mod], "Left", lazy.screen.prev_group(), desc="previous group ."),
    Key([mod], "Right", lazy.screen.next_group(), desc="next group."),
    #########################
    # SUPER + FUNCTION KEYS #
    #########################
    Key([mod], "F1", lazy.spawn(myBrowser)),
    Key([mod], "F2", lazy.spawn('atom')),
    Key([mod], "F3", lazy.spawn('inkscape')),
    Key([mod], "F4", lazy.spawn('gimp')),
    Key([mod], "F5", lazy.spawn('meld')),
    Key([mod], "F6", lazy.spawn('vlc --video-on-top')),
    Key([mod], "F7", lazy.spawn('virtualbox')),
    Key([mod], "F8", lazy.spawn('thunar'), desc="Open Thunar"),
    Key([mod], "F9", lazy.spawn('evolution')),
    Key([mod], "F10", lazy.spawn('spotify')),
    Key([mod], "F11", lazy.spawn('rofi -show run -fullscreen')),
    Key([mod], "F12", lazy.spawn('rofikb')),
    #########################
    # SUPER + SHIFT KEYS    #
    #########################
    Key([mod, "shift"], "m", lazy.spawn(
        "dmenu_run -i -nb '#191919' -nf \
        '#fea63c' -sb '#fea63c' -sf \
        '#191919' -fn 'NotoMonoRegular:bold:pixelsize=14'")),
    Key([mod, "shift"], "q", lazy.shutdown()),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "shift"], "Return", lazy.spawn('thunar')),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="sas"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right()),
    Key([mod], "Tab", lazy.next_layout(), desc="next layout."),
    Key([mod], "space", lazy.prev_layout(), desc="previous layout."),
    #########################
    # CONTROL + ALT KEYS    #
    #########################
    Key(["mod1", "control"], "a", lazy.spawn('atom'), desc="Open atom."),
    Key(["mod1", "control"], "b", lazy.spawn('thunar'), desc="Open thunar."),
    Key(["mod1", "control"], "c", lazy.spawn('Catfish'), desc="Open catfish."),
    Key(["mod1", "control"], "e", lazy.spawn('evolution'),
        desc="Open evolution."),
    Key(["mod1", "control"], "f", lazy.spawn('firefox'), desc="Open firefox."),
    Key(["mod1", "control"], "g", lazy.spawn(
        'chromium -no-default-browser-check'),
        desc="Open chromium no default check."),
    Key(["mod1", "control"], "i", lazy.spawn('nitrogen'),
        desc="Open nitrogen."),
    Key(["mod1", "control"], "k", lazy.spawn('slimlock'),
        desc="Open slimlock."),
    Key(["mod1", "control"], "m", lazy.spawn('xfce4-settings-manager'),
        desc="Open xfce4 settings manager."),
    Key(["mod1", "control"], "o", lazy.spawn(
        '~/.config/bspwm/scripts/compton-toggle.sh'), desc="compton toggle."),
    Key(["mod1", "control"], "r", lazy.spawn('rofi-theme-selector'),
        desc="Open rofi theme selector."),
    Key(["mod1", "control"], "s", lazy.spawn('subl3'),
        desc="Open sublime text (not registred)."),
    Key(["mod1", "control"], "t", lazy.spawn('termite'), desc="Open termite."),
    Key(["mod1", "control"], "u", lazy.spawn('pavucontrol'),
        desc="Open pavucontrol."),
    Key(["mod1", "control"], "v", lazy.spawn(myBrowser),
        desc="Open my browser."),
    Key(["mod1", "control"], "w", lazy.spawn('atom'), desc="Open atom."),
    Key(["mod1", "control"], "Return", lazy.spawn('termite'),
        desc="Open termite"),
    #########################
    # ALT + ... KEYS        #
    #########################
    Key(["mod1"], "f", lazy.spawn('variety -f')),
    Key(["mod1"], "t", lazy.spawn('variety -t')),
    Key(["mod1"], "n", lazy.spawn('variety -n')),
    Key(["mod1"], "p", lazy.spawn('variety -p')),
    Key(["mod1"], "Left", lazy.spawn('variety -p')),
    Key(["mod1"], "Right", lazy.spawn('variety -n')),
    Key(["mod1"], "Up", lazy.spawn("variety --pause")),
    Key(["mod1"], "Down", lazy.spawn("variety --resume"), desc="variety"),
    Key(["mod1"], "Tab", lazy.next_layout(), desc="next layout."),
    Key(["mod1"], "space", lazy.prev_layout(), desc="previous layout."),
    Key(["mod1"], "F2", lazy.spawn('gmrun')),
    Key(["mod1"], "F3", lazy.spawn('xfce4-appfinder')),

    #########################
    # CONTROL + SHIFT KEYS  #
    #########################
    # yield control + shift + 'Escape', lazy.spawn('xfce4-taskmanager')
    #########################
    #     SCREENSHOTS       #
    #########################
    Key([mod, "shift"], "Print", lazy.spawn('gnome-screenshot -i'),
        desc="sds"),
    Key([mod], "Print", lazy.spawn('xfce4-screenshooter')),
    Key([], "Print", lazy.spawn(
        "scrot --delay 3 " + home + "/Képek/ArcoLinuxD_%Y_%m_%d_%H_%M_%S.jpg"),
        desc="Create printscreen scrot. "),
    #########################
    #     MULTIMEDIA KEYS   #
    #########################

    #########################
    # Qtile LAYOUT KEYS     #
    #########################

    Key([mod], "k", lazy.layout.down()),
    Key([mod, "mod1"], "Down", lazy.layout.down(), desc="layout down."),
    Key([mod, "mod1"], "Up", lazy.layout.up(), desc="layout ."),
    Key([mod, "mod1"], "Right", lazy.layout.right(), desc="layout up."),
    Key([mod, "mod1"], "Left", lazy.layout.left(), desc="layout left."),
    Key([mod, "mod1"], "5", lazy.layout.size(500), desc="layout size 500."),

    # Grow size up, down, left, and right

    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(), desc="valami"
        ),

    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(), desc="csak"
        ),
    # ########################################################
    Key([mod, "mod1"], "k", lazy.layout.flip_up(), desc="flip up layout."),
    Key([mod, "mod1"], "j", lazy.layout.flip_down(), desc="flip down layout."),
    Key([mod, "mod1"], "l", lazy.layout.flip_right(),
        desc="flip right layout."),
    Key([mod, "mod1"], "h", lazy.layout.flip_left(),
        desc="flip left layout."),
    # #############################################
    # Switch window focus to other pane(s) of stack
    # Move windows up or down in current stack
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left()),
    # Toggle between different layouts as defined below
    Key([mod, "shift"], "f", lazy.window.toggle_floating()),
    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate(), desc="Layout rotate. "),
    # Media player controls
    Key([], "XF86AudioPlay", lazy.spawn("/usr/bin/playerctl play"),
        desc="Play"),
    Key([], "XF86AudioPause", lazy.spawn("/usr/bin/playerctl pause"),
        desc="Pause"),
    Key([], "XF86AudioNext", lazy.spawn("/usr/bin/playerctl next"),
        desc="Next"),
    Key([], "XF86AudioPrev", lazy.spawn("/usr/bin/playerctl previous"),
        desc="Previous"),
    # Pulse Audio controls
    Key([], "XF86AudioMute", lazy.spawn(
        "/usr/bin/pactl set-sink-mute \
        alsa_output.pci-0000_00_1b.0.analog-stereo toggle"),
        desc="Volume mute. "),
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "/usr/bin/pactl set-sink-volume \
        alsa_output.pci-0000_00_1b.0.analog-stereo -5%"),
        desc="Volume down 5%. "),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "/usr/bin/pactl set-sink-volume \
        alsa_output.pci-0000_00_1b.0.analog-stereo +5%"),
        desc="Volume up 5%. "),
]


groups = []

group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

group_labels = ["", "", "", "", "", "", "", "", "", ""]

group_layouts = ["max", "monadtall",
                 "bsp", "max", "max", "treetab", "max", "max", "max", "max"]


for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i]
            # matches=group_matches[i],

        ))

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group =
        # switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])


def init_layout_theme():
    return {"border_width": 3,
            "margin": 12,
            "border_focus": "#000000",
            "border_normal": "#606060",
            }


layout_theme = init_layout_theme()


layouts = [
    layout.Max(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.Stack(num_stacks=2, **layout_theme),
    layout.TreeTab(
        font="Mono", fontsize=12,
        panel_width=175, bg_color="#1c1b1c",
        active_bg="#606060", inactive_bg="#404040",
        border_width=2, padding_left=6, padding_x=6,
        padding_y=2, vspace=2),
]

# ### BAR COLORS #####


def init_colors():
    return [["#161616", "#008000"],
            ["#2C3B09", "#000000"],
            ["#8C8A7F", "#857F68"],
            ["#C45500", "#E7653F"],
            ["#32440E", "#2C3B09"],
            ["#758F5F", "#758F5F"],
            ["#995C6B", "#BB5D79"],
            ["#000000", "#565051"],
            ["#228B22"],
            ["#ffff99"]]


colors = init_colors()

# #### WIDGETS #####


def init_widgets_defaults():
    return dict(font="Inconsolata",
                fontsize=14,
                padding=6,
                foreground=colors[9],
                background=colors[1],)


def init_widgets_defaults_sep():
    return dict(linewidth=1,
                padding=0,
                foreground=colors[8],
                background=colors[1],)


widget_sep = init_widgets_defaults_sep()
widget_defaults = init_widgets_defaults()


def init_widgets_list():
    # prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [

        widget.GroupBox(
            font="Inconsolata",
            fontsize=18,
            borderwidth=0,
            active="#3CBC3C",
            inactive="#FF8C00",
            rounded=False,
            highlight_method="block",
            this_current_screen_border=colors[7],
            this_screen_border=colors[3],
            other_current_screen_border=colors[0],
            other_screen_border=colors[0],
            foreground=colors[8],
            background=colors[1]
        ),

        # widget.Prompt(
        #     prompt=prompt,
        #     font="Ubuntu Mono",
        #     padding=12,
        #     foreground=colors[8],
        #     background=colors[1]
        # ),

        # widget.Sep(
        #     linewidth=0,
        #     padding=12,
        #     foreground=colors[2],
        #     background=colors[1]
        # ),


        widget.WindowName(
            **widget_defaults
        ),

        widget.Sep(
            **widget_sep
        ),

        # widget.Cmus(),

        mpdwidget.Mpd(
            fmt_playing='%f [%v%%] %s',
            fmt_stopped='⏹️',
            reconnect=True,
            reconnect_interval=1,
            foreground_progress="#ff8c00",
            **widget_defaults
        ),

        # widget.Sep(
        #     linewidth=1,
        #     padding=0,
        #     foreground=colors[8],
        #     background=colors[1]
        # ),

        # arcobattery2.BatteryIcon(
        #     battery_name='BAT1',
        #     scale=0.6,
        #     y_poss=4,
        #     padding=0,
        #     theme_path=home + "/.config/qtile/battery_icons/"
        # ),

        widget.Sep(
            **widget_sep
        ),

        widget.CurrentLayoutIcon(
            scale=0.5,
            **widget_defaults
        ),

        widget.Sep(
            **widget_sep
        ),

        # widget.CheckUpdates(
        #     display_format="a: {updates}"),

        # widget.maildir(
        # maildirPath="~/.local/share/mail/krive79",
        # subFolders=[“path”: “INBOX”, “label”: “Home mail”],
        # separator=" ",
        # ),

        wttrweather.WttrWeather(
            location='Fábiánháza',
            format='2',
            units='&m',
            execute=myTerm + ' -e weatc',
            update_interval=600,
            **widget_defaults
        ),

        widget.Sep(
            **widget_sep
        ),

        widget.TextBox(
            text="📦",
            **widget_defaults
        ),

        pacman.Pacman(
            execute=myTerm + ' -e updatepackage',
            update_interval=600,
            **widget_defaults
        ),

        widget.Sep(
            **widget_sep
        ),

        net.Net(
            icon_up="⬆",
            icon_down="⬇",
            interface="enp0s31f6",
            **widget_defaults
        ),

        widget.Sep(
            **widget_sep
        ),

        widget.TextBox(
            text="🚚",
            **widget_defaults
        ),

        memory.Memory(
            fmt='{MemUsed} MB\n{Memsza}%',
            execute='urxvt -e htop',
            update_interval=1,
            **widget_defaults
        ),

        widget.Sep(
            **widget_sep
        ),

        widget.TextBox(
            text="🌡️",
            **widget_defaults
        ),

        widget.ThermalSensor(
            tag_sensor="Package id 0",
            **widget_defaults
        ),

        custom.Cpu(
            **widget_defaults),

        widget.Sep(
            **widget_sep
        ),

        widget.Volume(
            emoji=True,
            **widget_defaults
        ),

        widget.Volume(
            step=5,
            volume_app="qasmixer",
            **widget_defaults
        ),

        # widget.TextBox(
        #          font="Ubuntu Bold",
        #          text=" ☵",
        #          padding = 6,
        #          foreground=colors[6],
        #          background=colors[0],
        #          fontsize=14
        #          ),

        widget.Sep(
            **widget_sep
        ),

        # widget.TextBox(
        #         font="Ubuntu Bold",
        #         text=" 🕒",
        #         foreground=colors[6],
        #         background=colors[1],
        #         padding = 6,
        #         fontsize=14
        #         ),

        widget.TextBox(
            text="⏳",
            **widget_defaults
        ),

        widget.Clock(
            format="%Y-%m-%d\n%H:%M",
            **widget_defaults
        ),

        widget.Sep(
            **widget_sep
        ),

        widget.Systray(
            **widget_defaults
        ),

        widget.Sep(
            linewidth=0,
            padding=10,
            foreground=colors[2],
            background=colors[1]),
    ]
    return widgets_list


widgets_ = init_widgets_list()

# #### SCREENS ##### (TRIPLE MONITOR SETUP)


def init_widgets_screen1():
    # Slicing removes unwanted widgets on Monitors 1,3
    widgets_screen1 = init_widgets_list()
    return widgets_screen1


# def init_widgets_screen2():
#     # Monitor 2 will display all widgets in widgets_list
#     widgets_screen2 = init_widgets_list()
#     return widgets_screen2


def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=36))]
    # Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=35)),
    # Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=35))]


screens = init_screens()


# Drag floating layouts.
def init_mouse():
    return [
        Drag([mod], "Button1", lazy.window.set_position_floating(),
             start=lazy.window.get_position()),
        Drag([mod], "Button3", lazy.window.set_size_floating(),
             start=lazy.window.get_size()),
        Click([mod], "Button2", lazy.window.bring_to_front())
    ]


# # group prev next
# @lazy.function
# def window_to_prev_group(qtile):
#     if qtile.currentWindow is not None:
#         i = qtile.groups.index(qtile.currentGroup)
#         qtile.currentWindow.togroup(qtile.groups[i - 1].name)


# @lazy.function
# def window_to_next_group(qtile):
#     if qtile.currentWindow is not None:
#         i = qtile.groups.index(qtile.currentGroup)
#         qtile.currentWindow.togroup(qtile.groups[i + 1].name)

# for example firefox
#  1. "Navigator" xprop WM_CLASS
# output "Navigator", "Firefox"
# 2. "1" Workspace
# 3. "class_name": "firefox" run application name
# "Navigator": "1", "class_name": "firefox",


@hook.subscribe.client_new
def agroup(client):
    apps = {

        # 1 Browser
        "Navigator": "1", "class_name": "firefox",
        "chromium": "1", "class_name": myBrowser,

        # 2 Edit
        "sublime_text": "2", "class_name": "subl",
        "leafpad": "2", "class_name": "leafpad",

        # 3 Shell
        "urxvt": "3", "class_name": myTerm,

        # 4 Chat
        "discord": "4", "class_name": "discord",

        # 5 ImageViewers
        "gimp": "5", "class_name": "gimp",

        # 6 Boxes
        "VirtualBox": "6", "class_name": "virtualbox",

        # 7 Video
        "vlc": "7", "class_name": "vlc",

        #  8 File Manager
        "thunar": "8", "class_name": "thunar",
        "pcmanfm": "8", "class_name": "pcmanfm",

        # 9 Music
        "spotify": "9", "class_name": "spotify",

        # 0 Other
        "pamac-manager": "0", "class_name": "pamac-manager",

    }

    wm_class = client.window.get_wm_class()[0]
    group = apps.get(wm_class, None)
    if group:
        client.togroup(group)
        client.group.cmd_toscreen()


@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for() or
            window.window.get_wm_type() in floating_types):
        window.floating = True


floating_types = ["notification", "toolbar", "splash", "dialog",
                  "utility", "menu", "dropdown_menu", "popup_menu",
                  "tooltip,dock",
                  ]


follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': "Openbox Logout"},
    {'wname': "Spotify"},
    {'wname': 'branchdialog'},      # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass

], fullscreen_border_width=0, border_width=0)

auto_fullscreen = True
focus_on_window_activation = "smart"


dgroups_key_binder = None
dgroups_app_rules = []  # type: List


main = None


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])


wmname = "LG3D"
