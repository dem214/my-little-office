from random import choice, randint
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.db.transaction import atomic

from ...models import Employee, Position


class Command(BaseCommand):
    help = "Seeding database with some amount of data"

    def add_arguments(self, parser):
        parser.add_argument('--positions', nargs='?', type=int, default=15,
                            help="Amount of populating positions")
        parser.add_argument('--staff_l0', nargs='?', type=int, default=1,
                            help="Amount of populating staff with level 0")
        parser.add_argument('--staff_l1', nargs='?', type=int, default=5,
                            help="Amount of populating staff with level 1")
        parser.add_argument('--staff_l2', nargs='?', type=int, default=10,
                            help="Amount of populating staff with level 2")
        parser.add_argument('--staff_l3', nargs='?', type=int, default=15,
                            help="Amount of populating staff with level 3")
        parser.add_argument('--staff_l4', nargs='?', type=int, default=50,
                            help="Amount of populating staff with level 4")

    def handle(self, *args, **options):

        def gen_employee(positions, parents):
            names = fake.name().split(' ')
            parent = choice(parents)
            return Employee(
                second_name=names[-3],
                first_name=names[-2],
                patronim=names[-1],
                position=choice(positions),
                salary=Decimal(randint(10000, 50000) / 100),
                parent=parent,
                lft=1,
                rght=1,
                tree_id=parent.tree_id,
                level=parent.level+1,
            )

        def create_level_staff(amount, parents, positions):
            print(f'populating {amount} level 1 staff.')
            staff_presave = []
            for i in range(amount):
                staff_presave.append(gen_employee(positions, parents))
            staff = Employee.objects.bulk_create(staff_presave)
            print(f'populated: {", ".join(e.full_name for e in staff)}.')
            return staff

        from faker import Faker
        fake = Faker('ru_RU')

        print(f'populating {options["positions"]} positions')
        positions = Position.objects.bulk_create((
            Position(name=fake.job()) for i in range(options['positions'])
        ))
        print(f'populated: {", ".join(p.name for p in positions)}')

        print(f'populating {options["staff_l0"]} level 0 staff')
        level0 = list()
        for i in range(options['staff_l0']):
            names = fake.name().split(' ')
            level0.append(Employee.objects.create(
                second_name=names[-3],
                first_name=names[-2],
                patronim=names[-1],
                position=choice(positions),
                salary=Decimal(randint(10000, 100000) / 100),
            ))
        print(f'populated: {", ".join(e.full_name for e in level0)}')

        level1 = create_level_staff(options['staff_l1'], level0, positions)
        level2 = create_level_staff(options['staff_l2'], level1, positions)
        level3 = create_level_staff(options['staff_l3'], level2, positions)
        level4 = create_level_staff(options['staff_l4'], level3, positions)

        Employee.objects.rebuild()

        print('done')