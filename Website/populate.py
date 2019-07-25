import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Website.settings')
import django

django.setup()
import random
from faker import Faker
from Application.models import Topic, Webpage, AccessRecord, MyUser

fake_gen = Faker()

topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    top = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    top.save()
    return top


def populate(count=5):
    for entry in range(count):
        top = add_topic()

        fake_url = fake_gen.url()
        fake_name = fake_gen.company()
        fake_date = fake_gen.date()

        webpage = Webpage.objects.get_or_create(topic=top, name=fake_name, url=fake_url)[0]

        access_record = AccessRecord.objects.get_or_create(name=webpage, date=fake_date)[0]

        fake_first_name = fake_gen.first_name()
        fake_last_name = fake_gen.last_name()
        fake_email = fake_gen.email()

        user = MyUser.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)


if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating finished")
