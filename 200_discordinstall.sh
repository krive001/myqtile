#!/bin/bash

 git clone https://aur.archlinux.org/libc++.git  
 git clone https://aur.archlinux.org/discord.git  

cd libc++
makepkg -si  --nocheck --skipinteg --noconfirm 
cd ../discord 
makepkg -si --noconfirm

cd ..
rm -rf libc++
rm -rf  discord




