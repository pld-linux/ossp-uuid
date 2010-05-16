# TODO
# - fix bindings compilation (when library is not installed)
#
# Conditional build:
%bcond_without	php		# build PHP binding
%bcond_without	perl		# build Perl binding
%bcond_without	pgsql		# build postgresql binding

Summary:	Universally Unique Identifier library
Summary(pl.UTF-8):	Biblioteka unikalnych identyfikatorów UUID
Name:		ossp-uuid
Version:	1.6.2
Release:	7
License:	MIT
Group:		Libraries
Source0:	ftp://ftp.ossp.org/pkg/lib/uuid/uuid-%{version}.tar.gz
# Source0-md5:	5db0d43a9022a6ebbbc25337ae28942f
Patch0:		uuid-ossp-prefix.patch
URL:		http://www.ossp.org/pkg/lib/uuid/
BuildRequires:	libtool
%{?with_perl:BuildRequires:	perl-devel}
%{?with_php:BuildRequires:	php-devel >= 3:5.0.0}
%{?with_pgsql:BuildRequires:	postgresql-devel}
BuildRequires:	rpmbuild(macros) >= 1.519
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OSSP uuid is a ISO-C:1999 application programming interface (API) and
corresponding command line interface (CLI) for the generation of DCE
1.1, ISO/IEC 11578:1996 and RFC 4122 compliant Universally Unique
Identifier (UUID). It supports DCE 1.1 variant UUIDs of version 1
(time and node based), version 3 (name based, MD5), version 4 (random
number based) and version 5 (name based, SHA-1). Additional API
bindings are provided for the languages ISO-C++:1998, Perl:5 and
PHP:4/5. Optional backward compatibility exists for the ISO-C DCE-1.1
and Perl Data::UUID APIs.

%description -l pl.UTF-8
OSSP uuid to interfejs programistyczny (API) ISO-C:1999 i
odpowiadający mu interfejs linii poleceń (CLI) do generowania
całkowicie unikalnych identyfikatorów UUID (Universally Unique
Identifier) zgodnych z DCE 1.1, ISO/IEC 11578:1996 i RFC 4122.
Obsługuje wariant DCE 1.1 UUID-ów w wersji 1 (oparty na czasie i
węzłach), w wersji 3 (oparty na nazwie i MD5), w wersji 4 (oparty na
liczbach losowych) oraz w wersji 5 (oparty na nazwach i SHA-1).
Załączone są dodatkowe wiązania API do języków ISO-C++:1998, Perl:5
oraz PHP:4/5. Istnieje też opcjonalna warstwa kompatybilności dla API
ISO-C DCE-1.1 i perlowego Data::UUID.

%package devel
Summary:	Development files for Universally Unique Identifier library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki OSSP uuid
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development headers and libraries for OSSP uuid.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki OSSP uuid.

%package c++
Summary:	C++ support for Universally Unique Identifier library
Summary(pl.UTF-8):	Wiązania C++ dla biblioteki OSSP uuid
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description c++
C++ binding for OSSP uuid library.

%description c++ -l pl.UTF-8
Wiązania C++ dla biblioteki OSSP uuid.

%package c++-devel
Summary:	C++ development support for Universally Unique Identifier library
Summary(pl.UTF-8):	Pliki programistyczne wiązania C++ biblioteki OSSP uuid
Group:		Development/Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description c++-devel
C++ development headers and libraries for OSSP uuid.

%description c++-devel -l pl.UTF-8
Pliki programistyczne wiązania C++ biblioteki OSSP uuid.

%package dce
Summary:	DCE support for Universally Unique Identifier library
Summary(pl.UTF-8):	Obsługa DCE dla biblioteki OSSP uuid
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description dce
DCE OSSP uuid library.

%description dce -l pl.UTF-8
Biblioteka DCE OSSP uuid.

%package dce-devel
Summary:	DCE development support for Universally Unique Identifier library
Summary(pl.UTF-8):	Pliki programistyczne obsługi DCE dla biblioteki OSSP uuid
Group:		Development/Libraries
Requires:	%{name}-dce = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description dce-devel
DCE development headers and libraries for OSSP uuid.

%description dce-devel -l pl.UTF-8
Pliki programistyczne obsługi DCE dla biblioteki OSSP uuid.

%package -n perl-uuid
Summary:	OSSP uuid Perl Binding
Summary(pl.UTF-8):	Perlowe wiązania biblioteki OSSP uuid
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n perl-uuid
Perl OSSP uuid modules, which includes a Data::UUID replacement.

%description -n perl-uuid -l pl.UTF-8
Moduły Perla OSSP uuid, zawierające zamiennik Data::UUID.

%package -n php-uuid
Summary:	PHP support for Universally Unique Identifier library
Summary(pl.UTF-8):	Wiązania PHP dla biblioteki OSSP UUID
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4

%description -n php-uuid
UUID is a PHP extension for the creation of Universally Unique
Identifiers (UUID).

%description -n php-uuid -l pl.UTF-8
UUID to rozrzeszenie PHP do tworzenia całkowicie unikalnych
identyfikatorów UUID.

%package -n postgresql-uuid
Summary:	OSSP uuid bindings for PostgreSQL
Summary(pl.UTF-8):	Wiązania OSSP uuid dla PostgreSQL-a
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n postgresql-uuid
PostgreSQL OSSP uuid module.

%description -n postgresql-uuid -l pl.UTF-8
Moduł OSSP uuid dla PostgreSQL-a.

%prep
%setup -q -n uuid-%{version}
%patch0 -p1

%build
# Build the library.
%configure \
	--includedir=%{_includedir}/ossp-uuid \
	--disable-static \
	--with-dce \
	--with-cxx \
	--with%{!?with_perl:out}-perl \
	--with%{!?with_php:out}-php \
	--with%{!?with_pgsql:out}-pgsql

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_lib}
%{__make} install \
	WITH_PHP=no \
	WITH_PERL=no \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_libdir}/libossp-uuid.so.* $RPM_BUILD_ROOT/%{_lib}
ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/libossp-uuid.so.*.*) $RPM_BUILD_ROOT%{_libdir}/libossp-uuid.so

%if %{with perl}
%{__make} pure_install \
	-C perl \
	INSTALLDIRS=vendor \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{perl_vendorarch}/OSSP/uuid.pod
rm $RPM_BUILD_ROOT%{perl_vendorarch}/auto/OSSP/uuid/.packlist
rm $RPM_BUILD_ROOT%{perl_vendorarch}/auto/OSSP/uuid/uuid.bs
%endif

%if %{with php}
install -d $RPM_BUILD_ROOT{%{php_data_dir},%{php_sysconfdir}/conf.d}
%{__make} install \
	-C php \
	-f Makefile.local \
	EXTDIR=%{php_extensiondir} \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT{%{php_extensiondir},%{php_data_dir}}/uuid.php
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{name}.ini
; Enable %{name} extension module
extension=%{name}.so
EOF
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	c++ -p /sbin/ldconfig
%postun	c++ -p /sbin/ldconfig

%post	dce -p /sbin/ldconfig
%postun	dce -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HISTORY NEWS PORTING README SEEALSO THANKS TODO USERS
%attr(755,root,root) %{_bindir}/uuid
%attr(755,root,root) /%{_lib}/libossp-uuid.so.*.*.*
%attr(755,root,root) %ghost /%{_lib}/libossp-uuid.so.16
%{_mandir}/man1/uuid.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/uuid-config
%attr(755,root,root) %{_libdir}/libossp-uuid.so
%{_libdir}/libossp-uuid.la
%dir %{_includedir}/ossp-uuid
%{_includedir}/ossp-uuid/uuid.h
%{_pkgconfigdir}/ossp-uuid.pc
%{_mandir}/man1/uuid-config.1*
%{_mandir}/man3/ossp-uuid.3*

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libossp-uuid++.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libossp-uuid++.so.16

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libossp-uuid++.so
%{_libdir}/libossp-uuid++.la
%{_includedir}/ossp-uuid/uuid++.hh
%{_mandir}/man3/uuid++.3*

%files dce
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libossp-uuid_dce.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libossp-uuid_dce.so.16

%files dce-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libossp-uuid_dce.so
%{_libdir}/libossp-uuid_dce.la
%{_includedir}/ossp-uuid/uuid_dce.h

%if %{with perl}
%files -n perl-uuid
%defattr(644,root,root,755)
%dir %{perl_vendorarch}/OSSP
%{perl_vendorarch}/OSSP/uuid.pm
%dir %{perl_vendorarch}/auto/OSSP
%dir %{perl_vendorarch}/auto/OSSP/uuid
%attr(755,root,root) %{perl_vendorarch}/auto/OSSP/uuid/uuid.so
%{_mandir}/man3/OSSP::uuid.3*
%endif

%if %{with php}
%files -n php-uuid
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{name}.ini
%attr(755,root,root) %{php_extensiondir}/%{name}.so
%{php_data_dir}/uuid.php
%endif

%if %{with pgsql}
%files -n postgresql-uuid
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/postgresql/ossp-uuid.so
%{_datadir}/postgresql/uuid.sql
%endif
