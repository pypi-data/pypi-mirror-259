import cls_dao_model_1
import zpgs
import zsqlite
import os

pgs = zpgs.conn(host='will.center', port=3601, database='SYNC_YOUZHAI', user='postgres', password="postgres_pwd")
sqlite = zsqlite.conn(db_path="C:\\AIDE.db")

a = cls_dao_model_1.cls_dao_model()






