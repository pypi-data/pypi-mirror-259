import pymysql
import pymysqlreplication
import logging


# 提取授权操作中的权限
def extract_privileges(sql):
    start_index = sql.index("on") + 2
    end_index = sql.index("to")
    privileges = sql[start_index:end_index].split(",")
    return [privilege.strip() for privilege in privileges]

# 提取授权操作中的用户
def extract_user(sql):
    start_index = sql.index("to") + 2
    end_index = sql.index("@")
    user = sql[start_index:end_index]
    return user.strip()

# 监听binlog并处理事件
def listen_to_binlog():
    try:
        connection_settings = {
            "host": MYSQL_SETTINGS["host"],
            "port": MYSQL_SETTINGS["port"],
            "user": MYSQL_SETTINGS["user"],
            "passwd": MYSQL_SETTINGS["password"]
        }
        stream = pymysqlreplication.BinLogStreamReader(
            connection_settings=connection_settings,
            server_id=100,
            only_events=[pymysqlreplication.events.DeleteRowsEvent, pymysqlreplication.events.WriteRowsEvent, pymysqlreplication.events.UpdateRowsEvent]
        )
        for binlogevent in stream:
            for row in binlogevent.rows:
                event = {"schema": binlogevent.schema, "table": binlogevent.table}
                if isinstance(binlogevent, pymysqlreplication.events.DeleteRowsEvent):
                    event["action"] = "delete"
                    event["data"] = row["values"]
                elif isinstance(binlogevent, pymysqlreplication.events.WriteRowsEvent):
                    event["action"] = "insert"
                    event["data"] = row["values"]
                elif isinstance(binlogevent, pymysqlreplication.events.UpdateRowsEvent):
                    event["action"] = "update"
                    event["data"] = {"before": row["before_values"], "after": row["after_values"]}
                # 权限检查
                if check_permission(event["schema"], event["table"]):
                    # 在此处添加你的操作处理逻辑
                    print(event)
                    logging.info(event)
        stream.close()
    except Exception as e:
        # 异常处理
        logging.error("An error occurred: {}".format(str(e)))

# 主程序
if __name__ == "__main__":
    listen_to_binlog()