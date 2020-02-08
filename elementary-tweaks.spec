%global __provides_exclude_from ^%{_libdir}/%{appname}/.*\\.so$

Name:           elementary-tweaks
Summary:        Eleemntary-tweak tool to customize pantheon desktop
Version:        5.0.3
Release:        1%{?dist}
License:        GPLv3+

Source0:        https://github.com/a-mere-peasant/elementary-tweaks/archive/elementary-tweaks.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala




Provides:       elementary-tweaks = %{version}-%{release}


%description
The elementary tweak tool helps to cusomize the pantheon desktop enviornment's appearance easily and safely

%prep
%autosetup -n %{srcname} -p1


%build
%meson
%meson_build


%install
%meson_install



%files
%doc README.md
%license COPYING


