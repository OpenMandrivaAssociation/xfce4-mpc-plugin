Summary: 	A mpc plugin for the Xfce panel
Name: 		xfce4-mpc-plugin
Version: 	0.3.3
Release: 	%mkrel 1
License:	GPLv2+
Group: 		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-mpc-plugin
Source0: 	http://goodies.xfce.org/releases/xfce4-mpc-plugin/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	libxfcegui4-devel >= 4.4.2
BuildRequires:	perl(XML::Parser)
BuildRequires:	libmpd-devel
Requires:	mpd
Obsoletes:	xfce-mpc-plugin
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot

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
rm -rf %{buildroot}
%makeinstall_std 

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc ChangeLog AUTHORS README
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/xfce4-mpc-plugin.desktop
