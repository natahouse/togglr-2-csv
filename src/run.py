# from cli.save_credentials import save_credentials
from lib.get_time_entries import get_time_entries
from lib.date import create_togglr_date

# save_credentials()


start_date = create_togglr_date("2021-06-08")
end_date = create_togglr_date("2021-06-09")

times = get_time_entries(start_date, end_date)

print(times)
