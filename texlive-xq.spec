Name:		texlive-xq
Version:	0.4
Release:	1
Summary:	Support for writing about xiangqi
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/xq
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xq.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xq.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is for writing about xiangqi or chinese chess. You
can write games or parts of games and show diagrams with
special positions.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/*/*/xq
%{_texmfdistdir}/tex/latex/xq/xq.sty
%doc %{_texmfdistdir}/doc/fonts/xq

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
