Name:           cow
Version:        1
Release:        0.STAMP.HASH%{?dist}
Summary:        Compositor on Wayland - A stacking window manager

License:        ISC
URL:            https://codeberg.org/thomasadam/cow
Source0:        cow-1.0.tar.gz
Patch0:         logging.patch

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
%patch -P0 -p1

%build
export CFLAGS="%{optflags} -Wno-error=format-security"
%meson -Detcprefix=/
%meson_build

%install
%meson_install


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
* Tue May 12 2026 Martin Cermak <mcermak@redhat.com> - 1-0.8621417.2307f6a
- Automated build from upstream git commit 2307f6a

* Mon May 11 2026 Martin Cermak <mcermak@redhat.com> - 1-0.8526093.db394ca
- Automated build from upstream git commit db394ca

* Mon May 11 2026 Martin Cermak <mcermak@redhat.com> - 1-0.8525577.db394ca
- Automated build from upstream git commit db394ca

* Mon May 11 2026 Martin Cermak <mcermak@redhat.com> - 1-0.8482519.db394ca
- Automated build from upstream git commit db394ca

* Thu May 07 2026 Martin Cermak <mcermak@redhat.com> - 1-0.8184858.0b26e18
- Automated build from upstream git commit 0b26e18

* Wed May 06 2026 Martin Cermak <mcermak@redhat.com> - 1-0.8076157.8a1ce82
- Automated build from upstream git commit 8a1ce82

* Sun May 03 2026 Martin Cermak <mcermak@redhat.com> - 1-0.7844861.8a1ce82
- Automated build from upstream git commit 8a1ce82

* Thu Apr 30 2026 Martin Cermak <mcermak@redhat.com> - 1-0.7572216.8a1ce82
- Automated build from upstream git commit 8a1ce82

* Wed Apr 29 2026 Martin Cermak <mcermak@redhat.com> - 1-0.7493386.5885e05
- Automated build from upstream git commit 5885e05

* Sat Apr 25 2026 Martin Cermak <mcermak@redhat.com> - 1-0
- Initial package for Fedora
