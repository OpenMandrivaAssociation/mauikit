%define _disable_ld_no_undefined 1
%define _disable_lto 1

#define snapshot 20200312
%define libname %mklibname MauiKit
%define devname %mklibname -d MauiKit

Name:		mauikit
Version:	1.2.0
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	Library for developing MAUI applications
Url:		http://mauikit.org/
Source0:	https://invent.kde.org/maui/mauikit/-/archive/v%{version}/mauikit-v%{version}.tar.bz2
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
BuildRequires:	qt5-qtgraphicaleffects
BuildRequires:	qt5-qtdeclarative
BuildRequires:	qt5-qtquickcontrols2
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

%description -n %{devname}
Development files for MauiKit

MauiKit is a set of utilities and "templated" controls based on Kirigami and
QCC2 that follow the ongoing work on the Maui HIG.

It lets you quickly create a Maui application and access utilities and
widgets shared amoing the other Maui apps.

%prep
%autosetup -p1 -n %{name}-v%{version}
%cmake_kde5 -G Ninja

%build
export CC=gcc
export CXX=g++
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_datadir}/maui
%{_libdir}/qt5/qml/org/kde/appletdecoration
%{_libdir}/qt5/qml/org/kde/mauikit
%{_libdir}/qt5/qml/QtQuick/Controls.2/maui-style

%files -n %{libname}
%{_libdir}/libMauiKit.so

%files -n %{devname}
%{_includedir}/MauiKit
%{_libdir}/cmake/MauiKit
