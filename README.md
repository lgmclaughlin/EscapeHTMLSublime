Synopsis
========
This is a simple packaged plugin for Sublime Text that will allow one to escape HTML chars (<, >, &, ', and ") quickly by hitting [ctrl + alt + e].

Usage
=====
Highlight any areas of HTML you'd like to escape and press ctrl + alt + e (super + alt + e for OS X). Alternatively, you can select any amount of text and then open the Selection Menu. From here, click Escape HTML.

Motivation
==========
While working on a project in which we were putting example HTML snippets on webpages, I had no disire to go through and escape each character by hand for web display. As such, I wrote a quick plugin to do it for me. I figured I'd share it with the world in case it could help someone else as well.

Installation
============
For now, the package can only be installed through the following method:

1. Download [EscapeHTML.sublime-package]
2. Place package into 
  * Windows: %APPDATA%\Sublime Text [version]\Installed Packages
  * OS X:    ~/Library/Application Support/Sublime Text [version]/Installed Packages
  * Linux:   ~/.config/sublime-text-[version]/Installed Packages

Sublime takes care of the rest!

I hope to put this up on Package Control in the near future.
