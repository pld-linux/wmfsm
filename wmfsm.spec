Summary:	Disk free space monitor for WindowMaker
Summary(pl):	Monitor wolnej przestrzeni dysków dla WindowMakera
Name:		wmfsm
Version:	0.34
Release:	3
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.cs.ubc.ca/~cmg/%{name}-%{version}.tar.gz
# Source0-md5:	5ec81127146d8340a698cc5e26a66e43
Source1:	%{name}.desktop
URL:		http://www.cs.ubc.ca/~cmg/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wmfsm shows the percentage of free space across your file systems.

%description -l pl
wmfsm wy¶wietla ilo¶æ wolnego miejsca w procentach na zamontowanych
partycjach.

%prep
%setup -q

%build
cp -f %{_datadir}/automake/config.sub .
%{__aclocal}
%{__autoconf}
%configure
%{__make} \
	CFLAGS="%{rpmcflags} -I%{_includedir}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/docklets

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO wmfsm/wmfsmrc.sample
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/docklets/wmfsm.desktop
%{_mandir}/man1/*
