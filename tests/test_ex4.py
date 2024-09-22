import pytest
from django.contrib.auth.models import User



# @pytest.mark.django_db
# def test_set_check_password(user_1):
#     print("check password")
#     user_1.set_password("new-password")
#     assert user_1.check_password("new-password") is True


# @pytest.mark.django_db
# def test_set_check_username(user_1):
#     print("check username")
#     assert user_1.username == "test-user"


# @pytest.mark.django_db
# def test_new_user(new_user2):
#     print(new_user2.is_staff)
#     assert new_user2.is_staff


# @pytest.mark.django_db
# def test_new_user(user_factory):
#     user = user_factory.build()
#     count = User.objects.all().count()
#     print(count)
#     print(user.username)
#     assert True

@pytest.mark.django_db
def test_new_user(new_user1):
    print(new_user1.username)
    assert True


def test_product(db, product_factory):
    product = product_factory.create()
    print(product.description)
    assert True
