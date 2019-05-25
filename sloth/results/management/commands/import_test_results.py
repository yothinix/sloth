from pathlib import Path

from django.core.management.base import BaseCommand

import xmltodict

from ...models import Result


class Command(BaseCommand):
    def handle(self, *args, **options):
        current_dir = Path('.').cwd()
        file_path = current_dir / 'data' / 'report.xml'
        with file_path.open() as file:
            test_result = file.read()
            test_result_dict = xmltodict.parse(test_result)
            total_time = test_result_dict['testsuite']['@time']
            for testcase in test_result_dict['testsuite']['testcase']:
                instance, _ = Result.objects.get_or_create(
                    app_name=testcase['@classname'].split('.')[0],
                    class_name=testcase['@classname'],
                    file_name=testcase['@file'],
                    test_name=testcase['@name'],
                    time=testcase['@time']
                )
                print(instance)
