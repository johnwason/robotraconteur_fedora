Name:           robotraconteur-companion
Version:        0.4.2
Release:        1%{?dist}
Summary:        Robot Raconteur C++ Companion Library

License:        Apache-2.0
URL:            https://github.com/robotraconteur/robotraconteur_companion
Source0:        RobotRaconteurCompanion-%{version}-Source.tar.gz

BuildRequires:  cmake >= 3.5.1
BuildRequires:  boost-devel >= 1.58.0
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
BuildRequires:  gtest-devel
BuildRequires:  g++
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  yaml-cpp-devel
BuildRequires:  eigen3-devel
BuildRequires:  librobotraconteur-devel

%description
Robot Raconteur C++ companion library.

%package -n librobotraconteurcompanion0.4
Summary:        Robot Raconteur C++ companion runtime library.

%description -n librobotraconteurcompanion0.4
Robot Raconteur C++ companion runtime library. This package provides the run-time library of robotraconteur-companion.

%package -n librobotraconteur-companion-devel
Summary:        Robot Raconteur C++ companion development files
Requires:       librobotraconteur-companion0.4, librobotraconteur-devel, boost-devel >= 1.58.0, cmake, g++, gcc, make, openssl-devel, yaml-cpp-devel, eigen3-devel, opencv-devel

%description -n librobotraconteur-companion-devel
Robot Raconteur C++ companion development files. This package provides the development files of robotraconteur-companion.

%prep
%autosetup -n RobotRaconteurCompanion-%{version}-Source

%build
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=%{_prefix} \
         -DBUILD_DOCUMENTATION=OFF \
         -DBUILD_SHARED_LIBS=ON \
         -DROBOTRACONTEUR_COMPANION_SOVERSION_MAJOR_ONLY=ON \
         -DCMAKE_SKIP_RPATH=ON \
         -DBUILD_TESTING=OFF

make %{?_smp_mflags}

%install
cd build
make install DESTDIR=%{buildroot}

# Move files to match Fedora packaging guidelines if needed

%files -n librobotraconteurcompanion0.4
%license LICENSE.txt
%{_libdir}/libRobotRaconteurCompanion.so.*

%files -n librobotraconteur-companion-devel
%license LICENSE.txt
%{_includedir}/RobotRaconteurCompanion/
%{_libdir}/libRobotRaconteurCompanion.so
%{_libdir}/cmake/
%{_datadir}/robotraconteur/

%changelog
* Tue Jul 29 2025 John Wason <wason@wasontech.com> - 0.4.2-1
- Test RPM Build
