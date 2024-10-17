Name:		texlive-quattrocento
Version:	64372
Release:	2
Summary:	LaTeX support for Quattrocento and Quattrocento Sans fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/quattrocento
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quattrocento.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quattrocento.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the Quattrocento and Quattrocento Sans families of
fonts, designed by Pablo Impallari; the fonts themselves are
also provided, in both Type 1 and OpenType format. Quattrocento
is a classic typeface with wide and open letterforms, and great
x-height, which makes it very legible for body text at small
sizes. Tiny details that only show up at bigger sizes make it
also great for display use. Quattrocento Sans is the perfect
sans-serif companion for Quattrocento.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/quattrocento
%{_texmfdistdir}/fonts/map/dvips/quattrocento
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento
%{_texmfdistdir}/fonts/truetype/impallari/quattrocento
%{_texmfdistdir}/fonts/type1/impallari/quattrocento
%{_texmfdistdir}/fonts/vf/impallari/quattrocento
%{_texmfdistdir}/tex/latex/quattrocento
%doc %{_texmfdistdir}/doc/fonts/quattrocento

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
