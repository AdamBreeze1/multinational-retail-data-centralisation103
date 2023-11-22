UPDATE dim_products 
	SET product_price = REPLACE(product_price, '£', '');

ALTER TABLE dim_products
ADD COLUMN weight_class VARCHAR(50);

UPDATE dim_products
SET weight_class = 
    CASE 
        WHEN weight_in_kg < 2 THEN 'Light'
        WHEN weight_in_kg >= 2 AND weight_in_kg < 40 THEN 'Mid_Sized'
        WHEN weight_in_kg >= 40 AND weight_in_kg < 140 THEN 'Heavy'
        WHEN weight_in_kg >= 140 THEN 'Truck_Required'
    END;
	
ALTER TABLE dim_products
	ALTER COLUMN product_price TYPE float USING product_price::double precision,
	ALTER COLUMN weight_in_kg TYPE float,
	ALTER COLUMN "EAN" TYPE varchar (20),
	ALTER COLUMN product_code TYPE varchar (12),
	ALTER COLUMN date_added TYPE date,
	ALTER COLUMN uuid TYPE uuid using uuid::uuid,
	--ALTER COLUMN still_avaliable TYPE bool,
	ALTER COLUMN weight_class TYPE varchar (20);

-- Add a new boolean column
ALTER TABLE dim_products
ADD COLUMN is_available BOOLEAN;
-- Update the new column based on the existing values
UPDATE dim_products
SET is_available = (still_avaliable = 'Still_avaliable');
-- Drop the old text column
ALTER TABLE dim_products
DROP COLUMN still_avaliable;

SELECT * FROM dim_products



