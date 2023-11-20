"""from django.test import TestCase
from restapi import models
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework_api_key.models import APIKey
from rest_framework.test import APIClient
class TestModels(TestCase):
    def test_expense(self):
        expense = models.Expense.objects.create(
            amount=249.99,
            merchant="amazon",
            description="ANC headphones",
            category="music",
        )
        inserted_expense = models.Expense.objects.get(pk=expense.id)

        self.assertEqual(249.99, inserted_expense.amount)
        self.assertEqual("amazon", inserted_expense.merchant)
        self.assertEqual("ANC headphones", inserted_expense.description)
        self.assertEqual("music", inserted_expense.category)


class TestViews(TestCase):
    def setUp(self):
        # Create an API key for testing
        self.api_key, key = APIKey.objects.create_key(name="expense-service")
        self.client = APIClient()

    def test_expense_create(self):
        # Set the API key in the client's credentials
        self.client.credentials(HTTP_AUTHORIZATION=f"API-Key {self.api_key.key}")

        payload = {
            "amount": 50.0,
            "merchant": "AT&T",
            "description": "cell phone subscription",
            "category": "utilities",
        }
        res = self.client.post(
            "/api/expenses", data=payload, format="json"
        )

        self.assertEqual(201, res.status_code)

        json_res = res.json()

        self.assertEqual(payload["amount"], json_res["amount"])
        self.assertEqual(payload["merchant"], json_res["merchant"])
        self.assertEqual(payload["description"], json_res["description"])
        self.assertEqual(payload["category"], json_res["category"])
        self.assertIsInstance(json_res["id"], int)

    def test_expense_list(self):
        res = self.client.get(reverse("restapi:expense-list-create"), format="json")

        self.assertEqual(200, res.status_code)

        json_res = res.json()

        self.assertIsInstance(json_res, list)

        expenses = (
            models.Expense.objects.all()
        )  # Corrected the spelling "onjects" to "objects"
        self.assertEqual(len(expenses), len(json_res))

    def test_expense_create_required_fields_missing(self):
        payload = {
            "merchant": "AT&T",
            "description": "cell phone subscription",
            "category": "utilities",
        }
        res = self.client.post(
            reverse("restapi:expense-list-create"), data=payload, format="json"
        )

        self.assertEqual(400, res.status_code)

    def test_expense_retrieve(self):
        expense = models.Expense.objects.create(
            amount=300.0, merchant="Georgee", description="loan", category="Transfer"
        )
        res = self.client.get(
            reverse("restapi:expense-retrieve-delete", args=[expense.pk])
        )

        self.assertEqual(200, res.status_code)

        json_res = res.json()

        self.assertEqual(expense.id, json_res["id"])
        self.assertEqual(expense.amount, json_res["amount"])
        self.assertEqual(expense.merchant, json_res["merchant"])
        self.assertEqual(expense.description, json_res["description"])
        self.assertEqual(expense.category, json_res["category"])

    def test_delete(self):
        expense = models.Expense.objects.create(
            amount=400.0, merchant="Gee", description="loan", category="Transfer"
        )
        res = self.client.delete(
            reverse("restapi:expense-retrieve-delete", args=[expense.id])
        )
        self.assertEqual(204, res.status_code)
        self.assertFalse(models.Expense.objects.filter(pk=expense.id).exists())

    def test_list_expense_filter_by_merchant(self):
        amazon_expense = models.Expense.objects.create(
            amount=100, merchant="amazon", description="sunglasses", category="fashion"
        )
        ebay_expense = models.Expense.objects.create(
            amount=200, merchant="ebay", description="watch", category="fashion"
        )

        url = "/api/expenses?merchant=amazon"
        res = self.client.get(url, format="json")

        self.assertEqual(200, res.status_code)

        json_res = res.json()

        self.assertEqual(1, len(json_res))
        self.assertEqual(amazon_expense.id, json_res[0]["id"])
        self.assertEqual(amazon_expense.amount, json_res[0]["amount"])
        self.assertEqual(amazon_expense.merchant, json_res[0]["merchant"])
        self.assertEqual(amazon_expense.description, json_res[0]["description"])
        self.assertEqual(amazon_expense.category, json_res[0]["category"])
        """
"""
from django.test import TestCase
from django.urls import reverse
from rest_framework_api_key.models import APIKey
from rest_framework.test import APIClient
from restapi import models
from rest_framework_api_key.authentication import ApiKeyAuthentication

from rest_framework_api_key.authentication import ApiKeyAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework_api_key.models import APIKey

class TestModels(TestCase):
    def test_expense_creation(self):
        # Test the creation of an Expense object
        expense = models.Expense.objects.create(
            amount=249.99,
            merchant="amazon",
            description="ANC headphones",
            category="music",
        )
        inserted_expense = models.Expense.objects.get(pk=expense.id)

        self.assertEqual(249.99, inserted_expense.amount)
        self.assertEqual("amazon", inserted_expense.merchant)
        self.assertEqual("ANC headphones", inserted_expense.description)
        self.assertEqual("music", inserted_expense.category)

class TestViews(TestCase):
    def setUp(self):
        # Create an API key for testing
        self.api_key, key = APIKey.objects.create_key(name="expense-service")
        self.client = APIClient()

    def test_create_expense_with_valid_data(self):
        # Test creating an expense with valid data
        self.client.credentials(HTTP_AUTHORIZATION=f"API-Key {self.api_key.key}")

        payload = {
            "amount": 50.0,
            "merchant": "AT&T",
            "description": "cell phone subscription",
            "category": "utilities",
        }
        res = self.client.post(reverse("restapi:expense-list-create"), data=payload, format="json")

        self.assertEqual(201, res.status_code)
        json_res = res.json()

        self.assertEqual(payload["amount"], json_res["amount"])
        self.assertEqual(payload["merchant"], json_res["merchant"])
        self.assertEqual(payload["description"], json_res["description"])
        self.assertEqual(payload["category"], json_res["category"])
        self.assertIsInstance(json_res["id"], int)

    # Add more test methods for other views as needed with descriptive names

    def test_list_expenses_filter_by_merchant(self):
        # Test filtering expenses by merchant
        amazon_expense = models.Expense.objects.create(
            amount=100, merchant="amazon", description="sunglasses", category="fashion"
        )
        ebay_expense = models.Expense.objects.create(
            amount=200, merchant="ebay", description="watch", category="fashion"
        )

        url = reverse("restapi:expense-list-create") + "?merchant=amazon"
        res = self.client.get(url, format="json")

        self.assertEqual(200, res.status_code)
        json_res = res.json()

        self.assertEqual(1, len(json_res))
        self.assertEqual(amazon_expense.id, json_res[0]["id"])
        self.assertEqual(amazon_expense.amount, json_res[0]["amount"])
        self.assertEqual(amazon_expense.merchant, json_res[0]["merchant"])
        self.assertEqual(amazon_expense.description, json_res[0]["description"])
        self.assertEqual(amazon_expense.category, json_res[0]["category"])
"""
"""
from django.test import TestCase
from restapi import models
from django.urls import reverse
from rest_framework_api_key.models import APIKey
from rest_framework.test import APIClient

class TestModels(TestCase):
    def test_expense_creation(self):
        # Test the creation of an Expense object
        expense = models.Expense.objects.create(
            amount=249.99,
            merchant="amazon",
            description="ANC headphones",
            category="music",
        )
        inserted_expense = models.Expense.objects.get(pk=expense.id)

        self.assertEqual(249.99, inserted_expense.amount)
        self.assertEqual("amazon", inserted_expense.merchant)
        self.assertEqual("ANC headphones", inserted_expense.description)
        self.assertEqual("music", inserted_expense.category)

class TestViews(TestCase):
    def setUp(self):
        # Create an API key for testing
        self.api_key, key = APIKey.objects.create_key(name="expense-service")
        self.client = APIClient()

    def test_create_expense_with_valid_data(self):
        # Test creating an expense with valid data
        self.client.credentials(HTTP_AUTHORIZATION=f"Api-Key {self.api_key.key}")

        payload = {
            "amount": 50.0,
            "merchant": "AT&T",
            "description": "cell phone subscription",
            "category": "utilities",
        }
        res = self.client.post(reverse("restapi:expense-list-create"), data=payload, format="json")

        self.assertEqual(201, res.status_code)
        json_res = res.json()

        self.assertEqual(payload["amount"], json_res["amount"])
        self.assertEqual(payload["merchant"], json_res["merchant"])
        self.assertEqual(payload["description"], json_res["description"])
        self.assertEqual(payload["category"], json_res["category"])
        self.assertIsInstance(json_res["id"], int)

    def test_list_expenses_filter_by_merchant(self):
        # Test filtering expenses by merchant
        amazon_expense = models.Expense.objects.create(
            amount=100, merchant="amazon", description="sunglasses", category="fashion"
        )
        ebay_expense = models.Expense.objects.create(
            amount=200, merchant="ebay", description="watch", category="fashion"
        )

        url = reverse("restapi:expense-list-create") + "?merchant=amazon"
        res = self.client.get(url, format="json")

        self.assertEqual(200, res.status_code)
        json_res = res.json()

        self.assertEqual(1, len(json_res))
        self.assertEqual(amazon_expense.id, json_res[0]["id"])
        self.assertEqual(amazon_expense.amount, json_res[0]["amount"])
        self.assertEqual(amazon_expense.merchant, json_res[0]["merchant"])
        self.assertEqual(amazon_expense.description, json_res[0]["description"])
        self.assertEqual(amazon_expense.category, json_res[0]["category"])
"""
"""
doubt code
from django.test import TestCase
from restapi import models
from django.urls import reverse
from rest_framework_api_key.models import APIKey
from rest_framework.test import APIClient

class TestModels(TestCase):
    def test_expense_creation(self):
        # Test the creation of an Expense object
        expense = models.Expense.objects.create(
            amount=249.99,
            merchant="amazon",
            description="ANC headphones",
            category="music",
        )
        inserted_expense = models.Expense.objects.get(pk=expense.id)

        self.assertEqual(249.99, inserted_expense.amount)
        self.assertEqual("amazon", inserted_expense.merchant)
        self.assertEqual("ANC headphones", inserted_expense.description)
        self.assertEqual("music", inserted_expense.category)

class TestViews(TestCase):
    def setUp(self):
        # Create an API key for testing
        self.api_key, key = APIKey.objects.create_key(name="expense-service")
        self.client = APIClient()

    def test_create_expense_with_valid_data(self):
        # Test creating an expense with valid data
        self.client.credentials(HTTP_AUTHORIZATION=f"Api-Key {self.api_key.key}")

        payload = {
            "amount": 50.0,
            "merchant": "AT&T",
            "description": "cell phone subscription",
            "category": "utilities",
        }
        res = self.client.post(reverse("expense-list-create"), data=payload, format="json")

        self.assertEqual(201, res.status_code)
        json_res = res.json()

        self.assertEqual(payload["amount"], json_res["amount"])
        self.assertEqual(payload["merchant"], json_res["merchant"])
        self.assertEqual(payload["description"], json_res["description"])
        self.assertEqual(payload["category"], json_res["category"])
        self.assertIsInstance(json_res["id"], int)

    def test_list_expenses_filter_by_merchant(self):
        # Test filtering expenses by merchant
        amazon_expense = models.Expense.objects.create(
            amount=100, merchant="amazon", description="sunglasses", category="fashion"
        )
        ebay_expense = models.Expense.objects.create(
            amount=200, merchant="ebay", description="watch", category="fashion"
        )

        url = reverse("expense-list-create") + "?merchant=amazon"
        res = self.client.get(url, format="json")

        self.assertEqual(200, res.status_code)
        json_res = res.json()

        self.assertEqual(1, len(json_res))
        self.assertEqual(amazon_expense.id, json_res[0]["id"])
        self.assertEqual(amazon_expense.amount, json_res[0]["amount"])
        self.assertEqual(amazon_expense.merchant, json_res[0]["merchant"])
        self.assertEqual(amazon_expense.description, json_res[0]["description"])
        self.assertEqual(amazon_expense.category, json_res[0]["category"])
"""
from django.test import TestCase
from restapi import models
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework_api_key.models import APIKey
from rest_framework.test import APIClient


class TestModels(TestCase):
    def test_expense(self):
        expense = models.Expense.objects.create(
            amount=249.99,
            merchant="amazon",
            description="ANC headphones",
            category="music",
        )
        inserted_expense = models.Expense.objects.get(pk=expense.id)

        self.assertEqual(249.99, inserted_expense.amount)
        self.assertEqual("amazon", inserted_expense.merchant)
        self.assertEqual("ANC headphones", inserted_expense.description)
        self.assertEqual("music", inserted_expense.category)


class TestViews(TestCase):
    def setUp(self):
        # Create the user "Test1234" and set their password
        #  user = User.objects.create_user("Test1234", "testuser@example.com", "Test1234")
        api_key, key = APIKey.objects.create_key(name="expense-service")
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f"Api-Key {key}")
        # Log in the user using the client

    # self.client.login(username="Test1234", password="Test1234")

    def test_expense_create(self):
        payload = {
            "amount": 50.0,
            "merchant": "AT&T",
            "description": "cell phone subscription",
            "category": "utilities",
        }
        res = self.client.post(
            reverse("restapi:expense-list-create"), data=payload, format="json"
        )

        self.assertEqual(201, res.status_code)

        json_res = res.json()

        self.assertEqual(payload["amount"], json_res["amount"])
        self.assertEqual(payload["merchant"], json_res["merchant"])
        self.assertEqual(payload["description"], json_res["description"])
        self.assertEqual(payload["category"], json_res["category"])
        self.assertIsInstance(json_res["id"], int)

    def test_expense_list(self):
        res = self.client.get(reverse("restapi:expense-list-create"), format="json")

        self.assertEqual(200, res.status_code)

        json_res = res.json()

        self.assertIsInstance(json_res, list)

        expenses = (
            models.Expense.objects.all()
        )  # Corrected the spelling "onjects" to "objects"
        self.assertEqual(len(expenses), len(json_res))

    def test_expense_create_required_fields_missing(self):
        payload = {
            "merchant": "AT&T",
            "description": "cell phone subscription",
            "category": "utilities",
        }
        res = self.client.post(
            reverse("restapi:expense-list-create"), data=payload, format="json"
        )

        self.assertEqual(400, res.status_code)

    def test_expense_retrieve(self):
        expense = models.Expense.objects.create(
            amount=300.0, merchant="Georgee", description="loan", category="Transfer"
        )
        res = self.client.get(
            reverse("restapi:expense-retrieve-delete", args=[expense.pk])
        )

        self.assertEqual(200, res.status_code)

        json_res = res.json()

        self.assertEqual(expense.id, json_res["id"])
        self.assertEqual(expense.amount, json_res["amount"])
        self.assertEqual(expense.merchant, json_res["merchant"])
        self.assertEqual(expense.description, json_res["description"])
        self.assertEqual(expense.category, json_res["category"])

    def test_delete(self):
        expense = models.Expense.objects.create(
            amount=400.0, merchant="Gee", description="loan", category="Transfer"
        )
        res = self.client.delete(
            reverse("restapi:expense-retrieve-delete", args=[expense.id])
        )
        self.assertEqual(204, res.status_code)
        self.assertFalse(models.Expense.objects.filter(pk=expense.id).exists())

    def test_list_expense_filter_by_merchant(self):
        amazon_expense = models.Expense.objects.create(
            amount=100, merchant="amazon", description="sunglasses", category="fashion"
        )
        ebay_expense = models.Expense.objects.create(
            amount=200, merchant="ebay", description="watch", category="fashion"
        )

        url = "/api/expenses?merchant=amazon"
        res = self.client.get(url, format="json")

        self.assertEqual(200, res.status_code)

        json_res = res.json()

        self.assertEqual(1, len(json_res))
        self.assertEqual(amazon_expense.id, json_res[0]["id"])
        self.assertEqual(amazon_expense.amount, json_res[0]["amount"])
        self.assertEqual(amazon_expense.merchant, json_res[0]["merchant"])
        self.assertEqual(amazon_expense.description, json_res[0]["description"])
        self.assertEqual(amazon_expense.category, json_res[0]["category"])
