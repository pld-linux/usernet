Summary: A graphical utility for controlling network interfaces.
Name: usernet
Version: 1.0.9
Release: 2
Copyright: GPL
Group: Applications/System
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Source: usernet-%{PACKAGE_VERSION}.tar.gz
Requires: initscripts >= 3.20

%description
The usernet utility provides a graphical interface for manipulating
network interfaces (bringing them up or down and viewing their status).
Users can only manipulate interfaces that are user-controllable.  The
superuser can control all interfaces.

Install the usernet package if you'd like to provide a graphical utility
for manipulating network interfaces.

%prep
%setup

%build
make VERSION=%{PACKAGE_VERSION}

%install
make install BR=$RPM_BUILD_ROOT VERSION=%{PACKAGE_VERSION}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/usernet
/usr/share/usernet/%{PACKAGE_VERSION}
/usr/man/man1/usernet.1
/etc/X11/wmconfig/usernet
