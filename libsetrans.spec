Summary:	SELinux Translation library
Summary(pl.UTF-8):	Biblioteka tłumaczenia SELinuksa
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
mandatory access controls to Linux. The Security-enhanced Linux kernel
contains new architectural components originally developed to improve
the security of the Flask operating system. These architectural
components provide general support for the enforcement of many kinds
of mandatory access control policies, including those based on the
concepts of Type Enforcement, Role-based Access Control, and
Multi-level Security.

libsetrans provides an translation library to translate SELinux categories
from internal representations to user defined representation.

%description -l pl.UTF-8
Security-enhanced Linux jest prototypem jądra Linuksa i wielu
aplikacji użytkowych o funkcjach podwyższonego bezpieczeństwa.
Zaprojektowany jest tak, aby w prosty sposób ukazać znaczenie
obowiązkowej kontroli dostępu dla społeczności linuksowej. Ukazuje
również jak taką kontrolę można dodać do istniejącego systemu typu
Linux. Jądro SELinux zawiera nowe składniki architektury pierwotnie
opracowane w celu ulepszenia bezpieczeństwa systemu operacyjnego
Flask. Te elementy zapewniają ogólne wsparcie we wdrażaniu wielu 
typów polityk obowiązkowej kontroli dostępu, włączając te wzorowane 
na: Type Enforcement (TE), kontroli dostępu opartej na rolach (RBAC) 
i zabezpieczeniach wielopoziomowych.

libsetrans udostępnia bibliotekę tłumaczenia kategorii SELinuksa z
reprezentacji wewnętrznych na reprezentacje zdefiniowane przez
użytkownika.

%package devel
Summary:	Development fiels for libsetrans library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki libsetrans
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development fiels for libsetrans library.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki libsetrans.

%package static
Summary:	Static libsetrans library
Summary(pl.UTF-8):	Statyczna biblioteka libsetrans
Group:		Development/Libraries
#Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libsetrans library.

%description static -l pl.UTF-8
Statyczna biblioteka libsetrans.

%package utils
Summary:	libsetrans utils
Summary(pl.UTF-8):	Narzędzia dla libsetrans
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description utils
libsetrans utils.

%description utils -l pl.UTF-8
Narzędzia dla libsetrans.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir} \
	SHLIBDIR=$RPM_BUILD_ROOT/%{_lib}

# across /, so make it absolute
ln -nsf /%{_lib}/libsetrans.so.0 $RPM_BUILD_ROOT%{_libdir}/libsetrans.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) /%{_lib}/libsetrans.so.0
%{_mandir}/man8/mcs.8*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsetrans.so

%files static
%defattr(644,root,root,755)
%{_libdir}/libsetrans.a

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
