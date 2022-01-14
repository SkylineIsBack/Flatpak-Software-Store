#!/bin/bash

# By SkylineIsBack

if [ "$(id -u)" -ne 0 ]; then
        echo 'This installer script must be run as root.'
        exit 1
fi

echo "Starting installation"
echo""
sudo mv Flatpak-Software-Store.py /usr/bin/
sudo mv Flatpak-Software-Store.desktop /usr/share/applications/
sudo chmod +x /usr/bin/Flatpak-Software-Store.py
sudo chmod +x /usr/share/applications/Flatpak-Software-Store.desktop
echo "Successfully installed"