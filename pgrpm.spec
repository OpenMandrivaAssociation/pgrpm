# $Id: pgrpm.spec 100595 2006-12-20 20:44:47Z nanardon $

%define _pg_pkglibdir %([ -f /usr/bin/pg_config ] && /usr/bin/pg_config --pkglibdir)
%define _pg_datadir %([ -f /usr/bin/pg_config ] && /usr/bin/pg_config --sharedir)

%define name pgrpm
%define version 0.1.9
%define release %mkrel 5

Summary: RPM binding for postgresql
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
# Thanks to rpm.org to break compatibilty in way
# they force us to make a patch, showing warnings
# would have been anough w/o forcing everyone to make
# patch
Patch0:  rpm-44-compat.patch
License: GPL
Group: Databases
Url: http://pgfoundry.org/projects/pgrpm/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: postgresql-devel < 8.5
BuildRequires: rpm-devel
%if %{?pgmodules_req:1}%{!?pgmodules_req:0}
%pgmodules_req
%endif

%description
This contribution to postgres provides functions and operators to allow
sorting and checking strings version like rpm does.

%prep
%setup -q
%patch0 -b .rpm44-compat

%build
make

cat > README.urpmi <<EOF
Remember to run %_pg_datadir/contrib/pgrpm.sql or
%_pg_datadir/contrib/pgrpm-update.sql to finalyze
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
%_pg_pkglibdir/*.so
%_pg_datadir/contrib/*
