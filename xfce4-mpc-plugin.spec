%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A mpc plugin for the Xfce panel
Name:		xfce4-mpc-plugin
Version:	0.4.4
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-mpc-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-mpc-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	xfce4-panel-devel >= 4.9.0
BuildRequires:	pkgconfig(libxfce4ui-1) >= 4.9.0
BuildRequires:	exo-devel
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
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

chmod +x %{buildroot}%{_libdir}/xfce4/panel/plugins/*.so

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc ChangeLog AUTHORS README
%{_libdir}/xfce4/panel/plugins/libmpc.so
%{_datadir}/xfce4/panel/plugins/xfce4-mpc-plugin.desktop


%changelog
* Mon Apr 16 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.2-1
+ Revision: 791376
- fix file list
- update buildrequires
- update to new version 0.4.2
- spec file clean

* Sat Mar 12 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.6-1
+ Revision: 644051
- update to new version 0.3.6

* Sat Jul 24 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.5-1mdv2011.0
+ Revision: 557326
- update to new version 0.3.5

* Sat Jan 02 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.4-1mdv2010.1
+ Revision: 485065
- add buildrequires on exo-devel
- update to new version 0.3.4
- adapt to new urls

* Mon May 25 2009 Funda Wang <fwang@mandriva.org> 0.3.3-7mdv2010.0
+ Revision: 379434
- rebuild for new mpd

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.3-6mdv2009.1
+ Revision: 349472
- rebuild for xfce-4.6.0

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.3-5mdv2009.1
+ Revision: 295002
- rebuild for new Xfce4.6 beta1

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

* Wed Mar 26 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.3-1mdv2008.1
+ Revision: 190232
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - fix description-line-too-long
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Nov 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.2-2mdv2008.1
+ Revision: 110125
- correct buildrequires
- new license policy
- use upstream tarball name as a real name
- update description
- do not package COPYING, add README to the docs
- use upstream name

* Thu May 31 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.2-1mdv2008.0
+ Revision: 33444
- new version

* Fri May 25 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.0-2mdv2008.0
+ Revision: 31001
- requires mpd

* Thu May 24 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.0-1mdv2008.0
+ Revision: 30536
- Import xfce-mpc-plugin

