from datetime import datetime, timedelta
from calendar import day_name

'''UWAGA: w poleceniu (akapit "zadanie") jest mowa o solenizantach obchodzących urodziny w danym tygodniu, ale w akapicie 
"warunki akceptacji" jest mowa o wyświetleniu daty urodzin z tygodniowym wyprzedzeniem. W programie przyjęto wyświetlenie 
wszystkich solenizantów obchodzących urodziny w danym tygodniu z tygodniowym wyprzedzeniem'''



def get_birthdays_per_week(users):
    
    today_date = datetime.now()
    today_week = today_date.isocalendar().week
    birthday_persons_by_day = {}
    list_of_weeksdays = []

    for user in users:
        user_birthday = user['birthday'].date()
        user_birthday_weekday = user_birthday.weekday()

        if user_birthday_weekday == 5:
            day_of_making_wishes = user_birthday + timedelta(2)

        elif user_birthday_weekday == 6:
            day_of_making_wishes = user_birthday + timedelta(1)

        else:
            day_of_making_wishes = user_birthday

        reminder_day = day_of_making_wishes - timedelta(7)
        reminder_week = reminder_day.isocalendar().week
        weekday_of_making_wishes = day_of_making_wishes.weekday()

        if today_week == reminder_week:
            if weekday_of_making_wishes not in birthday_persons_by_day:
                birthday_persons_by_day[weekday_of_making_wishes] = user['name']
                list_of_weeksdays.append(weekday_of_making_wishes)
            else:
                birthday_persons_by_day[weekday_of_making_wishes] += ', ' + user['name']
    
    list_of_weeksdays.sort()
    
    for day in list_of_weeksdays:
        week_day = day_name[day] +':'
        birthday_persons_text = "{:<10} {}".format(week_day,birthday_persons_by_day[day] )
        print(birthday_persons_text)


