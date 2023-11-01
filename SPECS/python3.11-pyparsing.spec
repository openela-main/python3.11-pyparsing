%global __python3 /usr/bin/python3.11
%global python3_pkgversion 3.11

%global srcname pyparsing

%global python_wheelname %{srcname}-%{version}-py3-none-any.whl

# When bootstraping we don't have pytest yet
%bcond_without tests


Summary:        Python package with an object-oriented approach to text processing
Name:           python%{python3_pkgversion}-pyparsing
Version:        3.0.7
Release:        3%{?dist}

License:        MIT
URL:            https://github.com/pyparsing/pyparsing
Source0:        https://github.com/%{srcname}/%{srcname}/archive/%{srcname}_%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-rpm-macros
BuildRequires:  python%{python3_pkgversion}-setuptools

%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pytest
%endif

BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-wheel

%description
pyparsing is a module that can be used to easily and directly configure syntax
definitions for any number of text parsing applications.


%prep
%autosetup -p1 -n %{srcname}-%{srcname}_%{version}


%build
%py3_build_wheel


%install
%py3_install_wheel %{python_wheelname}


%if %{with tests}
%check
# Ignore the tests that require the missing railroad dependency
%pytest -v --ignore=tests/test_diagram.py -k "not testEmptyExpressionsAreHandledProperly"
%endif


%files -n python%{python3_pkgversion}-pyparsing
%license LICENSE
%doc CHANGES README.rst
%{python3_sitelib}/pyparsing/
%{python3_sitelib}/pyparsing-%{version}.dist-info/

%changelog
* Wed Feb 01 2023 Charalampos Stratakis <cstratak@redhat.com> - 3.0.7-3
- Explicitly require the python3.11-rpm-macros

* Wed Feb 01 2023 Charalampos Stratakis <cstratak@redhat.com> - 3.0.7-2
- Enable tests

* Fri Nov 25 2022 Charalampos Stratakis <cstratak@redhat.com> - 3.0.7-1
- Initial package
- Fedora contributions by:
      Alan Pevec <alan.pevec@redhat.com>
      Bill Nottingham <notting@fedoraproject.org>
      Charalampos Stratakis <cstratak@redhat.com>
      Dan Horák <dan@danny.cz>
      David King <amigadave@amigadave.com>
      David Malcolm <dmalcolm@redhat.com>
      Dennis Gilmore <dennis@ausil.us>
      Ignacio Vazquez-Abrams <ivazquez@fedoraproject.org>
      Iryna Shcherbina <shcherbina.iryna@gmail.com>
      Jesse Keating <jkeating@fedoraproject.org>
      José Abílio Oliveira Matos <jamatos@fedoraproject.org>
      José Matos <jamatos@fedoraproject.org>
      Lumir Balhar <lbalhar@redhat.com>
      Miro Hrončok <miro@hroncok.cz>
      Petr Viktorin <pviktori@redhat.com>
      Robert Kuska <rkuska@redhat.com>
      Slavek Kabrda <bkabrda@redhat.com>
      Terje Røsten <terje.rosten@ntnu.no>
      Thomas Spura <thomas.spura@gmail.com>
      Tomáš Hrnčiar <thrnciar@redhat.com>
      Ville Skyttä <scop@fedoraproject.org>
      yatin <ykarel@redhat.com>
      Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl>
