USE ${SCHEMA};
INSERT OVERWRITE DIRECTORY '${hiveconf:output_path}'
USING csv OPTIONS ('header'='true')

select /* TPC-DS query82.tpl 0.67 */  i_item_id
       ,i_item_desc
       ,i_current_price
 from item, inventory, date_dim, store_sales
 where i_current_price between 8 and 8+30
 and inv_item_sk = i_item_sk
 and d_date_sk=inv_date_sk
 and d_date between cast('2000-02-17' as date) and dateadd(day,60,cast('2000-02-17' as date))
 and i_manufact_id in (174,610,601,169)
 and inv_quantity_on_hand between 100 and 500
 and ss_item_sk = i_item_sk
 group by i_item_id,i_item_desc,i_current_price
 order by i_item_id
 limit 100;
