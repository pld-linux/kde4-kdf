#
%define		_state		stable
%define		orgname		kdf
%define		qtver		4.8.0

Summary:	K Desktop Environment - KDE Disk space GUI
Name:		kde4-kdf
Version:	4.12.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	70574c1b4e1fc4bb74e99c6943735b7d
URL:		http://www.kde.org/
BuildRequires:	kde4-kdebase-devel >= %{version}
Requires:	kde4-kdebase-workspace >= 4.11.4
Obsoletes:	kde4-kdeutils-kdf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program shows the disk usage of the mounted devices.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{orgname} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdf
%attr(755,root,root) %{_bindir}/kwikdisk
%attr(755,root,root) %{_libdir}/kde4/kcm_kdf.so
%{_datadir}/kde4/services/kcmdf.desktop
%{_datadir}/apps/kdf
%{_desktopdir}/kde4/kdf.desktop
%{_desktopdir}/kde4/kwikdisk.desktop
%{_iconsdir}/*/*/apps/kcmdf.*
%{_iconsdir}/*/*/apps/kdf.*
%{_iconsdir}/*/*/apps/kwikdisk.*
%{_docdir}/kde/HTML/en/kcontrol/blockdevices
