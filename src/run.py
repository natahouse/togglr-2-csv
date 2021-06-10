# from cli.save_credentials import save_credentials
import os
from lib.get_time_entries import get_time_entries
from lib.date import create_togglr_date
from lib.time_entry_2_nh_entry import time_entry_2_nh_entry
from lib.nh_entry_2_nh_csv import nh_entry_2_nh_csv
from lib.str_lines_2_csv_file import str_lines_2_csv_file

start_date = create_togglr_date("2021-06-09")
end_date = create_togglr_date("2021-06-10")

times = get_time_entries(start_date, end_date)

nh_entries = [time_entry_2_nh_entry(time, "ipê") for time in times]

nh_csv_lines = [nh_entry_2_nh_csv(nh_entry) for nh_entry in nh_entries]

str_lines_2_csv_file(f"{os.getcwd()}/output.csv", nh_csv_lines)
