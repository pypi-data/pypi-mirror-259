# coding=utf-8
import datetime as dt
import pandas
from sqlalchemy import text

# 数据库连接
td_config = {}  # dict


# 查询行情数据（股票）
def td_stock(
    startDate: dt.datetime,
    symbol: str,
    count: int = 1,
    unit: str = "1d",
    fields: list = ["open", "close", "high", "low", "volume", "money"],
    skip_paused=True,
    skip_st=False,
    df=True,
):
    conn = td_db_connect()
    with conn:
        s_table = "s_stocks_day"
        if unit == "1m":
            s_table = "s_stocks_minute"

        sql = 'SELECT %s FROM %s WHERE `symbol` = "%s" %s ORDER BY start_date DESC LIMIT %d;'
        where = ""

        if skip_st is True:
            where += "AND `isST` = 1"

        if skip_paused is True:
            where += "AND `isPaused` = 1"

        sql = sql % (fields, s_table, symbol, where, count)
        conn = taosws.connect("taosws://root:taosdata@localhost:6041")

        conn.select_db("financial")

        if df is True:
            result: pandas.DataFrame = pandas.read_sql(text(sql), conn)
        else:
            result = conn.query(sql)
            result = result.fetch_all()

        return result
