Name:           cow
Version:        1
Release:        0.STAMP.HASH%{?dist}
Summary:        Compositor on Wayland - A stacking window manager

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
CoW (Compositor on Wayland) is a stacking window manager for Wayland.
CoW aims to provide the look-and-feel of FVWM and MWM with a sensible
configuration mechanism using dedicated commands that can be used both
as a configuration file and via IPC at runtime.

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
* Wed Apr 29 2026 Martin Cermak <mcermak@redhat.com> - 1-0.7492120.5885e05
- Automated build from upstream git commit 5885e05

* Sat Apr 25 2026 Martin Cermak <mcermak@redhat.com> - 1-0
- Initial package for Fedora
