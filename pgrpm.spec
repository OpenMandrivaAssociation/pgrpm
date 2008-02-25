# $Id: pgrpm.spec 100595 2006-12-20 20:44:47Z nanardon $

%define name pgrpm
%define version 0.1.7
%define release %mkrel 3

Summary: RPM binding for postgresql
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Patch0:  pgrpm-null-ptr-depevr.patch
License: GPL
Group: Databases
Url: http://pgfoundry.org/projects/pgrpm/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: postgresql-devel
BuildRequires: rpm-devel
%if %{?pgmodules_req:1}%{!?pgmodules_req:0}
%pgmodules_req
%endif

%description
This contribution to postgres provides functions and operators to allow
sorting and checking strings version like rpm does.

%prep
%setup -q
%patch0 -p0 -b .null-ptr-dep

%build
make

cat > README.urpmi <<EOF
Remember to run %_datadir/pgsql/contrib/pgrpm.sql or
%_datadir/pgsql/contrib/pgrpm-update.sql to finalyze
installation into your postgresql server.
Something like:
  psql -U postgres template1 < FILE
should works.
EOF

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

rm -fr %buildroot%_datadir/doc/postgresql

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README*
%_libdir/pgsql/*.so
%_datadir/pgsql/contrib/*
