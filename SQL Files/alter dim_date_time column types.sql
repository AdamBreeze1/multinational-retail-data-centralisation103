ALTER TABLE dim_date_time
	ALTER COLUMN month TYPE varchar (2),
	ALTER COLUMN year TYPE varchar (4),
	ALTER COLUMN day TYPE varchar (2),
	ALTER COLUMN time_period TYPE varchar,
	ALTER COLUMN date_uuid TYPE uuid USING date_uuid::uuid;

SELECT * FROM dim_date_time