# me/tests.py
from django.test import SimpleTestCase
from django.urls import reverse


class AboutMeTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")

    def test_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>About this person</h1>")


class InterestsMeTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/interests/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("interests"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("interests"))
        self.assertTemplateUsed(response, "interests.html")

    def test_template_content(self):
        response = self.client.get(reverse("interests"))
        self.assertContains(response, "<h1>Interests</h1>")
