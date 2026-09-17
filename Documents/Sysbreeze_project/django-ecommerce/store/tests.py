from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .forms import RegistrationForm


class RegistrationFormTests(TestCase):
	def test_required_fields_and_password_confirmation_are_validated(self):
		form = RegistrationForm(
			data={
				'name': '',
				'username': '',
				'email': 'not-an-email',
				'password1': 'StrongPass123X',
				'password2': 'DifferentPass123X',
			}
		)

		self.assertFalse(form.is_valid())
		self.assertIn('name', form.errors)
		self.assertIn('username', form.errors)
		self.assertIn('email', form.errors)
		self.assertIn('password2', form.errors)

	def test_duplicate_username_and_email_are_rejected(self):
		User.objects.create_user(
			username='existing',
			email='existing@example.com',
			password='StrongPass123X',
		)

		username_form = RegistrationForm(
			data={
				'name': 'New User',
				'username': 'EXISTING',
				'email': 'new@example.com',
				'password1': 'StrongPass123X',
				'password2': 'StrongPass123X',
			}
		)
		email_form = RegistrationForm(
			data={
				'name': 'New User',
				'username': 'new-user',
				'email': 'EXISTING@EXAMPLE.COM',
				'password1': 'StrongPass123X',
				'password2': 'StrongPass123X',
			}
		)

		self.assertFalse(username_form.is_valid())
		self.assertFalse(email_form.is_valid())
		self.assertIn('username', username_form.errors)
		self.assertIn('email', email_form.errors)

	def test_registration_hashes_password_and_redirects_to_login(self):
		response = self.client.post(
			reverse('register'),
			{
				'name': 'New User',
				'username': 'new-user',
				'email': 'new@example.com',
				'password1': 'StrongPass123X',
				'password2': 'StrongPass123X',
			},
		)

		user = User.objects.get(username='new-user')
		self.assertRedirects(response, reverse('login'))
		self.assertEqual(user.first_name, 'New User')
		self.assertTrue(user.check_password('StrongPass123X'))
		self.assertNotEqual(user.password, 'StrongPass123X')


class AuthenticationViewTests(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(
			username='shopper',
			email='shopper@example.com',
			password='StrongPass123X',
		)

	def test_home_requires_authentication(self):
		response = self.client.get(reverse('home'))

		self.assertRedirects(response, f'{reverse("login")}?next={reverse("home")}')

	def test_login_accepts_username_and_email(self):
		for identifier in ('shopper', 'shopper@example.com'):
			self.client.logout()
			response = self.client.post(
				reverse('login'),
				{'username': identifier, 'password': 'StrongPass123X'},
			)
			self.assertRedirects(response, reverse('home'))
			self.assertTrue(response.wsgi_request.user.is_authenticated)

	def test_invalid_login_shows_error(self):
		response = self.client.post(
			reverse('login'),
			{'username': 'shopper', 'password': 'WrongPassword123X'},
		)

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'correct username or email and password')
		self.assertFalse(response.wsgi_request.user.is_authenticated)

	def test_logout_ends_session_and_requires_post(self):
		self.client.force_login(self.user)

		get_response = self.client.get(reverse('logout'))
		post_response = self.client.post(reverse('logout'))
		home_response = self.client.get(reverse('home'))

		self.assertEqual(get_response.status_code, 405)
		self.assertRedirects(post_response, reverse('login'))
		self.assertRedirects(home_response, f'{reverse("login")}?next={reverse("home")}')
