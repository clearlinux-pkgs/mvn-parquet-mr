#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-parquet-mr
Version  : 1.10.0
Release  : 6
URL      : https://github.com/apache/parquet-mr/archive/apache-parquet-1.10.0.tar.gz
Source0  : https://github.com/apache/parquet-mr/archive/apache-parquet-1.10.0.tar.gz
Source1  : https://repo.maven.apache.org/maven2/org/apache/parquet/parquet-avro/1.10.0/parquet-avro-1.10.0.jar
Source2  : https://repo.maven.apache.org/maven2/org/apache/parquet/parquet-avro/1.10.0/parquet-avro-1.10.0.pom
Source3  : https://repo.maven.apache.org/maven2/org/apache/parquet/parquet-column/1.10.0/parquet-column-1.10.0.jar
Source4  : https://repo.maven.apache.org/maven2/org/apache/parquet/parquet-column/1.10.0/parquet-column-1.10.0.pom
Source5  : https://repo.maven.apache.org/maven2/org/apache/parquet/parquet-common/1.10.0/parquet-common-1.10.0.jar
Source6  : https://repo.maven.apache.org/maven2/org/apache/parquet/parquet-common/1.10.0/parquet-common-1.10.0.pom
Source7  : https://repo.maven.apache.org/maven2/org/apache/parquet/parquet-encoding/1.10.0/parquet-encoding-1.10.0.jar
Source8  : https://repo.maven.apache.org/maven2/org/apache/parquet/parquet-encoding/1.10.0/parquet-encoding-1.10.0.pom
Source9  : https://repo.maven.apache.org/maven2/org/apache/parquet/parquet-jackson/1.10.0/parquet-jackson-1.10.0.jar
Source10  : https://repo.maven.apache.org/maven2/org/apache/parquet/parquet-jackson/1.10.0/parquet-jackson-1.10.0.pom
Source11  : https://repo.maven.apache.org/maven2/org/apache/parquet/parquet/1.10.0/parquet-1.10.0.pom
Source12  : https://repo1.maven.org/maven2/com/twitter/parquet-hadoop-bundle/1.6.0/parquet-hadoop-bundle-1.6.0.jar
Source13  : https://repo1.maven.org/maven2/com/twitter/parquet-hadoop-bundle/1.6.0/parquet-hadoop-bundle-1.6.0.pom
Source14  : https://repo1.maven.org/maven2/com/twitter/parquet/1.6.0/parquet-1.6.0.pom
Source15  : https://repo1.maven.org/maven2/org/apache/parquet/parquet-hadoop/1.10.0/parquet-hadoop-1.10.0.jar
Source16  : https://repo1.maven.org/maven2/org/apache/parquet/parquet-hadoop/1.10.0/parquet-hadoop-1.10.0.pom
Source17  : https://repo1.maven.org/maven2/org/apache/parquet/parquet/1.10.0/parquet-1.10.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-parquet-mr-data = %{version}-%{release}

%description
This contains all classes required to use Parquet within a Hadoop
environment.

%package data
Summary: data components for the mvn-parquet-mr package.
Group: Data

%description data
data components for the mvn-parquet-mr package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/parquet/parquet-avro/1.10.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/parquet/parquet-avro/1.10.0/parquet-avro-1.10.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/parquet/parquet-avro/1.10.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/parquet/parquet-avro/1.10.0/parquet-avro-1.10.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/parquet/parquet-column/1.10.0
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/parquet/parquet-column/1.10.0/parquet-column-1.10.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/parquet/parquet-column/1.10.0
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/parquet/parquet-column/1.10.0/parquet-column-1.10.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/parquet/parquet-common/1.10.0
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/parquet/parquet-common/1.10.0/parquet-common-1.10.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/parquet/parquet-common/1.10.0
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/parquet/parquet-common/1.10.0/parquet-common-1.10.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/parquet/parquet-encoding/1.10.0
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/parquet/parquet-encoding/1.10.0/parquet-encoding-1.10.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/parquet/parquet-encoding/1.10.0
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/apache/parquet/parquet-encoding/1.10.0/parquet-encoding-1.10.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/parquet/parquet-jackson/1.10.0
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/apache/parquet/parquet-jackson/1.10.0/parquet-jackson-1.10.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/parquet/parquet-jackson/1.10.0
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/apache/parquet/parquet-jackson/1.10.0/parquet-jackson-1.10.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/parquet/parquet/1.10.0
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/apache/parquet/parquet/1.10.0/parquet-1.10.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/twitter/parquet-hadoop-bundle/1.6.0
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/com/twitter/parquet-hadoop-bundle/1.6.0/parquet-hadoop-bundle-1.6.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/twitter/parquet-hadoop-bundle/1.6.0
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/com/twitter/parquet-hadoop-bundle/1.6.0/parquet-hadoop-bundle-1.6.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/twitter/parquet/1.6.0
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/com/twitter/parquet/1.6.0/parquet-1.6.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/parquet/parquet-hadoop/1.10.0
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/org/apache/parquet/parquet-hadoop/1.10.0/parquet-hadoop-1.10.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/parquet/parquet-hadoop/1.10.0
cp %{SOURCE16} %{buildroot}/usr/share/java/.m2/repository/org/apache/parquet/parquet-hadoop/1.10.0/parquet-hadoop-1.10.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/parquet/parquet/1.10.0
cp %{SOURCE17} %{buildroot}/usr/share/java/.m2/repository/org/apache/parquet/parquet/1.10.0/parquet-1.10.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/twitter/parquet-hadoop-bundle/1.6.0/parquet-hadoop-bundle-1.6.0.jar
/usr/share/java/.m2/repository/com/twitter/parquet-hadoop-bundle/1.6.0/parquet-hadoop-bundle-1.6.0.pom
/usr/share/java/.m2/repository/com/twitter/parquet/1.6.0/parquet-1.6.0.pom
/usr/share/java/.m2/repository/org/apache/parquet/parquet-avro/1.10.0/parquet-avro-1.10.0.jar
/usr/share/java/.m2/repository/org/apache/parquet/parquet-avro/1.10.0/parquet-avro-1.10.0.pom
/usr/share/java/.m2/repository/org/apache/parquet/parquet-column/1.10.0/parquet-column-1.10.0.jar
/usr/share/java/.m2/repository/org/apache/parquet/parquet-column/1.10.0/parquet-column-1.10.0.pom
/usr/share/java/.m2/repository/org/apache/parquet/parquet-common/1.10.0/parquet-common-1.10.0.jar
/usr/share/java/.m2/repository/org/apache/parquet/parquet-common/1.10.0/parquet-common-1.10.0.pom
/usr/share/java/.m2/repository/org/apache/parquet/parquet-encoding/1.10.0/parquet-encoding-1.10.0.jar
/usr/share/java/.m2/repository/org/apache/parquet/parquet-encoding/1.10.0/parquet-encoding-1.10.0.pom
/usr/share/java/.m2/repository/org/apache/parquet/parquet-hadoop/1.10.0/parquet-hadoop-1.10.0.jar
/usr/share/java/.m2/repository/org/apache/parquet/parquet-hadoop/1.10.0/parquet-hadoop-1.10.0.pom
/usr/share/java/.m2/repository/org/apache/parquet/parquet-jackson/1.10.0/parquet-jackson-1.10.0.jar
/usr/share/java/.m2/repository/org/apache/parquet/parquet-jackson/1.10.0/parquet-jackson-1.10.0.pom
/usr/share/java/.m2/repository/org/apache/parquet/parquet/1.10.0/parquet-1.10.0.pom
