# https://fedoraproject.org/wiki/Packaging:Haskell

%global ghc_without_dynamic 1
%global ghc_without_shared 1
%global without_prof 1
%global without_haddock 1

%global pkg_name idris
%global pkgver %{pkg_name}-%{version}

# no useful debuginfo for Haskell packages without C sources
%global debug_package %{nil}

Name:           %{pkg_name}
Version:        1.3.1
Release:        1%{?dist}
Summary:        Functional Programming Language with Dependent Types

License:        BSD
Url:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
#BuildRequires:  chrpath
%if %{defined fedora}
BuildRequires:  ghc-aeson-devel
%if 0%{?fedora} >= 27
BuildRequires:  ghc-annotated-wl-pprint-devel
%endif
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-ansi-wl-pprint-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-blaze-html-devel
BuildRequires:  ghc-blaze-markup-devel
BuildRequires:  ghc-bytestring-devel
%if 0%{?fedora} >= 27
BuildRequires:  ghc-cheapskate-devel
BuildRequires:  ghc-code-page-devel
%endif
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
%if 0%{?fedora} >= 27
BuildRequires:  ghc-fingertree-devel
%endif
BuildRequires:  ghc-fsnotify-devel
BuildRequires:  ghc-haskeline-devel
%if 0%{?fedora} >= 26
BuildRequires:  ghc-ieee754-devel
%endif
BuildRequires:  ghc-libffi-devel
%if 0%{?fedora} >= 27
BuildRequires:  ghc-megaparsec-devel
%endif
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-regex-tdfa-devel
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-split-devel
%if 0%{?fedora} >= 26
BuildRequires:  ghc-terminal-size-devel
%endif
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-uniplate-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-vector-binary-instances-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-zip-archive-devel
BuildRequires:  gmp-devel
# End cabal-rpm deps
%if 0%{?fedora} >= 27
BuildRequires:  ghc-lens-devel
%else
BuildRequires:  ghc-template-haskell-devel
%endif
BuildRequires:  ghc-zlib-devel
%else
BuildRequires:  ghc-libraries
BuildRequires:  gmp-devel%{?_isa}
BuildRequires:  zlib-devel%{?_isa}
%endif
BuildRequires:  cabal-install > 1.18
Requires:       gcc
Requires:       gmp-devel

%description
Idris is a general purpose language with full dependent types. It is compiled,
with eager evaluation. Dependent types allow types to be predicated on values,
meaning that some aspects of a program's behaviour can be specified precisely
in the type. The language is closely related to Epigram and Agda.
There is a tutorial at <http://www.idris-lang.org/documentation>.
Features include:

* Full, first class, dependent types with dependent pattern matching
* where clauses, with rule, case expressions, pattern matching let and lambda
bindings
* Interfaces (similar to type classes), monad comprehensions
* do notation, idiom brackets, syntactic conveniences for lists, tuples,
dependent pairs
* Totality checking
* Coinductive types
* Indentation significant syntax, extensible syntax
* Cumulative universes
* Simple foreign function interface (to C)
* Hugs style interactive environment.


%prep
%setup -q
cabal-tweak-flag FFI True
cabal-tweak-flag GMP True


%build
%global cabal cabal
%cabal update
%cabal sandbox init
%cabal install --only-dependencies --force-reinstalls
%ghc_bin_build


%install
%ghc_bin_install

find %{buildroot}%{_libdir} -name "libHS%{pkgver}-*.so" -delete
rm -r %{buildroot}%{ghclibdir}


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/idris-codegen-c
%{_bindir}/idris-codegen-javascript
%{_bindir}/idris-codegen-node
%{_datadir}/%{name}-%{version}
%{_mandir}/man1/idris.1*


%changelog
* Fri Nov  9 2018 Jens Petersen <petersen@redhat.com> - 1.3.1-1
- update to 1.3.1
- https://www.idris-lang.org/idris-1-3-1-released

* Sun Jun 24 2018 Jens Petersen <petersen@redhat.com> - 1.3.0-1
- update to 1.3.0
- https://www.idris-lang.org/idris-1-3-0-released

* Wed Feb 21 2018 Jens Petersen <petersen@redhat.com> - 1.2.0-1
- update to 1.2.0
- https://www.idris-lang.org/idris-1-2-0-released/

* Wed Dec  6 2017 Jens Petersen <petersen@redhat.com> - 1.1.1-1
- update to 1.1.1

* Wed Apr 12 2017 Jens Petersen <petersen@redhat.com> - 1.0-1
- 1.0
- https://www.idris-lang.org/idris-1-0-released/

* Tue Mar 28 2017 Jens Petersen <petersen@redhat.com> - 0.99.2-1
- 0.99.2

* Sun Mar 12 2017 Jens Petersen <petersen@redhat.com> - 0.99.1-1
- 0.99.1

* Sat Feb  4 2017 Jens Petersen <petersen@redhat.com> - 0.99-3
- enable FFI and GMP flags

* Tue Dec 27 2016 Jens Petersen <petersen@redhat.com> - 0.99-2
- rebuild

* Sat Dec  3 2016 Jens Petersen <petersen@redhat.com> - 0.99-1
- 0.99 release
- datadir patch from upstream

* Tue Oct  4 2016 Jens Petersen <petersen@redhat.com> - 0.12.3-1
- use license macro

* Tue Aug  9 2016 Jens Petersen <petersen@redhat.com> - 0.12.2-1
- 0.12.2

* Thu Jul 28 2016 Jens Petersen <petersen@redhat.com> - 0.12.1-1
- update to 0.12.1
- BR array
- require gmp-devel (#1360168)

* Mon Jun 27 2016 Jens Petersen <petersen@redhat.com> - 0.12-1
- 0.12

* Mon May 30 2016 Jens Petersen <petersen@redhat.com> - 0.11.2-1

* Fri May  6 2016 Jens Petersen <petersen@redhat.com> - 0.11.1-1
- 0.11.1
- has manpage

* Tue Mar 29 2016 Jens Petersen <petersen@redhat.com> - 0.11-1
- update to 0.11

* Tue Mar  1 2016 Jens Petersen <petersen@redhat.com> - 0.10.2-1
- update to 0.10.2

* Fri Feb 26 2016 Jens Petersen <petersen@redhat.com> - 0.10.1-1
- update to 0.10.1

* Mon Jan 25 2016 Jens Petersen <petersen@redhat.com> - 0.10-1
- update to 0.10

* Fri Jan  8 2016 Jens Petersen <petersen@redhat.com> - 0.9.20.2-1
- update to 0.9.20.2

* Wed Nov 18 2015 Jens Petersen <petersen@redhat.com> - 0.9.20.1-1
- update to 0.9.20.1

* Wed Nov 11 2015 Jens Petersen <petersen@redhat.com> - 0.9.20-1
- update to 0.9.20

* Sun Oct 04 2015 Jens Petersen <petersen@redhat.com> - 0.9.19.1-1
- update to 0.9.19.1

* Mon Sep 14 2015 Jens Petersen <petersen@redhat.com> - 0.9.19-2
- require gcc

* Sun Sep 13 2015 Jens Petersen <petersen@fedoraproject.org> - 0.9.19-1
- 0.9.19

* Wed Jan 21 2015 Jens Petersen <petersen@redhat.com> - 0.9.16-1
- update to 0.9.16

* Sun Nov 30 2014 Jens Petersen <petersen@redhat.com> - 0.9.15.1-1
- build with cabal-install 1.18 sandbox

* Wed Sep 10 2014 Jens Petersen <petersen@redhat.com> - 0.9.14.3-1
- disable dyn, prof, docs
- use cabal-dev to build missing deps, and exclude library

* Wed Sep 10 2014 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.9.14.3
- spec file generated by cabal-rpm-0.9.1
%doc README.md
