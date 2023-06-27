#
# Conditional build:
%bcond_without	tests	# testing
#
Summary:	6502/R65C02 disassembler
Summary(pl.UTF-8):	Disasembler dla procesorów 6502/R65C02
Name:		dxa
Version:	0.1.5
Release:	1
License:	GPL v2+
Group:		Development/Languages
Source0:	https://www.floodgap.com/retrotech/xa/dists/%{name}-%{version}.tar.gz
# Source0-md5:	6d69ae1772ed58de97b0180e480dfe0c
URL:		https://www.floodgap.com/retrotech/xa/#dxa
%{?with_tests:BuildRequires:	xa}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dxa is the semi-official disassembler for the xa package, a weakly
patched version of Marko Makela's d65 disassembler that generates
output similar to the de facto coding conventions used for xa.

%description -l en.UTF-8
dxa is the semi-official disassembler for the xa package, a weakly
patched version of Marko Mäkelä's d65 disassembler that generates
output similar to the de facto coding conventions used for xa.

%description -l pl.UTF-8
dxa to półoficjalny disasembler dla pakietu xa - słabo załatana wersja
disasemblera d65 (którego autorem jest Marko Mäkelä), generująca
wyjście podobne do konwencji kodowania używanej dla xa.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	LD="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} -Wall -Wmissing-prototypes" \
	LDFLAGS="%{rpmldflags}"

%{?with_tests:%{__make} -j1 test}

%install
rm -rf $RPM_BUILD_ROOT

install -D dxa $RPM_BUILD_ROOT%{_bindir}/dxa
install -Dp dxa.1 $RPM_BUILD_ROOT%{_mandir}/man1/dxa.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/dxa
%{_mandir}/man1/dxa.1*
