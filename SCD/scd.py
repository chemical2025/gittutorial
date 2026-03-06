# SCD TYPE 2 (SQL – Real World):

'''MERGE dim_customer AS target
USING stg_customer AS source
ON target.customer_id = source.customer_id
AND target.is_current = 1

WHEN MATCHED 
AND (
    target.name <> source.name OR
    target.city <> source.city OR
    target.email <> source.email
)
THEN UPDATE SET
    target.end_date = GETDATE(),
    target.is_current = 0

WHEN NOT MATCHED BY TARGET THEN
INSERT (
    customer_id,
    name,
    city,
    email,
    start_date,
    end_date,
    is_current
)
VALUES (
    source.customer_id,
    source.name,
    source.city,
    source.email,
    GETDATE(),
    NULL,
    1
);'''

# SCD TYPE 2 (PySpark – Real World Approach):

# Step 1: Identify changed records

target_df = target_table.toDF()

joined_df = source_df.alias("source").join(
    target_df.alias("target"),
    (col("source.customer_id") == col("target.customer_id")) &
    (col("target.is_current") == 1),
    "left"
)
# Step 2: Filter out changed records

changed_df = joined_df.filter(
    (col("source.name") != col("target.name")) |
    (col("source.city") != col("target.city")) |
    (col("source.email") != col("target.email"))
)

# Step 3: Expire old records

target_table.alias("target").merge(
    changed_df.alias("source"),
    "target.customer_id = source.customer_id AND target.is_current = 1"
).whenMatchedUpdate(
    set={
        "end_date": "current_timestamp()",
        "is_current": "0"
    }
).execute()

# Step 4: Insert new records

new_records = changed_df.select(
    col("source.customer_id"),
    col("source.name"),
    col("source.city"),
    col("source.email"),
    current_timestamp().alias("start_date"),
    lit(None).alias("end_date"),
    lit(1).alias("is_current")
)

new_records.write.format("delta").mode("append").save("/datalake/dim/dim_customer")