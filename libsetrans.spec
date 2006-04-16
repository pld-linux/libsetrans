Summary:	SELinux Translation library
Name:		libsetrans
Version:	0.1.20
Release:	0.9
License:	GPL v2
Group:		Libraries
Source0:	%{name}-%{version}.tgz
# Source0-md5:	79deb2119b69159e05c09345ed327fe1
BuildRequires:	libselinux-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Security-enhanced Linux is a feature of the Linux kernel and a number
of utilities with enhanced security functionality designed to add
mandatory access controls to Linux.  The Security-enhanced Linux
kernel contains new architectural components originally developed to
improve the security of the Flask operating system. These
architectural components provide general support for the enforcement
of many kinds of mandatory access control policies, including those
based on the concepts of Type Enforcement, Role-based Access
Control, and Multi-level Security.

libsetrans provides an translation library to translate SELinux categories
from internal representations to user defined representation.

%package static
Summary:	Static libsetrans library
Summary(pl):	Statyczna biblioteka libsetrans
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
Static libsetrans library.

%package utils
Summary:	libsetrans utils
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description utils

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir} \
	SHLIBDIR=$RPM_BUILD_ROOT/%{_lib}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/libsetrans.so.0
%{_mandir}/man8/mcs.8*

%files static
%defattr(644,root,root,755)
%{_libdir}/*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}
