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
meson setup build --prefix=/usr -Detcprefix=/
meson compile -C build 

%install
meson install -C build --destdir %{buildroot}


%files
%{_bindir}/cow
%{_bindir}/cow-start
%{_bindir}/cowbar
%{_bindir}/cowpager
%{_bindir}/moocow
%{_bindir}/cowident
%{_sysconfdir}/cow/cow.conf
%{_datadir}/wayland-sessions/cow.desktop

%changelog
* Thu Apr 30 2026 Martin Cermak <mcermak@redhat.com> - 1-0.7572216.8a1ce82
- Automated build from upstream git commit 8a1ce82

* Wed Apr 29 2026 Martin Cermak <mcermak@redhat.com> - 1-0.7493386.5885e05
- Automated build from upstream git commit 5885e05

* Sat Apr 25 2026 Martin Cermak <mcermak@redhat.com> - 1-0
- Initial package for Fedora
