%define		status		alpha
%define		pearname	Date_Holidays
Summary:	%{pearname} - driver based class to calculate holidays
Summary(pl.UTF-8):	%{pearname} - klasa oparta na sterownikach do wyliczania świąt
Name:		php-pear-%{pearname}
Version:	0.21.8
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	1530a1a62a7f5d7a863d01740da5550c
URL:		http://pear.php.net/package/Date_Holidays/
BuildRequires:	php-pear-PEAR >= 1:1.6.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	php-pear
Requires:	php-pear-Date
Requires:	php-pear-PEAR-core >= 1:1.3.1
Requires:	php-pear-XML_Serializer
Suggests:	php-pear-Console_Getargs
Obsoletes:	php-pear-Date_Holidays-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_noautoreq_pear Console/Getargs.php

%description
Date_Holidays helps you calculating the dates and titles of holidays
and other special celebrations. The calculation is driver-based so it
is easy to add new drivers that calculate a country's holidays. The
methods of the class can be used to get a holiday's date and title in
various languages.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Klasa Date_Holidays pomaga przy wyliczaniu dat i nazw świąt oraz
innych specjalnych okazji. Obliczenia są oparte na sterownikach, więc
łatwo można dodać nowe sterowniki obliczające święta narodowe. Metody
klasy mogą być używane do uzyskania dat i nazw świąt w różnych
językach.

Ta klasa ma w PEAR status: %{status}.

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
%doc docs/%{pearname}/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Date/*.php
%{php_pear_dir}/Date/Holidays
%{php_pear_dir}/data/%{pearname}
