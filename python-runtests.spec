# Created by pyp2rpm-3.3.2
%global pypi_name runtests

Name:           python-%{pypi_name}
Version:        0.0.27
Release:        1%{?dist}
Summary:        Simple testing of fresh package builds using pytest, with optional mpi4py support

License:        BSD-2-Clause
URL:            http://github.com/rainwoodman/runtests
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(coverage)
BuildRequires:  python3dist(mpi4py)
BuildRequires:  python3dist(mpi4py)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)

%description


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(coverage)
Requires:       python3dist(mpi4py)
Requires:       python3dist(mpi4py)
Requires:       python3dist(pytest)
%description -n python3-%{pypi_name}



%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Mon Mar 25 2019 Mike DePaulo <mikedep333@redhat.com> - 0.0.27-1
- Initial package.