# # # # # # # # # x=[1,2,3,4,5]

# # # # # # # # # print(x.pop())

# # # # # # # # name= ['ram','sham','sona']

# # # # # # # # for i in range(len(name)):
# # # # # # # #     print(f'labour {i+1} is {name[i]}')
# # # # # # for i in range(5):
# # # # # #     print((5-i)* '* ')

# # # # # # # for i in range(10):
# # # # # # #     if i%2==0:
# # # # # # #         print(i)

# # # # # paragraph = """Ralph Kimball founded the Kimball Group. Since the mid-1980s, he has been the 
# # # # # data warehouse and business intelligence industry’s thought leader on the dimen
# # # # # sional approach. He has educated tens of thousands of IT professionals. The Toolkit 
# # # # # books written by Ralph and his colleagues have been the industry’s best sellers 
# # # # # since 1996. Prior to working at Metaphor and founding Red Brick Systems, Ralph 
# # # # # coinvented the Star workstation, the fi rst commercial product with windows, icons, 
# # # # # and a mouse, at Xerox’s Palo Alto Research Center (PARC). Ralph has a PhD in 
# # # # # electrical engineering from Stanford University"""

# # # # # para= paragraph.lower().split(' ')
# # # # # # print(para)

# # # # # for i in para:
# # # # #     if i == 'the':
# # # # #         count = count+1
# # # # #     else:
# # # # #         continue
# # # # # print(count)
# # # import time
# # # name = ['ram','sham','sona']
# # # name_iter=0
# # # while(name_iter<len(name)):
# # #     print(name[name_iter])
# # #     time.sleep(3)
# # #     name_iter+=1

# # # print("1.Add\n2.Sub\n3.Multi\n4.Divid")
# # # while(True):
# # #     p=int(input('pls enter your choice : '))
# # #     if(p==1):
# # #         x=int(input("Enter the first number "))
# # #         y=int(input("Enter the second Number "))
# # #         z=(x+y)
# # #         print(z)
# # #     if(p==2):
# # #         x=int(input("Enter the first number "))
# # #         y=int(input("Enter the second Number "))
# # #         z=(x-y)
# # #         print(z)
# # #     if(p==3):
# # #         x=int(input("Enter the first number "))
# # #         y=int(input("Enter the second Number "))
# # #         z=(x*y)
# # #         print(z)
# # #     if(p==4):
# # #         x=int(input("Enter the first number "))
# # #         y=int(input("Enter the second Number "))
# # #         if (y!=0):
# # #             z1=(x/y)
# # #             print(z1)
# # #         else:
# # #             print("division can't possible")


# # x= list(range(0,11))
# # new_lst=[]
# # for i in x:
# #     if i%2==0:
# #      new_lst.append('even')
# #     else:
# #        new_lst.append('odd')
# # print(new_lst)

# # Python program to execute 
# # main directly 
# print ("Always executed")

# if __name__ == "__main__": 
# 	print ("Executed when invoked directly")
# else: 
# 	print ("Executed when imported")


from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, rand, unix_timestamp, current_date, monotonically_increasing_id
from pyspark.sql.types import StringType, DoubleType, LongType
from dbgenerator import Table, Column, Generator
import random
from datetime import datetime
# Initialize Spark session
spark = SparkSession.builder.master("local[*]").appName("SyntheticDataPipeline").getOrCreate()
# Define table schema for synthetic data using dbgenerator
def create_table_schema():
    table = Table("synthetic_data")
    table.add_column(Column("uuid", "uuid"))
    table.add_column(Column("transaction_id", "integer", min=1000000000, max=9999999999))
    table.add_column(Column("merchant_name", "name"))
    table.add_column(Column("transaction_city", "city"))
    table.add_column(Column("location_zip", "zipcode"))
    table.add_column(Column("merchant_state_code", "enum", values=["NM", "CA", "NY"]))
    table.add_column(Column("merchant_category", "enum", values=["5814", "5912", "5411"]))
    table.add_column(Column("transaction_country", "static", value="USA"))
    table.add_column(Column("transaction_date", "datetime", start="-30d", end="now"))
    table.add_column(Column("transaction_amount", "float", min=5.0, max=100.0))
    table.add_column(Column("tran_code", "enum", values=["MA", "02"]))
    table.add_column(Column("input_source", "enum", values=["01", "02"]))
    table.add_column(Column("approve_decline_code", "enum", values=["A", "R"]))
    table.add_column(Column("transaction_currency", "static", value="840"))
    table.add_column(Column("card_present_code", "integer", min=0, max=9))
    table.add_column(Column("transaction_state_name", "state"))
    table.add_column(Column("terminal_id", "pattern", pattern="??????"))
    table.add_column(Column("transaction_auth_code", "integer", min=100000, max=999999))
    table.add_column(Column("client_number", "integer", min=1000, max=9999))
    table.add_column(Column("system", "integer", min=1000, max=9999))
    table.add_column(Column("prin", "integer", min=1000, max=9999))
    table.add_column(Column("agent", "integer", min=1000, max=9999))
    table.add_column(Column("card_label", "enum", values=["Visa", "Mastercard"]))
    table.add_column(Column("card_type", "enum", values=["0-Full Credit", "1-Full Debit"]))
    table.add_column(Column("load_date", "static", value=datetime.now().strftime("%Y%m%d")))
    table.add_column(Column("source_publish_date", "timestamp"))
    return table
# Generate synthetic data
def generate_synthetic_data():
    table_schema = create_table_schema()
    generator = Generator([table_schema])
    data = generator.generate("synthetic_data", 1000)  # Generate 1000 records
    return spark.createDataFrame(data)
# Validate data
def validate_data(dataframe):
    validation_report = {
        "column_name": [],
        "null_count": [],
        "unique_count": [],
        "min_value": [],
        "max_value": [],
        "valid": []
    }
    for col_name in dataframe.columns:
        column = dataframe.select(col_name)
        null_count = column.filter(col(col_name).isNull()).count()
        unique_count = column.distinct().count()
        # Initialize min and max values as None
        min_value, max_value = None, None
        # Compute min and max values for numeric columns
        if dataframe.schema[col_name].dataType in [DoubleType(), LongType()]:
            min_value = column.select(col_name).rdd.min()[0]
            max_value = column.select(col_name).rdd.max()[0]
        validation_report["column_name"].append(col_name)
        validation_report["null_count"].append(null_count)
        validation_report["unique_count"].append(unique_count)
        validation_report["min_value"].append(min_value)
        validation_report["max_value"].append(max_value)
        # Check if data is valid (no nulls and reasonable unique count)
        validation_report["valid"].append(null_count == 0 and unique_count > 0)
    return validation_report
# Generate final data
final_data = generate_synthetic_data()
# Validate final data
validation_results = validate_data(final_data)
for key, values in validation_results.items():
    print(f"{key}: {values}")
# Display final dataset
final_data.show(10, truncate=False)