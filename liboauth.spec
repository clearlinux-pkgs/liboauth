#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : liboauth
Version  : 1.0.3
Release  : 13
URL      : https://sourceforge.net/projects/liboauth/files/liboauth-1.0.3.tar.gz
Source0  : https://sourceforge.net/projects/liboauth/files/liboauth-1.0.3.tar.gz
Summary  : OAuth - server to server secure API authentication
Group    : Development/Tools
License  : GPL-2.0 MIT OpenSSL
Requires: liboauth-lib = %{version}-%{release}
Requires: liboauth-license = %{version}-%{release}
BuildRequires : doxygen
BuildRequires : graphviz
BuildRequires : openssl-dev
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(nss)
Patch1: liboauth-openssl_1.1_compatibility.patch

%description
liboauth is a collection of c functions implementing the http://oauth.net API.
liboauth provides functions to escape and encode stings according to
OAuth specifications and offers high-level functionality built on top to sign
requests or verify signatures using either NSS or OpenSSL for calculating
the hash/signatures.

%package dev
Summary: dev components for the liboauth package.
Group: Development
Requires: liboauth-lib = %{version}-%{release}
Provides: liboauth-devel = %{version}-%{release}
Requires: liboauth = %{version}-%{release}

%description dev
dev components for the liboauth package.


%package lib
Summary: lib components for the liboauth package.
Group: Libraries
Requires: liboauth-license = %{version}-%{release}

%description lib
lib components for the liboauth package.


%package license
Summary: license components for the liboauth package.
Group: Default

%description license
license components for the liboauth package.


%prep
%setup -q -n liboauth-1.0.3
cd %{_builddir}/liboauth-1.0.3
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604353145
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1604353145
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/liboauth
cp %{_builddir}/liboauth-1.0.3/COPYING %{buildroot}/usr/share/package-licenses/liboauth/eda3f2529e7094f932fce6da9731f35f693c2659
cp %{_builddir}/liboauth-1.0.3/COPYING.GPL %{buildroot}/usr/share/package-licenses/liboauth/74a8a6531a42e124df07ab5599aad63870fa0bd4
cp %{_builddir}/liboauth-1.0.3/COPYING.MIT %{buildroot}/usr/share/package-licenses/liboauth/1be7c42bcbadfcecea76438685afb29fe755975a
cp %{_builddir}/liboauth-1.0.3/LICENSE.OpenSSL %{buildroot}/usr/share/package-licenses/liboauth/2b7ed594a25796f84812c487da49ea6f9260a979
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/oauth.h
/usr/lib64/liboauth.so
/usr/lib64/pkgconfig/oauth.pc
/usr/share/man/man3/oauth.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/liboauth.so.0
/usr/lib64/liboauth.so.0.8.7

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/liboauth/1be7c42bcbadfcecea76438685afb29fe755975a
/usr/share/package-licenses/liboauth/2b7ed594a25796f84812c487da49ea6f9260a979
/usr/share/package-licenses/liboauth/74a8a6531a42e124df07ab5599aad63870fa0bd4
/usr/share/package-licenses/liboauth/eda3f2529e7094f932fce6da9731f35f693c2659
