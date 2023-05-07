# maglit-cli
A small python script to shorten links via maglit.me, over cli

![ApplicationFrameHost_qXhcOwmgco](https://user-images.githubusercontent.com/83690012/236695665-3ff479d0-5fde-4aec-8f0e-1e425467c449.png)


## Features 

- [x] Optional password protection - custom or randomly generated 
- [x] Custom shortened link
- [x] Randomly generating shortened links
- [ ] Optionally saving password to re-use it for other links automatically
- [x] Generating a QR code for the shortened link 

## Todo

Somehow making the script unattended if inputs are passed to it already (such as the custom pass, or the link to shorten), making it useful when piping the output of a previous command (e.g ffsend) to this script to then shorten the link.

## Requirements:

* rich - ``pip install rich``
* requests - ``pip install requests``
* qrcode_terminal - ``pip install qrcode_terminal``
