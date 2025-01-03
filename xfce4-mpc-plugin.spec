%define url_ver %(echo %{version} | cut -c 1-3)
%define _disable_rebuild_configure 1

Summary:	A mpc plugin for the Xfce panel
Name:		xfce4-mpc-plugin
Version:	0.5.5
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		https://goodies.xfce.org/projects/panel-plugins/xfce4-mpc-plugin
Source0:	https://archive.xfce.org/src/panel-plugins/xfce4-mpc-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(libxfce4panel-2.0)
BuildRequires:	pkgconfig(libxfce4ui-2)
BuildRequires:	pkgconfig(exo-2)
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig(libmpd)

%description
This is a simple Xfce panel client plugin for Music Player Daemon.

Features :
* send Play/Stop/Next/Previous command to MPD
* uses gtk-theme media icons (at least nuvola, tango and rodent themes provides
  these icons)
* decrease/increase volume using the mouse wheel
* show the current volume, status and title as a tooltip when passing the mouse
  over the plugin
* show a simple playlist window upon middle-click, permitting to select a track
  to play
* configurable MPD host/port/password
* toggles repeat/random features in the right-click menu
* launch configurable client (gmpc, xterm -e ncmpc,..) through right-click menu

%prep
%autosetup -p1

%build
%configure \
	--disable-static

%make_build

%install
%make_install

chmod +x %{buildroot}%{_libdir}/xfce4/panel/plugins/*.so

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS README*
%{_libdir}/xfce4/panel/plugins/libmpc.so
%{_datadir}/xfce4/panel/plugins/xfce4-mpc-plugin.desktop
