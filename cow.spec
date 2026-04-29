Name:           cow
Version:        1
Release:        0.STAMP.HASH%{?dist}
Summary:        Cow

License:        MIT
URL:            https://github.com/rh-mcermak/cow.git

Source0:        https://github.com/rh-mcermak/cow/blob/main/cow-1.0.tar.gz

BuildRequires: cairo
BuildRequires: clang
BuildRequires: dnf
BuildRequires: dunst
BuildRequires: grim
BuildRequires: install
BuildRequires: libbsd
BuildRequires: libbsd-devel
BuildRequires: libevdev-devel
BuildRequires: libevdev-utils
BuildRequires: libinput-devel
BuildRequires: libwayland-client
BuildRequires: libxkbcommon
BuildRequires: libxkbcommon-devel
BuildRequires: libxkbcommon-utils
BuildRequires: meson
BuildRequires: pango
BuildRequires: pangocairo
BuildRequires: pango-devel
BuildRequires: pasystray
BuildRequires: river
BuildRequires: seat
BuildRequires: seatd
BuildRequires: slurp
BuildRequires: sudo
BuildRequires: /usr/bin/wl-clip-persist
BuildRequires: waybar
BuildRequires: wayland-client-devel
BuildRequires: wayland-devel
BuildRequires: wayland-protocols
BuildRequires: wayland-protocols-devel
BuildRequires: wl-clipboard
BuildRequires: wl-clip-persist
BuildRequires: wlroots-devel
BuildRequires: xkbcommon
BuildRequires: xterm
BuildRequires: zig

%description
Cow

%prep
%autosetup

%build
make

%install
mkdir -p %{buildroot}/usr/bin
install -m0755 mypkg %{buildroot}/usr/bin/mypkg

%files
/usr/bin/mypkg

%changelog
* Fri Apr 24 2026 You <mcermak@example.com> - 0-1
- Initial build
