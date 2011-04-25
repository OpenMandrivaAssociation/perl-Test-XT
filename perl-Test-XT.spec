%define upstream_name    Test-XT
%define upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Generate best practice author tests
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Remove)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Perl::MinimumVersion)
BuildRequires: perl(Pod::Simple)
BuildRequires: perl(Test::CPAN::Meta)
BuildRequires: perl(Test::MinimumVersion)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc LICENSE README META.yml Changes
%{_mandir}/man3/*
%perl_vendorlib/*


