%define _disable_ld_no_undefined 1

#define snapshot 20220107
%define libname %mklibname MauiKit
%define devname %mklibname -d MauiKit

Name:		mauikit
Version:	4.0.0
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	Library for developing MAUI applications
Url:		https://mauikit.org/
Source0:	https://invent.kde.org/maui/mauikit/-/archive/%{?snapshot:master/mauikit-master.tar.bz2#/mauikit-%{snapshot}.tar.bz2}%{!?snapshot:v%{version}/mauikit-v%{version}.tar.bz2}
#Patch1:		mauikit-set-soversion.patch

License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6ConfigWidgets)
#BuildRequires:	cmake(KDF6Dcoration2)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Declarative)
#BuildRequires:	cmake(KF6Plasma)
#BuildRequires:	cmake(KF6PlasmaQuick)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(Git)
BuildRequires:	cmake(KF6SyntaxHighlighting)
BuildRequires:	cmake(KF6Attica)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6WebEngineCore)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-atom)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xcb-icccm)
#BuildRequires:	qt5-qtgraphicaleffects
#BuildRequires:	qt5-qtdeclarative
#BuildRequires:	qt5-qtquickcontrols2

BuildRequires:  cmake(MauiMan4)

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
