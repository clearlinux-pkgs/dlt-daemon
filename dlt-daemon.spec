#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dlt-daemon
Version  : 2.18.0
Release  : 1
URL      : https://github.com/avinash-palleti/dlt-daemon/archive/v.2.18.0.tar.gz
Source0  : https://github.com/avinash-palleti/dlt-daemon/archive/v.2.18.0.tar.gz
Summary  : Diagnostic Log and Trace
Group    : Development/Tools
License  : BSD-3-Clause MIT MPL-2.0
Requires: dlt-daemon-bin
Requires: dlt-daemon-lib
Requires: dlt-daemon-data
Requires: dlt-daemon-license
Requires: dlt-daemon-man
BuildRequires : buildreq-cmake
BuildRequires : doxygen
BuildRequires : glibc-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(dbus-1)
BuildRequires : python3
BuildRequires : zlib-dev

%description
To build use cmake with -DWITH_DLT_COREDUMPHANDLER=ON -DTARGET_CPU_NAME={i686|x86_64}

%package bin
Summary: bin components for the dlt-daemon package.
Group: Binaries
Requires: dlt-daemon-data = %{version}-%{release}
Requires: dlt-daemon-license = %{version}-%{release}
Requires: dlt-daemon-man = %{version}-%{release}

%description bin
bin components for the dlt-daemon package.


%package data
Summary: data components for the dlt-daemon package.
Group: Data

%description data
data components for the dlt-daemon package.


%package dev
Summary: dev components for the dlt-daemon package.
Group: Development
Requires: dlt-daemon-lib = %{version}-%{release}
Requires: dlt-daemon-bin = %{version}-%{release}
Requires: dlt-daemon-data = %{version}-%{release}
Provides: dlt-daemon-devel = %{version}-%{release}

%description dev
dev components for the dlt-daemon package.


%package lib
Summary: lib components for the dlt-daemon package.
Group: Libraries
Requires: dlt-daemon-data = %{version}-%{release}
Requires: dlt-daemon-license = %{version}-%{release}

%description lib
lib components for the dlt-daemon package.


%package license
Summary: license components for the dlt-daemon package.
Group: Default

%description license
license components for the dlt-daemon package.


%package man
Summary: man components for the dlt-daemon package.
Group: Default

%description man
man components for the dlt-daemon package.


%prep
%setup -q -n dlt-daemon-v.2.18.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1538140650
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1538140650
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/dlt-daemon
cp COPYING %{buildroot}/usr/share/doc/dlt-daemon/COPYING
cp LICENSE %{buildroot}/usr/share/doc/dlt-daemon/LICENSE
cp gtest-1.7.0/LICENSE %{buildroot}/usr/share/doc/dlt-daemon/gtest-1.7.0_LICENSE
cp src/core_dump_handler/cityhash_c/COPYING %{buildroot}/usr/share/doc/dlt-daemon/src_core_dump_handler_cityhash_c_COPYING
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dlt-adaptor-stdin
/usr/bin/dlt-adaptor-udp
/usr/bin/dlt-control
/usr/bin/dlt-convert
/usr/bin/dlt-daemon
/usr/bin/dlt-dbus
/usr/bin/dlt-example-filetransfer
/usr/bin/dlt-example-user
/usr/bin/dlt-example-user-common-api
/usr/bin/dlt-example-user-func
/usr/bin/dlt-kpi
/usr/bin/dlt-logstorage-ctrl
/usr/bin/dlt-passive-node-ctrl
/usr/bin/dlt-receive
/usr/bin/dlt-sortbytimestamp
/usr/bin/dlt-system
/usr/bin/dlt-test-client
/usr/bin/dlt-test-filetransfer
/usr/bin/dlt-test-fork-handler
/usr/bin/dlt-test-init-free
/usr/bin/dlt-test-multi-process
/usr/bin/dlt-test-multi-process-client
/usr/bin/dlt-test-stress
/usr/bin/dlt-test-stress-client
/usr/bin/dlt-test-stress-user
/usr/bin/dlt-test-user

%files data
%defattr(-,root,root,-)
/usr/share/dlt-filetransfer/dlt-test-filetransfer-file
/usr/share/dlt-filetransfer/dlt-test-filetransfer-image.png

%files dev
%defattr(-,root,root,-)
/usr/include/dlt/dlt.h
/usr/include/dlt/dlt_client.h
/usr/include/dlt/dlt_common.h
/usr/include/dlt/dlt_common_api.h
/usr/include/dlt/dlt_filetransfer.h
/usr/include/dlt/dlt_offline_trace.h
/usr/include/dlt/dlt_protocol.h
/usr/include/dlt/dlt_shm.h
/usr/include/dlt/dlt_types.h
/usr/include/dlt/dlt_user.h
/usr/include/dlt/dlt_user_macros.h
/usr/include/dlt/dlt_version.h
/usr/lib64/libdlt.so
/usr/lib64/pkgconfig/automotive-dlt.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libdlt.so.2
/usr/lib64/libdlt.so.2.17.0

%files license
%defattr(0644,root,root,0755)
/usr/share/doc/dlt-daemon/COPYING
/usr/share/doc/dlt-daemon/LICENSE
/usr/share/doc/dlt-daemon/gtest-1.7.0_LICENSE
/usr/share/doc/dlt-daemon/src_core_dump_handler_cityhash_c_COPYING

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/dlt-convert.1.gz
/usr/share/man/man1/dlt-daemon.1.gz
/usr/share/man/man1/dlt-logstorage-ctrl.1.gz
/usr/share/man/man1/dlt-passive-node-ctrl.1.gz
/usr/share/man/man1/dlt-receive.1.gz
/usr/share/man/man1/dlt-sortbytimestamp.1.gz
/usr/share/man/man1/dlt-system.1.gz
/usr/share/man/man5/dlt-system.conf.5.gz
/usr/share/man/man5/dlt.conf.5.gz
