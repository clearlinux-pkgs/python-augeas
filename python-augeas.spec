#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-augeas
Version  : 1.1.0
Release  : 29
URL      : https://files.pythonhosted.org/packages/af/cc/5064a3c25721cd863e6982b87f10fdd91d8bcc62b6f7f36f5231f20d6376/python-augeas-1.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/af/cc/5064a3c25721cd863e6982b87f10fdd91d8bcc62b6f7f36f5231f20d6376/python-augeas-1.1.0.tar.gz
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
%setup -q -n python-augeas-1.1.0
cd %{_builddir}/python-augeas-1.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1615275698
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-augeas
cp %{_builddir}/python-augeas-1.1.0/COPYING %{buildroot}/usr/share/package-licenses/python-augeas/01a6b4bf79aca9b556822601186afab86e8c4fbf
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-augeas/01a6b4bf79aca9b556822601186afab86e8c4fbf

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
