ALTER TABLE dim_store_details
	ALTER COLUMN longitude TYPE float USING longitude::double precision,
	ALTER COLUMN locality TYPE varchar (225),
	ALTER COLUMN store_code TYPE varchar (12),
	ALTER COLUMN staff_numbers TYPE smallint USING staff_numbers::smallint,
	ALTER COLUMN opening_date TYPE date ,
	ALTER COLUMN store_type TYPE varchar (225),
	ALTER COLUMN latitude TYPE float USING latitude::double precision,
	ALTER COLUMN country_code TYPE varchar (2),
	ALTER COLUMN continent TYPE varchar (225);
SELECT * FROM dim_store_details
ORDER BY staff_numbers