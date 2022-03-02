.. _eA-tvIl1Zb:

=======================================
Standard System Directories
=======================================

xdg-user-dirs
=======================================

xdg-user-dirs is a tool to help manage "well known" user directories like the desktop folder and
the music folder. It also handles localization (i.e. translation) of the filenames.

You should first determine if the file in question is:

* A configuration file            - $XDG_CONFIG_HOME:$XDG_CONFIG_DIRS
* A data file                     - $XDG_DATA_HOME:$XDG_DATA_DIRS
* A non-essential (cache) file    - $XDG_CACHE_HOME


It is recommended that your application put its files in a subdirectory of the above directories.
Usually, something like:

* $XDG_DATA_DIRS/<application>/filename
* $XDG_DATA_DIRS/<vendor>/<application>/filename

When loading, you first try to load the file from the user-specific directories ($XDG_*_HOME) and,
if failed, from system directories ($XDG_*_DIRS). When saving, save to user-specific directories
only (since the user probably won't have write access to system directories).

::

    $XDG_DATA_HOME: user-specific data files.
        default:    $HOME/.local/share
        xenial:     None
        bionic:     None

    $XDG_CONFIG_HOME: user-specific configuration files.
        default:    $HOME/.config
        xenial:     None
        bionic:     None

    $XDG_DATA_DIRS: precedence-ordered set of system data directories.
        default:    /usr/local/share/:
                    /usr/share/
        xenial:     /usr/share//usr/share/xsessions/plasma:
                    /usr/local/share:
                    /usr/share:
                    /var/lib/snapd/desktop

        bionic:     /usr/share//usr/share/xsessions/plasma:
                    /usr/local/share:
                    /usr/share:
                    /var/lib/snapd/desktop

    $XDG_CONFIG_DIRS: precedence-ordered set of system configuration directories.
        default:    /etc/xdg
        xenial:     /etc/xdg/xdg-/usr/share/xsessions/plasma:
                    /etc/xdg:
                    /usr/share/kubuntu-default-settings/kf5-settings

        bionic:     /etc/xdg/xdg-/usr/share/xsessions/plasma:
                    /etc/xdg:
                    /usr/share/kubuntu-default-settings/kf5-settings

    $XDG_CACHE_HOME: user-specific non-essential data files.
        default:    $HOME/.cache
        xenial:     None
        bionic:     None

        Any files in here can be wiped out (eg not backed up) and should have no impact on the
        application other than regenerating the cache files (eg re-download)



References:
=======================================

1.  https://stackoverflow.com/a/1024339
2.  https://www.freedesktop.org/wiki/Software/xdg-user-dirs/
