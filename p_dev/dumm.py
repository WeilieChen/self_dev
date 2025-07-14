cp /home/wchen/blue/tailwindservice/datamodel2/prod-aws-backend/waka-pdmora-v01/prod-datamodel/model/databricks/staging/stg_tailwind_workpackage* .
cp /home/wchen/blue/tailwindservice/datamodel2/prod-aws-backend/waka-pdmora-v01/prod-datamodel/model/databricks/staging/stg_tailwind_* .



--- stg

cp /home/wchen/blue/tailwindservice/datamodel2/prod-aws-backend/waka-pdmora-v01/prod-datamodel/model/databricks/staging/stg_tailwind_bacpackage* .
cp /home/wchen/blue/tailwindservice/datamodel2/prod-aws-backend/waka-pdmora-v01/prod-datamodel/model/databricks/staging/stg_tailwind_managedcollection* .
cp /home/wchen/blue/tailwindservice/datamodel2/prod-aws-backend/waka-pdmora-v01/prod-datamodel/model/databricks/staging/stg_tailwind_packageexportrecord* .
cp /home/wchen/blue/tailwindservice/datamodel2/prod-aws-backend/waka-pdmora-v01/prod-datamodel/model/databricks/staging/stg_tailwind_persistedcollection* .
cp /home/wchen/blue/tailwindservice/datamodel2/prod-aws-backend/waka-pdmora-v01/prod-datamodel/model/databricks/staging/stg_tailwind_receivedpackage* .
cp /home/wchen/blue/tailwindservice/datamodel2/prod-aws-backend/waka-pdmora-v01/prod-datamodel/model/databricks/staging/stg_tailwind_replicationpackage* .
cp /home/wchen/blue/tailwindservice/datamodel2/prod-aws-backend/waka-pdmora-v01/prod-datamodel/model/databricks/staging/stg_tailwind_technicaldatapackage* .
cp /home/wchen/blue/tailwindservice/datamodel2/prod-aws-backend/waka-pdmora-v01/prod-datamodel/model/databricks/staging/stg_tailwind_workpackage* .



--- source


cp /home/wchen/blue/tailwindservice/datamodel2/prod-aws-backend/waka-pdmora-v01/prod-datamodel/model/databricks/sources/tailwind_workpackage*.md .

cp /home/wchen/blue/tailwindservice/datamodel2/prod-aws-backend/waka-pdmora-v01/prod-datamodel/model/databricks/sources/tailwind_bacpackage* .
cp /home/wchen/blue/tailwindservice/datamodel2/prod-aws-backend/waka-pdmora-v01/prod-datamodel/model/databricks/sources/tailwind_managedcollection* .
cp /home/wchen/blue/tailwindservice/datamodel2/prod-aws-backend/waka-pdmora-v01/prod-datamodel/model/databricks/sources/tailwind_packageexportrecord* .
cp /home/wchen/blue/tailwindservice/datamodel2/prod-aws-backend/waka-pdmora-v01/prod-datamodel/model/databricks/sources/tailwind_persistedcollection* .
cp /home/wchen/blue/tailwindservice/datamodel2/prod-aws-backend/waka-pdmora-v01/prod-datamodel/model/databricks/sources/tailwind_receivedpackage* .
cp /home/wchen/blue/tailwindservice/datamodel2/prod-aws-backend/waka-pdmora-v01/prod-datamodel/model/databricks/sources/tailwind_replicationpackage* .
cp /home/wchen/blue/tailwindservice/datamodel2/prod-aws-backend/waka-pdmora-v01/prod-datamodel/model/databricks/sources/tailwind_technicaldatapackage* .
cp /home/wchen/blue/tailwindservice/datamodel2/prod-aws-backend/waka-pdmora-v01/prod-datamodel/model/databricks/sources/tailwind_workpackage* .
;


;

;



select * from central_prod.bdf_silver_src.boa__tailwind__workpackagemasterkey limit 1
select * from central_prod.bdf_silver_src.boa__tailwind__workpackage limit 1
select * from central_prod.bdf_silver_src.boa__tailwind__workpackagemaster limit 1
select * from central_prod.bdf_silver_src.boa__tailwind__replicationpackage limit 1
select * from central_prod.bdf_silver_src.boa__tailwind__replicationpackagemaster limit 1
select * from central_prod.bdf_silver_src.boa__tailwind__technicaldatapackage limit 1
select * from central_prod.bdf_silver_src.boa__tailwind__technicaldatapackagemaster limit 1
select * from central_prod.bdf_silver_src.boa__tailwind__bacpackage limit 1
select * from central_prod.bdf_silver_src.boa__tailwind__bacpackagemaster limit 1
select * from central_prod.bdf_silver_src.boa__tailwind__packageexportrecord limit 1
select * from central_prod.bdf_silver_src.boa__tailwind__receivedpackage limit 1
select * from central_prod.bdf_silver_src.boa__tailwind__managedcollectionkey limit 1
select * from central_prod.bdf_silver_src.boa__tailwind__managedcollection limit 1
select * from central_prod.bdf_silver_src.boa__tailwind__persistedcollection limit 1
select * from central_prod.bdf_silver_src.boa__tailwind__persistedcollectionlivelink limit 1
select * from central_prod.bdf_silver_src.boa__tailwind__persistedcollectionnestinglink limit 1
select * from central_prod.bdf_silver_src.boa__tailwind__persistedcollectionrecipe limit 1
select * from central_prod.bdf_silver_src.boa__tailwind__simplenestedcollection limit 1;






drop table central_prod.central_prod.bdf_silver.tailwind_object_auxiliary_managedcollection_all
drop table central_prod.central_prod.bdf_silver.tailwind_object_core_package_all_by_id
drop table central_prod.central_prod.bdf_silver.tailwind_object_core_package_all_by_version
drop table central_prod.central_prod.bdf_silver.tailwind_object_core_package_deleted_all
drop table central_prod.central_prod.bdf_silver.tailwind_object_links_packagecollectionlink_rolea_to_roleb_all
drop table central_prod.central_prod.bdf_silver.tailwind_object_core_package_deleted_all