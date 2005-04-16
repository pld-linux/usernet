Summary:	A graphical utility for controlling network interfaces
Summary(pl):	Graficzne narzêdzie do kontroli interfejsów sieciowych
Name:		usernet
Version:	1.0.9
Release:	2
License:	GPL
Group:		Applications/System
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	49bd462e783ee274b9ec67a8c5c45dd6
Patch0:		%{name}-Makefile.patch
Requires:	initscripts >= 3.20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The usernet utility provides a graphical interface for manipulating
network interfaces (bringing them up or down and viewing their
status). Users can only manipulate interfaces that are
user-controllable. The superuser can control all interfaces.

Install the usernet package if you'd like to provide a graphical
utility for manipulating network interfaces.

%description -l pl
Narzêdzie usernet daje graficzny inferfejs do manipulowania
interfejsami sieciowymi (podnoszenia, wy³±czania, sprawdzania
statusu). U¿ytkownicy mog± manipulowaæ tylko interfejsami
kontrolowanymi przez u¿ytkowników. Administator mo¿e kontrolowaæ
wszystkie.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	VERSION=%{version}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	BR=$RPM_BUILD_ROOT \
	VERSION=%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/usernet
%dir %{_datadir}/usernet
%{_datadir}/usernet/%{version}
%{_mandir}/man1/*
%{_sysconfdir}/X11/wmconfig/usernet
