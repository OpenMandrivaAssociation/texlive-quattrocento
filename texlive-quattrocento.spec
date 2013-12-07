# revision 31763
# category Package
# catalog-ctan /fonts/quattrocento
# catalog-date 2013-09-23 22:17:51 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-quattrocento
Version:	20130923
Release:	4
Summary:	LaTeX support for Quattrocento and Quattrocento Sans fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/quattrocento
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quattrocento.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quattrocento.doc.tar.xz
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
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_464xel.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_4btof3.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_6abmaa.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_arxkdo.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_aykkbr.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_cpzb4n.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_dhs3d3.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_dn5k7b.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_dw2g3h.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_e45lg2.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_h2bn35.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_iyhp72.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_mamppr.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_n36lnh.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_nfidqf.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_ptp2lu.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_qceur4.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_tevtmb.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_tixcdz.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_vzn2dc.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_wpi2yi.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_xt7yz2.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_xvywtm.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_zdiabs.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_zievlx.enc
%{_texmfdistdir}/fonts/enc/dvips/quattrocento/qtrcnt_zq54sp.enc
%{_texmfdistdir}/fonts/map/dvips/quattrocento/quattrocento.map
%{_texmfdistdir}/fonts/opentype/impallari/quattrocento/Quattrocento-Bold.otf
%{_texmfdistdir}/fonts/opentype/impallari/quattrocento/Quattrocento-BoldItalic.otf
%{_texmfdistdir}/fonts/opentype/impallari/quattrocento/Quattrocento-Italic.otf
%{_texmfdistdir}/fonts/opentype/impallari/quattrocento/Quattrocento.otf
%{_texmfdistdir}/fonts/opentype/impallari/quattrocento/QuattrocentoSans-Bold.otf
%{_texmfdistdir}/fonts/opentype/impallari/quattrocento/QuattrocentoSans-BoldItalic.otf
%{_texmfdistdir}/fonts/opentype/impallari/quattrocento/QuattrocentoSans-Italic.otf
%{_texmfdistdir}/fonts/opentype/impallari/quattrocento/QuattrocentoSans.otf
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-Bold-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-Bold-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-Bold-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-Bold-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-Bold-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-Bold-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-Bold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-BoldItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-BoldItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-BoldItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-BoldItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-BoldItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-BoldItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-BoldItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-BoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-BoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-BoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-BoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/Quattrocento-BoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoRegular-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoRegular-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoRegular-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoRegular-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoRegular-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoRegular-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoRegular-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoRegular-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoRegular-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoRegular-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoRegular-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoRegular-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-sup-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-sup-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-sup-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-sup-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-tlf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-tlf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-tlf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-tlf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-sup-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-sup-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-sup-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-sup-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-tlf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-tlf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-tlf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-tlf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-BoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-sup-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-sup-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-sup-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-sup-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-tlf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-tlf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-tlf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-tlf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-sup-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-sup-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-sup-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-sup-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-tlf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-tlf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-tlf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-tlf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/impallari/quattrocento/QuattrocentoSans-tlf-ts1.tfm
%{_texmfdistdir}/fonts/type1/impallari/quattrocento/Quattrocento-Bold.pfb
%{_texmfdistdir}/fonts/type1/impallari/quattrocento/Quattrocento-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/impallari/quattrocento/QuattrocentoItalic.pfb
%{_texmfdistdir}/fonts/type1/impallari/quattrocento/QuattrocentoRegular.pfb
%{_texmfdistdir}/fonts/type1/impallari/quattrocento/QuattrocentoSans-Bold.pfb
%{_texmfdistdir}/fonts/type1/impallari/quattrocento/QuattrocentoSans-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/impallari/quattrocento/QuattrocentoSans-BoldItalicLCDFJ.pfb
%{_texmfdistdir}/fonts/type1/impallari/quattrocento/QuattrocentoSans-BoldLCDFJ.pfb
%{_texmfdistdir}/fonts/type1/impallari/quattrocento/QuattrocentoSans-Italic.pfb
%{_texmfdistdir}/fonts/type1/impallari/quattrocento/QuattrocentoSans-ItalicLCDFJ.pfb
%{_texmfdistdir}/fonts/type1/impallari/quattrocento/QuattrocentoSans.pfb
%{_texmfdistdir}/fonts/type1/impallari/quattrocento/QuattrocentoSansLCDFJ.pfb
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/Quattrocento-Bold-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/Quattrocento-Bold-sup-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/Quattrocento-Bold-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/Quattrocento-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/Quattrocento-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/Quattrocento-BoldItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/Quattrocento-BoldItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/Quattrocento-BoldItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/Quattrocento-BoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/Quattrocento-BoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoRegular-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoRegular-sup-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoRegular-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoRegular-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoRegular-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-Bold-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-Bold-sup-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-Bold-sup-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-Bold-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-Bold-tlf-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-BoldItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-BoldItalic-sup-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-BoldItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-BoldItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-BoldItalic-tlf-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-BoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-BoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-Italic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-Italic-sup-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-Italic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-Italic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-Italic-tlf-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-sup-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-sup-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-tlf-ot1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/impallari/quattrocento/QuattrocentoSans-tlf-ts1.vf
%{_texmfdistdir}/tex/latex/quattrocento/LY1Quattrocento-TLF.fd
%{_texmfdistdir}/tex/latex/quattrocento/LY1QuattrocentoSans-TLF.fd
%{_texmfdistdir}/tex/latex/quattrocento/OT1Quattrocento-TLF.fd
%{_texmfdistdir}/tex/latex/quattrocento/OT1QuattrocentoSans-TLF.fd
%{_texmfdistdir}/tex/latex/quattrocento/T1Quattrocento-TLF.fd
%{_texmfdistdir}/tex/latex/quattrocento/T1QuattrocentoSans-TLF.fd
%{_texmfdistdir}/tex/latex/quattrocento/TS1Quattrocento-TLF.fd
%{_texmfdistdir}/tex/latex/quattrocento/TS1QuattrocentoSans-TLF.fd
%{_texmfdistdir}/tex/latex/quattrocento/quattrocento.sty
%doc %{_texmfdistdir}/doc/fonts/quattrocento/OFL.txt
%doc %{_texmfdistdir}/doc/fonts/quattrocento/README
%doc %{_texmfdistdir}/doc/fonts/quattrocento/samples.pdf
%doc %{_texmfdistdir}/doc/fonts/quattrocento/samples.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
