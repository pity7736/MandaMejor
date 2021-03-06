from django.test import TestCase, Client

from ..models import Mandada, User


class MandadaViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        user1 = User.objects.create_user('user1@comparamejor.com')
        user2 = User.objects.create_user('user2@comparamejor.com')
        Mandada.objects.bulk_create((
            Mandada(user=user1, when='2016-08-30'),
            Mandada(user=user1, when='2016-08-27'),
            Mandada(user=user2, when='2016-08-25'),
            Mandada(user=user2, when='2016-08-26'),
            Mandada(user=user2, when='2016-08-28'),
            Mandada(user=user1, when='2016-08-28'),
            Mandada(user=user1, when='2016-08-30 09:10'),
        ))

    def setUp(self):
        self.client = Client()

    def test_get_mandadas(self):
        response = self.client.get('/mandadas/')

        self.assertEqual(response.data['count'], 7)
        self.assertEqual(response.status_code, 200)

    def test_get_mandadas_no_content(self):
        Mandada.objects.all().delete()
        response = self.client.get('/mandadas/')

        self.assertEqual(response.data['count'], 0)
        self.assertEqual(response.status_code, 204)

    def test_search_mandadas_by_date_range(self):
        response = self.client.get(
            '/mandadas/search/date/2016-08-28/2016-08-30/'
        )

        self.assertEqual(response.data['count'], 4)
        self.assertEqual(response.status_code, 200)

    def test_search_mandadas_by_data_same_date(self):

        response = self.client.get(
            '/mandadas/search/date/2016-08-28/2016-08-28/'
        )

        self.assertEqual(response.data['count'], 2)
        self.assertEqual(response.status_code, 200)

    def test_search_mandadas_by_date_without_other_date(self):
        response = self.client.get('/mandadas/search/date/2016-08-28/')

        self.assertEqual(response.status_code, 404)

    def test_search_mandadas_by_date_with_wrong_day(self):
        response = self.client.get(
            '/mandadas/search/date/2016-08-31/2016-08-40/'
        )

        self.assertEqual(response.status_code, 400)

    def test_search_mandadas_by_date_with_wrong_month(self):
        response = self.client.get(
            '/mandadas/search/date/2016-12-31/2016-13-40/'
        )

        self.assertEqual(response.status_code, 400)

    def test_get_mandadas_by_user_id(self):
        response = self.client.get('/mandadas/search/user/1/')

        self.assertEqual(response.data['count'], 4)
        self.assertEqual(response.data['data'][0]['user'], 1)
        self.assertEqual(response.data['data'][1]['user'], 1)
        self.assertEqual(response.data['data'][2]['user'], 1)
        self.assertEqual(response.status_code, 200)

    def test_get_mandadas_by_nonexistent_user(self):
        response = self.client.get('/mandadas/search/user/10/')

        self.assertEqual(response.data['count'], 0)
        self.assertEqual(response.status_code, 204)

    def test_get_mandadas_by_user_email(self):
        response = self.client.get(
            '/mandadas/search/user/user1@comparamejor.com/'
        )

        self.assertEqual(response.data['count'], 4)
        self.assertEqual(response.status_code, 200)

    def test_get_mandadas_by_user_id_and_date(self):
        params = {
            'user_id': 1,
            'init_date': '2016-08-28',
            'end_date': '2016-08-30'
        }
        response = self.client.get('/mandadas/search/', params)

        self.assertEqual(response.data['count'], 3)
        self.assertEqual(response.status_code, 200)

    def test_get_mandadas_by_user_email_and_date(self):
        params = {
            'user_email': 'user1@comparamejor.com',
            'init_date': '2016-08-28',
            'end_date': '2016-08-30'
        }
        response = self.client.get('/mandadas/search/', params)

        self.assertEqual(response.data['count'], 3)
        self.assertEqual(response.status_code, 200)
