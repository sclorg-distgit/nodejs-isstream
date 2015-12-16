%{?scl:%scl_package nodejs-isstream}
%{!?scl:%global package name %{name}}
%global npm_name isstream

%{?nodejs_find_provides_and_requires}

%{!?scl:%global enable_tests 0}
# tests are missing in npm tarball

Name:		%{?scl_prefix}nodejs-isstream
Version:	0.1.2
Release:	1.sc1%{?dist}
Summary:	Determine if an object is a Stream
Url:		https://github.com/rvagg/isstream
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	MIT

BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

BuildRequires:	%{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:	npm(core-util-is)
BuildRequires:	npm(inherits)
BuildRequires:	npm(isarray)
BuildRequires:	npm(string_decoder)
BuildRequires:	npm(tape)
%endif

%description
Determine if an object is a Stream

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json isstream.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
tar --xform 's/^package/readable-stream-1.0/' -zxf readable-stream-1.0.*.tgz && tar --xform 's/^package/readable-stream-1.1/' -zxf readable-stream-1.1.*.tgz && node test.js; rm -rf readable-stream-1.?/
%endif

%files
%{nodejs_sitelib}/isstream

%doc README.md LICENSE.md

%changelog
* Thu Jul 16 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.1.2-1
- Initial build
