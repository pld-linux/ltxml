Summary:	LT XML toolkit
Name:		ltxml
Version:	1.2.5
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.cogsci.ed.ac.uk/pub/LTXML/%{name}-%{version}.tar.gz
Patch1:		%{name}-CFLAGS.patch
URL:		http://www.ltg.ed.ac.uk/software/xml/
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

%package devel
Summary:	LT XML API libraries and header files
Group:		Development/Libraries

%description devel
LT XML API libraries and header files.

%prep
%setup -q -n %{name}-%{version}/XML
%patch1 -p2

%build
%{__autoconf}
%configure \
	--enable-multi-byte
%{__make} all

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	exec_prefix=$RPM_BUILD_ROOT%{_prefix} \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ../00README ../00COPYRIGHT
%doc doc/{*.gif,*.html,*.c}
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}*
%{_mandir}/*/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/*.a
