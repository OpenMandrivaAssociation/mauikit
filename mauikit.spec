%define snapshot 20200312
%define libname %mklibname MauiKit
%define devname %mklibname -d MauiKit

Name:		mauikit
Version:	0.0
Release:	0.%{snapshot}.1
Summary:	Library for developing MAUI applications
Url:		http://mauikit.org/
# git://anongit.kde.org/mauikit
Source0:	mauikit-%{snapshot}.tar.zst
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5SyntaxHighlighting)
BuildRequires:	cmake(KF5Attica)
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
%autosetup -p1 -n %{name}-%{snapshot}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_libdir}/qt5/qml/org/kde/mauikit
%{_libdir}/qt5/qml/QtQuick/Controls.2/maui-style

%files -n %{libname}
%{_libdir}/libMauiKit.so

%files -n %{devname}
%{_includedir}/MauiKit
%{_libdir}/cmake/MauiKit
