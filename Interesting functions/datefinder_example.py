from datefinder import find_dates

text = """We have one meeting on May 17th, 2021 at 9:00am and another meeting on 5/18/2021 at 10:00.
I hope you can attend one of the meetings."""

matches = find_dates(text)

for match in matches:
    print("Date and time:", match)
    print("Only day:", match.day)

