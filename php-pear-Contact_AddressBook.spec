%include	/usr/lib/rpm/macros.php
%define		_class		Contact
%define		_subclass	AddressBook
%define		_status		devel
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Address book export-import class
Summary(pl):	%{_pearname} - Klasa do importowania/eksportowania ksi±¿ki adresowej
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}dev1.tgz
# Source0-md5:	7cb8111400f3884a0e854a52dfdc1af7
URL:		http://pear.php.net/package/Contact_AddressBook/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package provides export-import address book mechanism.
Contact_AddressBook refers to needed structure, convert the various
address book structure format into it, then you can easily store it
into file, database or another storage media.

In PEAR status of this package is: %{_status}.

%description -l pl
Ten pakiet dostarcza mechanizm exportowania/importowania ksi±¿ki
adresowej. Contact_AddressBook odwo³uje siê do wymaganej struktury,
konwertuje do jej formatu ró¿ne formaty ksi±¿ek adresowych, które
nastêpnie mo¿na ³atwo zapisaæ do pliku, bazy danych lub na inny
no¶nik.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}dev1/%{_class}/%{_subclass}.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/
install %{_pearname}-%{version}dev1/%{_class}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}dev1/{README.txt,examples,gateaway,definitions}
%{php_pear_dir}/%{_class}/%{_subclass}.php
%{php_pear_dir}/%{_class}/%{_subclass}
