Name:       libquicktime
Version:    1.2.4
Release:    2%{?dist}
Summary:    Library for reading and writing Quicktime files
License:	LGPLv2+
URL:        http://libquicktime.sourceforge.net/

Source0:    http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# https://gitweb.gentoo.org/repo/gentoo.git/tree/media-libs/libquicktime
Patch0:     libquicktime-1.2.4-ffmpeg-2.patch
Patch1:     libquicktime-1.2.4-CVE-2016-2399.patch
Patch2:     libquicktime-1.2.4-ffmpeg-3.patch
Patch3:     libquicktime-1.2.4-ffmpeg-4.patch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:  faac-devel >= 1.24
BuildRequires:	faad2-devel >= 2.0
BuildRequires:  gettext-devel
BuildRequires:	gtk2-devel >= 2.4.0
BuildRequires:	lame-devel >= 3.93
BuildRequires:	libdv-devel
BuildRequires:	libGLU-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	libXaw-devel
BuildRequires:	libXt-devel
BuildRequires:	libXv-devel
BuildRequires:	pkgconfig(alsa) >= 0.9
BuildRequires:	pkgconfig(libdv) >= 0.102
BuildRequires:	pkgconfig(libpng) >= 1.2.23
BuildRequires:	pkgconfig(libswscale)
BuildRequires:  pkgconfig(schroedinger-1.0) >= 1.0.5
BuildRequires:	pkgconfig(x264) >= 0.48

%description
A simple and stable library, which can create reasonable compatible Quicktime
and AVI files either uncompressed (for high-end or production applications) or
with decent compression codecs for end user applications.

%package utils
Summary:	Utilities for working with Quicktime files

%description utils
This package contains utility programs for working with Quicktime files.

%package devel
Summary:	Development files for libquicktime
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	zlib-devel

%description devel
A simple and stable library, which can create reasonable compatible Quicktime
and AVI files either uncompressed (for high-end or production applications) or
with decent compression codecs for end user applications.

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
autoreconf -vif
%configure \
	--disable-static \
	--with-libdv \
	--without-doxygen

%make_build

%install
%make_install
find %{buildroot} -name "*.la" -delete

%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc README TODO
%{_libdir}/%{name}*.so.*
%{_libdir}/%{name}

%files utils
%{_bindir}/libquicktime_config
%{_bindir}/lqt_transcode
%{_bindir}/lqtplay
%{_bindir}/lqtremux
%{_bindir}/qt2text
%{_bindir}/qtdechunk
%{_bindir}/qtdump
%{_bindir}/qtinfo
%{_bindir}/qtrechunk
%{_bindir}/qtstreamize
%{_bindir}/qtyuv4toyuv
%{_mandir}/man1/lqtplay.1*

%files devel
%{_includedir}/lqt/
%{_libdir}/pkgconfig/libquicktime.pc
%{_libdir}/%{name}*.so

%changelog
* Fri Apr 27 2018 Simone Caronni <negativo17@gmail.com> - 1.2.4-2
- Add CVE and FFmpeg 4 patches.
- Update SPEC file.

* Tue Jun 14 2016 Simone Caronni <negativo17@gmail.com> - 1.2.4-1
- First build.
