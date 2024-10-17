%define _disable_ld_no_undefined 1

#define snapshot 20220107
%define libname %mklibname MauiKit
%define devname %mklibname -d MauiKit

Name:		mauikit
Version:	3.0.2
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	Library for developing MAUI applications
Url:		https://mauikit.org/
Source0:	https://invent.kde.org/maui/mauikit/-/archive/%{?snapshot:master/mauikit-master.tar.bz2#/mauikit-%{snapshot}.tar.bz2}%{!?snapshot:v%{version}/mauikit-v%{version}.tar.bz2}
Patch1:		mauikit-set-soversion.patch

License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KDecoration2)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5PlasmaQuick)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(Git)
BuildRequires:	cmake(KF5SyntaxHighlighting)
BuildRequires:	cmake(KF5Attica)
BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5WebEngine)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-atom)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:	qt5-qtgraphicaleffects
BuildRequires:	qt5-qtdeclarative
BuildRequires:	qt5-qtquickcontrols2

BuildRequires:  cmake(MauiMan3)

Requires:	%{libname} = %{EVRD}

%description
Library for developing MAUI applications

MauiKit is a set of utilities and "templated" controls based on Kirigami and
QCC2 that follow the ongoing work on the Maui HIG.

It lets you quickly create a Maui application and access utilities and
widgets shared amoing the other Maui apps.

%package -n %{libname}
Summary:	Library files for MauiKit
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libname}
Library files for MauiKit

MauiKit is a set of utilities and "templated" controls based on Kirigami and
QCC2 that follow the ongoing work on the Maui HIG.

It lets you quickly create a Maui application and access utilities and
widgets shared amoing the other Maui apps.

%package -n %{devname}
Summary:	Development files for MauiKit
Group:		Development/KDE and Qt
Requires:	%{name} = %{EVRD}
# This can't be a hard dependency -- mauikit-filebrowsing
# requires mauikit to build
Suggests:	cmake(MauiKitFileBrowsing)

%description -n %{devname}
Development files for MauiKit

MauiKit is a set of utilities and "templated" controls based on Kirigami and
QCC2 that follow the ongoing work on the Maui HIG.

It lets you quickly create a Maui application and access utilities and
widgets shared amoing the other Maui apps.

%prep
%autosetup -p1 -n %{name}-%{?snapshot:master}%{!?snapshot:v%{version}}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %{name}

%files -f %{name}.lang
%{_libdir}/qt5/qml/org/mauikit/*
%{_libdir}/qt5/qml/QtQuick/Controls.2/maui-style
%{_datadir}/org.mauikit.controls

%files -n %{libname}
%{_libdir}/libMauiKit3.so.*

%files -n %{devname}
%{_includedir}/MauiKit3
%{_libdir}/cmake/MauiKit3
%{_libdir}/libMauiKit3.so
