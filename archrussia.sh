sudo echo Welcome to archrussia!
sudo locale-gen
sudo localectl set-locale ru_RU.UTF-8
sudo ls /usr/share/kbd/consolefonts/ | grep 'ter-' | cut -d. -f1
sudo pacman -S ttf-dejavu
sudo pacman -S ttf-liberation
sudo setxkbmap -query
sudo localectl set-x11-keymap --no-convert us,ru pc105 "" grp:alt_shift_toggle
sudo reboot
