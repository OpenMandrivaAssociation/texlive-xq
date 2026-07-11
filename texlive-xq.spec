%global tl_name xq
%global tl_revision 78101

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.4
Release:	%{tl_revision}.1
Summary:	Support for writing about xiangqi
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/xq
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xq.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xq.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is for writing about xiangqi or chinese chess. You can write
games or parts of games and show diagrams with special positions.

