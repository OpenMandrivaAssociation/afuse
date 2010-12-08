Summary:	Implements filesystem automounting functionality similar to Linux's autofs
Name:		afuse
Version:	0.2
Release:	%mkrel 3
License:	GPLv2+
Group:		Networking/Other
URL:		http://sourceforge.net/projects/afuse/
Source0:	http://dfn.dl.sourceforge.net/sourceforge/afuse/%{name}-%{version}.tar.gz
Source1:	afuse.init
Source2:	afuse.sysconfig
Requires(post): rpm-helper
Requires(preun): rpm-helper
Requires:	fuse >= 2.5
BuildRequires:	fuse-devel >= 2.5
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Afuse is a FUSE based filesystem which implements filesystem automounting
functionality similar to Linux's autofs.

%prep

%setup -q

cp %{SOURCE1} .
cp %{SOURCE2} .

%build

%configure2_5x

%make

%install
rm -rf %{buildroot}

%makeinstall

install -d %{buildroot}%{_sysconfdir}/sysconfig
install -d %{buildroot}%{_initrddir}

install -m0755 afuse.init %{buildroot}%{_initrddir}/afuse
install -m0644 afuse.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/afuse

%post 
%_post_service afuse

%preun
%_preun_service afuse

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING COPYING.LIB ChangeLog README
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/afuse
%attr(0755,root,root) %{_initrddir}/afuse
%{_bindir}/%{name}

