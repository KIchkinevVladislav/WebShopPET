from http import HTTPStatus
from datetime import timedelta
from django.utils.timezone import now

from django.test import TestCase
from django.urls import reverse

from users.models import User, EmailVerification
from users.forms import UserRegistrationForm

class UserRegistarationTestCase(TestCase):

    def setUp(self):
        self.data = {
            'first_name': 'Slava', 'last_name': 'Kich',
            'username': 'ki', 'email': 'test@mail.ru',
            'password1': 'TESTpassword1', 'password2': 'TESTpassword1'
        }
        self.path = reverse('users:registration')

    def test_user_registaration_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store - Регистрация')
        self.assertTemplateUsed(response, 'users/registration.html')
        
    def test_user_registaration_post_success(self):

        username = self.data['username']
        self.assertFalse(User.objects.filter(username=username).exists())
        response = self.client.post(self.path, data=self.data)

        #проверка создания пользователя
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('users:login'))
        self.assertTrue(User.objects.filter(username=username).exists())

        #проверка создания объекта для верификации по емайлу
        email_verification = EmailVerification.objects.filter(user__username=username)
        self.assertTrue(email_verification.exists())
        self.assertEqual(
            email_verification.first().expiration.date(),
            (now() + timedelta(hours=48)).date()
        )

    def test_user_registaration_post_error(self):
        User.objects.create(username = self.data['username'])
        response = self.client.post(self.path, self.data)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Пользователь с таким именем уже существует.', html=True)
