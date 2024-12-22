from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from .youtubedatafetch import fetchchanneldetails



def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    scheduler.add_job(fetchchanneldetails, 'interval', hours=24, id='refresh_database', replace_existing=True)

    register_events(scheduler)
    scheduler.start()
