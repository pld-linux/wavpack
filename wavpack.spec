#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	Open audio compression codec
Summary(pl.UTF-8):	Otwarty kodek kompresji dźwięku
Name:		wavpack
Version:	5.8.1
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://www.wavpack.com/downloads.html
Source0:	https://www.wavpack.com/%{name}-%{version}.tar.xz
# Source0-md5:	ff40072de82dd299fc45161bc46b8566
URL:		https://www.wavpack.com/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.15
BuildRequires:	gettext-tools
BuildRequires:	libtool >= 2:2
BuildRequires:	rpm-build >= 4.6
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WavPack is a completely open audio compression format providing
lossless, high-quality lossy, and a unique hybrid compression mode.

Although the technology is loosely based on previous versions of
WavPack, the new version 4 format has been designed from the ground up
to offer unparalleled performance and functionality. In the default
lossless mode WavPack acts just like a WinZip compressor for audio
files. However, unlike MP3 or WMA encoding which can affect the sound
quality, not a single bit of the original information is lost, so
there's no chance of degradation. This makes lossless mode ideal for
archiving audio material or any other situation where quality is
paramount. The compression ratio depends on the source material, but
generally is between 30% and 70%.

The hybrid mode provides all the advantages of lossless compression
with an additional bonus. Instead of creating a single file, this mode
creates both a relatively small, high-quality lossy file that can be
used all by itself, and a "correction" file that (when combined with
the lossy file) provides full lossless restoration. For some users
this means never having to choose between lossless and lossy
compression!

%description -l pl.UTF-8
WavPack to całkowicie otwarty format kompresji dźwięku dostarczający
tryby kompresji: bezstratny, stratny wysokiej jakości oraz unikalny
hybrydowy.

Chociaż technologia jest luźno oparta na poprzednich wersjach
WavPacka, format nowej wersji 4 został zaprojektowany od nowa, aby
zaoferować niezrównaną wydajność i funkcjonalność. W domyślnym trybie
bezstratnym WavPack zachowuje się tak jak kompresor WinZip dla plików
dźwiękowych. Jednak w przeciwieństwie do kodowań MP3 czy WMA, które
wpływają na jakość dźwięku, żaden bit oryginalnej informacji nie jest
tracony, więc nie ma żadnych szans na degradację. Czyni to tryb
bezstratny idealnym do archiwizowania materiałów dźwiękowych oraz w
innych sytuacjach, gdzie jakość jest najważniejsza. Współczynnik
kompresji zależy od materiału źródłowego, ale zwykle jest pomiędzy
30% a 70%.

Tryb hybrydowy udostępnia wszystkie zalety kompresji bezstratnej z
dodatkowym ulepszeniem. Zamiast tworzenia pojedynczego pliku tryb ten
tworzy zarówno stosunkowo mały, wysokiej jakości plik stratny, który
może być używany jako taki oraz plik "poprawek", który (w połączeniu z
plikiem stratnym) odtwarza pełną jakość bez strat. Dla niektórych
użytkowników oznacza to, że nie muszą wybierać pomiędzy kompresją
bezstratną a stratną.

%package libs
Summary:	Wavpack library
Summary(pl.UTF-8):	Biblioteka Wavpack
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description libs
Wavpack library.

%description libs -l pl.UTF-8
Biblioteka Wavpack.

%package devel
Summary:	Header files for Wavpack
Summary(pl.UTF-8):	Pliki nagłówkowe Wavpack
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for Wavpack.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Wavpack.

%package static
Summary:	Static Wavpack library
Summary(pl.UTF-8):	Statyczna biblioteka Wavpack
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Wavpack library.

%description static -l pl.UTF-8
Statyczna biblioteka Wavpack.

%package apidocs
Summary:	API documentation for Wavpack library
Summary(pl.UTF-8):	Dokumentacja API biblioteki Wavpack
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for Wavpack library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki Wavpack.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-legacy \
	%{?with_static_libs:--enable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/wavpack

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/wavpack
%attr(755,root,root) %{_bindir}/wvgain
%attr(755,root,root) %{_bindir}/wvtag
%attr(755,root,root) %{_bindir}/wvunpack
%{_mandir}/man1/wavpack.1*
%{_mandir}/man1/wvgain.1*
%{_mandir}/man1/wvtag.1*
%{_mandir}/man1/wvunpack.1*

%files libs
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README.md
%attr(755,root,root) %{_libdir}/libwavpack.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwavpack.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwavpack.so
%{_libdir}/libwavpack.la
%{_includedir}/wavpack
%{_pkgconfigdir}/wavpack.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libwavpack.a
%endif

%files apidocs
%defattr(644,root,root,755)
%doc doc/{WavPack*.pdf,wavpack_doc.html,style.css}
