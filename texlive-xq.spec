# revision 15878
# category Package
# catalog-ctan /fonts/xq
# catalog-date 2007-03-13 09:23:19 +0100
# catalog-license lppl
# catalog-version 0.3
Name:		texlive-xq
Version:	0.3
Release:	1
Summary:	Support for writing about xiangqi
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/xq
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xq.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xq.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package is for writing about xiangqi or chinese chess. You
can write games or parts of games and show diagrams with
special positions.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
