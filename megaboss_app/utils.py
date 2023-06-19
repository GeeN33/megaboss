import pandas as pd

from megaboss_app.models import *

def import_excel_to_db(file, file_mame):

    plan, _ = Plan.objects.get_or_create(mame=file_mame)
    createds = 0
    try:
        excel_data_df = pd.read_excel(file, sheet_name='ПЛАН', header=None)

        ll=[]
        i=0

        for row in excel_data_df.to_dict(orient='records'):
            i += 1
            ll.append({'id_row':i, 'row':row })

        for j in range(len(ll)):
            if j > 5 and j < 100:
               data = data_to_dict(ll[j]['row'])
               _ , created = Plan_row.objects.update_or_create(plan=plan, id_row=ll[j]['id_row'], defaults=data)
               if created:
                  createds += 1
               # print(ll[j])

    except Exception:
        return (False, Plan_row.objects.count(), createds)

    return (True, Plan_row.objects.count(), createds)

def cache_excel_to_db(files, file_mame):

    plan, _ = Plan.objects.get_or_create(mame=file_mame)
    createds = 0
    try:
        for file in files:
           _ , created = Plan_row.objects.update_or_create(plan=plan, id_row=file['data']['id_row'], defaults=file['data'])
           if created:
              createds += 1


    except Exception:
        return (False, Plan_row.objects.count(), createds)

    return (True, Plan_row.objects.count(), createds)

def import_excel_to_cache(file, file_mame):

    plan_rows = Plan_row.objects.filter(plan__mame = file_mame)
    row_count = 0
    row_new = 0
    row_updata = 0
    row_error = 0

    try:
        excel_data_df = pd.read_excel(file, sheet_name='ПЛАН', header=None)
        plan_list=[]
        ll=[]
        i=0

        for row in excel_data_df.to_dict(orient='records'):
            i += 1
            ll.append({'id_row':i, 'row':row })

        for j in range(len(ll)):
            if j > 5 and j < 105:
               data = data_to_dict_cache(ll[j]['id_row'], 1 , ll[j]['row'])
               pp = plan_rows.filter(id_row=ll[j]['id_row']).values()
               if pp:
                   p = pp[0]
                   p.pop('id', None)
                   if not p == data:
                       row_updata += 1
               else:
                   row_new += 1
               row_count += 1
               datas = {
                   'data': data
               }
               plan_list.append(datas)

    except Exception:
        return (False, row_count, 0)

    return (True, row_count, row_new, row_updata, row_error, plan_list)

def data_to_dict( d):
    return  {
        'col_0': d[0],
        'col_1': d[1],
        'col_2' : d[2],
        'col_3' : d[3],
        'col_4' : d[4],
        'col_5' : d[5],
        'col_6' : d[6],
        'col_7' : d[7],
        'col_8' : d[8],
        'col_9' : d[9],
        'col_10' : d[10],
        'col_11' : d[11],
        'col_12'  : d[12],
        'col_13'  : d[13],
        'col_14'  : d[14],
        'col_15'  : d[15],
        'col_16'  : d[16],
        'col_17'  : d[17],
        'col_18'  : d[18],
        'col_19'  : d[19],
        'col_20'  : d[20],
        'col_21'  : d[21],
        'col_22'  : d[22],
        'col_23'  : d[23],
        'col_24'  : d[24],
        'col_25'  : d[25],
        'col_26'  : d[26],
        'col_27'  : d[27],
        'col_28' : d[28],
        'col_29'  : d[29],
        'col_30'  : d[30],
        'col_31'  : d[31],
        'col_32'  : d[32],
        'col_33'  : d[33],
        'col_34'  : d[34],
        'col_35'  : d[35],
        'col_36'  : d[36],
        'col_37'  : d[37],
        'col_38'  : d[38],
        'col_39'  : d[39],
        'col_40'  : d[40],
        'col_41'  : d[41],
        'col_42'  : d[42],
        'col_43'  : d[43],
        'col_44'  : d[44],
        'col_45'  : d[45],
        'col_46'  : d[46],
        'col_47'  : d[47],
        'col_48'  : d[48],
        'col_49'  : d[49],
        'col_50'  : d[50],
        'col_51'  : d[51],
        'col_52'  : d[52],
        'col_53'  : d[53],
        'col_54'  : d[54],
        'col_55'  : d[55],
        'col_56'  : d[56]
        }

def data_to_dict_cache(id_row ,plan_id, d):
    return  {
        'plan_id': plan_id,
        'id_row': id_row,
        'col_0': str(d[0]),
        'col_1': str(d[1]),
        'col_2' : str(d[2]),
        'col_3' : str(d[3]),
        'col_4' : str(d[4]),
        'col_5' : str(d[5]),
        'col_6' : str(d[6]),
        'col_7' : str(d[7]),
        'col_8' : str(d[8]),
        'col_9' : str(d[9]),
        'col_10' : str(d[10]),
        'col_11' : str(d[11]),
        'col_12'  : str(d[12]),
        'col_13'  : str(d[13]),
        'col_14'  : str(d[14]),
        'col_15'  : str(d[15]),
        'col_16'  : str(d[16]),
        'col_17'  : str(d[17]),
        'col_18'  : str(d[18]),
        'col_19'  : str(d[19]),
        'col_20'  : str(d[20]),
        'col_21'  : str(d[21]),
        'col_22'  : str(d[22]),
        'col_23'  : str(d[23]),
        'col_24'  : str(d[24]),
        'col_25'  : str(d[25]),
        'col_26'  : str(d[26]),
        'col_27'  : str(d[27]),
        'col_28' : str(d[28]),
        'col_29'  : str(d[29]),
        'col_30'  : str(d[30]),
        'col_31'  : str(d[31]),
        'col_32'  : str(d[32]),
        'col_33'  : str(d[33]),
        'col_34'  : str(d[34]),
        'col_35'  : str(d[35]),
        'col_36'  : str(d[36]),
        'col_37'  : str(d[37]),
        'col_38'  : str(d[38]),
        'col_39'  : str(d[39]),
        'col_40'  : str(d[40]),
        'col_41'  : str(d[41]),
        'col_42'  : str(d[42]),
        'col_43'  : str(d[43]),
        'col_44'  : str(d[44]),
        'col_45'  : str(d[45]),
        'col_46'  : str(d[46]),
        'col_47'  : str(d[47]),
        'col_48'  : str(d[48]),
        'col_49'  : str(d[49]),
        'col_50'  : str(d[50]),
        'col_51'  : str(d[51]),
        'col_52'  : str(d[52]),
        'col_53'  : str(d[53]),
        'col_54'  : str(d[54]),
        'col_55'  : str(d[55]),
        'col_56'  : str(d[56])
        }





def collums_load(apps, schema_editor):
    collums = {
        'col_0': 'Сводный код объекта ремонта (X/Y/Z)',
        'col_1': 'рег. № договора с ГИ-ГР',
        'col_2': 'Принципал',
        'col_3': 'Подразделение Принципала (ЛПУ, УПХГ, УГПГ, Завод и т.д.)',
        'col_4': 'Наименование объекта Диагностирования',
        'col_5': 'Наименование объекта диагностирования согласно карточке учета ОС',
        'col_6': 'Вид работ',
        'col_7': 'Содержание работ',
        'col_8': 'Инв. Номер',
        'col_9': 'Ед. изкмерения',
        'col_10': 'Кол-во',
        'col_11': 'Куратор',
        'col_12': 'Исполнители полевых работ',
        'col_13': 'Ведущий инженер КО',
        'col_14': 'Инженер КО',
        'col_15': 'Сметчик',
        'col_16': 'Стоимость работ, руб.',
        'col_17': 'I квартал',
        'col_18': 'II квартал',
        'col_19': 'III квартал',
        'col_20': 'IV квартал',
        'col_21': 'Исполнитель',
        'col_22': 'Соисполнитель',
        'col_23': 'Принадлежность к договору (ОСН, ДС1, ДС2 и т.д.)',
        'col_24': 'Стоимость работ Соисполнителя, руб без НДС',
        'col_25': 'ФАКТ',
        'col_26': 'Процент выполнения',
        'col_27': 'Финансовый акт, сумма без НДС в руб Полевой этап',
        'col_28': 'Финансовый акт, сумма без НДС в руб Камеральный этап',
        'col_29': 'ИТОГО выполнено работ, в руб без НДС Полевой+камеральный этап',
        'col_30': 'График производства работ',
        'col_31': 'Программа производства работ',
        'col_32': 'Допуск к производству работ',
        'col_33': 'Дата начала работ',
        'col_34': 'Дата окончания работ',
        'col_35': 'Дата начала работ Факт',
        'col_36': 'Дата окончания работ Факт',
        'col_37': 'Статус работ',
        'col_38': 'Выполнение физических объемов работ ФАКТ, ед.изм.',
        'col_39': 'Технический акт выполненных работ',
        'col_40': 'Приборы',
        'col_41': 'Автомобиль',
        'col_42': 'Дата выезда в командировку',
        'col_43': 'Дата возврата из командировки',
        'col_44': 'Технический отчет/Паспорт/Отчет о технич состоянии ПЛАН, шт.',
        'col_45': 'Технический отчет/Паспорт/Отчет о технич состоянии ПЕРЕДАНО ЗАКАЗЧИКУ НА СОГЛАСОВАНИЕ, шт.',
        'col_46': 'Технический отчет/Паспорт/Отчет о технич состоянии ОФОРМЛЕНО И СДАНО ЗАКАЗЧИКУ, шт.',
        'col_47': 'Технический отчет/Паспорт/Отчет о технич состоянии ДАТА СДАЧИ ПЛАН',
        'col_48': 'Технический отчет/Паспорт/Отчет о технич состоянии ДАТА СДАЧИ ФАКТ',
        'col_49': 'ЗЭПБ ПЛАН, шт.',
        'col_50': 'ЗЭПБ ПЛАН, дата сдачи по графику',
        'col_51': 'ЗЭПБ ФАКТ (передано Заказчику на согласование), шт.',
        'col_52': 'ЗЭПБ ФАКТ (оформлено и сдано Заказчику), шт.',
        'col_53': 'ЗЭПБ ФАКТ, дата сдачи',
        'col_54': 'ЗЭПБ ФАКТ ПЕРЕДАНО НА РЕГИСТРАЦИЮ В РТН, шт.',
        'col_55': 'ЗЭПБ ФАКТ ЗАРЕГИСТРИРО-ВАНО В РТН, шт.',
        'col_56': 'ЗЭПБ ФАКТ, дата регистрации'
    }
    Collums = apps.get_model('megaboss_app', 'Collums')
    for k, v in collums.items():
        collum, _ = Collums.objects.get_or_create(name=k, description=v)










