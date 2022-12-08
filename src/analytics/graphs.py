import pyspark
import matplotlib.pyplot as plt
from pyspark.sql.functions import year, month, dayofmonth
from pyspark.sql.types import IntegerType
from pyspark.sql.functions import col, lag, monotonically_increasing_id
from pyspark.sql.window import Window


conf = pyspark.SparkConf()
conf.set("spark.driver.memory", "8g")
conf.set("spark.worker.timeout", "10000000")
conf.set("spark.driver.maxResultSize", "0")
conf.set("spark.executor.memory", "8g")

sc = pyspark.SparkContext(conf=conf)
spark = pyspark.SQLContext.getOrCreate(sc)


def getdata():
    df = spark.read.format("csv").option("header", "true").load("./country.csv")

    df = df.withColumn("date", df.date.cast("timestamp")).orderBy("date")
    df = df.withColumn("month", month(df.date))
    df = df.withColumn("day", dayofmonth(df.date))
    df = df.withColumn("year", year(df.date))
    return df


def getstats(df, sm, sy, em, ey, country):

    startdate = sy + "-" + sm + "-01"
    if em == "02":
        enddate = ey + "-" + em + "-28"
    elif em in ["01", "03", "05", "07", "08", "10", "12"]:
        enddate = ey + "-" + em + "-31"
    else:
        enddate = ey + "-" + em + "-30"

    subset = df.filter((col("date") >= startdate) & (col("date") <= enddate))
    subset = subset.filter(col("administrative_area_level_1") == country)

    subset = subset.withColumn("ID", monotonically_increasing_id())
    windowSpec = Window.orderBy("ID")

    subset = subset.withColumn("deaths", subset["deaths"].cast(IntegerType()))
    subset = subset.withColumn("confirmed", subset["confirmed"].cast(IntegerType()))
    subset = subset.withColumn(
        "people_vaccinated", subset["people_vaccinated"].cast(IntegerType())
    )
    subset = subset.withColumn("recovered", subset["recovered"].cast(IntegerType()))

    # There's only one partition - alternatives to lead
    subset = subset.withColumn("prev_deaths", lag("deaths", 1).over(windowSpec))
    subset = subset.withColumn("prev_confirmed", lag("confirmed", 1).over(windowSpec))
    subset = subset.withColumn("prev_vac", lag("people_vaccinated", 1).over(windowSpec))
    subset = subset.withColumn("prev_recovered", lag("recovered", 1).over(windowSpec))

    subset = subset.withColumn("daily_deaths", subset["deaths"] - subset["prev_deaths"])
    subset = subset.withColumn(
        "daily_confirmed", subset["confirmed"] - subset["prev_confirmed"]
    )
    subset = subset.withColumn(
        "daily_vacs", subset["people_vaccinated"] - subset["prev_vac"]
    )
    subset = subset.withColumn(
        "daily_recovered", subset["recovered"] - subset["prev_recovered"]
    )

    subset = subset.withColumn("ID", monotonically_increasing_id())
    result = subset.select(
        "year",
        "month",
        "day",
        "deaths",
        "prev_deaths",
        "daily_deaths",
        "daily_confirmed",
        "daily_vacs",
        "daily_recovered",
        "ID",
    )

    totalDeaths = subset.filter(col("date") == enddate).select("deaths").collect()[0][0]
    return totalDeaths, result


def get_values(result):
    rows = result.count()
    conf, deaths, recovered, vacs = [], [], [], []
    dates = []
    for i in range(1, rows, rows // 10):
        res = result.select(
            "daily_confirmed", "daily_deaths", "daily_recovered", "daily_vacs"
        ).collect()[i]
        conf.append(res[0])
        deaths.append(res[1])
        recovered.append(res[2])
        vacs.append(res[3])
        y, m, d = result.select("year", "month", "day").collect()[i]
        dates.append(str(y) + "-" + str(m) + "-" + str(d))

    return dates, conf, deaths, recovered, vacs


def plot_rate(result):

    dates, conf, deaths, recovered, vacs = get_values(result)

    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, sharex=True, figsize=(15, 15))

    ax1.tick_params(labelbottom=True, labelsize=15)
    plt.tight_layout(pad=5)

    plt.subplot(411)
    ax1.plot(dates, conf)
    ax1.set_title("Daily Confirmed cases", color="blue")
    ax1.set_ylabel("No. of Cases", fontsize=15)
    ax1.set_xlabel("Time period", fontsize=10)
    ax1.tick_params(labelbottom=True, labelsize=11)
    ax1.grid()

    plt.subplot(412)
    ax2.plot(dates, deaths)
    ax2.set_title("Daily Deaths", color="blue")
    ax2.set_ylabel("No. of Deaths", fontsize=15)
    ax2.set_xlabel("Time period", fontsize=10)
    ax2.tick_params(labelbottom=True, labelsize=12)
    ax2.grid()

    plt.subplot(413)
    ax3.plot(dates, recovered)
    ax3.set_title("Daily recovered", color="blue")
    ax3.set_ylabel("No. of Recovered", fontsize=15)
    ax3.set_xlabel("Time period", fontsize=10)
    ax3.tick_params(labelbottom=True, labelsize=13)
    ax3.grid()

    plt.subplot(414)
    ax4.plot(dates, vacs)
    ax4.set_title("Daily Vaccinated", color="blue")
    ax4.set_ylabel("No. of Vaccinated (in mils)", fontsize=15)
    ax4.set_xlabel("Time Period", fontsize=10)
    ax4.tick_params(labelbottom=True, labelsize=14)
    ax4.grid()

    # fig.show()
    return fig
