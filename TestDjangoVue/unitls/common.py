# -*- coding: utf-8 -*-
from collections import Iterable

__AUTHOR__ = 'DaVenshee'

import os
import sys

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TestDjangoVue.settings")

import django
django.setup()


from testvue.models import TestModel


def gen_model():
    for i in range(1000):
        t = TestModel(name = str(i))
        t.save()


if __name__ == '__main__':
    # gen_model()
    rs =TestModel.objects.all()
    print(isinstance(rs, Iterable))
    print(TestModel.objects.count())
    # for r in rs:
    #     print(r)