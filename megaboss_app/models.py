from django.db import models

from users.models import User


# Create your models here.

class Plan(models.Model):
    mame = models.CharField(max_length=100)

    def __str__(self):
        return self.mame


class Plan_row(models.Model):

    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='plan_row')
    id_row =models.IntegerField()

    col_0 = models.CharField(max_length=200,null=True, verbose_name='Сводный код объекта ремонта (X/Y/Z)')
    col_1  = models.CharField(max_length=200,null=True, verbose_name='рег. № договора с ГИ-ГР')
    col_2  = models.CharField(max_length=200, null=True, verbose_name='Принципал')
    col_3 = models.CharField(max_length=200, null=True, verbose_name='Подразделение Принципала (ЛПУ, УПХГ, УГПГ, Завод и т.д.)')
    col_4  = models.CharField(max_length=200, null=True, verbose_name='Наименование объекта Диагностирования')
    col_5  = models.CharField(max_length=200,null=True, verbose_name='Наименование объекта диагностирования согласно карточке учета ОС')
    col_6  = models.CharField(max_length=200,null=True, verbose_name='Вид работ')
    col_7  = models.CharField(max_length=200, null=True, verbose_name='Содержание работ')
    col_8  = models.CharField(max_length=200, null=True, verbose_name='Инв. Номер')
    col_9  = models.CharField(max_length=200,null=True, verbose_name='Ед. изкмерения')
    col_10  = models.CharField(max_length=200,null=True, verbose_name='Кол-во')
    col_11  = models.CharField(max_length=200, null=True, verbose_name='Куратор')
    col_12  = models.CharField(max_length=200, null=True, verbose_name='Исполнители полевых работ')
    col_13  = models.CharField(max_length=200,null=True, verbose_name='Ведущий инженер КО')
    col_14  = models.CharField(max_length=200,null=True, verbose_name='Инженер КО')
    col_15 = models.CharField(max_length=200, null=True, verbose_name='Сметчик')
    col_16  = models.CharField(max_length=200, null=True, verbose_name='Стоимость работ, руб.')
    col_17  = models.CharField(max_length=200, null=True, verbose_name='I квартал')
    col_18  = models.CharField(max_length=200, null=True, verbose_name='II квартал')
    col_19  = models.CharField(max_length=200, null=True, verbose_name='III квартал')
    col_20  = models.CharField(max_length=200,null=True, verbose_name='IV квартал')
    col_21  = models.CharField(max_length=200,null=True, verbose_name='Исполнитель')
    col_22  = models.CharField(max_length=200, null=True, verbose_name='Соисполнитель')
    col_23  = models.CharField(max_length=200, null=True, verbose_name='Принадлежность к договору (ОСН, ДС1, ДС2 и т.д.)')
    col_24  = models.CharField(max_length=200,null=True, verbose_name='Стоимость работ Соисполнителя, руб без НДС')
    col_25  = models.CharField(max_length=200,null=True, verbose_name='ФАКТ')
    col_26 = models.CharField(max_length=200, null=True, verbose_name='Процент выполнения')
    col_27  = models.CharField(max_length=200, null=True, verbose_name='Финансовый акт, сумма без НДС в руб Полевой этап')
    col_28  = models.CharField(max_length=200, null=True, verbose_name='Финансовый акт, сумма без НДС в руб Камеральный этап')
    col_29  = models.CharField(max_length=200, null=True, verbose_name='ИТОГО выполнено работ, в руб без НДС Полевой+камеральный этап')
    col_30  = models.CharField(max_length=200, null=True, verbose_name='График производства работ')
    col_31  = models.CharField(max_length=200, null=True, verbose_name='Программа производства работ')
    col_32  = models.CharField(max_length=200,null=True, verbose_name='Допуск к производству работ')
    col_33  = models.CharField(max_length=200,null=True, verbose_name='Дата начала работ')
    col_34  = models.CharField(max_length=200, null=True, verbose_name='Дата окончания работ')
    col_35  = models.CharField(max_length=200, null=True, verbose_name='Дата начала работ Факт')
    col_36  = models.CharField(max_length=200,null=True, verbose_name='Дата окончания работ Факт')
    col_37  = models.CharField(max_length=200,null=True, verbose_name='Статус работ')
    col_38  = models.CharField(max_length=200, null=True, verbose_name='Выполнение физических объемов работ ФАКТ, ед.изм.')
    col_39  = models.CharField(max_length=200, null=True, verbose_name='Технический акт выполненных работ')
    col_40  = models.CharField(max_length=200, null=True, verbose_name='Приборы')
    col_41  = models.CharField(max_length=200, null=True, verbose_name='Автомобиль')
    col_42  = models.CharField(max_length=200, null=True, verbose_name='Дата выезда в командировку')
    col_43  = models.CharField(max_length=200,null=True, verbose_name='Дата возврата из командировки')
    col_44  = models.CharField(max_length=200,null=True, verbose_name='Технический отчет/Паспорт/Отчет о технич состоянии ПЛАН, шт.')
    col_45  = models.CharField(max_length=200, null=True, verbose_name='Технический отчет/Паспорт/Отчет о технич состоянии ПЕРЕДАНО ЗАКАЗЧИКУ НА СОГЛАСОВАНИЕ, шт.')
    col_46  = models.CharField(max_length=200, null=True, verbose_name='Технический отчет/Паспорт/Отчет о технич состоянии ОФОРМЛЕНО И СДАНО ЗАКАЗЧИКУ, шт.')
    col_47  = models.CharField(max_length=200,null=True, verbose_name='Технический отчет/Паспорт/Отчет о технич состоянии ДАТА СДАЧИ ПЛАН')
    col_48  = models.CharField(max_length=200,null=True, verbose_name='Технический отчет/Паспорт/Отчет о технич состоянии ДАТА СДАЧИ ФАКТ')
    col_49  = models.CharField(max_length=200, null=True, verbose_name='ЗЭПБ ПЛАН, шт.')
    col_50  = models.CharField(max_length=200, null=True, verbose_name='ЗЭПБ ПЛАН, дата сдачи по графику')
    col_51  = models.CharField(max_length=200, null=True, verbose_name='ЗЭПБ ФАКТ (передано Заказчику на согласование), шт.')
    col_52  = models.CharField(max_length=200, null=True, verbose_name='ЗЭПБ ФАКТ (оформлено и сдано Заказчику), шт.')
    col_53  = models.CharField(max_length=200, null=True, verbose_name='ЗЭПБ ФАКТ, дата сдачи')
    col_54 = models.CharField(max_length=200, null=True, verbose_name='ЗЭПБ ФАКТ ПЕРЕДАНО НА РЕГИСТРАЦИЮ В РТН, шт.')
    col_55  = models.CharField(max_length=200, null=True, verbose_name='ЗЭПБ ФАКТ ЗАРЕГИСТРИРО-ВАНО В РТН, шт.')
    col_56  = models.CharField(max_length=200, null=True, verbose_name='ЗЭПБ ФАКТ, дата регистрации')

class Collums(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)

class CollumsUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    collum = models.ForeignKey(Collums, on_delete=models.PROTECT, related_name='collum')
    checked = models.BooleanField(default=1, null=True)

    def json(self):
        return {
            'collum': self.collum.name,
            'descript': self.collum.description,
            'checked': self.checked,
        }



# {'svodnyij_kod_obekta_remonta_xyz': 'Сводный код объекта ремонта (X/Y/Z)', 'reg__dogovora_s_gi_gr': 'рег. № договора с ГИ-ГР', 'printsipal': 'Принципал',
# 'naimenovanie_obekta_diagnostirovaniya': 'Наименование объекта Диагностирования',
# 'naimenovanie_obekta_diagnostirovaniya_soglasno_kartochke_ucheta_os': 'Наименование объекта диагностирования согласно карточке учета ОС',
# 'vid_rabot': 'Вид работ', 'soderzhanie_rabot': 'Содержание работ', 'inv_nomer': 'Инв. Номер',
# 'ed_izkmereniya': 'Ед. изкмерения', 'kol_vo': 'Кол-во', 'kurator': 'Куратор', 'ispolniteli_polevyih_rabot': 'Исполнители полевых работ',
# 'veduschij_inzhener_ko': 'Ведущий инженер КО', 'inzhener_ko': 'Инженер КО', 'stoimost_rabot_rub': 'Стоимость работ, руб.',
# 'i_kvartal': 'I квартал', 'ii_kvartal': 'II квартал', 'iii_kvartal': 'III квартал', 'iv_kvartal': 'IV квартал',
# 'ispolnitel': 'Исполнитель', 'soispolnitel': 'Соисполнитель', 'prinadlezhnost_k_dogovoru_osn_ds1_ds2_i_td': 'Принадлежность к договору (ОСН, ДС1, ДС2 и т.д.)',
# 'stoimost_rabot_soispolnitelya_rub_bez_nds': 'Стоимость работ Соисполнителя, руб без НДС', 'fakt': 'ФАКТ', 'protsent_vyipolneniya': 'Процент выполнения',
# 'finansovyij_akt_summa_bez_nds_v_rub_polevoj_etap': 'Финансовый акт, сумма без НДС в руб Полевой этап',
# 'finansovyij_akt_summa_bez_nds_v_rub_kameralnyij_etap': 'Финансовый акт, сумма без НДС в руб Камеральный этап',
# 'itogo_vyipolneno_rabot_v_rub_bez_nds_polevojkameralnyij_etap': 'ИТОГО выполнено работ, в руб без НДС Полевой+камеральный этап',
# 'grafik_proizvodstva_rabot': 'График производства работ', 'programma_proizvodstva_rabot': 'Программа производства работ',
# 'dopusk_k_proizvodstvu_rabot': 'Допуск к производству работ', 'data_nachala_rabot': 'Дата начала работ',
# 'data_okonchaniya_rabot': 'Дата окончания работ', 'data_nachala_rabot_fakt': 'Дата начала работ Факт',
# 'data_okonchaniya_rabot_fakt': 'Дата окончания работ Факт', 'status_rabot': 'Статус работ',
# 'vyipolnenie_fizicheskih_obemov_rabot_fakt_edizm': 'Выполнение физических объемов работ ФАКТ, ед.изм.',
# 'tehnicheskij_akt_vyipolnennyih_rabot': 'Технический акт выполненных работ', 'priboryi': 'Приборы', 'avtomobil': 'Автомобиль',
# 'data_vyiezda_v_komandirovku': 'Дата выезда в командировку', 'data_vozvrata_iz_komandirovki': 'Дата возврата из командировки',
# 'tehnicheskij_otchetpasportotchet_o_tehnich_sostoyanii_plan_sht': 'Технический отчет/Паспорт/Отчет о технич состоянии ПЛАН, шт.',
# 'tehnicheskij_otchetpasportotchet_o_tehnich_sostoyanii_peredano_zakazchiku_na_soglasovanie_sht': 'Технический отчет/Паспорт/Отчет о технич состоянии ПЕРЕДАНО ЗАКАЗЧИКУ НА СОГЛАСОВАНИЕ, шт.',
# 'tehnicheskij_otchetpasportotchet_o_tehnich_sostoyanii_oformleno_i_sdano_zakazchiku_sht': 'Технический отчет/Паспорт/Отчет о технич состоянии ОФОРМЛЕНО И СДАНО ЗАКАЗЧИКУ, шт.',
# 'tehnicheskij_otchetpasportotchet_o_tehnich_sostoyanii_data_sdachi_plan': 'Технический отчет/Паспорт/Отчет о технич состоянии ДАТА СДАЧИ ПЛАН', 'tehnicheskij_otchetpasportotchet_o_tehnich_sostoyanii_data_sdachi_fakt': 'Технический отчет/Паспорт/Отчет о технич состоянии ДАТА СДАЧИ ФАКТ',
# 'zepb_plan_sht': 'ЗЭПБ ПЛАН, шт.', 'zepb_plan_data_sdachi_po_grafiku': 'ЗЭПБ ПЛАН, дата сдачи по графику',
# 'zepb_fakt_peredano_zakazchiku_na_soglasovanie_sht': 'ЗЭПБ ФАКТ (передано Заказчику на согласование), шт.',
# 'zepb_fakt_oformleno_i_sdano_zakazchiku_sht': 'ЗЭПБ ФАКТ (оформлено и сдано Заказчику), шт.',
# 'zepb_fakt_data_sdachi': 'ЗЭПБ ФАКТ, дата сдачи', 'zepb_fakt_peredano_na_registratsiyu_v_rtn_sht': 'ЗЭПБ ФАКТ ПЕРЕДАНО НА РЕГИСТРАЦИЮ В РТН, шт.',
# 'zepb_fakt_zaregistriro_vano_v_rtn_sht': 'ЗЭПБ ФАКТ ЗАРЕГИСТРИРО-ВАНО В РТН, шт.', 'zepb_fakt_data_registratsii': 'ЗЭПБ ФАКТ, дата регистрации'}
#
# svodnyij_kod_obekta_remonta_xyz = models.CharField(max_length=200,null=True, verbose_name='Сводный код объекта ремонта (X/Y/Z)')
# reg_dogovora_s_gi_gr = models.CharField(max_length=200,null=True, verbose_name='рег. № договора с ГИ-ГР')
# printsipal = models.CharField(max_length=200, null=True, verbose_name='Принципал')
# naimenovanie_obekta_diagnostirovaniya = models.CharField(max_length=200, null=True, verbose_name='Наименование объекта Диагностирования')
# naimenovanie_obekta_diagnostirovaniya_soglasno_kartochke_ucheta_os = models.CharField(max_length=200,null=True, verbose_name='Наименование объекта диагностирования согласно карточке учета ОС')
# vid_rabot = models.CharField(max_length=200,null=True, verbose_name='Вид работ')
# soderzhanie_rabot = models.CharField(max_length=200, null=True, verbose_name='Содержание работ')
# inv_nomer = models.CharField(max_length=200, null=True, verbose_name='Инв. Номер')
# ed_izkmereniya = models.CharField(max_length=200,null=True, verbose_name='Ед. изкмерения')
# kol_vo = models.CharField(max_length=200,null=True, verbose_name='Кол-во')
# kurator = models.CharField(max_length=200, null=True, verbose_name='Куратор')
# ispolniteli_polevyih_rabot = models.CharField(max_length=200, null=True, verbose_name='Исполнители полевых работ')
# veduschij_inzhener_ko = models.CharField(max_length=200,null=True, verbose_name='Ведущий инженер КО')
# inzhener_ko = models.CharField(max_length=200,null=True, verbose_name='Инженер КО')
# stoimost_rabot_rub = models.CharField(max_length=200, null=True, verbose_name='Стоимость работ, руб.')
# i_kvartal = models.CharField(max_length=200, null=True, verbose_name='I квартал')
# ii_kvartal = models.CharField(max_length=200, null=True, verbose_name='II квартал')
# iii_kvartal = models.CharField(max_length=200, null=True, verbose_name='III квартал')
# iv_kvartal = models.CharField(max_length=200,null=True, verbose_name='IV квартал')
# ispolnitel = models.CharField(max_length=200,null=True, verbose_name='Исполнитель')
# soispolnitel = models.CharField(max_length=200, null=True, verbose_name='Соисполнитель')
# prinadlezhnost_k_dogovoru_osn_ds1_ds2_i_td = models.CharField(max_length=200, null=True, verbose_name='Принадлежность к договору (ОСН, ДС1, ДС2 и т.д.)')
# stoimost_rabot_soispolnitelya_rub_bez_nds = models.CharField(max_length=200,null=True, verbose_name='Стоимость работ Соисполнителя, руб без НДС')
# fakt = models.CharField(max_length=200,null=True, verbose_name='ФАКТ')
# protsent_vyipolneniya = models.CharField(max_length=200, null=True, verbose_name='Процент выполнения')
# finansovyij_akt_summa_bez_nds_v_rub_polevoj_etap = models.CharField(max_length=200, null=True, verbose_name='Финансовый акт, сумма без НДС в руб Полевой этап')
# finansovyij_akt_summa_bez_nds_v_rub_kameralnyij_etap = models.CharField(max_length=200, null=True, verbose_name='Финансовый акт, сумма без НДС в руб Камеральный этап')
# itogo_vyipolneno_rabot_v_rub_bez_nds_polevojkameralnyij_etap = models.CharField(max_length=200, null=True, verbose_name='ИТОГО выполнено работ, в руб без НДС Полевой+камеральный этап')
# grafik_proizvodstva_rabot = models.CharField(max_length=200, null=True, verbose_name='График производства работ')
# programma_proizvodstva_rabot = models.CharField(max_length=200, null=True, verbose_name='Программа производства работ')
# dopusk_k_proizvodstvu_rabot = models.CharField(max_length=200,null=True, verbose_name='Допуск к производству работ')
# data_nachala_rabot = models.CharField(max_length=200,null=True, verbose_name='Дата начала работ')
# data_okonchaniya_rabot = models.CharField(max_length=200, null=True, verbose_name='Дата окончания работ')
# data_nachala_rabot_fakt = models.CharField(max_length=200, null=True, verbose_name='Дата начала работ Факт')
# data_okonchaniya_rabot_fakt = models.CharField(max_length=200,null=True, verbose_name='Дата окончания работ Факт')
# status_rabot = models.CharField(max_length=200,null=True, verbose_name='Статус работ')
# vyipolnenie_fizicheskih_obemov_rabot_fakt_edizm = models.CharField(max_length=200, null=True, verbose_name='Выполнение физических объемов работ ФАКТ, ед.изм.')
# tehnicheskij_akt_vyipolnennyih_rabot = models.CharField(max_length=200, null=True, verbose_name='Технический акт выполненных работ')
# priboryi = models.CharField(max_length=200, null=True, verbose_name='Приборы')
# avtomobil = models.CharField(max_length=200, null=True, verbose_name='Автомобиль')
# data_vyiezda_v_komandirovku = models.CharField(max_length=200, null=True, verbose_name='Дата выезда в командировку')
# data_vozvrata_iz_komandirovki = models.CharField(max_length=200,null=True, verbose_name='Дата возврата из командировки')
# tehnicheskij_otchetpasportotchet_o_tehnich_sostoyanii_plan_sht = models.CharField(max_length=200,null=True, verbose_name='Технический отчет/Паспорт/Отчет о технич состоянии ПЛАН, шт.')
# tehnicheskij_otchetpasportotchet_o_tehnich_sostoyanii_peredano_zakazchiku_na_soglasovanie_sht = models.CharField(max_length=200, null=True, verbose_name='Технический отчет/Паспорт/Отчет о технич состоянии ПЕРЕДАНО ЗАКАЗЧИКУ НА СОГЛАСОВАНИЕ, шт.')
# tehnicheskij_otchetpasportotchet_o_tehnich_sostoyanii_oformleno_i_sdano_zakazchiku_sht = models.CharField(max_length=200, null=True, verbose_name='Технический отчет/Паспорт/Отчет о технич состоянии ОФОРМЛЕНО И СДАНО ЗАКАЗЧИКУ, шт.')
# tehnicheskij_otchetpasportotchet_o_tehnich_sostoyanii_data_sdachi_plan = models.CharField(max_length=200,null=True, verbose_name='Технический отчет/Паспорт/Отчет о технич состоянии ДАТА СДАЧИ ПЛАН')
# tehnicheskij_otchetpasportotchet_o_tehnich_sostoyanii_data_sdachi_fakt = models.CharField(max_length=200,null=True, verbose_name='Технический отчет/Паспорт/Отчет о технич состоянии ДАТА СДАЧИ ФАКТ')
# zepb_plan_sht = models.CharField(max_length=200, null=True, verbose_name='ЗЭПБ ПЛАН, шт.')
# zepb_plan_data_sdachi_po_grafiku = models.CharField(max_length=200, null=True, verbose_name='ЗЭПБ ПЛАН, дата сдачи по графику')
# zepb_fakt_peredano_zakazchiku_na_soglasovanie_sht = models.CharField(max_length=200, null=True, verbose_name='ЗЭПБ ФАКТ (передано Заказчику на согласование), шт.')
# zepb_fakt_oformleno_i_sdano_zakazchiku_sht = models.CharField(max_length=200, null=True, verbose_name='ЗЭПБ ФАКТ (оформлено и сдано Заказчику), шт.')
# zepb_fakt_data_sdachi = models.CharField(max_length=200, null=True, verbose_name='ЗЭПБ ФАКТ, дата сдачи')
# zepb_fakt_peredano_na_registratsiyu_v_rtn_sht = models.CharField(max_length=200, null=True, verbose_name='ЗЭПБ ФАКТ ПЕРЕДАНО НА РЕГИСТРАЦИЮ В РТН, шт.')
# zepb_fakt_zaregistriro_vano_v_rtn_sht = models.CharField(max_length=200, null=True, verbose_name='ЗЭПБ ФАКТ ЗАРЕГИСТРИРО-ВАНО В РТН, шт.')
# zepb_fakt_data_registratsii = models.CharField(max_length=200, null=True, verbose_name='ЗЭПБ ФАКТ, дата регистрации')
