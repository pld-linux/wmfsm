Summary:	Disk free space monitor for WindowMaker
Summary(pl):	Monitor wolnej przestrzeni dysków dla WindowMakera
Name:		wmfsm
Version: 	0.31
Release:	1
Copyright:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	http://wmfsm.netpedia.net/%{name}-%{version}.tar.gz
Source1:	wmfsm.desktop
BuildRequires:	XFree86-devel
BuildRequires:	xpm-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%define		_applnkdir	%{_datadir}/applnk

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
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/DockApplets} 

install -s %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

gzip -9nf BUGS CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {BUGS,CHANGES,README}.gz wmfsm/wmfsmrc.sample
%attr(755,root,root) %{_bindir}/%{name}

%{_applnkdir}/DockApplets/wmfsm.desktop
