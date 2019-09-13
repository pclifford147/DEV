from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('mssql+pyodbc://pclifford:Siskin6f@Carousel_UAT_32')
meta = MetaData()

result1 = engine.execute('select top 10 * from [ETL_T24R15].[T24_Borrowers] order by Name1')

for row1 in result1:
    print(row1)

borrowers = Table(
    'T24_Borrowers', meta,
    Column('Name1', String)
    ,schema='ETL_T24R15'
)

# b = borrowers.select()
# conn = engine.connect()
# result = conn.execute(b)

# for row in result:
#    print(row)
