
Name:    elementary-tweaks
Version: 5.0
Release: 1%{?dist}
Summary: Tweaks to customize the pantheon desktop enviornment

License: GPL v3.0
Source0: https://github.com/elementary-tweaks/elementary-tweaks/archive/master.zip -O elementary-tweaks-master.zip

%description
Elemenatry tweak tool that let's one customize the pantheon desktop's appearance easily and safely.
Change  the themes and icons, also has support for changing the window button layout from the classic elementary style.

%build
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Debug -DCMAKE_INSTALL_PREFIX=/usr ../
make

%install
sudo make install

%files
%{_bindir}/

%changelog


