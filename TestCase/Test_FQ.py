# -*- coding: utf-8 -*-
# Created by iFantastic on 2018/12/23
"""

author: jaxon
create time: 2018/12/23

"""
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco.drivers.unity3d import UnityPoco
from Config.VarConfig import *



def Login():
    poco = AndroidUiautomationPoco()
    '''时间戳'''
    T = int(time.time())
    '''清除APP数据'''
    clear_app("com.huifenqi.broker")
    '''启动APP'''
    start_app("com.huifenqi.broker")
    '''等待5S'''
    # sleep(5)
    '''等待某个元素出现'''
    account = poco("com.huifenqi.broker:id/et_account")
    poco.wait_for_any([account])
    '''帐号输入框'''
    account_box = poco("com.huifenqi.broker:id/et_account")
    account_box.click()
    account_box.set_text('18301065521')
    '''密码输入框'''
    password_box = poco("com.huifenqi.broker:id/et_password")
    password_box.click()
    password_box.set_text('123456')
    '''点击登录'''
    poco("com.huifenqi.broker:id/tv_login").click()
    toast = poco("com.huifenqi.broker:id/tv_cancle")
    poco.wait_for_all([toast])
    txt = toast.get_text()
    return txt


def SetRentInfo():
    poco = AndroidUiautomationPoco()
    '''时间戳'''
    T = int(time.time())
    '''清除APP数据'''
    clear_app("com.huifenqi.broker")
    '''启动APP'''
    start_app("com.huifenqi.broker")
    '''等待5S'''
    # sleep(5)
    '''等待某个元素出现'''
    account = poco("com.huifenqi.broker:id/et_account")
    poco.wait_for_any([account])
    '''帐号输入框'''
    account_box = poco("com.huifenqi.broker:id/et_account")
    account_box.click()
    account_box.set_text('18301065521')
    '''密码输入框'''
    password_box = poco("com.huifenqi.broker:id/et_password")
    password_box.click()
    password_box.set_text('123456')
    '''点击登录'''
    poco("com.huifenqi.broker:id/tv_login").click()
    toast = poco("com.huifenqi.broker:id/tv_cancle")
    poco.wait_for_all([toast])
    '''"发现新版本"浮层处理'''
    toast = poco("com.huifenqi.broker:id/tv_cancle")
    '''判断如果有此元素则点击“以后再说”,如果无此元素则pass'''
    try:
        if toast.exists():
            poco("com.huifenqi.broker:id/tv_cancle").click()
    except:
        pass
    poco("android.widget.ImageView").click()
    '''点击分期合同button'''
    poco("com.huifenqi.broker:id/contract_img").click()
    poco("com.huifenqi.broker:id/tv_commit").click()
    '''创建分期合同'''
    poco("com.huifenqi.broker:id/iv_new_con").click()
    '''点击租客姓名输入框'''
    poco("com.huifenqi.broker:id/et_zuke_name").click()
    '''输入租客姓名'''
    poco("com.huifenqi.broker:id/et_zuke_name").set_text("陈杰")
    '''点击租客电话输入框、输入租客电话....'''
    poco("com.huifenqi.broker:id/et_zuke_phone").click()
    poco("com.huifenqi.broker:id/et_zuke_phone").set_text("18301065521")
    poco("com.huifenqi.broker:id/et_zuke_idnum").click()
    poco("com.huifenqi.broker:id/et_zuke_idnum").set_text("41032319921205451X")
    poco("com.huifenqi.broker:id/tv_rental_type").click()
    poco(text="合租").click()
    poco("com.huifenqi.broker:id/et_community_name").click()
    poco("com.huifenqi.broker:id/et_community_name").set_text(("小区名称%d")%T)
    poco("com.huifenqi.broker:id/et_house_number").click()
    poco("com.huifenqi.broker:id/et_house_number").set_text(("门牌号%d")%T)
    # poco("com.huifenqi.broker:id/et_room_number").click()
    poco("com.huifenqi.broker:id/et_room_number").set_text(("房间号%d")%T)
    intro = poco("com.huifenqi.broker:id/btn")
    able = intro.attr('enabled')
    return able


def SetInstallment():
    poco = AndroidUiautomationPoco()
    # 时间戳
    T = int(time.time())
    # 清除APP数据
    clear_app("com.huifenqi.broker")
    '''启动APP'''
    start_app("com.huifenqi.broker")
    '''等待某个元素出现'''
    account = poco("com.huifenqi.broker:id/et_account")
    poco.wait_for_any([account])
    '''帐号输入框'''
    account_box = poco("com.huifenqi.broker:id/et_account")
    account_box.click()
    account_box.set_text('18301065521')
    '''密码输入框'''
    password_box = poco("com.huifenqi.broker:id/et_password")
    password_box.click()
    password_box.set_text('123456')
    '''点击登录'''
    poco("com.huifenqi.broker:id/tv_login").click()
    toast = poco("com.huifenqi.broker:id/tv_cancle")
    poco.wait_for_all([toast])
    '''"发现新版本"浮层处理'''
    toast = poco("com.huifenqi.broker:id/tv_cancle")
    '''判断如果有此元素则点击“以后再说”,如果无此元素则pass'''
    try:
        if toast.exists():
            poco("com.huifenqi.broker:id/tv_cancle").click()
    except:
        pass
    poco("android.widget.ImageView").click()
    '''点击分期合同button'''
    poco("com.huifenqi.broker:id/contract_img").click()
    poco("com.huifenqi.broker:id/tv_commit").click()
    '''创建分期合同'''
    poco("com.huifenqi.broker:id/iv_new_con").click()
    '''点击租客姓名输入框'''
    poco("com.huifenqi.broker:id/et_zuke_name").click()
    '''输入租客姓名'''
    poco("com.huifenqi.broker:id/et_zuke_name").set_text("陈杰")
    '''点击租客电话输入框、输入租客电话....'''
    poco("com.huifenqi.broker:id/et_zuke_phone").click()
    poco("com.huifenqi.broker:id/et_zuke_phone").set_text("18301065521")
    poco("com.huifenqi.broker:id/et_zuke_idnum").click()
    poco("com.huifenqi.broker:id/et_zuke_idnum").set_text("41032319921205451X")
    poco("com.huifenqi.broker:id/tv_rental_type").click()
    poco(text="合租").click()
    poco("com.huifenqi.broker:id/et_community_name").click()
    poco("com.huifenqi.broker:id/et_community_name").set_text(("小区名称%d") % T)
    poco("com.huifenqi.broker:id/et_house_number").click()
    poco("com.huifenqi.broker:id/et_house_number").set_text(("门牌号%d") % T)
    poco("com.huifenqi.broker:id/et_room_number").click()
    poco("com.huifenqi.broker:id/et_room_number").set_text(("房间号%d") % T)

    '''点击下一步button'''
    poco("com.huifenqi.broker:id/btn").click()
    poco("com.huifenqi.broker:id/et_paymoney").click()
    poco("com.huifenqi.broker:id/et_paymoney").set_text("0.01")
    '''起租日'''
    poco("com.huifenqi.broker:id/tv_date_start").click()
    try:
        if poco("com.huifenqi.broker:id/tvTitle").exists():
            poco("com.huifenqi.broker:id/btnSubmit").click()
    except:
        pass
    '''到期日'''
    poco("com.huifenqi.broker:id/tv_date_end").click()
    try:
        if poco("com.huifenqi.broker:id/tvTitle").exists():
            poco("android:id/numberpicker_input").swipe([-0.026, -0.1003])
            poco("com.huifenqi.broker:id/btnSubmit").click()
    except:
        pass
    '''收付款方式'''
    poco("com.huifenqi.broker:id/tv_pay_type").click()
    poco("com.huifenqi.broker:id/btnSubmit").click()
    intro = poco("com.huifenqi.broker:id/btn")
    FQable = intro.attr('enabled')
    return FQable


def CreateContract():
    poco = AndroidUiautomationPoco()
    # '''时间戳'''
    T = int(time.time())
    # '''清除APP数据'''
    clear_app("com.huifenqi.broker")
    '''启动APP'''
    start_app("com.huifenqi.broker")
    '''等待5S'''
    # sleep(5)
    '''等待某个元素出现'''
    account = poco("com.huifenqi.broker:id/et_account")
    poco.wait_for_any([account])
    '''帐号输入框'''
    account_box = poco("com.huifenqi.broker:id/et_account")
    account_box.click()
    account_box.set_text('18301065521')
    '''密码输入框'''
    password_box = poco("com.huifenqi.broker:id/et_password")
    password_box.click()
    password_box.set_text('123456')
    '''点击登录'''
    poco("com.huifenqi.broker:id/tv_login").click()
    toast = poco("com.huifenqi.broker:id/tv_cancle")
    poco.wait_for_all([toast])
    txt = toast.get_text()

    # sleep(8)
    '''"发现新版本"浮层处理'''
    toast = poco("com.huifenqi.broker:id/tv_cancle")
    '''判断如果有此元素则点击“以后再说”,如果无此元素则pass'''
    try:
        if toast.exists():
            poco("com.huifenqi.broker:id/tv_cancle").click()
    except:
        pass
    poco("android.widget.ImageView").click()
    '''点击分期合同button'''
    poco("com.huifenqi.broker:id/contract_img").click()
    poco("com.huifenqi.broker:id/tv_commit").click()
    '''创建分期合同'''
    poco("com.huifenqi.broker:id/iv_new_con").click()
    '''点击租客姓名输入框'''
    poco("com.huifenqi.broker:id/et_zuke_name").click()
    '''输入租客姓名'''
    poco("com.huifenqi.broker:id/et_zuke_name").set_text("陈杰")
    '''点击租客电话输入框、输入租客电话....'''
    poco("com.huifenqi.broker:id/et_zuke_phone").click()
    poco("com.huifenqi.broker:id/et_zuke_phone").set_text("18301065521")
    poco("com.huifenqi.broker:id/et_zuke_idnum").click()
    poco("com.huifenqi.broker:id/et_zuke_idnum").set_text("41032319921205451X")
    poco("com.huifenqi.broker:id/tv_rental_type").click()
    poco(text="合租").click()
    poco("com.huifenqi.broker:id/et_community_name").click()
    poco("com.huifenqi.broker:id/et_community_name").set_text(("小区名称%d") % T)
    poco("com.huifenqi.broker:id/et_house_number").click()
    poco("com.huifenqi.broker:id/et_house_number").set_text(("门牌号%d") % T)
    poco("com.huifenqi.broker:id/et_room_number").click()
    poco("com.huifenqi.broker:id/et_room_number").set_text(("房间号%d") % T)

    '''点击下一步button'''
    poco("com.huifenqi.broker:id/btn").click()
    poco("com.huifenqi.broker:id/et_paymoney").click()
    poco("com.huifenqi.broker:id/et_paymoney").set_text("0.01")
    '''起租日'''
    poco("com.huifenqi.broker:id/tv_date_start").click()
    try:
        if poco("com.huifenqi.broker:id/tvTitle").exists():
            poco("com.huifenqi.broker:id/btnSubmit").click()
    except:
        pass
    '''到期日'''
    poco("com.huifenqi.broker:id/tv_date_end").click()
    try:
        if poco("com.huifenqi.broker:id/tvTitle").exists():
            poco("android:id/numberpicker_input").swipe([-0.026, -0.1003])
            poco("com.huifenqi.broker:id/btnSubmit").click()
    except:
        pass
    '''收付款方式'''
    poco("com.huifenqi.broker:id/tv_pay_type").click()
    poco("com.huifenqi.broker:id/btnSubmit").click()
    '''点击下一步button'''
    poco("com.huifenqi.broker:id/btn").click()
    '''点击确定button'''
    poco("com.huifenqi.broker:id/btn").click()
    poco("com.huifenqi.broker:id/grid_lc").child("android.widget.LinearLayout")[1].child(
        "android.widget.RelativeLayout").child("com.huifenqi.broker:id/image").click()

    '''从相册选择照片'''
    poco("android.widget.LinearLayout")[1].child("com.huifenqi.broker:id/tv_item").click()
    poco("com.huifenqi.broker:id/id_gridView").child("android.widget.RelativeLayout")[0].child(
        "com.huifenqi.broker:id/id_item_select").click()
    poco("com.huifenqi.broker:id/tv_title_right").click()
    '''点击提交button'''
    poco("com.huifenqi.broker:id/btn").click()
    sleep(3)
    '''重复合同浮层文案处理'''
    try:
        if poco("android:id/alertTitle").exists():
            poco("android:id/button1").click()
    except:
        pass
    End_txt = poco(text="合同号")
    poco.wait_for_any([End_txt])
    Contract_ui = poco("com.huifenqi.broker:id/tv_con_num")
    Contract_no = Contract_ui.attr("text")
    print("合同号为：", Contract_no)
    Title_txt = poco("com.huifenqi.broker:id/tv_qrcode_info")
    Title = Title_txt.get_text()
    return Title




if __name__ == '__main__':
    pass