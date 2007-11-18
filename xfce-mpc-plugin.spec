Summary: 	A mpc plugin for the Xfce panel
Name: 		xfce-mpc-plugin
Version: 	0.3.2
Release: 	%mkrel 1
License:	GPL
Group: 		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-mpc-plugin
Source0: 	http://goodies.xfce.org/releases/xfce4-mpc-plugin/xfce4-mpc-plugin-%{version}.tar.bz2
Requires:	xfce-panel >= 4.4
BuildRequires:	xfce-panel-devel >= 4.4
BuildRequires:	libxfcegui4-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	libmpd-devel
Requires:	mpd
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot

%description
A mpc plugin for the Xfce panel.

%prep
%setup -qn xfce4-mpc-plugin-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std 

%find_lang xfce4-mpc-plugin

%clean
rm -rf %{buildroot}

%files -f xfce4-mpc-plugin.lang
%defattr(-,root,root)
%doc ChangeLog COPYING AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/xfce4-mpc-plugin.desktop
      