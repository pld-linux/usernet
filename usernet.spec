Summary:	A graphical utility for controlling network interfaces.
Name:		usernet
Version:	1.0.9
Release:	2
License:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Source0:	usernet-%{PACKAGE_VERSION}.tar.gz
Requires:	initscripts >= 3.20

%description
The usernet utility provides a graphical interface for manipulating
network interfaces (bringing them up or down and viewing their
status). Users can only manipulate interfaces that are
user-controllable. The superuser can control all interfaces.

Install the usernet package if you'd like to provide a graphical
utility for manipulating network interfaces.

%prep
%setup -q

%build
make VERSION=%{version}

%install
rm -rf $RPM_BUILD_ROOT
make install BR=$RPM_BUILD_ROOT VERSION=%{version}

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/usernet
%{_datadir}/usernet/%{version}
%{_mandir}/man1/*
%{_sysconfdir}/X11/wmconfig/usernet
