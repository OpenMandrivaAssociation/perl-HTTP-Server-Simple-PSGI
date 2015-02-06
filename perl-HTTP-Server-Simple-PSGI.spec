%define upstream_name    HTTP-Server-Simple-PSGI
%define upstream_version 0.16

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	PSGI handler for HTTP::Server::Simple
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/HTTP/HTTP-Server-Simple-PSGI-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(HTTP::Server::Simple)
BuildArch:	noarch

%description
HTTP::Server::Simple::PSGI is a HTTP::Server::Simple based HTTP server that
can run PSGI applications. This module only depends on the
HTTP::Server::Simple manpage, which itself doesn't depend on any non-core
modules so it's best to be used as an embedded web server.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.140.0-3mdv2011.0
+ Revision: 657779
- rebuild for updated spec-helper
- rebuild for updated spec-helper

* Sat Oct 16 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.140.0-1mdv2011.0
+ Revision: 586066
- import perl-HTTP-Server-Simple-PSGI


