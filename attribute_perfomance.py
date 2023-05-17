import psycopg2
import pandas as pd
import csv
import urllib3
import io

try:
    conn = psycopg2.connect(database='wolfnet_data_services',
                            user='wntdba', password='YGSeZPwadyFvVVw',
                            host='pgsqlc1.prod.aws.wolfnet.com', port='5432')

except Exception as err:
    print('Error while creating the connection ', err)

else:
    print('connection established to pgload02')
    try:
        cursor = conn.cursor()
        df = pd.read_csv(
            'https://s3-us-west-2.amazonaws.com/raw-data-test.movoto.com/ojoattributes/attributes_report.csv')
        # df = pd.read_csv('attribute_stats_all_mls_2022_05_01_00_29_12.csv')
        print(df)
        output = io.StringIO()
        df.to_csv(output, sep='\t', header=False, index=False)
        output.seek(0)
        contents = output.getvalue()
        cursor.execute(f'SET search_path TO attribute_performance')
        cursor.copy_from(output, 'attributes_report_raw', sep='\t')

    except Exception as err:
        print('Error while inserting data from csv to attributes_report_raw ', err)
    else:
        try:
            sql = """ 
             update attributes_report_raw set min_rt_new='0:00:00' where min_rt_new in ('None','No');
             update attributes_report_raw set avg_rt_new='0:00:00' where avg_rt_new in ('None','No');
             update attributes_report_raw set max_rt_new='0:00:00' where max_rt_new in ('None','No');
             insert into  attributes_report(feed_name ,
                pipeline ,
                new_listings ,
                first_found_new ,
                recovery_cases_new ,
                new_listings_recovered ,
                new_listings_not_recovered ,
                min_rt ,
                new_recovery_lessOrEq_avg_time ,
                avg_rt,
                new_recovery_greater_avg_time ,
                max_rt ,
                report_date)
                select ojo_source_name as feed_name,
                case when ojo_source_name in (select ojo_source_name from feed_pipeline) then 'Plaid' else 'PyRets' end as pipeline,
                new_listings_requests as new_listings,
                first_found_new as first_found_new,
                recovery_cases_new as recovery_cases_new,
                new_listings_recovered as new_listings_recovered,
                new_listings_not_recovered as new_listings_not_recovered,
                EXTRACT(EPOCH FROM (TO_TIMESTAMP(min_rt_new, 'HH24:MI')::TIME))/60 as min_rt,
                new_listings_recovery_lessOrEq_avg_time as new_recovery_lessOrEq_avg_time,
                EXTRACT(EPOCH FROM (TO_TIMESTAMP(avg_rt_new, 'HH24:MI')::TIME))/60 as avg_rt,
                new_listings_recovered_greater_avg_time as new_recovery_greater_avg_time,
                EXTRACT(EPOCH FROM (TO_TIMESTAMP(max_rt_new, 'HH24:MI')::TIME))/60 as max_rt,
                report_end_time as report_date
                from attributes_report_raw where report_end_time > (select max(report_date) from attributes_report )
                ON CONFLICT (feed_name,report_date) DO NOTHING;


                insert into  raw(
                feed_name ,
                pipeline ,
                report_date,				
                new_listings ,
                coverage_one_hr,
                coverage_three_hr,
                coverage_six_hr,
                coverage_percent_one_hr,
                coverage_percent_three_hr,
                coverage_percent_six_hr
                )
                select 
                feed_name as feed_name,
                case when feed_name in (select ojo_source_name from feed_pipeline) then 'Plaid' else 'PyRets' end as pipeline,
                report_date as report_date,
                new_listings as new_listings,
                case 
                when (min_rt<60 or min_rt=60) and (avg_rt<60 or avg_rt=60) and (max_rt<60 or max_rt=60) then
                first_found_new + new_recovery_lessOrEq_avg_time + new_recovery_greater_avg_time
                when (min_rt<60 or min_rt=60) and (avg_rt<60 or avg_rt=60) and max_rt>60 then 
                first_found_new + new_recovery_lessOrEq_avg_time + floor(((new_recovery_greater_avg_time/(max_rt-avg_rt)) * (60 - avg_rt)))
                when (min_rt<60 or min_rt=60) and avg_rt>60 then
                first_found_new + floor(((new_recovery_lessOrEq_avg_time/(avg_rt-min_rt)) * (60 - min_rt)))
                when min_rt>60 then first_found_new end as coverage_one_hr,
                case 
                when (min_rt<180 or min_rt=180) and (avg_rt<180 or avg_rt=180) and (max_rt<180 or max_rt=180) then
                first_found_new + new_recovery_lessOrEq_avg_time + new_recovery_greater_avg_time
                when (min_rt<180 or min_rt=180) and (avg_rt<180 or avg_rt=180) and max_rt>180 then 
                first_found_new + new_recovery_lessOrEq_avg_time + floor(((new_recovery_greater_avg_time/(max_rt-avg_rt)) * (180 - avg_rt)))
                when (min_rt<180 or min_rt=180) and avg_rt>180 then
                first_found_new + floor(((new_recovery_lessOrEq_avg_time/(avg_rt-min_rt)) * (180 - min_rt)))
                when min_rt>180 then first_found_new end as coverage_three_hr,
                case 
                when (min_rt<360 or min_rt=360) and (avg_rt<360 or avg_rt=360) and (max_rt<360 or max_rt=360) then
                first_found_new + new_recovery_lessOrEq_avg_time + new_recovery_greater_avg_time
                when (min_rt<360 or min_rt=360) and (avg_rt<360 or avg_rt=360) and max_rt>360 then 
                first_found_new + new_recovery_lessOrEq_avg_time + floor(((new_recovery_greater_avg_time/(max_rt-avg_rt)) * (360 - avg_rt)))
                when (min_rt<360 or min_rt=360) and avg_rt>360 then
                first_found_new + floor(((new_recovery_lessOrEq_avg_time/(avg_rt-min_rt)) * (360 - min_rt)))
                when min_rt>360 then first_found_new end as coverage_six_hr,
                case 
                when (recovery_cases_new + first_found_new<>0) then floor(((case 
                when (min_rt<60 or min_rt=60) and (avg_rt<60 or avg_rt=60) and (max_rt<60 or max_rt=60) then
                first_found_new + new_recovery_lessOrEq_avg_time + new_recovery_greater_avg_time
                when (min_rt<60 or min_rt=60) and (avg_rt<60 or avg_rt=60) and max_rt>60 then 
                first_found_new + new_recovery_lessOrEq_avg_time + floor(((new_recovery_greater_avg_time/(max_rt-avg_rt)) * (60 - avg_rt)))
                when (min_rt<60 or min_rt=60) and avg_rt>60 then
                first_found_new + floor(((new_recovery_lessOrEq_avg_time/(avg_rt-min_rt)) * (60 - min_rt)))
                when min_rt>60 then first_found_new end)*100)/new_listings)
                else 100 end as coverage_percent_one_hr,
                case 
                when (recovery_cases_new + first_found_new <>0) then floor(((case 
                when (min_rt<180 or min_rt=180) and (avg_rt<180 or avg_rt=180) and (max_rt<180 or max_rt=180) then
                first_found_new + new_recovery_lessOrEq_avg_time + new_recovery_greater_avg_time
                when (min_rt<180 or min_rt=180) and (avg_rt<180 or avg_rt=180) and max_rt>180 then 
                first_found_new + new_recovery_lessOrEq_avg_time + floor(((new_recovery_greater_avg_time/(max_rt-avg_rt)) * (180 - avg_rt)))
                when (min_rt<180 or min_rt=180) and avg_rt>180 then
                first_found_new + floor(((new_recovery_lessOrEq_avg_time/(avg_rt-min_rt)) * (180 - min_rt)))
                when min_rt>180 then first_found_new end)*100)/new_listings) 
                else 100 end as coverage_percent_three_hr,
                case 
                when (recovery_cases_new + first_found_new <>0) then floor(((case 
                when (min_rt<360 or min_rt=360) and (avg_rt<360 or avg_rt=360) and (max_rt<360 or max_rt=360) then
                first_found_new + new_recovery_lessOrEq_avg_time + new_recovery_greater_avg_time
                when (min_rt<360 or min_rt=360) and (avg_rt<360 or avg_rt=360) and max_rt>360 then 
                first_found_new + new_recovery_lessOrEq_avg_time + floor(((new_recovery_greater_avg_time/(max_rt-avg_rt)) * (360 - avg_rt)))
                when (min_rt<360 or min_rt=360) and avg_rt>360 then
                first_found_new + floor(((new_recovery_lessOrEq_avg_time/(avg_rt-min_rt)) * (360 - min_rt)))
                when min_rt>360 then first_found_new end)*100)/new_listings) 
                else 100 end as coverage_percent_six_hr
                from attributes_report where report_date > (select max(report_date) from raw )
                ON CONFLICT (feed_name,report_date) DO NOTHING;

             """
            cursor.execute(sql)
        except Exception as err:
            print('error while updating raw csv data in attributes_report_raw')
        else:
            print('updated raw data in attributes_report_raw')
            conn.commit()

finally:
    cursor.close()
    conn.close()



























