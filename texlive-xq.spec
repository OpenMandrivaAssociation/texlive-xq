# revision 15878
# category Package
# catalog-ctan /fonts/xq
# catalog-date 2007-03-13 09:23:19 +0100
# catalog-license lppl
# catalog-version 0.3
Name:		texlive-xq
Version:	0.3
Release:	2
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
%{_texmfdistdir}/fonts/source/public/xq/xqaddsignsbase.mf
%{_texmfdistdir}/fonts/source/public/xq/xqaddsignslarge.mf
%{_texmfdistdir}/fonts/source/public/xq/xqaddsignsnormal.mf
%{_texmfdistdir}/fonts/source/public/xq/xqbase.mf
%{_texmfdistdir}/fonts/source/public/xq/xqhints.mf
%{_texmfdistdir}/fonts/source/public/xq/xqlarge.mf
%{_texmfdistdir}/fonts/source/public/xq/xqnormal.mf
%{_texmfdistdir}/fonts/source/public/xq/xqwestbase.mf
%{_texmfdistdir}/fonts/source/public/xq/xqwestlarge.mf
%{_texmfdistdir}/fonts/source/public/xq/xqwestnormal.mf
%{_texmfdistdir}/fonts/tfm/public/xq/xqlarge.tfm
%{_texmfdistdir}/fonts/tfm/public/xq/xqnormal.tfm
%{_texmfdistdir}/tex/latex/xq/xq.sty
%doc %{_texmfdistdir}/doc/fonts/xq/README
%doc %{_texmfdistdir}/doc/fonts/xq/xqexample.pdf
%doc %{_texmfdistdir}/doc/fonts/xq/xqexample.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
