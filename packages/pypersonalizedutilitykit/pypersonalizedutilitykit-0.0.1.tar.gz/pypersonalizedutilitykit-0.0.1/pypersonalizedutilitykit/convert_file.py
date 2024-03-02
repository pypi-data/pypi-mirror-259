# -*- coding:utf-8 -*-
"""
@Time        : 2023/10/28
@File        : convert_file.py
@Author      : lyz
@version     : python 3
@Description :
"""
# def convert_to_json_file(dt,pth,**kw):
#     '''
#     将python字典(db_data)转换为json字符串写入文件中
#     '''
#     filename = kw['dbtype'] + '_' + kw['description'] + '_' + dt['pdb']['db_name'] + '.json'
#     with open(os.path.join(pth,filename),'w', encoding="utf-8") as fp:
#         json.dump(dt,fp,indent=1)
#     return filename
#
# def convert_to_dict(jdir,jfile):
#     '''
#     读取json文件中的数据，转换为python字典
#     '''
#     ret = None
#     jnfile = os.path.join(jdir,jfile)
#     with open(jnfile,'r', encoding="utf-8") as fp:
#         ret = json.load(fp)
#     return ret