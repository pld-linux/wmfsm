Summary:	Disk free space monitor for WindowMaker
Summary(pl):	Monitor wolnej przestrzeni dysków dla WindowMakera
Name:		wmfsm
Version:	0.33
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
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
wmfsm wy¶wietla ilo¶æ wolnego miejsca w procentach na zamontowanych
partycjach.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make} CFLAGS="%{rpmcflags} -I%{_includedir}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

#install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO wmfsm/wmfsmrc.sample
%attr(755,root,root) %{_bindir}/%{name}

#%{_applnkdir}/DockApplets/wmfsm.desktop
