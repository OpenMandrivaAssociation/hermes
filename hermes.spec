%define major	1
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Hermes pixel format conversion library
Name:		hermes
Version:	1.3.3
Release:	13
License:	LGPLv2
Group:		System/Libraries
Url:		ftp://ftp.scene.org/pub/resources/code/libs/hermes/download.html
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

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries
Provides:	hermes

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{devname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel
Obsoletes:	%{_lib}hermes1-devel

%description -n %{devname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -qn Hermes-%{version}

%build
# FIXME: gold linker dies with internal error in convert_types, at ../../gold/gold.h:192 on i586
%ifarch %{ix86}
export CC="%{__cc} -fuse-ld=bfd"
export CXX="%{__cxx} -fuse-ld=bfd"
mkdir -p BFD
ln -sf /usr/bin/ld.bfd BFD/ld
export PATH=$PWD/BFD:$PATH
%endif
%configure2_5x \
	--disable-static \
	--disable-x86asm

make

%install
%makeinstall

%files -n %{libname}
%{_libdir}/libHermes.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING INSTALL.DOS INSTALL.unix TODO TODO.conversion 
%doc docs/api/*.htm
%{_includedir}/*
%{_libdir}/lib*.so

