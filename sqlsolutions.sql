
/*select count(distinct Order_ID) from `case.items` where Article_Group = 'Coffee' ; */

select  sum(Quantity_ordered *  Number_of_capsules / One_or_Two_Cup_Product )/count(distinct Order_ID)  from `case.items` where Article_Group = 'Coffee' 

/*select Order_ID where (SELECT Order_ID FROM `case.items` WHERE  SKU = 'Ristretta Milano Black') from `case.items` */

select  distinct SKU, count(SKU) from `case.items` as Count WHERE Order_ID in (SELECT Order_ID FROM `case.items` WHERE  SKU = 'Ristretta Milano Black') and SKU != 'Ristretta Milano Black' group by 1 order by 2 desc
