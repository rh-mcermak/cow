#!/bin/bash

pushd $(mktemp -d)
git clone https://github.com/rh-mcermak/cow.git
rm -f ~/.config/cow
cp cow/config/cow.conf ~/.config/cow
rm -rf ~/.config/waybar
cp -r cow/config/waybar ~/.config
popd
