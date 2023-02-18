
/*select count(distinct Order_ID) from `case.items` where Article_Group = 'Coffee' ; */

select  sum(Quantity_ordered *  Number_of_capsules / One_or_Two_Cup_Product )/count(distinct Order_ID)  from `case.items` where Article_Group = 'Coffee' 
