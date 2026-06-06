import time

def main1():
    class Phones:
        phone = None
        def __new__(cls, *args, **kwargs):
            if cls.phone == None:
                cls.phone = 'Iphone 17 Pro Max'
            return cls.phone
            
    ch = 0
    while ch < 3:
        ch = int(input('Какой телефон вы хотите приобрести?: [0 - Samsung Galaxy S23 Ultra, 1 - Google Pixel 8 Pro, 2 - OnePlus 11, 3 - Уйти с магазина] '))
        match ch:
            case 0:
                a = Phones()
                print(f'Увы, вы купили: {a}')
            case 1:
                b = Phones()
                print(f'Увы, вы купили: {b}')
            case 2:
                c = Phones()
                print(f'Увы, вы купили: {c}')
            case 3:
                d = Phones()
                print(f"Увы, вы все равно ушли отсюда с {d}")
            case _:
                print(f'Вы остались без телефона')

                
if __name__ == "__main__":
    main1()