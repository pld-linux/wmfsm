Summary:	Disk free space monitor for WindowMaker
Summary(pl):	Monitor wolnej przestrzeni dysków dla WindowMakera
Name:		wmfsm
Version: 	0.27
Release:	2
Copyright:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	http://wmfsm.netpedia.net/%{name}-%{version}.tar.gz
Source1:	wmfsm.desktop
BuildPrereq:	XFree86-devel
BuildPrereq:	xpm-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix	/usr/X11R6

%description
wmfsm shows the percentage of free space across your file systems.

%description -l pl
wmfsm wy¶wietla ilo¶æ wolnego miejsca w procentach na zamontowanych 
partycjach.

%prep
%setup -q

%build
make -C %{name} \
	CFLAGS="$RPM_OPT_FLAGS -I/usr/X11R6/include"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},/etc/X11/applnk/DockApplets} 
install -s %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/applnk/DockApplets

gzip -9nf BUGS CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {BUGS,CHANGES}.gz
%attr(755,root,root) %{_bindir}/%{name}

/etc/X11/applnk/DockApplets/wmfsm.desktop
