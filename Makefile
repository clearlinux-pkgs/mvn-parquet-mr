PKG_NAME := mvn-parquet-mr
URL = https://repo1.maven.org/maven2/com/twitter/parquet-hadoop-bundle/1.6.0/parquet-hadoop-bundle-1.6.0.jar
ARCHIVES = https://repo1.maven.org/maven2/com/twitter/parquet-hadoop-bundle/1.6.0/parquet-hadoop-bundle-1.6.0.pom :  https://repo1.maven.org/maven2/org/apache/parquet/parquet-hadoop/1.10.0/parquet-hadoop-1.10.0.jar : https://repo1.maven.org/maven2/org/apache/parquet/parquet-hadoop/1.10.0/parquet-hadoop-1.10.0.pom :

include ../common/Makefile.common
