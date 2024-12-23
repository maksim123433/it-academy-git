from enum import Enum

class Role(Enum):
    DIRECTOR = 'Директор отвечает за общее руководство компанией, принятие стратегических решений и контроль за выполнением задач.'
    FINANCIAL_MANAGER = 'Финансовый менеджер занимается управлением финансовыми потоками компании, анализом доходов и расходов, а также планированием бюджета.'
    PRODUCT_MANAGER = 'Продуктовый менеджер отвечает за разработку и управление продуктами компании, анализ рынка и улучшение продуктовой линейки.'

class Administration:
    def __init__(self):
        self.__director = None
        self.financial_manager = None
        self.product_manager = None

    def change_director(self, new_director):
        '''Изменяет имя директора.'''
        self.__director = new_director
        print(f'Изменение имени директора на {new_director}')

    def get_director(self):
        '''Возвращает имя директора'''
        return self.__director

class NameDescriptor:
    def __get__(self, instance, owner):
        return instance._name

    def __set__(self, instance, value):
        '''Устанавливает название фирмы в таком виде  |name|.'''
        instance._name = f"|{value}|"
        print(f'Название фирмы изменено на {instance._name}')

class Person:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.offices = []

    def create_shop(self):
        '''Создает новый офис'''
        while True:
            try:
                office_name = input('Введите название офиса: ')
                office_capital = float(input('Введите капитал офиса: '))

                if office_capital > self.balance:
                    print('Капитал офиса не может быть больше баланса.')
                    continue

                print('\nРоли в администрации:')
                print(f'DIRECTOR: {Role.DIRECTOR.value}')
                print(f'FINANCIAL_MANAGER: {Role.FINANCIAL_MANAGER.value}')
                print(f'PRODUCT_MANAGER: {Role.PRODUCT_MANAGER.value}')

                admin = Administration()
                admin.financial_manager = input('Введите имя финансового менеджера: ')
                admin.product_manager = input('Введите имя товарного менеджера: ')
                admin.change_director(self.name)

                new_office = StoreMainOffice(office_name, office_capital, admin)
                self.offices.append(new_office)
                self.balance -= office_capital
                return new_office

            except ValueError as e:
                print(f'Ошибка ввода: {e}. Пожалуйста, попробуйте снова.')
                continue

    def create_store(self, main_office):
        '''Создает магазин'''
        while True:
            try:
                name_store = input('Введите название магазина: ')
                store_type = input(
                    'Какой тип магазина хотите создать? (ShoeStore, StoreOfClothing, RandomStore) или введите "выход" для завершения: '
                )
                if store_type.lower() == 'выход':
                    return 0

                seller = input('Введите имя продавца: ')
                assortment = []

                print('Доступные товары у провайдеров:')
                print('Поставщик Максима:')
                for product, price in Provider_Max.product_list.items():
                    print(f'{product}: {price} у.е.')
                print('Поставщик Тона:')
                for product, price in Provider_Ton.product_list.items():
                    print(f'{product}: {price} у.е.')

                while True:
                    try:
                        amount_of_assortment = int(input('Введите количество видов товаров, которые хотите добавить: '))
                        break
                    except ValueError:
                        print('Ошибка: введите корректное число.')

                for _ in range(amount_of_assortment):
                    product = input('Введите название товара: ')
                    price = None

                    if product in Provider_Max.product_list:
                        price = Provider_Max.product_list[product]
                    elif product in Provider_Ton.product_list:
                        price = Provider_Ton.product_list[product]
                    elif product.lower() == 'нет' or product.lower() == 'no':
                        break
                    else:
                        print('Такого товара нет, попробуйте еще раз.')
                        continue

                    if price <= main_office.capital:
                        assortment.append(product)
                        main_office.capital -= price
                        print(f'{product} добавлен в ассортимент. Цена: {price} у.е.')
                    else:
                        print(
                            f'Недостаточно капитала для добавления {product}. Текущий капитал: {main_office.capital} у.е.'
                        )

                if store_type == 'ShoeStore':
                    store = ShoeStore(
                        self.name,
                        name_store,
                        main_office.capital,
                        main_office.admin,
                        seller,
                        assortment,
                    )
                elif store_type == 'StoreOfClothing':
                    while True:
                        try:
                            number_of_fitting_rooms = int(input('Введите количество примерочных: '))
                            break
                        except ValueError:
                            print('Ошибка: введите корректное число.')

                    store = StoreOfClothing(
                        self.name,
                        name_store,
                        main_office.capital,
                        main_office.admin,
                        seller,
                        assortment,
                        number_of_fitting_rooms,
                    )
                else:
                    store = RandomStore(
                        self.name,
                        name_store,
                        main_office.capital,
                        main_office.admin,
                        assortment,
                    )

                main_office.shops_in_MainOffice.append(store)
                main_office + 1  #кол магащинов с add
                break

            except ValueError as e:
                print(f'Ошибка ввода: {e}. Пожалуйста, попробуйте снова.')

            another_store = input('Хотите создать еще один магазин? (да/нет): ').lower()
            if another_store not in ['да', 'yes']:
                break

    def full_info_person(self) -> str:
        '''Возвращает полную информацию о человеке.'''
        info = f'Имя: {self.name}\nБаланс: {self.balance}'
        return info

    def get_full_info_offices(self) -> str:
        '''Возвращает полную информацию обо всех офисах.'''
        if not self.offices:
            return 'Пока ничего нет'
        else:
            info = 'Ваши офисы:\n'
            for office in self.offices:
                info += f'\nОфис: {office.name}\nКапитал: {office.capital}\nКоличество магазинов: {len(office.shops_in_MainOffice)}\n'
                info += f'Директор: {office.admin.get_director()}\n'
                info += f'Финансовый менеджер: {office.admin.financial_manager}\n'
                info += f'Товарный менеджер: {office.admin.product_manager}\n'
                info += f'Магазины:\n'
                for store in office.shops_in_MainOffice:
                    info += f'Информация о магазине:\n{store.full_info_store()}\n'
            return info

    @staticmethod
    def regular_calculator(num1, num2, operation):
        '''Выполняет простые арифметические операции.'''
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            if num2 != 0:
                return num1 / num2
            else:
                return 'Деление на ноль невозможно.'
        else:
            return 'Неизвестная операция.'

class StoreMainOffice:
    name = NameDescriptor()

    def __init__(self, name, capital, admin):
        self.name = name
        self.capital = capital
        self.number_of_stores = 0
        self.admin = admin
        self.shops_in_MainOffice = []

    def __call__(self):
        '''Возвращает название офиса.'''
        return self.name

    def change_director(self, new_director):
        '''Изменяет директора офиса.'''
        self.admin.change_director(new_director)

    def full_info_office(self) -> str:
        '''Возвращает полную информацию о главном офисе.'''
        info = f'Название фирмы: {self.name}\nКапитал: {self.capital}\n'
        return info

    def __add__(self, other: int):
        '''Увеличивает количество магазинов в главном офисе.'''
        if isinstance(other, int):
            self.number_of_stores += other
        else:
            raise TypeError('Ожидалось целое число')
        return self

    def full_info_store(self) -> str:
        '''Возвращает общую информацию о магазине чтобы наследовать.'''
        return 'Пока не нет информации о магазинах.'

    def remove_store(self, store_name):
        '''Удаляет магазин из офиса по его названию.'''
        for store in self.shops_in_MainOffice:
            if store.name_store == store_name:
                self.shops_in_MainOffice.remove(store)
                self.number_of_stores -= 1
                print(f'Магазин {store_name} был удален.')
                return
        print(f'Магазин {store_name} не найден.')

    @classmethod
    def compare_stores(cls, store1, store2):
        '''Сравнивает два магазина по капиталу и выводит результат.'''
        print(f'\nСравнение магазинов:\n{store1.full_info_store()}\n{store2.full_info_store()}')
        if store1 < store2:
            print(f'{store1.name_store} имеет меньший капитал, чем {store2.name_store}.')  # Изменено на name_store
        elif store2 < store1:
            print(f'{store2.name_store} имеет меньший капитал, чем {store1.name_store}.')  # Изменено на name_store
        else:
            print('Оба магазина имеют одинаковый капитал.')

class ShoeStore(StoreMainOffice):
    def __lt__(self, other):
        '''Сравнивает капитал текущего магазина с другим магазином.'''
        if isinstance(other, StoreMainOffice):
            return self.capital < other.capital
        else:
            raise TypeError('Вы ввели не тот тип данных для <')  # для разраба

    def __init__(self, name_offic, name_store, capital, admin, seller, assortment):
        super().__init__(name_offic, capital, admin)
        self.name_store = name_store
        self.seller = seller
        self.assortment = assortment

    def full_info_store(self) -> str:
        '''Возвращает полную информацию о магазине обуви.'''
        info = f'Название магазина: {self.name_store}\nПродавец: {self.seller}\nАссортимент: {", ".join(self.assortment)}'
        return info

class StoreOfClothing(ShoeStore):
    def __init__(self, name_offic, name_store, capital, admin, seller, assortment, number_of_fitting_rooms):
        super().__init__(name_offic, name_store, capital, admin, seller, assortment,)
        self.number_of_fitting_rooms = number_of_fitting_rooms

    def full_info_store(self) -> str:
        '''Возвращает полную информацию о магазине одежды.'''
        info = super().full_info_store()
        info += f'\nКоличество примерочных: {self.number_of_fitting_rooms}'
        return info

class RandomStore(StoreMainOffice):
    def __init__(self,name_offic, name_store, capital, admin, assortment):
        super().__init__(name_offic,name_store, capital)
        self.admin = admin
        self.assortment = assortment

    def full_info_store(self) -> str:
        '''Возвращает полную информацию о случайном магазине.'''
        info = super().full_info_store()
        info += f'\nАссортимент: {", ".join(self.assortment)}'
        return info

class Provider:
    def __init__(self, name, product_type, product_list):
        self.name = name
        self.product_type = product_type
        self.product_list = product_list

    def full_info_provider(self) -> str:
        '''Возвращает полную информацию о провайдере.'''
        info = f'Имя: {self.name}\nТип продукции: {self.product_type}\nСписок продукции: {", ".join(self.product_list)}'
        return info

Provider_Max = Provider('Maksim', 'обувной', {'кроссы': 1000, 'шлепки': 1101})
Provider_Ton = Provider('Ton', 'одёжка', {'футболки': 500, 'джинсы': 1500})

def compare_selected_stores(selected_office):
    '''Сравнивает выбранные магазины в указанном офисе.'''
    while True:
        print('Доступные магазины:')
        for store in selected_office.shops_in_MainOffice:
            print(store.name_store)  # Изменено на name_store

        first_store_name = input('Введите название первого магазина для сравнения: ')
        second_store_name = input('Введите название второго магазина для сравнения: ')

        first_store = None
        second_store = None

        for store in selected_office.shops_in_MainOffice:
            if store.name_store == first_store_name:
                first_store = store
            if store.name_store == second_store_name:
                second_store = store

        if first_store is None or second_store is None:
            print('Один или оба магазина не найдены. Попробуйте снова.')
            continue

        StoreMainOffice.compare_stores(first_store, second_store)
        break

def display_offices_and_stores(person):
    '''Отображает офисы и магазины человека.'''
    print('Ваши офисы:')
    print(person.get_full_info_offices())

def remove_store_or_office(person):
    '''Удаляет магазин или офис по выбору пользователя.'''
    while True:
        display_offices_and_stores(person)

        choice = input(f'{person.name}, хотите ли вы удалить магазин или офис? (магазин/офис/нет): ').lower()
        if choice == 'магазин':
            office_name = input('Введите название офиса, из которого хотите удалить магазин: ')
            office = None
            for something in person.offices:
                if something.name == office_name:
                    office = something
                    break
            if office:
                store_name = input('Введите название магазина для удаления: ')
                office.remove_store(store_name)
            else:
                print('Офис не найден.')
        elif choice == 'офис':
            office_name = input('Введите название офиса для удаления: ')
            office = None
            for something in person.offices:
                if something.name == office_name:
                    office = something
                    break
            if office:
                person.offices.remove(office)
                print(f'Офис {office_name} был удален.')
            else:
                print('Офис не найден.')
        elif choice == 'нет':
            break
        else:
            print('Ошибка: требуется дать ответ магазин или офис.')

def main():
    '''Основная функция '''
    print(f'Здравствуйте! Чтобы выполнять дальнейшие действия, заполните анкету.')
    name = input('Введите ваше имя: ')

    while True:
        try:
            balance = float(input('Какой в данный момент у вас баланс: '))
            break
        except ValueError:
            print('Ошибка: введите корректное число для баланса.')

    person_first = Person(name, balance)

    while True:
        print(f'{person_first.name}, хотите ли вы создать новый офис? (да/нет)')
        choice = input().lower()
        if choice in ['да', 'yes']:
            person_first.create_shop()
            print('Пора создавать магазины.')
            while True:
                person_first.create_store(person_first.offices[-1])
                another_store = input('Хотите создать еще один магазин в этом офисе? (да/нет): ').lower()
                if another_store not in ['да', 'yes']:
                    break
        elif choice in ['нет', 'no']:
            break
        else:
            print('Ошибка: требуется дать ответ да или нет.')
            continue

    print('Давайте подведем итог, что у нас получилось!')
    print(person_first.full_info_person())
    print(person_first.get_full_info_offices())
    print('\n')

    print('А хотите сравнить ваши магазины по их капиталу в товарах (без учета выделенных денег)? (да/нет)')
    choice_for_compare = input().lower()
    if choice_for_compare in ['да', 'yes']:
        if not person_first.offices:
            print('У вас нет офисов для сравнения.')
            return

        office_name = input('Введите название офиса для сравнения: ')
        selected_office = None
        for office in person_first.offices:
            if office.name == office_name:
                selected_office = office
                break

        if selected_office:
            compare_selected_stores(selected_office)
        else:
            print('Офис не найден.')

    remove_store_or_office(person_first)

main()
