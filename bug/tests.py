from django.test import TestCase
from django.db.models import Count
from .models import A, B, C

class Tests(TestCase):
    def test_bug(self):
        a = A.objects.create()
        B.objects.create(a=a)
        B.objects.create(a=a)
        C.objects.create(a=a)
        query = A.objects.annotate(b_count=Count('b'), c_count=Count('c'))
        a = query.get()
        print('SQL:')
        print(query.query)
        print()
        # duh...
        self.assertEquals(2, a.b_count)
        # 2?! It's clearly 1!
        self.assertEquals(1, a.c_count)
