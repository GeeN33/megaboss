from django.http import JsonResponse
from django.shortcuts import render
from django.contrib import messages
from rest_framework import permissions
from rest_framework.views import APIView
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

from megaboss_app.models import Plan_row, Collums, CollumsUser
from megaboss_app.utils import import_excel_to_db, import_excel_to_cache, cache_excel_to_db


def index(request):
    collum = ['col_0', 'col_1', 'col_2', 'col_3', 'col_4', 'col_5', 'col_6', 'col_7', 'col_8']
    plan_rows = Plan_row.objects.filter(plan_id=1).values_list(*collum)

    collum_list=[]
    for c in collum:
        collum_list.append(Plan_row._meta.get_field(c).verbose_name)

    for p in collum_list:
        print(p)

    for p in plan_rows:
        print(p)



    return render(request, "megaBoss1.html",  context = {"collum_list": collum_list, "plan_rows": plan_rows})

def import_excel(request):
    if request.method == 'POST' and request.FILES['file']:
        file= request.FILES['file']
        rez = import_excel_to_db(file.read(), file.name)
        if rez[0]:
            messages.success(request, f'Данные загружены успешно! всего в базе строк {rez[1]}, новых {rez[2]}')
        else:
             messages.error(request, 'Что то с файлом не так!!!')

        return render(request, 'import_excel.html', {
            'uploaded_file_url': file.name
        })

    return render(request, 'import_excel.html', {})

class GetCollum(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request):
        data={}
        collums = CollumsUser.objects.filter(user=self.request.user)
        data = [collum.json() for collum in collums]
        return JsonResponse(data, safe=False, json_dumps_params={"ensure_ascii": True}, status=200)

class SetCollum(APIView):

    permission_classes = [permissions.IsAuthenticated,]

    def get(self, request):
        collumsget =  self.request.query_params.getlist('collums[]')

        collums = CollumsUser.objects.filter(user=self.request.user)

        for collum in  collums:
            if collum.collum.name in collumsget:
                collum.checked = 1
                collum.save()
            else:
                collum.checked = 0
                collum.save()


        return JsonResponse({'ok':'ok'},  safe=False, json_dumps_params={"ensure_ascii": True}, status=200)

class GetList(APIView):

    permission_classes = [permissions.IsAuthenticated,]

    def get(self, request):
        collum = CollumsUser.objects.filter(user=self.request.user).filter(checked=1).values_list('collum__name',flat=True)
        if not collum:
            collum = ['col_0', 'col_1', 'col_2', 'col_3', 'col_4', 'col_5', 'col_6', 'col_7', 'col_8']
            cc = Collums.objects.filter(name__in=collum)
            for cl in cc :
               CollumsUser.objects.get_or_create(user_id=self.request.user.id, collum_id=cl.id)

        plan_rows = Plan_row.objects.filter(plan_id=1).values_list(*collum)

        collum_list=[]
        for c in collum:
            collum_list.append(Plan_row._meta.get_field(c).verbose_name)

        plan_rows_list=[]
        for p in plan_rows:
            plan_rows_list.append(p)

        data={
            'collumlist': collum_list,
            'planrows': plan_rows_list
        }

        # for p in collum_list:
        #     print(p)
        #
        # for p in plan_rows:
        #     print(p)

        return JsonResponse(data,  safe=False, json_dumps_params={"ensure_ascii": True}, status=200)

class Import_Excel(APIView):

    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request, format=None):
        data = {}
        file =  request.data['file']
        rez = import_excel_to_cache(file.read(), file.name)
        if rez[0]:
            cache.set('filename', file.name, timeout=CACHE_TTL)
            cache.set('plan', rez[5], timeout=CACHE_TTL)
            print(f'Данные загружены успешно! всего в базе строк {rez[1]}, новых {rez[2]}, обновленных {rez[3]}, ошибок {rez[4]}')
            data = {
                'file_name': file.name,
                'count_all': rez[1],
                'row_new': rez[2],
                'row_updata': rez[3],
                'row_error': rez[4],
            }
        else:
            print('Что то с файлом не так!!!')

        return JsonResponse(data, safe=False, json_dumps_params={"ensure_ascii": True}, status=202)


class Save_Excel(APIView):

    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        data = {}
        rez =  self.request.query_params.get('save')
        if rez == 'ok':
            if 'plan' in cache and 'filename' in cache:
                plan = cache.get('plan')
                file_mame = cache.get('filename')
                upbd = cache_excel_to_db(plan, file_mame)
                print('upbd' ,upbd )
                cache.delete('plan')
                cache.delete('filename')

        else:
            cache.delete('plan')
            cache.delete('filename')

        return JsonResponse(data, safe=False, json_dumps_params={"ensure_ascii": True}, status=202)