Name:		texlive-menu
Version:	15878
Release:	2
Summary:	Typesetting menus
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/menu
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/menu.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/menu.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/menu.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines command \menu which assists typesetting of
a path through a program's menu.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/menu/menu.sty
%doc %{_texmfdistdir}/doc/latex/menu/README
%doc %{_texmfdistdir}/doc/latex/menu/menu.pdf
#- source
%doc %{_texmfdistdir}/source/latex/menu/menu.dtx
%doc %{_texmfdistdir}/source/latex/menu/menu.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
