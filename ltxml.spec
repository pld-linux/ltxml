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

%package devel
Summary:	LT XML API libraries and header files
Group:		Development/Libraries

%description devel


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
%doc ../00README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}*
%{_mandir}/*/*

%files devel
%defattr(644,root,root,755)
%doc ../00README ../00COPYRIGHT 
%doc doc/{*.gif,*.html,*.c}
%{_includedir}/*
%{_libdir}/*.a
