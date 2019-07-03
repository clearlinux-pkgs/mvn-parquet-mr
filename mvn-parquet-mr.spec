#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-parquet-mr
Version  : 1.6.0
Release  : 1
URL      : https://repo1.maven.org/maven2/com/twitter/parquet-hadoop-bundle/1.6.0/parquet-hadoop-bundle-1.6.0.jar
Source0  : https://repo1.maven.org/maven2/com/twitter/parquet-hadoop-bundle/1.6.0/parquet-hadoop-bundle-1.6.0.jar
Source1  : https://repo1.maven.org/maven2/com/twitter/parquet-hadoop-bundle/1.6.0/parquet-hadoop-bundle-1.6.0.pom
Source2  : https://repo1.maven.org/maven2/org/apache/parquet/parquet-hadoop/1.10.0/parquet-hadoop-1.10.0.jar
Source3  : https://repo1.maven.org/maven2/org/apache/parquet/parquet-hadoop/1.10.0/parquet-hadoop-1.10.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-parquet-mr-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-parquet-mr package.
Group: Data

%description data
data components for the mvn-parquet-mr package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/twitter/parquet-hadoop-bundle/1.6.0
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/com/twitter/parquet-hadoop-bundle/1.6.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/twitter/parquet-hadoop-bundle/1.6.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/twitter/parquet-hadoop-bundle/1.6.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/parquet/parquet-hadoop/1.10.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/parquet/parquet-hadoop/1.10.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/parquet/parquet-hadoop/1.10.0
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/parquet/parquet-hadoop/1.10.0


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/twitter/parquet-hadoop-bundle/1.6.0/parquet-hadoop-bundle-1.6.0.jar
/usr/share/java/.m2/repository/com/twitter/parquet-hadoop-bundle/1.6.0/parquet-hadoop-bundle-1.6.0.pom
/usr/share/java/.m2/repository/org/apache/parquet/parquet-hadoop/1.10.0/parquet-hadoop-1.10.0.jar
/usr/share/java/.m2/repository/org/apache/parquet/parquet-hadoop/1.10.0/parquet-hadoop-1.10.0.pom
