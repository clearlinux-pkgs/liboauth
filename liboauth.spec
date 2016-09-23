#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : liboauth
Version  : 1.0.3
Release  : 2
URL      : http://downloads.sourceforge.net/project/liboauth/liboauth-1.0.3.tar.gz
Source0  : http://downloads.sourceforge.net/project/liboauth/liboauth-1.0.3.tar.gz
Summary  : OAuth - server to server secure API authentication
Group    : Development/Tools
License  : GPL-2.0 MIT
Requires: liboauth-lib
Requires: liboauth-doc
BuildRequires : doxygen
BuildRequires : graphviz
BuildRequires : openssl-dev
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(nss)

%description
liboauth is a collection of c functions implementing the http://oauth.net API.
liboauth provides functions to escape and encode stings according to
OAuth specifications and offers high-level functionality built on top to sign
requests or verify signatures using either NSS or OpenSSL for calculating
the hash/signatures.

%package dev
Summary: dev components for the liboauth package.
Group: Development
Requires: liboauth-lib
Provides: liboauth-devel

%description dev
dev components for the liboauth package.


%package doc
Summary: doc components for the liboauth package.
Group: Documentation

%description doc
doc components for the liboauth package.


%package lib
Summary: lib components for the liboauth package.
Group: Libraries

%description lib
lib components for the liboauth package.


%prep
%setup -q -n liboauth-1.0.3

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
