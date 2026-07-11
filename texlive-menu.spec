%global tl_name menu
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.994
Release:	%{tl_revision}.1
Summary:	Typesetting menus
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/menu
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/menu.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/menu.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/menu.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package defines command \menu which assists typesetting of a path
through a program's menu.

