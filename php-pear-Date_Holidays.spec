%include	/usr/lib/rpm/macros.php
%define		_class		Date
%define		_subclass	Holidays
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - driver based class to calculate holidays
Summary(pl.UTF-8):	%{_pearname} - klasa oparta na sterownikach do wyliczania świąt
Name:		php-pear-%{_pearname}
Version:	0.17.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	7063137ac130a086370086111d60ca2d
URL:		http://pear.php.net/package/Date_Holidays/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Date
Requires:	php-pear-PEAR-core >= 1:1.3.1
Requires:	php-pear-XML_Serializer
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'pear(Console/Getargs.*)'

%description
Date_Holidays helps you calculating the dates and titles of holidays
and other special celebrations. The calculation is driver-based so it
is easy to add new drivers that calculate a country's holidays. The
methods of the class can be used to get a holiday's date and title in
various languages.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa Date_Holidays pomaga przy wyliczaniu dat i nazw świąt oraz
innych specjalnych okazji. Obliczenia są oparte na sterownikach, więc
łatwo można dodać nowe sterowniki obliczające święta narodowe. Metody
klasy mogą być używane do uzyskania dat i nazw świąt w różnych
językach.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/data/%{_pearname}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Date_Holidays
