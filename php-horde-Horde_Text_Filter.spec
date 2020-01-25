# TODO
# - system locale dir
%define		status		stable
%define		pearname	Horde_Text_Filter
Summary:	%{pearname} - Horde Text Filter API
Name:		php-horde-Horde_Text_Filter
Version:	1.1.5
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	2bc8f4ec6d91d441b4e2d24d4e788011
URL:		https://github.com/horde/horde/tree/master/framework/Text_Filter/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_Exception < 2.0.0
Requires:	php-horde-Horde_Util < 2.0.0
Requires:	php-pear >= 4:1.3.6-2
Suggests:	php-horde-Horde_Text_Filter_Csstidy
Suggests:	php-horde-Horde_Text_Flowed
Suggests:	php-horde-Horde_Translation
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	 pear(Horde/Text/Filter/Csstidy.*) pear(Horde/Text/Flowed.*) pear(Horde/Translation.*)

%description
The Horde_Text_Filter library provides common methods for fitering and
converting text.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc optional-packages.txt
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde/Text/Filter.php
%{php_pear_dir}/Horde/Text/Filter
%{php_pear_dir}/data/Horde_Text_Filter
