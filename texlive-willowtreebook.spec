Name:		texlive-willowtreebook
Version:	60638
Release:	1
Summary:	Easy basic book class, built on memoir
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/willowtreebook
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/willowtreebook.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/willowtreebook.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The willowtreebook class is a simple book class, which the
author uses for his lecture notes to be found on his web page
Benjamin McKay. It actually just selects options for the more
sophisticated memoir class.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/willowtreebook
%doc %{_texmfdistdir}/doc/latex/willowtreebook

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
