%define upstream_name    Test-XT
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Generate best practice author tests
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Remove)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Perl::MinimumVersion)
BuildRequires:	perl(Pod::Simple)
BuildRequires:	perl(Test::CPAN::Meta)
BuildRequires:	perl(Test::MinimumVersion)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Pod)
BuildArch:	noarch

%description
A number of Test modules have been written over the years to support
authors. Typically, these modules have standard short test scripts
documented in them that you can cut and paste into your distribution.

Unfortunately almost all of these cut-and-paste test scripts are wrong.

Either the test script runs during install time, or it runs with an
out-of-date version of the test module, or the author adds the test modules
as an (unnecesary) dependency at install time, or for automated testing.

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
%doc LICENSE README META.yml Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Jul 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.40.0-1mdv2011
+ Revision: 690331
- update to new version 0.04

* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.20.0-2
+ Revision: 658550
- rebuild for updated spec-helper

* Fri Jul 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2011.0
+ Revision: 553971
- import perl-Test-XT


* Fri Jul 16 2010 cpan2dist 0.02-1mdv
- initial mdv release, generated with cpan2dist
