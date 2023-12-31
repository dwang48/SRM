from django.urls import path
from cost_analysis import views

# urlpatterns = [
#     path('suliao/', views.calculate_cost, name='calculate_suliao'),
#     path('zhusu/', views.calculate_cost, name='calculate_zhusu'),
#     path('penwu/', views.calculate_cost, name='calculate_penwu'),
#     path('diandu/', views.calculate_cost, name='calculate_diandu'),
#     path('tangjin/', views.calculate_cost, name='calculate_tangjin'),
#     path('yinshua/', views.calculate_cost, name='calculate_yinshua'),
#     path('penhui/', views.calculate_cost, name='calculate_penhui'),
#     path('zuzhuang/', views.calculate_cost, name='calculate_zuzhuang'),
#     path('chongya/', views.calculate_cost, name='calculate_chongya'),
#     path('paoguang/', views.calculate_cost, name='calculate_paoguang'),
#     path('yanghua/', views.calculate_cost, name='calculate_yanghua'),
#     path('suanxi/', views.calculate_cost, name='calculate_suanxi'),
#     path('kezi/', views.calculate_cost, name='calculate_kezi'),
#     path('citie/', views.calculate_cost, name='calculate_citie'),
#     path('chuizhong/', views.calculate_cost, name='calculate_chuizhong'),
#     path('tanhuan/', views.calculate_cost, name='calculate_tanhuan'),
#     path('lvjianchengpin/', views.calculate_cost, name='calculate_lvjianchengpin'),
#     path('zhanban/', views.calculate_cost, name='calculate_zhanban'),
#     path('zhixiang/', views.calculate_cost, name='calculate_zhixiang'),
#     path('baozhuangdai/', views.calculate_cost, name='calculate_baozhuangdai'),
#     path('caihe/', views.calculate_cost, name='calculate_caihe'),
#     path('xisupan/', views.calculate_cost, name='calculate_xisupan'),
#     path('zhuanyinzhi/', views.calculate_cost, name='calculate_zhuanyinzhi'),
#     path('dianpian/', views.calculate_cost, name='calculate_dianpian'),
#     path('bozhi/', views.calculate_cost, name='calculate_bozhi'),
#     path('biaoqian/', views.calculate_cost, name='calculate_biaoqian'),
#     path('shousuomo/', views.calculate_cost, name='calculate_shousuomo'),
#     path('mojia/', views.calculate_cost, name='calculate_mojia'),
#     path('moxin/', views.calculate_cost, name='calculate_moxin'),
#     path('boliguan/', views.calculate_cost, name='calculate_boliguan'),
#     path('miantou/', views.calculate_cost, name='calculate_miantou'),
#     path('jingpian/', views.calculate_cost, name='calculate_jingpian'),
#     path('jiaotou/', views.calculate_cost, name='calculate_jiaotou'),
#     path('shuamao/', views.calculate_cost, name='calculate_shuamao'),
# ]
categories = [
    'suliao', 'zhusu', 'pentu', 'diandu', 'tangjin', 'yinshua',
    'penhui', 'zuzhuang', 'chongya', 'paoguang_yanghua', 'chongya_paoguang_yanghua', 'suanxi',
    'kezi', 'citie', 'chuizhong', 'tanhuan', 'lvjianchengpin', 'zhanban',
    'zhixiang', 'baozhuangdai', 'caihe', 'xisupan', 'zhuanyinzhi', 
    'dianpian', 'bozhi', 'biaoqian', 'shousuomo', 'mojia', 'moxin',
    'boliguan', 'miantou', 'jingpian', 'jiaotou', 'shuamao'
]
urlpatterns = []

for category in categories:
    calculate_path = path(f'{category}/', views.calculate_cost, name=f'calculate_{category}')
    save_record_path = path(f'{category}/save_record/', views.save_record, name=f'save_record_{category}')
    # process_data_path = path(f'{category}/process_data/',views.process_data, name=f'process_data_{category}')

    urlpatterns.extend([calculate_path, save_record_path])
