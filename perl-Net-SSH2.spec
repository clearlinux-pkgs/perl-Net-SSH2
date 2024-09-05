#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v18
# autospec commit: eaa4f711da30
#
Name     : perl-Net-SSH2
Version  : 0.74
Release  : 18
URL      : https://cpan.metacpan.org/authors/id/R/RK/RKITOVER/Net-SSH2-0.74.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RK/RKITOVER/Net-SSH2-0.74.tar.gz
Summary  : 'Support for the SSH 2 protocol via libssh2.'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Net-SSH2-perl = %{version}-%{release}
Requires: libssh2
BuildRequires : buildreq-cpan
BuildRequires : pkgconfig(libssh2)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
=pod
=head1 NAME
Net::SSH2 - Support for the SSH 2 protocol via libssh2.
=head1 SYNOPSIS

%package dev
Summary: dev components for the perl-Net-SSH2 package.
Group: Development
Provides: perl-Net-SSH2-devel = %{version}-%{release}
Requires: perl-Net-SSH2 = %{version}-%{release}

%description dev
dev components for the perl-Net-SSH2 package.


%package perl
Summary: perl components for the perl-Net-SSH2 package.
Group: Default
Requires: perl-Net-SSH2 = %{version}-%{release}

%description perl
perl components for the perl-Net-SSH2 package.


%prep
%setup -q -n Net-SSH2-0.74
cd %{_builddir}/Net-SSH2-0.74

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Net::SSH2.3
/usr/share/man/man3/Net::SSH2::Channel.3
/usr/share/man/man3/Net::SSH2::Dir.3
/usr/share/man/man3/Net::SSH2::File.3
/usr/share/man/man3/Net::SSH2::KnownHosts.3
/usr/share/man/man3/Net::SSH2::Listener.3
/usr/share/man/man3/Net::SSH2::PublicKey.3
/usr/share/man/man3/Net::SSH2::SFTP.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
