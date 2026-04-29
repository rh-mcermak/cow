#!/bin/bash

pushd $(mktemp -d)
git clone https://github.com/rh-mcermak/cow.git
rm -f ~/.config/cow
cp cow/config/cow.conf ~/.config/cow
rm -rf ~/.config/waybar
cp -r cow/config/waybar ~/.config
popd

cat >cow.repo <EOF
[copr:copr.fedorainfracloud.org:mcermak:cow]
name=Copr repo for cow owned by mcermak
baseurl=https://download.copr.fedorainfracloud.org/results/mcermak/cow/fedora-$releasever-$basearch/
type=rpm-md
skip_if_unavailable=True
gpgcheck=1
gpgkey=https://download.copr.fedorainfracloud.org/results/mcermak/cow/pubkey.gpg
repo_gpgcheck=0
enabled=1
enabled_metadata=1

[coprdep:https_download_copr_fedorainfracloud_org_results_leloubil_wl_clip_persist_fedora_releasever_basearch]
name=Copr copr.fedorainfracloud.org/mcermak/cow external runtime dependency #1 - https_download_copr_fedorainfracloud_org_results_leloubil_wl_clip_persist_fedora_releasever_basearch
baseurl=https://download.copr.fedorainfracloud.org/results/leloubil/wl-clip-persist/fedora-$releasever-$basearch
type=rpm-md
skip_if_unavailable=True
repo_gpgcheck=0
gpgcheck=0
enabled=1
enabled_metadata=1
EOF

sudo cp cow.repo /etc/yum.repos.d/
sudo yum clean all
sudo yum install cow
