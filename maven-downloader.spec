Name:           maven-downloader
Version:        1.1
Release:        5%{?dist}
# Maven-shared defines maven-downloader version as 1.2
Epoch:          1
Summary:        Maven artifact downloader
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-osgi
# svn export http://svn.apache.org/repos/asf/maven/shared/tags/maven-downloader-1.1 maven-downloader-1.1
# tar caf maven-downloader-1.1.tar.xz maven-downloader-1.1/
Source0:        %{name}-%{version}.tar.xz
# ASL mandates that the licence file be included in redistributed source
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:      noarch

BuildRequires:  java-devel
BuildRequires:  junit
BuildRequires:  maven-local
BuildRequires:  maven-shared
BuildRequires:  plexus-containers-component-metadata

Obsoletes:      maven-shared-downloader < %{epoch}:%{version}-%{release}
Provides:       maven-shared-downloader = %{epoch}:%{version}-%{release}

%description
Provide a super simple interface for downloading a single artifact.

This is a replacement package for maven-shared-downloader

%package javadoc
Group:          Documentation
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
    
%description javadoc
API documentation for %{name}.


%prep
%setup -q

%pom_add_dep org.apache.maven:maven-compat

# Replace plexus-maven-plugin with plexus-component-metadata
%pom_xpath_set "pom:plugin[pom:artifactId[text()='plexus-maven-plugin']]//pom:goal[text()='descriptor']" generate-metadata
%pom_xpath_set "pom:artifactId[text()='plexus-maven-plugin']" plexus-component-metadata

cp %{SOURCE1} LICENSE.txt

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt


%changelog
* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.1-5
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Wed Feb 20 2013 Tomas Radej <tradej@redhat.com> - 1:1.1-4
- Added BR on maven-shared

* Fri Feb 15 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.1-3
- Use new pom macros to fix plexus-component-metadata

* Fri Feb 08 2013 Tomas Radej <tradej@redhat.com> - 1:1.1-2
- Building the new way

* Fri Jan 11 2013 Tomas Radej <tradej@redhat.com> - 1:1.1-1
- Initial version

