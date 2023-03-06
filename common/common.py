from rest_framework.views import APIView


class TodoView(APIView):
    user_id = ''

    def dispatch(self, request, *args, **kwargs):
        self.user_id = request.headers.get('id',False)

        return super(TodoView, self).dispatch(request, *args, **kwargs)
