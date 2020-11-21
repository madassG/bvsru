from datetime import date, datetime,timedelta


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self, i=0):
        total = 0
        today = datetime.date(datetime.now() - timedelta(days=i))
        for record in self.records:
            if record.date == today:
                total += record.amount
        return total

    def get_week_stats(self):
        total = 0
        for i in range(7):
            total += self.get_today_stats(i)
        return total


class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)
    def get_calories_remained(self):
        if self.get_today_stats() >= self.limit:
            return("Хватит есть!")
        else:
            return(f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {self.limit - self.get_today_stats()} кКал")


class CashCalculator(Calculator):
    USD_RATE = 76.0
    EURO_RATE = 90.0

    def __init__(self, limit):
        super().__init__(limit)

    def get_today_cash_remained(self, currency):
        current_spent = self.get_today_stats()
        currency_text = "руб"
        if currency == "usd":
            self.limit = self.limit / self.USD_RATE
            current_spent = current_spent / self.USD_RATE
            currency_text = "USD"
        elif currency == "eur":
            self.limit = self.limit / self.EURO_RATE
            current_spent = current_spent / self.EURO_RATE
            currency_text = "Euro"

        print(self.limit, ' ', current_spent)
        if current_spent == self.limit:
            return("Денег нет, держись")
        elif current_spent > self.limit:
            return(f"Денег нет, держись: твой долг - {1.0 *round(current_spent-self.limit, 2)} {currency_text}")
        else:
            return(f"На сегодня осталось {1.0 * round(self.limit - current_spent, 2)} {currency_text}")



class Record:
    def __init__(self, amount, comment, date = f"{datetime.now().day}.{datetime.now().month}.{datetime.now().year}"):
        self.amount = amount
        self.date = datetime.date(datetime.strptime(date, "%d.%m.%Y"))
        self.comment = comment


# r1 = Record(amount=152, comment="Безудержный шопинг", date="20.11.2020")
# r2 = Record(amount=152, comment="gay")
# CashCalculator1 = CashCalculator(760)
#
# CashCalculator1.add_record(r1)
# CashCalculator1.add_record(r2)
#
# print(CashCalculator1.EURO_RATE)
# print(CashCalculator1.get_today_stats())
# print(CashCalculator1.get_week_stats())
# print(CashCalculator1.get_today_cash_remained("usd"))