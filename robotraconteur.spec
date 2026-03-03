Name:           robotraconteur
Version:        1.2.7
Release:        1%{?dist}
Summary:        Robot Raconteur is a communication framework for Robotics and Automation

License:        Apache-2.0
URL:            https://github.com/robotraconteur/robotraconteur
Source0:        RobotRaconteur-%{version}-Source.tar.gz
Patch:         395.patch
ExcludeArch:   s390x

BuildRequires:  cmake >= 3.5.1
BuildRequires:  boost-devel >= 1.58.0
BuildRequires:  bluez-libs-devel
BuildRequires:  dbus-devel
BuildRequires:  openssl-devel
BuildRequires:  libusb1-devel
BuildRequires:  zlib-devel
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  gtest-devel
BuildRequires:  g++
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  swig
BuildRequires:  python3-pytest

Requires:       bluez-libs
Requires:       dbus
Requires:       libusb1
Requires:       python3-numpy
Requires:       python3

%description
Robot Raconteur is a communication framework for Robotics and Automation.

%package -n librobotraconteurcore1
Summary:        Robot Raconteur runtime library
Requires:       bluez-libs, dbus, libusb1

%description -n librobotraconteurcore1
This package provides the run-time library of Robot Raconteur.

%package -n librobotraconteur-devel
Summary:        Robot Raconteur development files
Requires:       librobotraconteurcore1, robotraconteurgen boost-devel >= 1.58.0, cmake, g++, gcc, make, openssl-devel

%description -n librobotraconteur-devel
This package provides development files for Robot Raconteur.

%package -n python3-robotraconteur
Summary:        Robot Raconteur Python 3 module
Requires:       bluez-libs, dbus, libusb1, python3-numpy, python3

%description -n python3-robotraconteur
Robot Raconteur Python module. Use with python 3.

%package -n robotraconteurgen
Summary:        RobotRaconteurGen tool
Requires:       librobotraconteurcore1

%description -n robotraconteurgen
This package provides the RobotRaconteurGen tool.

%prep
%autosetup -n RobotRaconteur-%{version}-Source -p1

%conf
%cmake \
   -DBUILD_GEN=ON \
   -DBUILD_PYTHON=OFF \
   -DBUILD_PYTHON3=ON \
   -DUSE_PREGENERATED_SOURCE=OFF \
   -DPYTHON3_EXECUTABLE=%{__python3} \
   -DINSTALL_PYTHON3_PIP=ON \
   -DBUILD_DOCUMENTATION=OFF \
   -DBUILD_SHARED_LIBS=ON \
   -DROBOTRACONTEURCORE_SOVERSION_MAJOR_ONLY=ON \
   -DROBOTRACONTEUR_SKIP_RPATH=ON \
   -DROBOTRACONTEUR_TESTING_DISABLE_DISCOVERY_LOOPBACK=ON \
   -DCMAKE_GTEST_DISCOVER_TESTS_DISCOVERY_MODE=PRE_TEST \
   -DBUILD_TESTING=ON \
   -DCMAKE_DISABLE_PRECOMPILE_HEADERS=ON \
   -DINSTALL_PYTHON3_PIP_EXTRA_ARGS="--compile --no-build-isolation \
      --no-deps --root-user-action=ignore"

%build
export LD_LIBRARY_PATH=%{_builddir}/%{?buildsubdir}/%{_vpath_builddir}/out/lib:$LD_LIBRARY_PATH
%cmake_build

%install
%cmake_install

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}:$LD_LIBRARY_PATH
%ctest -j1 -C Release

# Move files to match Fedora packaging guidelines if needed

%files -n librobotraconteurcore1
%license LICENSE.txt
%{_libdir}/libRobotRaconteurCore.so.1{,.*}

%files -n librobotraconteur-devel
%license LICENSE.txt
%{_includedir}/RobotRaconteur.h
%{_includedir}/RobotRaconteur/
%{_libdir}/libRobotRaconteurCore.so
%{_libdir}/cmake/

%files -n python3-robotraconteur
%license LICENSE.txt
%{python3_sitearch}/RobotRaconteur/
%{python3_sitearch}/robotraconteur-*.dist-info/

%files -n robotraconteurgen
%license LICENSE.txt
%{_bindir}/RobotRaconteurGen
%{_mandir}/man1/robotraconteurgen.1*

%changelog
* Thu Dec 18 2025 John Wason <wason@wasontech.com> - 1.2.7-1
- Update to upstream version 1.2.7
* Sun Aug 31 2025 John Wason <wason@wasontech.com> - 1.2.6-1
- Test RPM Build
