import findspark
findspark.init()

import pyspark # only run after findspark.init()
from pyspark.sql import SparkSession
from pyspark.sql.functions import year, month, dayofmonth
from pyspark.sql.types import IntegerType
from pyspark.sql.functions import col
from pyspark.sql import functions as F

spark = SparkSession.builder.getOrCreate()

def getdata():
    df=spark.read.format("csv").option("header","true").load("./country.csv")

    df = df.withColumn('date', df.date.cast('timestamp')).orderBy('date')
    df = df.withColumn('month',month(df.date))
    df = df.withColumn('day',dayofmonth(df.date))
    df = df.withColumn('year',year(df.date))
    return df

def getstats(df,sm,sy,em,ey,country):

    startdate = sy + '-' + sm + '-01'
    enddate = ey + '-' + em + '-30'
    print("StartDate:", startdate)
    print("EndDate:", enddate)
    subset = df.filter( (col('date') >= startdate)  & (col('date') <= enddate) )
    subset = df.filter(col('administrative_area_level_1') == country)

    # Deaths
    subset = subset.withColumn("deaths", subset["deaths"].cast(IntegerType()))  
    #totalDeaths = subset.groupBy().agg(F.sum("deaths")).collect()[0][0]
    totalDeaths = subset.filter(col('date') == enddate).select('deaths').collect()[0][0]
    return totalDeaths

def plot(x):
    return x