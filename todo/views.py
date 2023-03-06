from django.shortcuts import render
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task
from common.common import TodoView


# Create your views here.
class TaskCreate(TodoView):
    def post(self, request):
        #user_id = request.data.get('user_id', "")
        user_id = self.user_id
        name = request.data.get('name', "")
        end_date = request.data.get('end_date', None)
        if end_date:
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        task = Task.objects.create(user_id=user_id, name=name, end_date=end_date)

        return Response(dict(msg='Create success To-do list', name=task.name,
                             start_date=task.start_date.strftime('%Y-%m-%d'), end_date=task.end_date))


class TaskSelect(APIView):
    def post(self, request):
        user_id = request.data.get('user_id', "")

        tasks = Task.objects.filter(user_id=user_id)
        tasks_list = []
        for task in tasks:
            tasks_list.append(
                dict(name=task.name, start_date=task.start_date, end_date=task.end_date, state=task.state))

        return Response(dict(task=tasks_list))


class Todo(APIView):
    def post(self,request):
        user_id = request.data.get('user_id', "")
        name = request.data.get('name', "")
        end_date = request.data.get('end_date', None)
        if end_date:
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        Task.objects.create(user_id=user_id, name=name, end_date=end_date)

        tasks = Task.objects.all()
        task_list = []
        for task in tasks:
            task_list.append(
                dict(name=task.name, start_date=task.start_date, end_date=task.end_date, state=task.state))
        context = dict(task_list=task_list)
        return render(request, 'todo/todo.html', context=context)

    def get(self, request):
        tasks = Task.objects.all()
        task_list = []
        for task in tasks:
            task_list.append(
                dict(name=task.name, start_date=task.start_date, end_date=task.end_date, state=task.state))
        context = dict(task_list=task_list)
        return render(request, 'todo/todo.html', context=context)


class Test(TodoView):
    def post(self, request):
        print(self.user_id)
        return Response(status=400, data=dict(user_id=self.user_id))