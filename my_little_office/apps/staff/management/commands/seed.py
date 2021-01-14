from random import choice, randint
from decimal import Decimal

from django.core.management.base import BaseCommand

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
            """Generate employee ready to creating throgh comprehension."""
            names = fake.name().split(' ')
            parent = choice(parents)
            return Employee(
                second_name=names[-3],
                first_name=names[-2],
                patronym=names[-1],
                position=choice(positions),
                salary=Decimal(randint(10000, 50000) / 100),
                parent=parent,
                # Lil trick right here
                # manager cannot make `bulk_create` cause there are not null
                # field so, we make some defalt value and when all
                # data populated -- call `rebuild` to recreate the tree
                # noqa, People talk about this at https://stackoverflow.com/questions/12661488/how-optimize-adding-new-nodes-in-django-mptt
                lft=1,
                rght=1,
                tree_id=parent.tree_id,
                level=parent.level+1,
            )

        def create_level_staff(level, amount, parents, positions):
            print(f'populating {amount} level {level} staff.')
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
                patronym=names[-1],
                position=choice(positions),
                salary=Decimal(randint(10000, 100000) / 100),
            ))
        print(f'populated: {", ".join(e.full_name for e in level0)}')

        level1 = create_level_staff(1, options['staff_l1'], level0, positions)
        level2 = create_level_staff(2, options['staff_l2'], level1, positions)
        level3 = create_level_staff(3, options['staff_l3'], level2, positions)
        create_level_staff(4, options['staff_l4'], level3, positions)

        # Do not forget `rebuild` tree to make mptt work properly`
        Employee.objects.rebuild()

        print('done')
