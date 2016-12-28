#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xfce4-sensors-plugin
Version  : 1.2.4
Release  : 2
URL      : http://mirrors.tummy.com/pub/archive.xfce.org/src/panel-plugins/xfce4-sensors-plugin/1.2/xfce4-sensors-plugin-1.2.4.tar.bz2
Source0  : http://mirrors.tummy.com/pub/archive.xfce.org/src/panel-plugins/xfce4-sensors-plugin/1.2/xfce4-sensors-plugin-1.2.4.tar.bz2
Summary  : Library for the Xfce 4 Sensors Plugin and Viewer
Group    : Development/Tools
License  : GPL-2.0
Requires: xfce4-sensors-plugin-bin
Requires: xfce4-sensors-plugin-lib
Requires: xfce4-sensors-plugin-data
Requires: xfce4-sensors-plugin-locales
BuildRequires : intltool
BuildRequires : netcat
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(libnotify)
BuildRequires : pkgconfig(libxfce4panel-1.0)
BuildRequires : pkgconfig(libxfce4ui-1)
BuildRequires : pkgconfig(libxfce4util-1.0)

%description
Xfce4-Sensors-Plugin
====================
Version 1.0.0 - For Xfce 4 Panel 4.6.0 (and hopefully newer as well!)

%package bin
Summary: bin components for the xfce4-sensors-plugin package.
Group: Binaries
Requires: xfce4-sensors-plugin-data

%description bin
bin components for the xfce4-sensors-plugin package.


%package data
Summary: data components for the xfce4-sensors-plugin package.
Group: Data

%description data
data components for the xfce4-sensors-plugin package.


%package dev
Summary: dev components for the xfce4-sensors-plugin package.
Group: Development
Requires: xfce4-sensors-plugin-lib
Requires: xfce4-sensors-plugin-bin
Requires: xfce4-sensors-plugin-data
Provides: xfce4-sensors-plugin-devel

%description dev
dev components for the xfce4-sensors-plugin package.


%package lib
Summary: lib components for the xfce4-sensors-plugin package.
Group: Libraries
Requires: xfce4-sensors-plugin-data

%description lib
lib components for the xfce4-sensors-plugin package.


%package locales
Summary: locales components for the xfce4-sensors-plugin package.
Group: Default

%description locales
locales components for the xfce4-sensors-plugin package.


%prep
%setup -q -n xfce4-sensors-plugin-1.2.4

%build
export LANG=C
export SOURCE_DATE_EPOCH=`date +%s -r configure`
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install
%find_lang xfce4-sensors-plugin

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xfce4-sensors
/usr/libexec/xfce4/panel-plugins/xfce4-sensors-plugin

%files data
%defattr(-,root,root,-)
/usr/share/applications/xfce4-sensors.desktop
/usr/share/icons/hicolor/24x24/apps/xfce-sensors.png
/usr/share/icons/hicolor/32x32/apps/xfce-sensors.png
/usr/share/icons/hicolor/48x48/apps/xfce-sensors.png
/usr/share/icons/hicolor/64x64/apps/xfce-sensors.png
/usr/share/icons/hicolor/scalable/apps/xfce-sensors.svg
/usr/share/xfce4/panel-plugins/xfce4-sensors-plugin.desktop

%files dev
%defattr(-,root,root,-)
/usr/lib64/pkgconfig/libxfce4sensors-1.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/xfce4/modules/libxfce4sensors.so
/usr/lib64/xfce4/modules/libxfce4sensors.so.1
/usr/lib64/xfce4/modules/libxfce4sensors.so.1.2.4

%files locales -f xfce4-sensors-plugin.lang
%defattr(-,root,root,-)

