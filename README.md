# maglit-cli
A small python script to shorten links via maglit.me, over cli

![ApplicationFrameHost_O3syXWBZf5](https://user-images.githubusercontent.com/83690012/236696225-6e4bb2a6-dd00-47e7-8f93-615f64217fb2.png)


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
