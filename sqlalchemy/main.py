#!/home/douglasmg7/miniconda3/envs/fastapi/bin/python
from sqlalchemy import create_engine, text

#  engine = create_engine("sqlite+pysqlite:///:memory:")
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

#  with engine.connect() as conn:
    #  result = conn.execute(text("select 'hello world'"))
    #  print(result.all())

with engine.connect() as conn:
    conn.execute(text("CREATE TABLE some_table (x int, y int)"))
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
    )
    conn.commit()

#  # "begin once"
#  with engine.begin() as conn:
    #  conn.execute(
        #  text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        #  [{"x": 6, "y": 8}, {"x": 9, "y": 10}],
    #  )

with engine.connect() as conn:
    result = conn.execute(text("SELECT x, y FROM some_table"))
    for row in result:
        print(f"x: {row.x}  y: {row.y}")
