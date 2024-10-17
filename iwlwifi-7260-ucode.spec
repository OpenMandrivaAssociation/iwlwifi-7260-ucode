Summary:	Intel Wireless 7260 microcode
Name:		iwlwifi-7260-ucode
Version:	25.228.9.0
Release:	1
Source0:	http://www.intellinuxwireless.org/iwlwifi/downloads/%{name}-%{version}.tgz
License:	Proprietary
Group:		System/Kernel and hardware
Url:		https://intellinuxwireless.org/
BuildArch: noarch

%description
The file iwlwifi-7260-*.ucode provided in this package is required to be
present on your system in order for the Intel Wireless 7260 Network
Connection Adapter driver for Linux (iwlagn) to be able to operate on
your system.

%prep
%setup -q

%build

%install
install -d %{buildroot}/lib/firmware
install -m644 *.ucode %{buildroot}/lib/firmware/


%files
%doc LICENSE.* README.*
/lib/firmware/*.ucode
