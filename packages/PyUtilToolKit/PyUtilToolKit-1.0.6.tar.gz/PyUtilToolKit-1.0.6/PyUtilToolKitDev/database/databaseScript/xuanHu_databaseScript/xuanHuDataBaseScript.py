# -*- coding:utf-8 -*-
"""
@Time        : 2024/1/8
@File        : xuanHuDataBaseScript.py
@Author      : lyz
@version     : python 3
@Description :
"""
import time

from PyUtilToolKit.base_tool import specifyTime
from PyUtilToolKit.database.database_design.database_base import *

class DbMedpotMiniapp:
    '''
    创建新用户脚本
    '''
    def __init__(self, user_n, password_s, port_n,host_p, database_n):
        self.dbo = DbOperation(user_n=user_n, password_s=password_s, port_n=port_n,host_p=host_p, database_n=database_n)

    def updateUserInfo(self, phone):
        '''
        1、禁用原有用户信息
        update tb_doctor_base_info set is_delete = 0 where phone = '19828304890';
        '''
        self.dbo.update_data('update tb_doctor_base_info set is_delete = 0 where phone = {}'.format(phone))

    def selectUserId(self, phone):
        '''
        2、查询出对应电话的user_id供以下使用
        select user_id from tb_doctor_base_info where phone = '19828304890';
        '''
        user_id = self.dbo.select_data('select user_id from tb_doctor_base_info where phone = {}'.format(phone))
        return user_id[0]["user_id"]

    def chong_zhi_lie_biao_sql(self):

        data = self.dbo.select_data('SELECT count(*) FROM tb_recharge_record '
                'WHERE (user_base_id IN (892458041165238272)) '
                'AND (is_succes IN (0)) '
                'and create_time >= "{}" '
                'ORDER BY create_time DESC'.format(specifyTime(seconds=-300)))
        return data[0]["count(*)"]

    def selectUserIdSec(self, phone):
        '''
        5、查询user_id
        select user_id from tb_doctor_base_info where phone = '19828304890';
        '''
        user_id = self.dbo.select_data('select user_id from tb_doctor_base_info where is_delete = 1 and phone = {}'.format(phone))
        return user_id[0]["user_id"]

    def updateUserInfoSec(self, user_id, phone):
        '''
        6、这里的941679257821667328 来源第五步的查询结果
        update tb_doctor_base_info set user_id = 941679257821667328 where is_delete = 0 and phone = '19828304890';
        delete from tb_doctor_base_info where is_delete = 1 and phone = '19828304890';
        update tb_doctor_base_info set is_delete = 1 where is_delete = 0 and phone = '19828304890';
        '''
        self.dbo.update_data('update tb_doctor_base_info set user_id = {} '
                             'where is_delete = 0 and phone = {}'.format(user_id, phone))
        time.sleep(1)
        self.dbo.delete_data('delete from tb_doctor_base_info where is_delete = 1 and phone = {}'.format(phone))
        time.sleep(1)
        self.dbo.update_data('update tb_doctor_base_info set is_delete = 1 where is_delete = 0 and phone = {}'.format(phone))
class DbMedcrabUserServer:
    '''
    恢复原始用户信息脚本
    '''
    def __init__(self, user_n, password_s, port_n, host_p, database_n):
        self.dbo = DbOperation(user_n=user_n, password_s=password_s, port_n=port_n, host_p=host_p,
                               database_n=database_n)
    def deleteUserData(self, user_id):
        '''
        3、941676340871979008来源 def selectUserId 查询的结果
        delete from tb_user_wechat_bind where user_id = 941676340871979008;
        delete from tb_user_wechat_account where user_id = 941676340871979008;
        delete from tb_user_platform where id = (select platform_user_id from tb_user_medpot where id = 941676340871979008);
        delete from tb_user_medpot where id = 941676340871979008;
        '''
        self.dbo.delete_data('delete from tb_user_wechat_bind where user_id = {}'.format(user_id))
        time.sleep(1)
        self.dbo.delete_data('delete from tb_user_wechat_account where user_id = {}'.format(user_id))
        time.sleep(1)
        self.dbo.delete_data('delete from tb_user_platform where id = '
                             '(select platform_user_id from tb_user_medpot where id = {})'.format(user_id))
        time.sleep(1)
        self.dbo.delete_data('delete from tb_user_medpot where id = {}'.format(user_id))
    def deleteUserOtherData(self, phone):
        '''
        4、删除冗余信息
        delete from tb_user_base_account where user_id = (select id from tb_user where user_phone = '19828304890');
        delete from tb_user_detail where user_id = (select id from tb_user where user_phone = '19828304890');
        delete from tb_user where user_phone = '19828304890';
        '''
        self.dbo.delete_data('delete from tb_user_base_account where user_id ='
                             '(select id from tb_user where user_phone = {})'.format(phone))
        time.sleep(1)
        self.dbo.delete_data('delete from tb_user_detail where user_id ='
                             '(select id from tb_user where user_phone = {})'.format(phone))
        time.sleep(1)
        self.dbo.delete_data("delete from tb_user where user_phone = '{}'".format(phone))

if __name__ == '__main__':
    db = DbMedpotMiniapp(user_n='preuser', password_s='yx@#pre123', port_n=13307,
                      host_p='47.108.223.149', database_n='medpot_miniapp')
    dbo = DbMedcrabUserServer(user_n='preuser', password_s='yx@#pre123', port_n=13307,
                      host_p='47.108.223.149', database_n='medcrab_user_server')
    # db.updateUserInfo(18512805718)
    print(type(db.chong_zhi_lie_biao_sql()))
    # dbo.deleteUserData(db.selectUserId(18512805718))
    # dbo.deleteUserOtherData(18512805718)
    # db.updateUserInfoSec(user_id=db.selectUserIdSec(18512805718),phone=18512805718)

    # db.selectUserId(18512805718)
