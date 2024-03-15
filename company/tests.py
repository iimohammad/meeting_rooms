from django.test import TestCase
from django.urls import reverse
from accounts.models import CustomUser
from .models import *
from .views import *


class TeamCreateViewTest(TestCase):
    def setUp(self):
        # Create a user
        self.user = CustomUser.objects.create_user(username='AliStev', password='8318@8318')
        # Create a company
        self.company = Company.objects.create(name="Apple", phone="09334236754",
                                              address="One Apple Park Way, Cupertino, California")

    def test_team_creation(self):
        # Login the user
        self.client.login(username='AliStev', password='8318@8318')

        # Create a team
        response = self.client.post(reverse('create-team'), {
            'company': self.company.id,
            'name': 'Conference Room',
            'manager': self.user.id,
            'members': [self.user.id],
        })

        # Check if the team was created successfully
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation
        self.assertTrue(Team.objects.filter(name='Conference Room').exists())
        self.assertEqual(Team.objects.filter(name='Conference Room')[0].company, self.company)
        self.assertEqual(Team.objects.filter(name='Conference Room')[0].name, 'Conference Room')
        self.assertEqual(Team.objects.filter(name='Conference Room')[0].manager, self.user)
        self.assertEqual(Team.objects.filter(name='Conference Room')[0].members.all()[0], self.user)

    def test_success_url(self):
        # Create a team
        team = Team.objects.create(name='Conference Room', company=self.company, manager=self.user)

        # Get the success URL
        view = TeamCreateView()
        view.object = team
        success_url = view.get_success_url()

        # Check if the success URL is correctly generated
        expected_url = reverse('team-list', kwargs={'company_id': team.company.id})
        self.assertEqual(success_url, expected_url)


class TeamDeleteViewTest(TestCase):
    def setUp(self):
        # Create a user
        self.user = CustomUser.objects.create_user(username='AliStev', password='8318@8318')
        # Create a company
        self.company = Company.objects.create(name="Apple", phone="09334236754",
                                              address="One Apple Park Way, Cupertino, California")
        # Create a team and associate it with the company created earlier
        self.team = Team.objects.create(name='Test Team', company=self.company, manager=self.user)

    def test_team_deletion(self):
        # Login the user
        self.client.login(username='AliStev', password='8318@8318')

        # Get the URL for the TeamDeleteView
        url = reverse('delete-team', kwargs={'pk': self.team.pk})

        # Send a DELETE request to delete the team
        response = self.client.delete(url)

        # Check if the team was deleted successfully
        self.assertEqual(response.status_code, 302)  # Expected redirect status code
        self.assertFalse(Team.objects.filter(pk=self.team.pk).exists())  # Team should not exist in the database

        # Check the redirect URL
        expected_url = reverse('team-list', kwargs={'company_id': self.team.company.id})
        self.assertRedirects(response, expected_url)


""" class TeamUpdateViewTest(TestCase):
    def setUp(self):
        # Create a user
        self.user1 = CustomUser.objects.create_user(username='AliStev', password='8318@8318')
        # Create another user
        self.user2 = CustomUser.objects.create_user(username='PeteGR7', password='P831T@RR')
        # Create a company
        self.company = Company.objects.create(name="Apple", phone="09334236754",
                                              address="One Apple Park Way, Cupertino, California")
        # Create a team and associate it with the company created earlier
        self.team = Team.objects.create(name='Test Team 1', company=self.company, manager=self.user1)

    def test_team_update(self):
        # Login the user
        self.client.login(username='AliStev', password='8318@8318')

        # Get the URL for the TeamUpdateView
        url = reverse('update-team', kwargs={'pk': self.team.pk})

        # Send a POST request to update the team
        updated_data = {
            'name': 'Test Team 2',
            'manager': self.user2,
            'company': self.team.company.id,
        }
        response = self.client.post(url, data=updated_data)

        # Check if the team was updated successfully
        self.assertEqual(response.status_code, 200)  # Expected redirect status code
        self.team.refresh_from_db()  # Refresh the team instance from the database
        self.assertEqual(self.team.name, 'Test Team 2')
        self.assertEqual(self.team.manager, self.user2)

        # Check the redirect URL
        expected_url = reverse('team-list', kwargs={'company_id': self.team.company.id})
        self.assertRedirects(response, expected_url) """


class TeamListViewTest(TestCase):
    def setUp(self):
        # Create a user
        self.user1 = CustomUser.objects.create_user(username='AliStev', password='8318@8318')
        # Create another user
        self.user2 = CustomUser.objects.create_user(username='PeteGR7', password='P831T@RR')
        # Create a company
        self.company = Company.objects.create(name="Apple", phone="09334236754",
                                              address="One Apple Park Way, Cupertino, California")
        # Create a team and associate it with the company created earlier
        self.team = Team.objects.create(name='Test Team 1', company=self.company, manager=self.user1)

    def test_team_list_view(self):
        # Login the user
        self.client.login(username='AliStev', password='8318@8318')

        # Get the URL for the TeamListView
        url = reverse('team-list', kwargs={'company_id': self.team.company.id})

        # Send a GET request to retrieve the team list
        response = self.client.get(url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the team name is present in the response content
        self.assertContains(response, self.team.name)

        # Check if the context object name 'teams' is correctly populated
        teams_in_context = response.context['teams']
        self.assertEqual(list(teams_in_context), [self.team])


""" class TeamDetailViewTest(TestCase):
    def setUp(self):
        # Create a sample Team instance for testing
        self.company = Company.objects.create(name="Apple", phone="09334236754",
                                              address="One Apple Park Way, Cupertino, California")
        self.manager = CustomUser.objects.create_user(username='AliStev', password='8318@8318')
        self.team = Team.objects.create(
            company=self.company,
            name="Test Team",
            manager=self.manager,
            permission=True,
            priority=5,
        )

    def test_team_detail_view(self):
        # Get the URL for the TeamDetailView using the team's primary key
        url = reverse("team-detail", kwargs={"pk": self.team.pk})
        response = self.client.get(url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 302)

        # check if the team's name or manager is displayed correctly in the response content.
        self.assertContains(response, self.team.name)
        self.assertContains(response, self.manager.username) """


class CompanyCreateViewTest(TestCase):
    def test_company_create_view(self):
        # Get the URL for the CompanyCreateView
        url = reverse("create-company")

        # Create a POST request with valid data
        data = {
            "name": "Apple",
            "phone": "09123456789",
            "address": "One Apple Park Way, Cupertino, California",
        }
        response = self.client.post(url, data)

        # Check that the response status code is 302 (redirect)
        # self.assertEqual(response.status_code, 302)

        # Check that the company was created successfully
        # self.assertTrue(Company.objects.filter(name="Apple").exists())

        # Check that the redirect URL matches the success_url
        self.assertEqual(response.url, "/accounts/login/?next=/company/create_company/")

        # Check if invalid data results in form errors
        # invalid_data = {
        #     "name": "",  # Invalid name (empty)
        #     "phone": "123",  # Invalid phone number
        #     "address": "Sample Address",
        # }
        # invalid_response = self.client.post(url, invalid_data)
        # self.assertContains(invalid_response, "Enter a valid mobile number")


""" class CompanyUpdateViewTest(TestCase):
    def setUp(self):
        # Create a sample Company instance for testing
        self.company = Company.objects.create(
            name="Apple",
            phone="09123456789",
            address="One Apple Park Way, Cupertino, California",
        )

    def test_company_update_view(self):
        # Get the URL for the CompanyUpdateView using the company's primary key
        url = reverse("update-company", kwargs={"pk": self.company.pk})

        # Create a POST request with updated data
        updated_data = {
            "name": "Google",
            "phone": "09129876543",
            "address": "Somewhere under the sky",
        }
        response = self.client.post(url, updated_data)

        # Check that the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)

        # Check that the company was updated successfully
        updated_company = Company.objects.get(pk=self.company.pk)
        self.assertEqual(updated_company.name, "Google")
        self.assertEqual(updated_company.phone, "09129876543")
        self.assertEqual(updated_company.address, "Somewhere under the sky")

        # Check that the redirect URL matches the success_url
        self.assertEqual(response.url, reverse("company-list")) """


""" class CompanyDeleteViewTest(TestCase):
    def setUp(self):
        # Create a sample Company instance for testing
        self.company = Company.objects.create(
            name="Apple",
            phone="09123456789",  # Adjust phone number as needed
            address="One Apple Park Way, Cupertino, California",
        )

    def test_company_delete_view(self):
        # Get the URL for the CompanyDeleteView using the company's primary key
        url = reverse('delete-company', kwargs={'pk': self.company.pk})

        # Create a POST request to simulate deleting the company
        response = self.client.post(url)

        # Check that the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)

        # Check that the company was deleted successfully
        self.assertFalse(Company.objects.filter(name='Apple').exists())

        # Check that the redirect URL matches the success_url
        self.assertEqual(response.url, reverse('company-list')) """


""" class CompanyListViewTest(TestCase):
    def setUp(self):
        # Create sample Company instances for testing
        Company.objects.create(name="Apple", phone="09123456789", address="Address A")
        Company.objects.create(name="Google", phone="09129876543", address="Address B")

    def test_company_list_view(self):
        # Get the URL for the CompanyListView
        url = reverse("company-list")

        # Make a GET request to the view
        response = self.client.get(url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the correct template is used
        self.assertTemplateUsed(response, "company_list.html")

        # Check if the companies are present in the context
        companies_in_context = response.context["companies"]
        self.assertEqual(companies_in_context.count(), 2)  # Assuming you have 2 sample companies

        # Check if company names are displayed in the response content.
        self.assertContains(response, "Company A")
        self.assertContains(response, "Company B") """
