Name:           cow
Version:        1
Release:        0.STAMP.HASH%{?dist}
Summary:        Cow

License:        MIT
URL:            https://codeberg.org/thomasadam/cow

Source0:        cow-1.0.tar.gz

BuildRequires: cairo
BuildRequires: clang
BuildRequires: libbsd
BuildRequires: libbsd-devel
BuildRequires: libevdev-devel
BuildRequires: libinput-devel
BuildRequires: libwayland-client
BuildRequires: libxkbcommon
BuildRequires: libxkbcommon-devel
BuildRequires: meson
BuildRequires: pango
BuildRequires: pango-devel
BuildRequires: wayland-devel
BuildRequires: wayland-protocols-devel
BuildRequires: wlroots-devel
BuildRequires: zig

Requires: dunst
Requires: grim
Requires: libevdev-utils
Requires: libxkbcommon-utils
Requires: pasystray
Requires: river
Requires: seatd
Requires: slurp
Requires: waybar
Requires: wl-clipboard
Requires: wl-clip-persist
Requires: xterm


%description
Cow

%prep
%setup -n cow-1.0

%build
export CFLAGS="%{optflags} -Wno-error=format-security"
meson setup build --prefix=/usr
meson compile -C build 

%install
meson install -C build --destdir %{buildroot}


%files
/usr/bin/cow
/usr/bin/cow-start
/usr/bin/cowbar
/usr/bin/cowpager
/usr/bin/moocow
/usr/etc/cow/cow.conf
/usr/share/wayland-sessions/cow.desktop

%changelog
* Fri Apr 24 2026 You <mcermak@example.com> - cow-1.0
- Install steps:
  sudo systemctl start seatd
  sudo usermod -G seat $USER
  install config files per
  https://codeberg.org/thomasadam/cow ---> Where to Start

  
