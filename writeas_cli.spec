%global         github_owner writeas
%global         github_name  writeas-cli
%global         github_commit 99e1973652c719ee59c77c76946af965c7e60e2b
%global         debug_package %{nil}
%define         build_timestamp %(date +"%Y%m%d")

Name:           %{github_name}
Version:        %{build_timestamp}
Release:        %{github_commit}
Summary:        Command line utility for publishing to Write.as and any other WriteFreely instance.
License:        GPL-3.0-only

URL:            https://github.com/%{github_owner}/%{github_name}
Source0:        https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_commit}.tar.gz

BuildRequires: golang-bin
BuildRequires: git

%description
Command line utility for publishing to Write.as and any other WriteFreely instance.

%prep
%setup -n %{name}-%{github_commit}

%build
cd ./cmd/writeas && go build .
cd ../wf && go build .

%install
install -p -D -m 755 ./cmd/writeas/writeas %{buildroot}%{_bindir}/writeas
install -p -D -m 755 ./cmd/wf/wf %{buildroot}%{_bindir}/wf

%files
%license LICENSE
%doc README.md
%{_bindir}/writeas
%{_bindir}/wf

%changelog
* Sun Nov 8 2020 Thomas Vassilian <tvassili@redhat.com> - 1-0
- initial build for fedora
