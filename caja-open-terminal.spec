%define url_ver %(echo %{version}|cut -d. -f1,2)
%define oname   mate-file-manager-open-terminal

Summary:        Caja extension for an open terminal shortcut
Name:           caja-open-terminal
Version:        1.6.0
Release:        2
URL:            https://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/%{url_ver}/%{oname}-%{version}.tar.xz
License:        GPLv2+
Group:          Graphical desktop/Other

BuildRequires:  pkgconfig(libcaja-extension)
BuildRequires:  pkgconfig(mate-desktop-2.0)
BuildRequires:  intltool
BuildRequires:  pkgconfig(mate-doc-utils)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)

Requires:       gsettings-desktop-schemas

%rename %{oname}

%description
This is a proof-of-concept Caja extension which allows you to open
a terminal in arbitrary local folders.

%prep
%setup -q -n %{oname}-%{version}

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x \
        --disable-static \
        --disable-schemas-compile
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README COPYING
%{_libdir}/caja/extensions-2.0/libcaja-open-terminal.so
%{_datadir}/MateConf/gsettings/caja-open-terminal.convert
%{_datadir}/glib-2.0/schemas/org.mate.caja-open-terminal.gschema.xml

