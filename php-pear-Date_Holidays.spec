%include	/usr/lib/rpm/macros.php
%define		_class		Date
%define		_subclass	Holidays
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - driver based class to calculate holidays
Summary(pl):	%{_pearname} - klasa oparta na sterownikach do wyliczania ¶wi±t
Name:		php-pear-%{_pearname}
Version:	0.13.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	8b50ff11c6d01d8df95b13cbe40e5b40
URL:		http://pear.php.net/package/Date_Holidays/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
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
Klasa Date_Holidays pomaga przy wyliczaniu dat i nazw ¶wi±t oraz
innych specjalnych okazji. Obliczenia s± oparte na sterownikach, wiêc
³atwo mo¿na dodaæ nowe sterowniki obliczaj±ce ¶wiêta narodowe. Metody
klasy mog± byæ u¿ywane do uzyskania dat i nazw ¶wi±t w ró¿nych
jêzykach.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%build
cd %{_pearname}-%{version}/examples
cat addingTranslations.php | sed 's,/var/lib/pear/data/Date_Holidays,%{php_pear_dir}/%{_class}/%{_subclass},' > a
mv -f a addingTranslations.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/{Driver,lang/{Christian,Germany,UNO}}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_subclass}/Driver/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Driver
install %{_pearname}-%{version}/lang/Christian/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/lang/Christian
install %{_pearname}-%{version}/lang/Germany/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/lang/Germany
install %{_pearname}-%{version}/lang/UNO/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/lang/UNO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/examples
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
