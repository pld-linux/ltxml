Summary:	LT XML toolkit
Summary(pl):	Zestaw narzêdzi LT XML
Name:		ltxml
Version:	1.2.5
Release:	2
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.cogsci.ed.ac.uk/pub/LTXML/%{name}-%{version}.tar.gz
# Source0-md5:	7aa37556dc9b532013c3bf9698e7d630
Patch0:		%{name}-CFLAGS.patch
Patch1:		%{name}-shared.patch
Patch2:		%{name}-link.patch
URL:		http://www.ltg.ed.ac.uk/software/xml/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This release contains version 1.2 of the LT XML toolkit and API,
including everything required to process a very wide range of
well-formed XML documents, as well as normalised SGML documents
produced with the LT NSL toolkit.

The basic architecture is one in which XML and nSGML documents can be
piped through any tools built using our API for augmentation,
extraction, etc.

%description -l pl
Ten pakiet zawiera wersjê 1.2 zestawu narzêdzi i API LT XML,
zawieraj±c± wszystko co potrzeba do przetwarzania szerokiego
zakresu dobrze sformu³owanych dokumentów XML, a tak¿e dobrze
unormowanych dokumentów SGML wyprodukowanych przez zestaw narzêdzi LT
NSL.

Podstawowa architektura jest taka, w której dokumenty XML i nSGML mog±
byæ przepuszczane przez dowolne narzêdzia zbudowane przy u¿yciu tego
API do powiêkszania, wyci±gania itp.

%package devel
Summary:	LT XML API libraries and header files
Summary(pl):	Pliki nag³ówkowe i biblioteki API LT XML
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
LT XML API libraries and header files.

%description devel -l pl
Pliki nag³ówkowe i biblioteki API LT XML.

%package static
Summary:	Static LT XML libraries
Summary(pl):	Statyczne biblioteki LT XML
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static LT XML libraries.

%description static -l pl
Statyczne biblioteki LT XML.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cd XML
cp -f /usr/share/automake/config.* .
%{__autoconf}
%configure \
	--enable-multi-byte
%{__make} all

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C XML install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	exec_prefix=$RPM_BUILD_ROOT%{_prefix} \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc 00README 00COPYRIGHT XML/doc/{*.gif,*.html,*.c}
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/liblt*.so.*.*.*
%{_prefix}/lib/%{name}*
%{_mandir}/man[15]/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblt*.so
%{_libdir}/liblt*.la
%{_includedir}/ltxml12

%files static
%defattr(644,root,root,755)
%{_libdir}/liblt*.a
