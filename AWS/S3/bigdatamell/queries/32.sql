USE ${SCHEMA};
INSERT OVERWRITE DIRECTORY '${hiveconf:output_path}'
USING csv OPTIONS ('header'='true')

select /* TPC-DS query32.tpl 0.7 */  sum(cs_ext_discount_amt)  as "excess discount amount" 
from 
   catalog_sales 
   ,item 
   ,date_dim
where
i_manufact_id = 328
and i_item_sk = cs_item_sk 
and d_date between '2000-02-04' and 
        dateadd(day,90,cast('2000-02-04' as date))
and d_date_sk = cs_sold_date_sk 
and cs_ext_discount_amt  
     > ( 
         select 
            1.3 * avg(cs_ext_discount_amt) 
         from 
            catalog_sales 
           ,date_dim
         where 
              cs_item_sk = i_item_sk 
          and d_date between '2000-02-04' and
                             dateadd(day,90,cast('2000-02-04' as date))
          and d_date_sk = cs_sold_date_sk 
      ) 
limit 100;
