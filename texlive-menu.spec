# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/menu
# catalog-date 2009-03-06 22:55:22 +0100
# catalog-license other-free
# catalog-version 0.994
Name:		texlive-menu
Version:	0.994
Release:	5
Summary:	Typesetting menus
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/menu
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/menu.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/menu.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/menu.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.994-2
+ Revision: 753853
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.994-1
+ Revision: 718992
- texlive-menu
- texlive-menu
- texlive-menu
- texlive-menu

