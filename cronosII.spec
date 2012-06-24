Summary:	The GNOME Email Client
Summary(pl.UTF-8):	Klient poczty dla GNOME
Name:		cronosII
Version:	0.2.2.23
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/cronosii/%{name}-%{version}.tar.bz2
# Source0-md5:	bf69cd713de0cba8d1da79d5e6687176
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-includes.patch
URL:		http://cronosII.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	gettext-devel
BuildRequires:	glib-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gnome-print-devel >= 0.28
BuildRequires:	gdk-pixbuf-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Cronos II is a powerful GNOME mail client that uses its own database
storage format to ensure the high performance it reaches.

%description -l fr.UTF-8
Cronos II est un puissant lecteur de mails pour GNOME. Il utilise son
propre format de stockage des mails afin d'avoir les hautes
performances qu'il est capable d'atteidre.

%description -l pl.UTF-8
Cronos II jest klientem poczty dla GNOME używającym własnego formatu
bazy poczty mającego na celu zapewnienie wysokiej wydajności podczas
jej czytania.

%prep
%setup -q
%patch0 -p1
%patch1

rm -f acinclude.m4 missing

%build
rm -f missing
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I %{_aclocaldir}/gnome
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopdir=%{_applnkdir}/Network/Mail \
	Internetdir=%{_applnkdir}/Network/Mail

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc TODO README NEWS FEATURES AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_applnkdir}/*/*/*.desktop
%{_pixmapsdir}/*
%{_mandir}/man*/*
