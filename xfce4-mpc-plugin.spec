%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A mpc plugin for the Xfce panel
Name:		xfce4-mpc-plugin
Version:	0.4.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-mpc-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-mpc-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	libxfcegui4-devel >= 4.4.2
BuildRequires:	exo-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	libmpd-devel
Requires:	mpd
Obsoletes:	xfce-mpc-plugin

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
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc ChangeLog AUTHORS README
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/xfce4-mpc-plugin.desktop
