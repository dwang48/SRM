# Generated by Django 4.2.4 on 2023-11-03 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cost_analysis', '0011_计算模版'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='计算模版',
            options={'verbose_name': '计算模版', 'verbose_name_plural': '计算模版'},
        ),
        migrations.AlterField(
            model_name='计算模版',
            name='类别',
            field=models.CharField(choices=[('塑料成品', '塑料成品'), ('注塑', '注塑'), ('喷涂', '喷涂'), ('电镀', '电镀'), ('烫金', '烫金'), ('印刷', '印刷'), ('喷绘', '喷绘'), ('组装', '组装'), ('冲压', '冲压'), ('抛光', '抛光'), ('氧化', '氧化'), ('酸洗', '酸洗'), ('刻字', '刻字'), ('磁铁', '磁铁'), ('垂重', '垂重'), ('弹簧', '弹簧'), ('铝件成品', '铝件成品'), ('栈板', '栈板'), ('纸箱/纸板', '纸箱/纸板'), ('包装袋', '包装袋'), ('彩盒', '彩盒'), ('吸塑盘', '吸塑盘'), ('转印纸', '转印纸'), ('垫片', '垫片'), ('箔纸', '箔纸'), ('标签', '标签'), ('收缩膜', '收缩膜'), ('模架', '模架'), ('模芯', '模芯'), ('玻璃管', '玻璃管'), ('棉头', '棉头'), ('镜片', '镜片'), ('胶头', '胶头'), ('刷毛', '刷毛')], max_length=200, unique=True),
        ),
    ]
