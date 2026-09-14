Name:           robotraconteur-companion
Version:        0.4.3
Release:        1%{?dist}
Summary:        Robot Raconteur C++ Companion Library

License:        Apache-2.0
URL:            https://github.com/robotraconteur/robotraconteur_companion
Source0:        %{url}/releases/download/v%{version}/RobotRaconteurCompanion-%{version}-Source.tar.gz
Patch0:         https://patch-diff.githubusercontent.com/raw/robotraconteur/robotraconteur_companion/pull/77.patch
ExcludeArch:    s390x

BuildRequires:  cmake
BuildRequires:  boost-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
BuildRequires:  gtest-devel
BuildRequires:  g++
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  yaml-cpp-devel
BuildRequires:  eigen3-devel
BuildRequires:  opencv-devel
BuildRequires:  librobotraconteur-devel
BuildRequires:  fdupes
# Documentation
BuildRequires:  doxygen

%description
Robot Raconteur C++ Companion library.

%package -n librobotraconteurcompanion0.4
Summary:        Robot Raconteur C++ Companion runtime library.

%description -n librobotraconteurcompanion0.4
Robot Raconteur C++ Companion runtime library. This package provides the run-time library of robotraconteur-companion.

%package -n librobotraconteur-companion-devel
Summary:        Robot Raconteur C++ Companion development files
Requires:       librobotraconteurcompanion0.4%{?_isa} = %{version}-%{release}
Requires:       librobotraconteur-devel
Requires:       boost-devel
Requires:       yaml-cpp-devel
Requires:       eigen3-devel
Requires:       opencv-devel

%description -n librobotraconteur-companion-devel
Robot Raconteur C++ Companion development files. This package provides the development files of robotraconteur-companion.

%package -n librobotraconteur-companion-devel-doc
Summary:        Documentation for the Robot Raconteur C++ Companion Library
BuildArch: noarch

%description -n librobotraconteur-companion-devel-doc
Documentation for the Robot Raconteur C++ Companion Library

%prep
%autosetup -n RobotRaconteurCompanion-%{version}-Source -p1

%build
%cmake \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DBUILD_DOCUMENTATION=ON \
    -DBUILD_SHARED_LIBS=ON \
    -DROBOTRACONTEUR_COMPANION_SOVERSION_MAJOR_ONLY=ON \
    -DCMAKE_SKIP_RPATH=ON \
    -DBUILD_TESTING=ON \
    -DCMAKE_DISABLE_PRECOMPILE_HEADERS=ON

export LD_LIBRARY_PATH=%{_builddir}/%{?buildsubdir}/%{_vpath_builddir}:$LD_LIBRARY_PATH
%cmake_build
%cmake_build --target RobotRaconteurCompanion_doc

%install
%cmake_install

mkdir -p %{buildroot}%{_docdir}/librobotraconteur-companion-devel-doc
cp -a %{_vpath_builddir}/docs/* %{buildroot}%{_docdir}/librobotraconteur-companion-devel-doc/

%fdupes %{buildroot}%{_docdir}

%check
export LD_LIBRARY_PATH=%{_builddir}/%{?buildsubdir}/%{_vpath_builddir}:$LD_LIBRARY_PATH
%ctest -j1

# Move files to match Fedora packaging guidelines if needed

%files -n librobotraconteurcompanion0.4
%license LICENSE.txt
%{_libdir}/libRobotRaconteurCompanion.so.*

%files -n librobotraconteur-companion-devel
%license LICENSE.txt
%{_includedir}/RobotRaconteurCompanion/
%{_libdir}/libRobotRaconteurCompanion.so
%{_libdir}/cmake/RobotRaconteurCompanion/
%{_datadir}/robotraconteur/

%files -n librobotraconteur-companion-devel-doc
%license LICENSE.txt
%{_docdir}/librobotraconteur-companion-devel-doc/

%changelog
* Sun Sep 13 2026 John Wason <wason@wasontech.com> - 0.4.3-1
- Update to version 0.4.3

* Tue Jul 29 2025 John Wason <wason@wasontech.com> - 0.4.2-1
- Test RPM Build
