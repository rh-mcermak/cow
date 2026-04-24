Name:           cow
Version:        0
Release:        1%{?dist}
Summary:        Cow

License:        MIT
URL:            https://github.com/rh-mcermak/cow.git

Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc, make

%description
Example package built from upstream git.

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
