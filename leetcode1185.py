import datetime

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        weeks = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        end_date = datetime.datetime(2022, 1, 2)
        start_date = datetime.datetime(year, month, day)
        day_diff = (start_date - end_date).days
        week_diff = day_diff%7
        print(weeks[week_diff])
        return weeks[week_diff]


s = Solution()
w = s.dayOfTheWeek(31, 8, 2019)

