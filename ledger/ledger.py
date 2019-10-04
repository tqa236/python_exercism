# -*- coding: utf-8 -*-
from datetime import datetime


class LedgerEntry(object):
    def __init__(self):
        self.date = None
        self.description = None
        self.change = None


def create_entry(date, description, change):
    entry = LedgerEntry()
    entry.date = datetime.strptime(date, "%Y-%m-%d")
    entry.description = description
    entry.change = change
    return entry


def format_entries(currency, locale, entries):
    if locale == "en_US":
        table = "Date" + 7 * " " + "| Description" + 15 * " " + "| Change" + 7 * " "
    elif locale == "nl_NL":
        table = (
            "Datum" + 6 * " " + "| Omschrijving" + 14 * " " + "| Verandering" + 2 * " "
        )

    while entries:
        table += "\n"

        # Find next entry in order
        min_entry_index = 0
        for i in range(1, len(entries)):
            entry = entries[i]
            min_entry = entries[min_entry_index]
            if entry.date < min_entry.date:
                min_entry_index = i
            elif entry.date == min_entry.date and entry.change < min_entry.change:
                min_entry_index = i
            elif (
                entry.date == min_entry.date
                and entry.change == min_entry.change
                and entry.description < min_entry.description
            ):
                min_entry_index = i
        entry = entries.pop(min_entry_index)

        # Write entry date to table
        month = f"{entry.date.month:02d}"
        date_str = month + "/"
        day = f"{entry.date.day:02d}"
        date_str += day + "/"
        year = f"{entry.date.year:04d}"
        date_str += year
        table += date_str
        table += " | "

        # Write entry description to table
        # Truncate if necessary
        if len(entry.description) > 25:
            table = table + "".join(entry.description[:22])
            table += "..."
        else:
            for i in range(25):
                if len(entry.description) > i:
                    table += entry.description[i]
                else:
                    table += " "
        table += " | "

        # Write entry change to table
        change_str = ""
        if entry.change < 0:
            change_str = "("
        currency_dict = {"USD": "$", "EUR": "€"}
        change_str += currency_dict[currency]
        change_euro = abs(int(entry.change / 100.0))
        euro_parts = []
        while change_euro > 0:
            euro_parts.insert(0, str(change_euro % 1000))
            change_euro = change_euro // 1000
        if not euro_parts:
            change_str += "0"
        else:
            while True:
                change_str += euro_parts[0]
                euro_parts.pop(0)
                if not euro_parts:
                    break
                change_str += ","
        change_str += "."
        change_cents = abs(entry.change) % 100
        change_cents = f"{change_cents:02d}"
        change_str += change_cents
        if entry.change < 0:
            change_str += ")"
        else:
            change_str += " "
        change_str = (13 - len(change_str)) * " " + change_str
        table += change_str
    return table
