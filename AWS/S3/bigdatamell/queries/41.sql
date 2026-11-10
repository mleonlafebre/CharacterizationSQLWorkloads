USE ${SCHEMA};
INSERT OVERWRITE DIRECTORY '${hiveconf:output_path}'
USING csv OPTIONS ('header'='true')

select /* TPC-DS query41.tpl 0.62 */  distinct(i_product_name)
 from item i1
 where i_manufact_id between 741 and 741+40 
   and (select count(*) as item_cnt
        from item
        where (i_manufact = i1.i_manufact and
        ((i_category = 'Women' and 
        (i_color = 'metallic' or i_color = 'seashell') and 
        (i_units = 'Lb' or i_units = 'Bundle') and
        (i_size = 'extra large' or i_size = 'medium')
        ) or
        (i_category = 'Women' and
        (i_color = 'floral' or i_color = 'bisque') and
        (i_units = 'Dozen' or i_units = 'Unknown') and
        (i_size = 'petite' or i_size = 'small')
        ) or
        (i_category = 'Men' and
        (i_color = 'blue' or i_color = 'purple') and
        (i_units = 'Ton' or i_units = 'Bunch') and
        (i_size = 'N/A' or i_size = 'large')
        ) or
        (i_category = 'Men' and
        (i_color = 'moccasin' or i_color = 'snow') and
        (i_units = 'Pound' or i_units = 'Each') and
        (i_size = 'extra large' or i_size = 'medium')
        ))) or
       (i_manufact = i1.i_manufact and
        ((i_category = 'Women' and 
        (i_color = 'black' or i_color = 'deep') and 
        (i_units = 'Case' or i_units = 'N/A') and
        (i_size = 'extra large' or i_size = 'medium')
        ) or
        (i_category = 'Women' and
        (i_color = 'cyan' or i_color = 'frosted') and
        (i_units = 'Cup' or i_units = 'Carton') and
        (i_size = 'petite' or i_size = 'small')
        ) or
        (i_category = 'Men' and
        (i_color = 'blanched' or i_color = 'wheat') and
        (i_units = 'Ounce' or i_units = 'Box') and
        (i_size = 'N/A' or i_size = 'large')
        ) or
        (i_category = 'Men' and
        (i_color = 'ghost' or i_color = 'burlywood') and
        (i_units = 'Gross' or i_units = 'Dram') and
        (i_size = 'extra large' or i_size = 'medium')
        )))) > 0
 order by i_product_name
 limit 100;
