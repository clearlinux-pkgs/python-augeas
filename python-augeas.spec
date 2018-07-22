#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-augeas
Version  : 1.0.3
Release  : 14
URL      : https://files.pythonhosted.org/packages/b4/d7/62d335d9df28e2f78207dcd12bbbcee89a7b5ba6d247feaddc9d04f27e1e/python-augeas-1.0.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/b4/d7/62d335d9df28e2f78207dcd12bbbcee89a7b5ba6d247feaddc9d04f27e1e/python-augeas-1.0.3.tar.gz
Summary  : Python bindings for Augeas
Group    : Development/Tools
License  : LGPL-2.1 LGPL-2.1+
Requires: python-augeas-python3
Requires: python-augeas-license
Requires: python-augeas-python
Requires: cffi
BuildRequires : augeas-dev
BuildRequires : buildreq-distutils3
BuildRequires : cffi
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
python-augeas is a set of Python bindings around augeas.

%package license
Summary: license components for the python-augeas package.
Group: Default

%description license
license components for the python-augeas package.


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
%setup -q -n python-augeas-1.0.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532292194
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/python-augeas
cp COPYING %{buildroot}/usr/share/doc/python-augeas/COPYING
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/python-augeas/COPYING

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
