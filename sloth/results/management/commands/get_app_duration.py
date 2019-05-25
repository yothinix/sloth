from django.core.management.base import BaseCommand

from ...models import Result


class Command(BaseCommand):
    def handle(self, *args, **options):
        apps = []
        total_test_time = 0
        all_results = Result.objects.all()
        for result in all_results:
            app_name = result.app_name
            if app_name not in apps:
                apps.append(app_name)

        print(f"{'App':<20}TIME(s)")
        print('--------------------------------------')
        for app in apps:
            app_test_time = 0
            app_tests = Result.objects.filter(app_name=app)
            for test in app_tests:
                app_test_time += test.time

            total_test_time += app_test_time
            print(f'{app:<20}{app_test_time:.2f}')
        print('--------------------------------------')
        print(f"{'TOTAL TEST TIME':<20}{total_test_time:.2f}")
