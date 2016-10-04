# https://fedoraproject.org/wiki/Packaging:Haskell

%global ghc_without_dynamic 1
%global ghc_without_shared 1
%global without_prof 1
%global without_haddock 1

%global pkg_name idris

# no useful debuginfo for Haskell packages without C sources
%global debug_package %{nil}

Name:           %{pkg_name}
Version:        0.12.3
Release:        1%{?dist}
Summary:        Functional Programming Language with Dependent Types

License:        BSD
Url:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
#BuildRequires:  chrpath
#BuildRequires:  ghc-annotated-wl-pprint-devel
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-ansi-wl-pprint-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-blaze-html-devel
BuildRequires:  ghc-blaze-markup-devel
BuildRequires:  ghc-bytestring-devel
#BuildRequires:  ghc-cheapskate-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
#BuildRequires:  ghc-fingertree-devel
# not in epel7 yet
%if %{defined fedora}
BuildRequires:  ghc-fsnotify-devel
%endif
BuildRequires:  ghc-haskeline-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-optparse-applicative-devel
#BuildRequires:  ghc-parsers-devel
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-split-devel
# for lens
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-compat-devel
BuildRequires:  ghc-transformers-devel
#BuildRequires:  ghc-trifecta-devel
BuildRequires:  ghc-uniplate-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-vector-binary-instances-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-zip-archive-devel
BuildRequires:  ghc-zlib-devel
# End cabal-rpm deps
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


%build
[ -d "$HOME/.cabal" ] || cabal update
%global cabal cabal
%cabal sandbox init
%cabal install --only-dependencies
%ghc_bin_build


%install
%ghc_bin_install

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
