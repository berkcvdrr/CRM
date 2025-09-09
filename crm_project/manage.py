import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','crm_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError('djangodan veriler getiremedi')