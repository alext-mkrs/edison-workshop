Description
===========

This repo contains source code and slides for the Edison workshop,
a short 3-4 hour course for those who want to get a hang of Edison,
its capabilities and ecosystem.

It's not intended to be a comprehensive all-covered training, rather a smaller,
easy to consume fun event where people may touch and play with Edison to consider
it for their projects.

Within the workshop we do a general overview of Edison's features and ways to
program and expand it (30 minutes to 1 hour max). After that an example
hands-on project is run (2-3 hours max) where each participant has access to
an Edison and a basic sensor set (see Bill of materials section below).

See README files in sub-directories for additional information.

Bill of materials (per one participant)
=======================================

* Edison Compute Module with an Edison Kit for Arduino - 1 pc.
* [Seeed Studio Grove Starter Kit Plus](http://www.seeedstudio.com/depot/Grove-Starter-Kit-Plus-p-1294.html?cPath=73) - 1 pc.
  * We use only Base Shield, Temperature & Light sensors, 16x2 I2C LCD and
  a USB cable out of the whole set, but it's always handy to have more
  if your participants want to pursue their own project within the allotted time.

This is not the only possible set, but this is what I have and used extensively.

Board preparation (per board)
==============================

```bash
# Setup Internet connectivity
$> configure_edison --setup

# Configure package repo feeds
$> cat >> /etc/opkg/base-feeds.conf <<EOF
src/gz all http://repo.opkg.net/edison/repo/all
src/gz edison http://repo.opkg.net/edison/repo/edison
src/gz core2-32 http://repo.opkg.net/edison/repo/core2-32
EOF

# Change root password back to empty (Wi-Fi setup earlier enforces a non-empty one)
$> passwd

# Install necessary packages, Python modules, clone the workshop git repo,
# zero out the Wi-Fi config (contains plaintext passphrase for WPA-PSK)
$> opkg update && opkg install git vim vim-common vim-syntax vim-vimrc python-pip mraa upm && pip install flask && cd ~ && git clone https://github.com/alext-mkrs/edison-workshop.git && echo "" > /etc/wpa_supplicant/wpa_supplicant.conf && echo -e "\n\nDONE\n\n"
```