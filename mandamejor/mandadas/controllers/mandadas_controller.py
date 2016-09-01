

from ..models import Mandada


class MandadaController:

    def __init__(self, init_date=None, end_date=None, user_id=None,
                 user_email=None):
        self.init_date = init_date
        self.end_date = end_date
        self.user_id = user_id
        self.user_email = user_email
        self.queryset = Mandada.objects.all()

    def run_query(self):
        if self.init_date and self.end_date:
            self._filter_by_date()
        if self.user_email:
            self._filter_by_user_email()
        if self.user_id:
            self._filter_by_user_id()
        return self.queryset

    def _filter_by_date(self):
        assert self.init_date, 'init_date is obligatory'
        assert self.end_date, 'end_date is obligatory'
        self.queryset = self.queryset.filter(
            when__range=(self.init_date, self.end_date)
        )

    def _filter_by_user_id(self):
        assert self.user_id, 'user_id is obligatory'
        self.queryset = self.queryset.filter(user__id=self.user_id)

    def _filter_by_user_email(self):
        assert self.user_email, 'user_email is obligatory'
        self.queryset = self.queryset.filter(user__email=self.user_email)
