
## statusTracker
Simple python use case to track the status of service in cloud. Useful to setup alerts (if necessary) to proactively notify users internally upon outages.


##  validating using sqllite3 cli
```
sqlite> select * from serviceoutages;
astro|Incident/16380572|Astro Deploy is Down|2023-03-07 22:02:31+00:00
astro|Incident/16046604|Cloud Image Repository has degraded performance|2023-02-07 15:41:27+00:00
astro|Incident/15915919|Astronomer Cloud UI Unavailable|2023-01-23 22:47:41+00:00
astro|Incident/14437746|Third Party Authentication Outage Causing Astro Downtime|2022-12-05 22:23:45+00:00
astro|Incident/13324179|New users are getting Internal server error  when accessing airflow UI.|2022-11-18 16:47:42+00:00
astro|Incident/12768295|Updating Variables Corrupts Secret Variables|2022-11-09 23:02:28+00:00
astro|Incident/12685284|Astro UI & CLI Outage|2022-11-01 20:47:03+00:00
astro|Incident/12616812|Airflow Worker Node Scaling Issue|2022-10-27 16:24:08+00:00
astro|Incident/12261795|Authentication Issue|2022-10-18 22:05:52+00:00
astro|Incident/11413718|Astro UI in degraded state.|2022-10-05 14:13:04+00:00
astro|Incident/11234921|Deployments showing unhealthy in Astro UI.|2022-09-23 16:08:30+00:00
astro|Incident/11185766|Astro Docker Registry down|2022-09-20 00:52:42+00:00
astro|Incident/11133052|Astro Deploy Image Updates Failing|2022-09-14 23:23:21+00:00
astro|Incident/11020597|Image update issues|2022-08-31 21:13:42+00:00
astro|Incident/10892107|Worker size in Cloud UI not consistently respected|2022-08-24 17:43:00+00:00
astro|Incident/10711349|Astro Authentication Unavailable For Some Users|2022-07-28 18:53:04+00:00
astro|Incident/10505700|Astro Platform UI Down|2022-07-09 16:56:39+00:00
astro|Incident/10369992|User Access Unavailable|2022-06-21 07:45:00+00:00
astro|Incident/9898313|Issues with Astro-Runtime v5.0.0 deployments|2022-05-03 00:41:21+00:00
astro|Incident/9687706|Scheduled Maintenance - Deployment Management|2022-04-07 02:57:24+00:00
astro|Incident/9671757|Deployment Status is broken|2022-03-31 03:17:29+00:00
astro|Incident/9505570|New images not being deployed|2022-03-11 06:00:00+00:00
astro|Incident/9082015|API Key / Access Token Issue|2022-01-14 19:32:48+00:00
astro|Incident/9067361|DB Maintenance|2022-01-13 04:00:30+00:00
astro|Incident/8868646|Deployments and Login Instability|2021-12-16 23:49:43+00:00
```

