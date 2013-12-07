%define major	1
%define libname	%mklibname kate %{major}
%define liboggkate %mklibname oggkate %{major}
%define devname	%mklibname -d kate

Summary:	Karaoke and text codec for embedding in ogg
Name:		libkate
Version:	0.4.1
Release:	6
License:	BSD
Group:		System/Libraries
Url:		http://code.google.com/p/libkate/
Source0:	http://libkate.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:	doxygen
BuildRequires:	liboggz-tools
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(python)

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

%package -n %{libname}
Group:		System/Libraries
Summary:	Karaoke and text codec for embedding in ogg

%description -n %{libname}
This package includes a shared library for %{name}.

%package -n %{liboggkate}
Group:		System/Libraries
Summary:	Karaoke and text codec for embedding in ogg

%description -n %{liboggkate}
This package includes a shared library for %{name}.

%package -n %{devname}
Group:		Development/C
Summary:	Karaoke and text codec for embedding in ogg
Requires:	%{libname} = %{version}-%{release}
Requires:	%{liboggkate} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}kate-static-devel < 0.4.1-3

%description -n %{devname}
This package includes the development files for %{name}.

%package -n python-kdj
Group:		Development/Python
Summary:	Karaoke and text codec for embedding in ogg
Requires:	liboggz-tools
Requires:	%{name}-tools = %{version}-%{release}
Requires:	wxPythonGTK

%description -n python-kdj
This package includes the python binding for %{name}.

%package tools
Group:		Video
Summary:	Karaoke and text codec for embedding in ogg
Requires:	%{libname} = %{version}-%{release}

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
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std
mkdir -p installed-docs
mv %{buildroot}%{_datadir}/doc/%{name}/html installed-docs
rm -rf %{buildroot}%{_datadir}/doc

%files tools
%doc README THANKS AUTHORS
%{_bindir}/katalyzer
%{_bindir}/katedec
%{_bindir}/kateenc
%{_mandir}/man1/katalyzer.1*
%{_mandir}/man1/katedec.1*
%{_mandir}/man1/kateenc.1*

%files -n %{libname}
%{_libdir}/libkate.so.%{major}*

%files -n %{liboggkate}
%{_libdir}/liboggkate.so.%{major}*

%files -n %{devname}
%doc ChangeLog installed-docs/*
%{_libdir}/libkate.so
%{_libdir}/liboggkate.so
%{_libdir}/pkgconfig/kate.pc
%{_libdir}/pkgconfig/oggkate.pc
%{_includedir}/kate

%files -n python-kdj
%{_bindir}/KateDJ
%{py_puresitedir}/kdj
%{_mandir}/man1/KateDJ.1*

