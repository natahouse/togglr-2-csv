from .time_entry_2_nh_entry import NHEntry, NH_ENTRY_HEADER

NH_CSV_SEPARATOR = "; "
NH_CSV_HEADER = NH_CSV_SEPARATOR.join(NH_ENTRY_HEADER)


def nh_entry_2_nh_csv(nh_entry: NHEntry):
    line = []

    for key in nh_entry:
        line.append(f"{nh_entry[key]}")

    return NH_CSV_SEPARATOR.join(line)
