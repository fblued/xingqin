# coding:utf-8
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xiangqin.settings')

import django
django.setup()

from project_1.models import Female,Man


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
    return p

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name,views=views,likes=likes)[0]
    return c
'''name,  sex, age, education, Occupation,
	height, weight, BJHouseholds, car, house, hometown, 
	require, flag, WxNo, message

, sex = sex, age = age, education =education,
		Occupation=Occupation, weight=weight, BJHouseholds = BJHouseholds, car=car,
		house=house, hometown=hometown, flag=flag, WxNo=WxNo, message=message

, sex="f", age=18, education="初中",Occupation="在读",
   	height=140, weight = 25, BJHouseholds = False, car= False, house=False,
   	hometown="x", require="x", flag=False, WxNo="11", message="x"
	'''
def add_Female(name,  sex, age, education, Occupation,
	height, weight, BJHouseholds, car, house,  flag,
        hometown="",require="",  WxNo="", message="",img="") :
	f = Female.objects.get_or_create(name = name, sex = sex, age = age, education =education,
		Occupation=Occupation, weight=weight, BJHouseholds = BJHouseholds, car=car,
		house=house, hometown=hometown, flag=flag, WxNo=WxNo, message=message,
		img=img)[0]
	return f

def add_Man(name,  sex, age, education, Occupation, 
        height, weight, BJHouseholds, car, house,  flag,
        hometown="",require="",  WxNo="", message="",img="") :
        m = Man.objects.get_or_create(name = name, sex = sex, age = age, education =education,
            Occupation=Occupation, weight=weight, BJHouseholds = BJHouseholds, car=car,
            house=house, hometown=hometown, flag=flag, WxNo=WxNo, message=message,
            img=img)[0]
        return m

def populate():

  add_Female(name="f_1", sex="f", age=35, education="大专", Occupation="在读", height=109, weight=180, BJHouseholds=False, car=False, house=False, flag=False, img="001.jpg")
  add_Female(name="f_2", sex="f", age=42, education="大专", Occupation="在读", height=133, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="002.jpg")
  add_Female(name="f_3", sex="f", age=43, education="大专", Occupation="私企白领", height=200, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="003.jpg")
  add_Female(name="f_4", sex="f", age=44, education="硕士", Occupation="国企", height=111, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="004.jpg")
  add_Female(name="f_5", sex="f", age=44, education="大本", Occupation="在读", height=151, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="005.jpg")
  add_Female(name="f_6", sex="f", age=46, education="大专", Occupation="国企", height=193, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="006.jpg")
  add_Female(name="f_7", sex="f", age=44, education="初中", Occupation="在读", height=111, weight=180, BJHouseholds=False, car=False, house=False, flag=False, img="007.jpg")
  add_Female(name="f_8", sex="f", age=35, education="硕士", Occupation="自由职业", height=200, weight=180, BJHouseholds=False, car=False, house=False, flag=False, img="008.jpg")
  add_Female(name="f_9", sex="f", age=40, education="大本", Occupation="自由职业", height=202, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="009.jpg")
  add_Female(name="f_10", sex="f", age=47, education="博士", Occupation="国企", height=188, weight=100, BJHouseholds=False, car=False, house=False, flag=False, img="010.jpg")
  add_Female(name="f_11", sex="f", age=42, education="初中", Occupation="国企", height=214, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="011.jpg")
  add_Female(name="f_12", sex="f", age=46, education="大专", Occupation="在读", height=208, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="012.jpg")
  add_Female(name="f_13", sex="f", age=39, education="博士", Occupation="私企白领", height=189, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="013.jpg")
  add_Female(name="f_14", sex="f", age=40, education="大专", Occupation="国企", height=200, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="014.jpg")
  add_Female(name="f_15", sex="f", age=46, education="大专", Occupation="其他", height=162, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="015.jpg")
  add_Female(name="f_16", sex="f", age=35, education="高中", Occupation="公务员", height=168, weight=180, BJHouseholds=False, car=False, house=False, flag=False, img="016.jpg")
  add_Female(name="f_17", sex="f", age=46, education="博士", Occupation="公务员", height=156, weight=100, BJHouseholds=False, car=False, house=False, flag=False, img="017.jpg")
  add_Female(name="f_18", sex="f", age=43, education="大专", Occupation="公务员", height=106, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="018.jpg")
  add_Female(name="f_19", sex="f", age=40, education="高中", Occupation="自由职业", height=194, weight=100, BJHouseholds=False, car=False, house=False, flag=False, img="019.jpg")
  add_Female(name="f_20", sex="f", age=49, education="博士", Occupation="其他", height=173, weight=100, BJHouseholds=False, car=False, house=False, flag=False, img="020.jpg")
  add_Female(name="f_21", sex="f", age=48, education="博士", Occupation="在读", height=209, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="021.jpg")
  add_Female(name="f_22", sex="f", age=48, education="高中", Occupation="私企白领", height=146, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="022.jpg")
  add_Female(name="f_23", sex="f", age=43, education="高中", Occupation="公务员", height=154, weight=180, BJHouseholds=False, car=False, house=False, flag=False, img="023.jpg")
  add_Female(name="f_24", sex="f", age=37, education="大专", Occupation="在读", height=219, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="024.jpg")
  add_Female(name="f_25", sex="f", age=45, education="硕士", Occupation="其他", height=219, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="025.jpg")
  add_Female(name="f_26", sex="f", age=38, education="高中", Occupation="在读", height=206, weight=180, BJHouseholds=False, car=False, house=False, flag=False, img="026.jpg")
  add_Female(name="f_27", sex="f", age=36, education="硕士", Occupation="其他", height=167, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="027.jpg")
  add_Female(name="f_28", sex="f", age=40, education="大本", Occupation="公务员", height=147, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="028.jpg")
  add_Female(name="f_29", sex="f", age=40, education="初中", Occupation="国企", height=191, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="029.jpg")
  add_Female(name="f_30", sex="f", age=43, education="高中", Occupation="私企白领", height=168, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="030.jpg")
  add_Female(name="f_31", sex="f", age=36, education="硕士", Occupation="公务员", height=179, weight=100, BJHouseholds=False, car=False, house=False, flag=False, img="031.jpg")
  add_Female(name="f_32", sex="f", age=43, education="硕士", Occupation="私企白领", height=183, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="032.jpg")
  add_Female(name="f_33", sex="f", age=48, education="高中", Occupation="公务员", height=173, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="033.jpg")
  add_Female(name="f_34", sex="f", age=46, education="大本", Occupation="公务员", height=134, weight=180, BJHouseholds=False, car=False, house=False, flag=False, img="034.jpg")
  add_Female(name="f_35", sex="f", age=43, education="大专", Occupation="其他", height=203, weight=100, BJHouseholds=False, car=False, house=False, flag=False, img="035.jpg")
  add_Female(name="f_36", sex="f", age=40, education="博士", Occupation="私企白领", height=140, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="036.jpg")
  add_Female(name="f_37", sex="f", age=43, education="高中", Occupation="自由职业", height=213, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="037.jpg")
  add_Female(name="f_38", sex="f", age=38, education="硕士", Occupation="公务员", height=113, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="038.jpg")
  add_Female(name="f_39", sex="f", age=38, education="博士", Occupation="公务员", height=111, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="039.jpg")
  add_Female(name="f_40", sex="f", age=36, education="博士", Occupation="自由职业", height=201, weight=180, BJHouseholds=False, car=False, house=False, flag=False, img="040.jpg")
  add_Female(name="f_41", sex="f", age=40, education="初中", Occupation="私企白领", height=155, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="041.jpg")
  add_Female(name="f_42", sex="f", age=48, education="高中", Occupation="其他", height=137, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="042.jpg")
  add_Female(name="f_43", sex="f", age=36, education="大本", Occupation="国企", height=137, weight=100, BJHouseholds=False, car=False, house=False, flag=False, img="043.jpg")
  add_Female(name="f_44", sex="f", age=37, education="高中", Occupation="其他", height=151, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="044.jpg")
  add_Female(name="f_45", sex="f", age=46, education="高中", Occupation="公务员", height=144, weight=100, BJHouseholds=False, car=False, house=False, flag=False, img="045.jpg")
  add_Female(name="f_46", sex="f", age=35, education="初中", Occupation="公务员", height=168, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="046.jpg")
  add_Female(name="f_47", sex="f", age=47, education="博士", Occupation="公务员", height=208, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="047.jpg")
  add_Female(name="f_48", sex="f", age=43, education="大本", Occupation="国企", height=208, weight=100, BJHouseholds=False, car=False, house=False, flag=False, img="048.jpg")
  add_Female(name="f_49", sex="f", age=48, education="博士", Occupation="其他", height=210, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="049.jpg")
  add_Female(name="f_50", sex="f", age=44, education="初中", Occupation="私企白领", height=149, weight=180, BJHouseholds=False, car=False, house=False, flag=False, img="050.jpg")
  add_Female(name="f_51", sex="f", age=49, education="初中", Occupation="自由职业", height=190, weight=180, BJHouseholds=False, car=False, house=False, flag=False, img="051.jpg")
  add_Female(name="f_52", sex="f", age=37, education="初中", Occupation="在读", height=139, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="052.jpg")
  add_Female(name="f_53", sex="f", age=40, education="初中", Occupation="自由职业", height=157, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="053.jpg")
  add_Female(name="f_54", sex="f", age=40, education="硕士", Occupation="自由职业", height=172, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="054.jpg")
  add_Female(name="f_55", sex="f", age=40, education="大本", Occupation="私企白领", height=103, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="055.jpg")
  add_Female(name="f_56", sex="f", age=49, education="初中", Occupation="公务员", height=215, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="056.jpg")
  add_Female(name="f_57", sex="f", age=49, education="初中", Occupation="自由职业", height=211, weight=100, BJHouseholds=False, car=False, house=False, flag=False, img="057.jpg")
  add_Female(name="f_58", sex="f", age=35, education="大专", Occupation="自由职业", height=219, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="058.jpg")
  add_Female(name="f_59", sex="f", age=39, education="硕士", Occupation="国企", height=212, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="059.jpg")
  add_Female(name="f_60", sex="f", age=49, education="硕士", Occupation="其他", height=175, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="060.jpg")
  add_Female(name="f_61", sex="f", age=40, education="大专", Occupation="国企", height=113, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="061.jpg")
  add_Female(name="f_62", sex="f", age=48, education="高中", Occupation="其他", height=158, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="062.jpg")
  add_Female(name="f_63", sex="f", age=49, education="大本", Occupation="自由职业", height=113, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="063.jpg")
  add_Female(name="f_64", sex="f", age=39, education="硕士", Occupation="在读", height=135, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="064.jpg")
  add_Female(name="f_65", sex="f", age=35, education="初中", Occupation="在读", height=155, weight=100, BJHouseholds=False, car=False, house=False, flag=False, img="065.jpg")
  add_Female(name="f_66", sex="f", age=44, education="初中", Occupation="其他", height=214, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="066.jpg")
  add_Female(name="f_67", sex="f", age=45, education="初中", Occupation="自由职业", height=146, weight=180, BJHouseholds=False, car=False, house=False, flag=False, img="067.jpg")
  add_Female(name="f_68", sex="f", age=39, education="博士", Occupation="自由职业", height=197, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="068.jpg")
  add_Female(name="f_69", sex="f", age=49, education="博士", Occupation="自由职业", height=122, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="069.jpg")
  add_Female(name="f_70", sex="f", age=41, education="高中", Occupation="在读", height=190, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="070.jpg")
  add_Female(name="f_71", sex="f", age=43, education="硕士", Occupation="在读", height=164, weight=100, BJHouseholds=False, car=False, house=False, flag=False, img="071.jpg")
  add_Female(name="f_72", sex="f", age=46, education="大本", Occupation="私企白领", height=154, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="072.jpg")
  add_Female(name="f_73", sex="f", age=38, education="大专", Occupation="其他", height=212, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="073.jpg")
  add_Female(name="f_74", sex="f", age=38, education="大专", Occupation="其他", height=103, weight=100, BJHouseholds=False, car=False, house=False, flag=False, img="074.jpg")
  add_Female(name="f_75", sex="f", age=45, education="大专", Occupation="国企", height=122, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="075.jpg")
  add_Female(name="f_76", sex="f", age=41, education="硕士", Occupation="公务员", height=218, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="076.jpg")
  add_Female(name="f_77", sex="f", age=49, education="大专", Occupation="其他", height=172, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="077.jpg")
  add_Female(name="f_78", sex="f", age=37, education="大专", Occupation="公务员", height=103, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="078.jpg")
  add_Female(name="f_79", sex="f", age=48, education="初中", Occupation="国企", height=182, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="079.jpg")
  add_Female(name="f_80", sex="f", age=45, education="高中", Occupation="其他", height=202, weight=180, BJHouseholds=False, car=False, house=False, flag=False, img="080.jpg")
  add_Female(name="f_81", sex="f", age=42, education="高中", Occupation="自由职业", height=106, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="081.jpg")
  add_Female(name="f_82", sex="f", age=36, education="硕士", Occupation="自由职业", height=124, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="082.jpg")
  add_Female(name="f_83", sex="f", age=37, education="硕士", Occupation="国企", height=178, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="083.jpg")
  add_Female(name="f_84", sex="f", age=48, education="博士", Occupation="其他", height=200, weight=100, BJHouseholds=False, car=False, house=False, flag=False, img="084.jpg")
  add_Female(name="f_85", sex="f", age=46, education="高中", Occupation="其他", height=117, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="085.jpg")
  add_Female(name="f_86", sex="f", age=40, education="大专", Occupation="自由职业", height=166, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="086.jpg")
  add_Female(name="f_87", sex="f", age=44, education="初中", Occupation="国企", height=111, weight=100, BJHouseholds=False, car=False, house=False, flag=False, img="087.jpg")
  add_Female(name="f_88", sex="f", age=46, education="大本", Occupation="在读", height=200, weight=180, BJHouseholds=False, car=False, house=False, flag=False, img="088.jpg")
  add_Female(name="f_89", sex="f", age=46, education="初中", Occupation="在读", height=183, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="089.jpg")
  add_Female(name="f_90", sex="f", age=43, education="硕士", Occupation="其他", height=212, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="090.jpg")
  add_Female(name="f_91", sex="f", age=38, education="硕士", Occupation="在读", height=100, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="091.jpg")
  add_Female(name="f_92", sex="f", age=38, education="大本", Occupation="私企白领", height=189, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="092.jpg")
  add_Female(name="f_93", sex="f", age=47, education="硕士", Occupation="私企白领", height=177, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="093.jpg")
  add_Female(name="f_94", sex="f", age=42, education="初中", Occupation="国企", height=182, weight=180, BJHouseholds=False, car=False, house=False, flag=False, img="094.jpg")
  add_Female(name="f_95", sex="f", age=45, education="大本", Occupation="国企", height=202, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="095.jpg")
  add_Female(name="f_96", sex="f", age=39, education="硕士", Occupation="自由职业", height=101, weight=100, BJHouseholds=False, car=False, house=False, flag=False, img="096.jpg")
  add_Female(name="f_97", sex="f", age=44, education="大本", Occupation="国企", height=176, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="097.jpg")
  add_Female(name="f_98", sex="f", age=41, education="大本", Occupation="国企", height=213, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="098.jpg")
  add_Female(name="f_99", sex="f", age=45, education="高中", Occupation="自由职业", height=111, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="099.jpg")
  add_Female(name="f_100", sex="f", age=41, education="大本", Occupation="在读", height=202, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="100.jpg")


  add_Man(name="m_1", sex="m", age=36, education="硕士", Occupation="在读", height=205, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="/man/001.jpg")
  add_Man(name="m_2", sex="m", age=36, education="高中", Occupation="在读", height=131, weight=180, BJHouseholds=False, car=False, house=False, flag=False, img="/man/002.jpg")
  add_Man(name="m_3", sex="m", age=35, education="初中", Occupation="国企", height=161, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="/man/003.jpg")
  add_Man(name="m_4", sex="m", age=38, education="大专", Occupation="其他", height=211, weight=180, BJHouseholds=False, car=False, house=False, flag=False, img="/man/004.jpg")
  add_Man(name="m_5", sex="m", age=42, education="初中", Occupation="公务员", height=144, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="/man/005.jpg")
  add_Man(name="m_6", sex="m", age=49, education="硕士", Occupation="公务员", height=173, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="/man/006.jpg")
  add_Man(name="m_7", sex="m", age=48, education="大专", Occupation="公务员", height=155, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="/man/007.jpg")
  add_Man(name="m_8", sex="m", age=45, education="硕士", Occupation="国企", height=172, weight=180, BJHouseholds=False, car=False, house=False, flag=False, img="/man/008.jpg")
  add_Man(name="m_9", sex="m", age=37, education="博士", Occupation="其他", height=117, weight=180, BJHouseholds=False, car=False, house=False, flag=False, img="/man/009.jpg")
  add_Man(name="m_10", sex="m", age=38, education="硕士", Occupation="其他", height=165, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="/man/010.jpg")
  add_Man(name="m_11", sex="m", age=35, education="高中", Occupation="国企", height=219, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="/man/011.jpg")
  add_Man(name="m_12", sex="m", age=44, education="博士", Occupation="私企白领", height=202, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="/man/012.jpg")
  add_Man(name="m_13", sex="m", age=41, education="高中", Occupation="在读", height=135, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="/man/013.jpg")
  add_Man(name="m_14", sex="m", age=39, education="大专", Occupation="公务员", height=128, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="/man/014.jpg")
  add_Man(name="m_15", sex="m", age=47, education="初中", Occupation="在读", height=150, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="/man/015.jpg")
  add_Man(name="m_16", sex="m", age=37, education="博士", Occupation="国企", height=104, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="/man/016.jpg")
  add_Man(name="m_17", sex="m", age=40, education="大本", Occupation="其他", height=119, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="/man/017.jpg")
  add_Man(name="m_18", sex="m", age=47, education="初中", Occupation="自由职业", height=188, weight=180, BJHouseholds=False, car=False, house=False, flag=False, img="/man/018.jpg")
  add_Man(name="m_19", sex="m", age=48, education="大专", Occupation="公务员", height=193, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="/man/019.jpg")
  add_Man(name="m_20", sex="m", age=43, education="硕士", Occupation="其他", height=132, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="/man/020.jpg")
  add_Man(name="m_21", sex="m", age=42, education="大本", Occupation="私企白领", height=167, weight=100, BJHouseholds=False, car=False, house=False, flag=False, img="/man/021.jpg")
  add_Man(name="m_22", sex="m", age=45, education="博士", Occupation="公务员", height=139, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="/man/022.jpg")
  add_Man(name="m_23", sex="m", age=46, education="大本", Occupation="公务员", height=157, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="/man/023.jpg")
  add_Man(name="m_24", sex="m", age=42, education="大本", Occupation="自由职业", height=114, weight=100, BJHouseholds=False, car=False, house=False, flag=False, img="/man/024.jpg")
  add_Man(name="m_25", sex="m", age=45, education="博士", Occupation="其他", height=190, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="/man/025.jpg")
  add_Man(name="m_26", sex="m", age=37, education="大本", Occupation="私企白领", height=120, weight=180, BJHouseholds=False, car=False, house=False, flag=False, img="/man/026.jpg")
  add_Man(name="m_27", sex="m", age=43, education="初中", Occupation="国企", height=192, weight=100, BJHouseholds=False, car=False, house=False, flag=False, img="/man/027.jpg")
  add_Man(name="m_28", sex="m", age=45, education="初中", Occupation="国企", height=216, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="/man/028.jpg")
  add_Man(name="m_29", sex="m", age=39, education="高中", Occupation="私企白领", height=126, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="/man/029.jpg")
  add_Man(name="m_30", sex="m", age=38, education="博士", Occupation="私企白领", height=169, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="/man/030.jpg")
  add_Man(name="m_31", sex="m", age=46, education="博士", Occupation="在读", height=119, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="/man/031.jpg")
  add_Man(name="m_32", sex="m", age=36, education="硕士", Occupation="其他", height=209, weight=180, BJHouseholds=False, car=False, house=False, flag=False, img="/man/032.jpg")
  add_Man(name="m_33", sex="m", age=43, education="博士", Occupation="国企", height=196, weight=180, BJHouseholds=False, car=False, house=False, flag=False, img="/man/033.jpg")
  add_Man(name="m_34", sex="m", age=40, education="硕士", Occupation="在读", height=108, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="/man/034.jpg")
  add_Man(name="m_35", sex="m", age=48, education="博士", Occupation="私企白领", height=146, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="/man/035.jpg")
  add_Man(name="m_36", sex="m", age=43, education="大专", Occupation="私企白领", height=196, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="/man/036.jpg")
  add_Man(name="m_37", sex="m", age=36, education="高中", Occupation="其他", height=215, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="/man/037.jpg")
  add_Man(name="m_38", sex="m", age=36, education="博士", Occupation="在读", height=102, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="/man/038.jpg")
  add_Man(name="m_39", sex="m", age=45, education="初中", Occupation="公务员", height=159, weight=100, BJHouseholds=False, car=False, house=False, flag=False, img="/man/039.jpg")
  add_Man(name="m_40", sex="m", age=49, education="硕士", Occupation="其他", height=151, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="/man/040.jpg")
  add_Man(name="m_41", sex="m", age=46, education="博士", Occupation="国企", height=132, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="/man/041.jpg")
  add_Man(name="m_42", sex="m", age=36, education="大本", Occupation="私企白领", height=145, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="/man/042.jpg")
  add_Man(name="m_43", sex="m", age=45, education="高中", Occupation="在读", height=146, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="/man/043.jpg")
  add_Man(name="m_44", sex="m", age=36, education="高中", Occupation="国企", height=167, weight=180, BJHouseholds=False, car=False, house=False, flag=False, img="/man/044.jpg")
  add_Man(name="m_45", sex="m", age=47, education="博士", Occupation="在读", height=215, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="/man/045.jpg")
  add_Man(name="m_46", sex="m", age=47, education="大本", Occupation="其他", height=189, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="/man/046.jpg")
  add_Man(name="m_47", sex="m", age=39, education="大本", Occupation="公务员", height=196, weight=180, BJHouseholds=False, car=False, house=False, flag=False, img="/man/047.jpg")
  add_Man(name="m_48", sex="m", age=41, education="初中", Occupation="国企", height=114, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="/man/048.jpg")
  add_Man(name="m_49", sex="m", age=39, education="初中", Occupation="私企白领", height=109, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="/man/049.jpg")
  add_Man(name="m_50", sex="m", age=48, education="博士", Occupation="私企白领", height=130, weight=180, BJHouseholds=False, car=False, house=False, flag=False, img="/man/050.jpg")
  add_Man(name="m_51", sex="m", age=49, education="大专", Occupation="自由职业", height=131, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="/man/051.jpg")
  add_Man(name="m_52", sex="m", age=39, education="硕士", Occupation="公务员", height=216, weight=180, BJHouseholds=False, car=False, house=False, flag=False, img="/man/052.jpg")
  add_Man(name="m_53", sex="m", age=49, education="博士", Occupation="公务员", height=154, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="/man/053.jpg")
  add_Man(name="m_54", sex="m", age=37, education="大本", Occupation="私企白领", height=180, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="/man/054.jpg")
  add_Man(name="m_55", sex="m", age=45, education="大专", Occupation="私企白领", height=178, weight=180, BJHouseholds=False, car=False, house=False, flag=False, img="/man/055.jpg")
  add_Man(name="m_56", sex="m", age=41, education="高中", Occupation="私企白领", height=174, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="/man/056.jpg")
  add_Man(name="m_57", sex="m", age=38, education="博士", Occupation="自由职业", height=142, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="/man/057.jpg")
  add_Man(name="m_58", sex="m", age=35, education="硕士", Occupation="在读", height=103, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="/man/058.jpg")
  add_Man(name="m_59", sex="m", age=49, education="高中", Occupation="国企", height=130, weight=100, BJHouseholds=False, car=False, house=False, flag=False, img="/man/059.jpg")
  add_Man(name="m_60", sex="m", age=45, education="大本", Occupation="其他", height=140, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="/man/060.jpg")
  add_Man(name="m_61", sex="m", age=45, education="高中", Occupation="私企白领", height=132, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="/man/061.jpg")
  add_Man(name="m_62", sex="m", age=36, education="大本", Occupation="其他", height=163, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="/man/062.jpg")
  add_Man(name="m_63", sex="m", age=45, education="高中", Occupation="公务员", height=191, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="/man/063.jpg")
  add_Man(name="m_64", sex="m", age=42, education="博士", Occupation="在读", height=192, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="/man/064.jpg")
  add_Man(name="m_65", sex="m", age=44, education="博士", Occupation="在读", height=156, weight=100, BJHouseholds=False, car=False, house=False, flag=False, img="/man/065.jpg")
  add_Man(name="m_66", sex="m", age=44, education="初中", Occupation="在读", height=154, weight=180, BJHouseholds=False, car=False, house=False, flag=False, img="/man/066.jpg")
  add_Man(name="m_67", sex="m", age=46, education="初中", Occupation="自由职业", height=159, weight=100, BJHouseholds=False, car=False, house=False, flag=False, img="/man/067.jpg")
  add_Man(name="m_68", sex="m", age=48, education="大本", Occupation="私企白领", height=171, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="/man/068.jpg")
  add_Man(name="m_69", sex="m", age=36, education="初中", Occupation="国企", height=120, weight=180, BJHouseholds=False, car=False, house=False, flag=False, img="/man/069.jpg")
  add_Man(name="m_70", sex="m", age=39, education="高中", Occupation="私企白领", height=121, weight=100, BJHouseholds=False, car=False, house=False, flag=False, img="/man/070.jpg")
  add_Man(name="m_71", sex="m", age=43, education="大专", Occupation="自由职业", height=135, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="/man/071.jpg")
  add_Man(name="m_72", sex="m", age=44, education="大本", Occupation="私企白领", height=148, weight=180, BJHouseholds=False, car=False, house=False, flag=False, img="/man/072.jpg")
  add_Man(name="m_73", sex="m", age=36, education="初中", Occupation="其他", height=110, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="/man/073.jpg")
  add_Man(name="m_74", sex="m", age=44, education="初中", Occupation="国企", height=157, weight=100, BJHouseholds=False, car=False, house=False, flag=False, img="/man/074.jpg")
  add_Man(name="m_75", sex="m", age=45, education="高中", Occupation="其他", height=192, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="/man/075.jpg")
  add_Man(name="m_76", sex="m", age=40, education="博士", Occupation="国企", height=139, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="/man/076.jpg")
  add_Man(name="m_77", sex="m", age=44, education="高中", Occupation="私企白领", height=197, weight=100, BJHouseholds=False, car=False, house=False, flag=False, img="/man/077.jpg")
  add_Man(name="m_78", sex="m", age=45, education="大专", Occupation="自由职业", height=135, weight=100, BJHouseholds=False, car=False, house=False, flag=False, img="/man/078.jpg")
  add_Man(name="m_79", sex="m", age=48, education="硕士", Occupation="其他", height=193, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="/man/079.jpg")
  add_Man(name="m_80", sex="m", age=48, education="硕士", Occupation="公务员", height=184, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="/man/080.jpg")
  add_Man(name="m_81", sex="m", age=38, education="大本", Occupation="其他", height=202, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="/man/081.jpg")
  add_Man(name="m_82", sex="m", age=43, education="硕士", Occupation="公务员", height=193, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="/man/082.jpg")
  add_Man(name="m_83", sex="m", age=49, education="博士", Occupation="其他", height=206, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="/man/083.jpg")
  add_Man(name="m_84", sex="m", age=39, education="初中", Occupation="其他", height=204, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="/man/084.jpg")
  add_Man(name="m_85", sex="m", age=47, education="大本", Occupation="私企白领", height=155, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="/man/085.jpg")
  add_Man(name="m_86", sex="m", age=38, education="大本", Occupation="私企白领", height=138, weight=140, BJHouseholds=False, car=False, house=False, flag=False, img="/man/086.jpg")
  add_Man(name="m_87", sex="m", age=37, education="硕士", Occupation="公务员", height=104, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="/man/087.jpg")
  add_Man(name="m_88", sex="m", age=42, education="大本", Occupation="国企", height=119, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="/man/088.jpg")
  add_Man(name="m_89", sex="m", age=36, education="初中", Occupation="自由职业", height=189, weight=100, BJHouseholds=False, car=False, house=False, flag=False, img="/man/089.jpg")
  add_Man(name="m_90", sex="m", age=45, education="大本", Occupation="自由职业", height=112, weight=180, BJHouseholds=False, car=False, house=False, flag=False, img="/man/090.jpg")
  add_Man(name="m_91", sex="m", age=41, education="大本", Occupation="自由职业", height=149, weight=100, BJHouseholds=False, car=False, house=False, flag=False, img="/man/091.jpg")
  add_Man(name="m_92", sex="m", age=48, education="高中", Occupation="私企白领", height=178, weight=100, BJHouseholds=False, car=False, house=False, flag=False, img="/man/092.jpg")
  add_Man(name="m_93", sex="m", age=36, education="初中", Occupation="在读", height=115, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="/man/093.jpg")
  add_Man(name="m_94", sex="m", age=48, education="大专", Occupation="私企白领", height=149, weight=100, BJHouseholds=False, car=False, house=False, flag=False, img="/man/094.jpg")
  add_Man(name="m_95", sex="m", age=43, education="大本", Occupation="私企白领", height=107, weight=180, BJHouseholds=False, car=False, house=False, flag=False, img="/man/095.jpg")
  add_Man(name="m_96", sex="m", age=36, education="初中", Occupation="私企白领", height=103, weight=100, BJHouseholds=False, car=False, house=False, flag=False, img="/man/096.jpg")
  add_Man(name="m_97", sex="m", age=47, education="初中", Occupation="自由职业", height=143, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="/man/097.jpg")
  add_Man(name="m_98", sex="m", age=42, education="博士", Occupation="私企白领", height=189, weight=120, BJHouseholds=False, car=False, house=False, flag=False, img="/man/098.jpg")
  add_Man(name="m_99", sex="m", age=35, education="博士", Occupation="私企白领", height=168, weight=100, BJHouseholds=False, car=False, house=False, flag=False, img="/man/099.jpg")
  add_Man(name="m_100", sex="m", age=38, education="初中", Occupation="私企白领", height=191, weight=160, BJHouseholds=False, car=False, house=False, flag=False, img="/man/100.jpg")


'''
    python_cat = add_cat('Python', views=128, likes=64)

    add_page(cat=python_cat,
        title="Official Python Tutorial",
        url="http://docs.python.org/2/tutorial/")

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

              add_Female(name="f_1", sex="f", age=18, education="初中",Occupation="在读",
    height=140, weight = 25, BJHouseholds = False, car= False, house=False,
    hometown="x", require="x", flag=False,WxNo="11", message="x", img="1.jpg")
'''

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()