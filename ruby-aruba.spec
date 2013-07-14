#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	aruba
Summary:	CLI Steps for Cucumber, hand-crafted for you in Aruba
Name:		rubygem-%{pkgname}
Version:	0.5.2
Release:	1
Group:		Development/Languages
# aruba itself is MIT
# icons in templates/images are CC-BY
# jquery.js itself is MIT or GPLv2
# jquery.js includes sizzle.js, which is MIT or BSD or GPLv2
License:	MIT and CC-BY and (MIT or GPLv2) and (MIT or BSD or GPLv2)
Source0:	http://rubygems.org/gems/%{pkgname}-%{version}.gem
# Source0-md5:	e048f42c74d41f6587bfdec83bec7a31
URL:		http://github.com/cucumber/aruba
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-bcat >= 0.6.1
BuildRequires:	ruby-kramdown < 1
BuildRequires:	ruby-kramdown >= 0.14
BuildRequires:	ruby-rake >= 0.9.2
BuildRequires:	ruby-rspec >= 2.7.0
%endif
# Doesn't work with ffi 1.0.10, see https://github.com/cucumber/aruba/issues/114
BuildConflicts:	ruby-ffi = 1.0.10
# used in one of the features
BuildRequires:	bc
Requires:	ruby-childprocess < 0.4
Requires:	ruby-childprocess >= 0.3.6
Requires:	ruby-cucumber >= 1.1.1
Requires:	ruby-rspec-expectations >= 2.7.0
Conflicts:	ruby-ffi = 1.0.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Aruba is Cucumber extension for Command line applications written in
any programming language.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%if %{with tests}
cucumber
rspec spec
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md History.md LICENSE
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
