%global tl_name actuarialangle
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1
Release:	%{tl_revision}.1
Summary:	Angle symbol denoting a duration in actuarial and financial notation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/actuarialangle
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/actuarialangle.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/actuarialangle.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/actuarialangle.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides commands to typeset the "angle" symbol denoting a
duration in actuarial notation, such as in symbols for the present value
of certain or life annuities, and an over angle square bracket used to
emphasize joint status in symbols of life contingencies.

