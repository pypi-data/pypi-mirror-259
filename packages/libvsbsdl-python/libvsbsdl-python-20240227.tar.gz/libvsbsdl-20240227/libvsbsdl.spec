Name: libvsbsdl
Version: 20240227
Release: 1
Summary: Library to access the BSD disklabel volume system format
Group: System Environment/Libraries
License: LGPL-3.0-or-later
Source: %{name}-%{version}.tar.gz
URL: https://github.com/libyal/libvsbsdl
            
BuildRequires: gcc            

%description -n libvsbsdl
Library to access the BSD disklabel volume system format

%package -n libvsbsdl-static
Summary: Library to access the BSD disklabel volume system format
Group: Development/Libraries
Requires: libvsbsdl = %{version}-%{release}

%description -n libvsbsdl-static
Static library version of libvsbsdl.

%package -n libvsbsdl-devel
Summary: Header files and libraries for developing applications for libvsbsdl
Group: Development/Libraries
Requires: libvsbsdl = %{version}-%{release}

%description -n libvsbsdl-devel
Header files and libraries for developing applications for libvsbsdl.

%package -n libvsbsdl-python3
Summary: Python 3 bindings for libvsbsdl
Group: System Environment/Libraries
Requires: libvsbsdl = %{version}-%{release} python3
BuildRequires: python3-devel python3-setuptools

%description -n libvsbsdl-python3
Python 3 bindings for libvsbsdl

%package -n libvsbsdl-tools
Summary: Several tools for Several tools for reading BSD disklabel volume systems
Group: Applications/System
Requires: libvsbsdl = %{version}-%{release}

%description -n libvsbsdl-tools
Several tools for Several tools for reading BSD disklabel volume systems

%prep
%setup -q

%build
%configure --prefix=/usr --libdir=%{_libdir} --mandir=%{_mandir} --enable-python
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -n libvsbsdl
%license COPYING COPYING.LESSER
%doc AUTHORS README
%{_libdir}/*.so.*

%files -n libvsbsdl-static
%license COPYING COPYING.LESSER
%doc AUTHORS README
%{_libdir}/*.a

%files -n libvsbsdl-devel
%license COPYING COPYING.LESSER
%doc AUTHORS README
%{_libdir}/*.so
%{_libdir}/pkgconfig/libvsbsdl.pc
%{_includedir}/*
%{_mandir}/man3/*

%files -n libvsbsdl-python3
%license COPYING COPYING.LESSER
%doc AUTHORS README
%{_libdir}/python3*/site-packages/*.a
%{_libdir}/python3*/site-packages/*.so

%files -n libvsbsdl-tools
%license COPYING COPYING.LESSER
%doc AUTHORS README
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Tue Feb 27 2024 Joachim Metz <joachim.metz@gmail.com> 20240227-1
- Auto-generated

