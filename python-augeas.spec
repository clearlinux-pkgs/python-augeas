#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-augeas
Version  : 0.5.0
Release  : 7
URL      : http://pypi.debian.net/python-augeas/python-augeas-0.5.0.tar.gz
Source0  : http://pypi.debian.net/python-augeas/python-augeas-0.5.0.tar.gz
Summary  : Python bindings for Augeas
Group    : Development/Tools
License  : LGPL-2.1 LGPL-2.1+
Requires: python-augeas-python3
Requires: python-augeas-python
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools

%description
python-augeas is a set of Python bindings around augeas.

%package python
Summary: python components for the python-augeas package.
Group: Default
Requires: python-augeas-python3

%description python
python components for the python-augeas package.


%package python3
Summary: python3 components for the python-augeas package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-augeas package.


%prep
%setup -q -n python-augeas-0.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1528563648
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
