from specials.funcs.create_weekend_dates import create_weekend_dates
from specials.models import Special

def update_upcoming_weekends():
  reoccuring = Special.objects.all().exclude(reoccuring_weekend='')

  for item in reoccuring:
    reoccuring_weekend = item.reoccuring_weekend
    print(item.title)
    weekend_from, weekend_until = create_weekend_dates(reoccuring_weekend)
    print(reoccuring_weekend)
    print('Friday:', weekend_from)
    print('Sunday:', weekend_until)

    if str(item.start) != str(weekend_from):
      print('updating date for,', item.title)
      item.start = weekend_from
      item.end = weekend_until
      item.save()
    