Summary:	Open audio compression codec
Summary(pl):	Otwarty kodek kompresji d�wik�ku
Name:		wavpack
Version:	4.2
Release:	1
License:	other
Group:		Libraries
Source0:	http://www.wavpack.com/%{name}-%{version}.tar.bz2
# Source0-md5:	2e740b2e36833e78a227913cf0efc3b6
URL:		http://www.wavpack.com
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
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

#%description -l pl
#write me

%package libs
Summary:	Wavpack library
Summary(pl):	Biblioteka Wavpack
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description libs
Wavpack library.

%description libs -l pl
Biblioteka Wavpack.

%package devel
Summary:	Header files for Wavpack
Summary(pl):	Pliki nag��wkowe Wavpack
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for Wavpack.

%description devel -l pl
Pliki nag��wkowe biblioteki Wavpack.

%package static
Summary:	Static Wavpack library
Summary(pl):	Statyczna biblioteka Wavpack
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Wavpack library.

%description static -l pl
Statyczna biblioteka Wavpack.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README license.txt
%attr(755,root,root) %{_bindir}/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/wavpack
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a