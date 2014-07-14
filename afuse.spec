Name:		afuse
Summary:	An automounter implemented with FUSE
Version:	0.4
Release:	1
License:	GPLv2+
Group:		Networking/Other
Source0:	https://afuse.googlecode.com/files/%{name}-%{version}.tar.gz
URL:		https://github.com/pcarrier/afuse/
BuildRequires:	fuse-devel

%description
Afuse is an automounting file system implemented in user-space using FUSE. 
Afuse currently implements the most basic functionality that can be expected 
by an automounter; that is it manages a directory of virtual directories. If 
one of these virtual directories is accessed and is not already automounted, 
afuse will attempt to mount a filesystem onto that directory. If the mount 
succeeds the requested access proceeds as normal, otherwise it will fail 
with an error.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/afuse
%{_bindir}/afuse-avahissh

