"""Central scheduler for periodic tasks."""
import schedule
import time

from control import irrigation, compost_tea


def init_schedule():
    schedule.every().day.at("06:00").do(irrigation.check_and_water)
    schedule.every().day.at("18:00").do(irrigation.check_and_water)
    schedule.every().day.at("07:00").do(compost_tea.start_brew)


def run():
    init_schedule()
    while True:
        schedule.run_pending()
        time.sleep(1)
