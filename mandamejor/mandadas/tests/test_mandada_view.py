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
        ))

    def setUp(self):
        self.client = Client()

    def test_get_mandadas(self):
        response = self.client.get('/mandadas/')

        self.assertEqual(len(response.data), 6)
        self.assertEqual(response.status_code, 200)

    def test_get_mandadas_no_content(self):
        Mandada.objects.all().delete()
        response = self.client.get('/mandadas/')

        self.assertEqual(len(response.data), 0)
        self.assertEqual(response.status_code, 204)

    def test_search_mandadas_by_when_date(self):
        response = self.client.get('/mandadas/search/', {'when': '2016-08-28'})

        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['when'], '2016-08-28')

    def test_get_mandadas_by_user(self):
        response = self.client.get('/mandadas/user/1/')

        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]['user'], 1)
        self.assertEqual(response.data[1]['user'], 1)
        self.assertEqual(response.data[2]['user'], 1)
        self.assertEqual(response.status_code, 200)

    def test_get_mandadas_by_nonexistent_user(self):
        response = self.client.get('/mandadas/user/10/')

        self.assertEqual(len(response.data), 0)
        self.assertEqual(response.status_code, 204)
