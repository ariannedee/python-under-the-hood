from datetime import date, timedelta


class Goal:
    """Track a goal that you want to perform for X days"""
    class_attr = True

    def __init__(self, name, num_days, days_since_start=0):
        """
        :param name: Description of the goal
        :param num_days: # of days to perform it (in a row)
        :param days_since_start: # days since you started the goal (e.g. already in-progress)
        """
        self.name = name
        self.num_days = num_days
        self.start_date = date.today() - timedelta(days=days_since_start)
        for i in range(num_days):
            setattr(self, f'day_{i + 1}', False)

    def complete(self, day, note=None):
        setattr(self, f'day_{day}', True)
        if note:
            setattr(self, f'day_{day}_note', note)

    def get_summary(self):
        result = f"{self.name} for {self.num_days} days"
        days_since_start = (date.today() - self.start_date).days

        for day in range(1, min(days_since_start, self.num_days) + 1):
            result += '\n' + self.get_day_summary(day)

        return result

    def get_day_summary(self, day):
        if not hasattr(self, f'day_{day}'):
            return None

        if getattr(self, f'day_{day}'):
            complete = '✅'
        else:
            complete = '❌'
        if hasattr(self, f'day_{day}' + '_note'):
            note = '- ' + getattr(self, f'day_{day}' + '_note')
        else:
            note = ''
        return f"Day {day}: {complete} {note}"


if __name__ == '__main__':
    goal = Goal('Exercise 20 mins', num_days=20, days_since_start=7)
    goal.complete(1, 'ran 20 mins')
    goal.complete(3, 'HIIT class')
    goal.complete(5)
    goal.complete(6, 'walked to dinner')

    print(goal.get_summary())
