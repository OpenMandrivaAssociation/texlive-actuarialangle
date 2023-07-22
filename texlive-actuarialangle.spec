Name:		texlive-actuarialangle
Version:	67201
Release:	1
Summary:	Symbol for use in "present value" statements of an annuity
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/actuarialangle
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/actuarialangle.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/actuarialangle.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines a single command \actuarialangle to typeset
"angles" in the 'present value of an annuity' symbols common in
actuarial and financial notation.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/actuarialangle
%doc %{_texmfdistdir}/doc/latex/actuarialangle

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
