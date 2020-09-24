#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-augeas
Version  : 1.0.3
Release  : 23
URL      : https://files.pythonhosted.org/packages/b4/d7/62d335d9df28e2f78207dcd12bbbcee89a7b5ba6d247feaddc9d04f27e1e/python-augeas-1.0.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/b4/d7/62d335d9df28e2f78207dcd12bbbcee89a7b5ba6d247feaddc9d04f27e1e/python-augeas-1.0.3.tar.gz
Summary  : Python bindings for Augeas
Group    : Development/Tools
License  : LGPL-2.1 LGPL-2.1+
Requires: python-augeas-license = %{version}-%{release}
Requires: python-augeas-python = %{version}-%{release}
Requires: python-augeas-python3 = %{version}-%{release}
Requires: cffi
BuildRequires : augeas-dev
BuildRequires : buildreq-distutils3
BuildRequires : cffi

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
Requires: python-augeas-python3 = %{version}-%{release}

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
cd %{_builddir}/python-augeas-1.0.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583539769
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-augeas
cp %{_builddir}/python-augeas-1.0.3/COPYING %{buildroot}/usr/share/package-licenses/python-augeas/0bf81afbc585fd8fa3a9267d33498831f5a5c9c2
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-augeas/0bf81afbc585fd8fa3a9267d33498831f5a5c9c2

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
