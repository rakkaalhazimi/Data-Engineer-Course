# Install PySpark for Windows

## 1. Install java
- Download java JDK ver. 11 from [here](https://www.oracle.com/java/technologies/javase/jdk11-archive-downloads.html)
- Choose the directory for java then set the directory into `JAVA_HOME` PATH variable. ex: "C:\ProgramFiles\Java\jdk-11.0.14"
- Add your java `/bin` directory into PATH variable. ex: "C:\ProgramFiles\Java\jdk-11.0.14\bin"

## 2. Install spark
- Download spark from [here](https://spark.apache.org/downloads.html)
- Choose the directory for java then set the directory into `SPARK_HOME` PATH variable. ex: "C:\ProgramFiles\D:\ProgramFiles\spark-3.2.1-bin-hadoop3.2"
- Add your spark `/bin` directory into PATH variable. ex: "C:\ProgramFiles\spark-3.2.1-bin-hadoop3.2\bin"

## 3. Install hadoop
Download hadoop that match your pyspark, for v.3.2.0 is [here](https://hadoop.apache.org/release/3.2.0.html)
- Choose the directory for java then set the directory into `SPARK_HOME` PATH variable. ex: "C:\ProgramFiles\hadoop-3.2.0"
- Add your hadoop `/bin` directory into PATH variable. ex: "C:\ProgramFiles\spark-3.2.1-bin-hadoop3.2.0\bin"

## 4. Download hadoop winutils
- Download hadoop winutils that matched your hadoop version, for v.3.2.0 is [here](https://github.com/cdarlint/winutils/tree/master/hadoop-3.2.0/bin)
- Move all the folder inside your hadoop `/bin` directory. ex: "C:\ProgramFiles\spark-3.2.1-bin-hadoop3.2.0\bin"

## 5. Install pyspark
Get pyspark library from python by typing:
```
pip install pyspark
```
in your terminal.

## 6. Set PYSPARK_PYTHON path
Now we need to connect python to spark, set environment `PYSPARK_PYTHON=python` into PATH variable.
 