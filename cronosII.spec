Summary:	The GNOME Email Client
Summary(pl):	Klient poczty dla GNOME
Name:		cronosII
Version:	0.2.1
Release:	1
License:	GPL
Group:		Applications/Mail
Group(de):	Applikationen/Post
Group(pl):	Aplikacje/Poczta
Group(pt):	Aplicações/Correio Eletrônico
Source0:	ftp://cronosii.sourceforge.net/pub/cronosii/%{name}-%{version}.tar.bz2
URL:		http://cronosII.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	gettext-devel
BuildRequires:	glib-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gnome-print-devel >= 0.20.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6

%description
Cronos II is a powerful GNOME mail client that uses its own database
storage format to ensure the high performance it reachs.

%description -l fr
Cronos II est un puissant lecteur de mails pour GNOME. Il utilise son
propre format de stockage des mails afin d'avoir les hautes
performances qu'il est capable d'atteidre.

%description -l pl
Cronos II jest klientem poczty dla GNOME u¿ywaj±cym w³asnego formatu
bazy poczty maj±cego na celu zapewnienie wysokiej wydajno¶ci podczas
jej czytania.

%prep
%setup -q

%build
gettextize -c -f
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopdir=%{_applnkdir}/Network/Mail \
	Internetdir=%{_applnkdir}/Network/Mail 

gzip -9nf TODO README NEWS FEATURES AUTHORS ChangeLog

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_applnkdir}/*/*/*.desktop
%{_pixmapsdir}/*
%{_mandir}/man*/*
