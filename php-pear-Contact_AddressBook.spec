%include	/usr/lib/rpm/macros.php
%define		_class		Contact
%define		_subclass	AddressBook
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Address book export-import class
Summary(pl.UTF-8):	%{_pearname} - Klasa do importowania/eksportowania książki adresowej
Name:		php-pear-%{_pearname}
Version:	0.5.0
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	9834f0a60102160a7ea983441e277734
URL:		http://pear.php.net/package/Contact_AddressBook/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear >= 4:1.0-7
Requires:	php-pear-File >= 1.2.1
Requires:	php-pear-Net_UserAgent_Detect >= 2.0.1
Requires:	php-pear-PEAR-core >= 1:1.2.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package provides export-import address book mechanism.
Contact_AddressBook refers to needed structure, convert the various
address book structure format into it, then you can easily store it
into file, database or another storage media.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten pakiet dostarcza mechanizm exportowania/importowania książki
adresowej. Contact_AddressBook odwołuje się do wymaganej struktury,
konwertuje do jej formatu różne formaty książek adresowych, które
następnie można łatwo zapisać do pliku, bazy danych lub na inny
nośnik.

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
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/%{_subclass}.php
%{php_pear_dir}/%{_class}/%{_subclass}

%{php_pear_dir}/data/%{_pearname}
