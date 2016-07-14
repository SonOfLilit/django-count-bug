```python
def test_bug(self):
    a = A.objects.create()
    B.objects.create(a=a)
    B.objects.create(a=a)
    C.objects.create(a=a)
    # duh...
    a = A.objects.annotate(b_count=Count('b'), c_count=Count('c')).get()
    self.assertEquals(2, a.b_count)
    # 2?! It's clearly 1!
    self.assertEquals(1, a.c_count)
```

Reproduces on `sqlite3` as well as heroku-hosted `postgresql`.

mailto:aur@feezback.com