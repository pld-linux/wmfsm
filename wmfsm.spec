Summary:	Disk free space monitor for WindowMaker
Summary(pl):	Monitor wolnej przestrzeni dysk�w dla WindowMakera
Name:		wmfsm
Version:	0.33
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(pl):	X11/Zarz�dcy Okien/Narz�dzia
Source0:	http://www.cs.mcgill.ca/~cgray4/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
URL:		http://www.cs.mcgill.ca/~cgray4/
BuildRequires:	XFree86-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
wmfsm shows the percentage of free space across your file systems.

%description -l pl
wmfsm wy�wietla ilo�� wolnego miejsca w procentach na zamontowanych
partycjach.

%prep
%setup -q

%build
aclocal
autoconf
%configure
%{__make} CFLAGS="%{rpmcflags} -I%{_includedir}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

#install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz wmfsm/wmfsmrc.sample
%attr(755,root,root) %{_bindir}/%{name}

#%{_applnkdir}/DockApplets/wmfsm.desktop
