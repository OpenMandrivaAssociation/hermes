%define prefix %{_prefix}
%define lib_name_orig libhermes
%define lib_major 1
%define lib_name %mklibname hermes %{lib_major}

Summary:	Hermes pixel format conversion library
Name:		hermes
Version:	1.3.3
Release:	%mkrel 12
License:	LGPL
Group:		System/Libraries
URL:		http://clanlib.org/hermes/
Source0:	http://dark.x.dtu.dk/~mbn/clanlib/download/Hermes-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
HERMES is a library designed to convert a source buffer with a specified pixel
format to a destination buffer with possibly a different format at the maximum
possible speed.

On x86 and MMX architectures, handwritten assembler routines take over
the job and do it lightning fast.

On top of that, HERMES provides fast surface clearing, stretching and some
dithering. Supported platforms are basically all that have an ANSI C compiler
as there is no platform specific code but those are supported: DOS, Win32
(Visual C), Linux, FreeBSD (IRIX, Solaris are on hold at the moment), some BeOS
support.

%package -n %{lib_name}
Summary: Main library for %{name}
Group: System/Libraries
Obsoletes: Hermes hermes
Provides: Hermes hermes

%description -n %{lib_name}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{lib_name}-devel
Summary: Headers for developing programs that will use %{name}
Group: Development/C
Requires: %{lib_name} = %{version}
Provides: %{lib_name_orig}-devel
Obsoletes: Hermes-devel hermes-devel
Provides: Hermes-devel hermes-devel

%description -n %{lib_name}-devel
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

%prep
%setup -q -n Hermes-%{version}

%build
%configure2_5x \
    --disable-x86asm
make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{lib_name}
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING INSTALL.DOS INSTALL.unix TODO TODO.conversion 
%{_libdir}/lib*.so.*

%files -n %{lib_name}-devel
%defattr(-, root, root)
%doc docs/api/*.htm
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/*.*a




%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.3-10mdv2011.0
+ Revision: 665409
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.3-9mdv2011.0
+ Revision: 605854
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.3-8mdv2010.1
+ Revision: 522846
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.3.3-7mdv2010.0
+ Revision: 425142
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.3.3-6mdv2009.0
+ Revision: 221127
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.3.3-5mdv2008.1
+ Revision: 126656
- kill re-definition of %%buildroot on Pixel's request


* Mon Mar 19 2007 Oden Eriksson <oeriksson@mandriva.com> 1.3.3-5mdv2007.1
+ Revision: 146693
- disable inline asm code by using "--disable-x86asm", it does not build otherwise

* Sun Mar 18 2007 Oden Eriksson <oeriksson@mandriva.com> 1.3.3-4mdv2007.1
+ Revision: 146024
- bump release
- added a gcc4 patch by pld (P0)
- Import hermes

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 1.3.3-3mdv2007.1
- use the mkrel macro

