# Generated from dm-timestamps-1.2.0.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	dm-timestamps

Summary:	DataMapper plugin for magical timestamps
Name:		rubygem-%{rbname}

Version:	1.2.0
Release:	3
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		https://github.com/datamapper/dm-timestamps
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
DataMapper plugin for magical timestamps

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/*.rdoc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/LICENSE
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}


%changelog
* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.2.0-2
+ Revision: 774161
- mass rebuild of ruby packages against ruby 1.9.1

* Mon Jan 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2.0-1
+ Revision: 767073
- imported package rubygem-dm-timestamps

