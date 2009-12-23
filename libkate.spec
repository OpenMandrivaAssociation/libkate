%define name libkate
%define version 0.3.7
%define release %mkrel 1
%define major 1
%define libname %mklibname kate %major
%define develname %mklibname -d kate
%define staticname %mklibname -s -d kate

Summary: Karaoke and text codec for embedding in ogg
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://libkate.googlecode.com/files/%{name}-%{version}.tar.gz
License: BSD
Group: System/Libraries
Url: http://code.google.com/p/libkate/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: python-devel
BuildRequires: libpng-devel
BuildRequires: libogg-devel
BuildRequires: liboggz-tools

%description
Kate is an overlay codec, originally designed for karaoke and text,
that can be multiplixed in Ogg. Text and images can be carried by a
Kate stream, and animated. Most of the time, this would be multiplexed
with audio/video to carry subtitles, song lyrics (with or without
karaoke data), etc, but doesn't have to be.

Series of curves (splines, segments, etc) may be attached to various
properties (text position, font size, etc) to create animated
overlays. This allows scrolling or fading text to be defined. This can
even be used to draw arbitrary shapes, so hand drawing can also be
represented by a Kate stream.

%package -n %libname
Group: System/Libraries
Summary: Karaoke and text codec for embedding in ogg

%description -n %libname
Kate is an overlay codec, originally designed for karaoke and text,
that can be multiplixed in Ogg. Text and images can be carried by a
Kate stream, and animated. Most of the time, this would be multiplexed
with audio/video to carry subtitles, song lyrics (with or without
karaoke data), etc, but doesn't have to be.

Series of curves (splines, segments, etc) may be attached to various
properties (text position, font size, etc) to create animated
overlays. This allows scrolling or fading text to be defined. This can
even be used to draw arbitrary shapes, so hand drawing can also be
represented by a Kate stream.

%package -n %develname
Group: Development/C
Summary: Karaoke and text codec for embedding in ogg
Requires: %libname = %version-%release
Provides: %name-devel = %version-%release

%description -n %develname
Kate is an overlay codec, originally designed for karaoke and text,
that can be multiplixed in Ogg. Text and images can be carried by a
Kate stream, and animated. Most of the time, this would be multiplexed
with audio/video to carry subtitles, song lyrics (with or without
karaoke data), etc, but doesn't have to be.

Series of curves (splines, segments, etc) may be attached to various
properties (text position, font size, etc) to create animated
overlays. This allows scrolling or fading text to be defined. This can
even be used to draw arbitrary shapes, so hand drawing can also be
represented by a Kate stream.

%package -n %staticname
Group: Development/C
Summary: Karaoke and text codec for embedding in ogg
Requires: %develname = %version-%release
Provides: %name-static-devel = %version-%release

%description -n %staticname
Kate is an overlay codec, originally designed for karaoke and text,
that can be multiplixed in Ogg. Text and images can be carried by a
Kate stream, and animated. Most of the time, this would be multiplexed
with audio/video to carry subtitles, song lyrics (with or without
karaoke data), etc, but doesn't have to be.

Series of curves (splines, segments, etc) may be attached to various
properties (text position, font size, etc) to create animated
overlays. This allows scrolling or fading text to be defined. This can
even be used to draw arbitrary shapes, so hand drawing can also be
represented by a Kate stream.

%package -n python-kdj
Group: Development/Python
Summary: Karaoke and text codec for embedding in ogg
Requires: liboggz-tools
Requires: %name-tools = %version-%release
Requires: wxPythonGTK

%description -n python-kdj
Kate is an overlay codec, originally designed for karaoke and text,
that can be multiplixed in Ogg. Text and images can be carried by a
Kate stream, and animated. Most of the time, this would be multiplexed
with audio/video to carry subtitles, song lyrics (with or without
karaoke data), etc, but doesn't have to be.

Series of curves (splines, segments, etc) may be attached to various
properties (text position, font size, etc) to create animated
overlays. This allows scrolling or fading text to be defined. This can
even be used to draw arbitrary shapes, so hand drawing can also be
represented by a Kate stream.

%package tools
Group: Video
Summary: Karaoke and text codec for embedding in ogg
Requires: %libname = %version-%release

%description tools
Kate is an overlay codec, originally designed for karaoke and text,
that can be multiplixed in Ogg. Text and images can be carried by a
Kate stream, and animated. Most of the time, this would be multiplexed
with audio/video to carry subtitles, song lyrics (with or without
karaoke data), etc, but doesn't have to be.

Series of curves (splines, segments, etc) may be attached to various
properties (text position, font size, etc) to create animated
overlays. This allows scrolling or fading text to be defined. This can
even be used to draw arbitrary shapes, so hand drawing can also be
represented by a Kate stream.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot} installed-docs
%makeinstall_std
mkdir -p installed-docs
mv %buildroot%_datadir/doc/%name/html installed-docs
rm -rf %buildroot%_datadir/doc

%clean
rm -rf %{buildroot}

%files tools
%defattr(-,root,root)
%_bindir/katalyzer
%_bindir/katedec
%_bindir/kateenc
%_mandir/man1/katalyzer.1*
%_mandir/man1/katedec.1* 
%_mandir/man1/kateenc.1*

%files -n %libname
%defattr(-,root,root)
%doc README THANKS AUTHORS
%_libdir/libkate.so.%{major}*
%_libdir/liboggkate.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%doc ChangeLog installed-docs/*
%_libdir/libkate.so
%_libdir/liboggkate.so
%_libdir/libkate.la
%_libdir/liboggkate.la
%_libdir/pkgconfig/kate.pc
%_libdir/pkgconfig/oggkate.pc
%_includedir/kate

%files -n %staticname
%defattr(-,root,root)
%_libdir/libkate.a
%_libdir/liboggkate.a

%files -n python-kdj
%defattr(-,root,root)
%_bindir/KateDJ
%py_puresitedir/kdj
%_mandir/man1/KateDJ.1*

