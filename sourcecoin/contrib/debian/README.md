
Debian
====================
This directory contains files used to package CM_LowercaseCoinNamed/CM_LowercaseCoinName-qt
for Debian-based Linux systems. If you compile CM_LowercaseCoinNamed/CM_LowercaseCoinName-qt yourself, there are some useful files here.

## CM_LowercaseCoinName: URI support ##


CM_LowercaseCoinName-qt.desktop  (Gnome / Open Desktop)
To install:

	sudo desktop-file-install CM_LowercaseCoinName-qt.desktop
	sudo update-desktop-database

If you build yourself, you will either need to modify the paths in
the .desktop file or copy or symlink your CM_LowercaseCoinName-qt binary to `/usr/bin`
and the `../../share/pixmaps/CM_LowercaseCoinName128.png` to `/usr/share/pixmaps`

CM_LowercaseCoinName-qt.protocol (KDE)

