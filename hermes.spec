%define prefix %{_prefix}
%define lib_name_orig libhermes
%define lib_major 1
%define lib_name %mklibname hermes %{lib_major}

Summary:	Hermes pixel format conversion library
Name:		hermes
Version:	1.3.3
Release:	%mkrel 5
License:	LGPL
Group:		System/Libraries
URL:		http://clanlib.org/hermes/
Source0:	http://dark.x.dtu.dk/~mbn/clanlib/download/Hermes-%{version}.tar.bz2

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

%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig

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


