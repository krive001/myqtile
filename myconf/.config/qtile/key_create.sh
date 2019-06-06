#!/bin/bash

 qtile-cmd -o cmd -f display_kb > $HOME/.config/qtile/menu1.txt
 sed 's/^..//;s/\\n.*//;1,2d' $HOME/.config/qtile/menu1.txt > $HOME/.config/qtile/menu.txt
 rm $HOME/.config/qtile/menu1.txt
 