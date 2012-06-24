%include	/usr/lib/rpm/macros.php
%define		_class		Date
%define		_subclass	Holidays
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - driver based class to calculate holidays
Summary(pl):	%{_pearname} - klasa oparta na sterownikach do wyliczania �wi�t
Name:		php-pear-%{_pearname}
Version:	0.13.0
Release:	4
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	8b50ff11c6d01d8df95b13cbe40e5b40
URL:		http://pear.php.net/package/Date_Holidays/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-Date
Requires:	php-pear-PEAR >= 1:1.3.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Date_Holidays helps you calculating the dates and titles of
holidays and other special celebrations. The calculation is
driver-based so it is easy to add new drivers that calculate
a country's holidays. The methods of the class can be used
to get a holiday's date and title in various languages.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa Date_Holidays pomaga przy wyliczaniu dat i nazw �wi�t oraz
innych specjalnych okazji. Obliczenia s� oparte na sterownikach, wi�c
�atwo mo�na doda� nowe sterowniki obliczaj�ce �wi�ta narodowe. Metody
klasy mog� by� u�ywane do uzyskania dat i nazw �wi�t w r�nych
j�zykach.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}

%{php_pear_dir}/data/%{_pearname}
