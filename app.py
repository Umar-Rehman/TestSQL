##testing jenkins
import queries

SQL = queries.SQLQuery("SQL Server", ".\SQLExpress", "JenkinsGIT", "GITdata")
SQL.insert_data_from_csv("./log.csv")