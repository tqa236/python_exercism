"""Refactor a ledger printer."""
import locale as lc
from datetime import datetime


class LedgerEntry(object):
    """Ledger object."""

    def __init__(self, date, description, change):
        """Initialize."""
        self.date = date
        self.description = description
        self.change = change

    def __lt__(self, other):
        """Override the < operator."""
        return (self.date, self.change, self.description) < (
            other.date,
            other.change,
            other.description,
        )


def create_entry(date, description, change):
    """Create a ledger entry."""
    return LedgerEntry(datetime.strptime(date, "%Y-%m-%d"), description, change)


def format_entries(currency, locale, entries):
    """Format the entries."""
    lc.setlocale(lc.LC_ALL, locale + ".utf8")

    date_format = lc.nl_langinfo(lc.D_FMT)
    column_name_dict = {
        "en_US": ["Date", "Description", "Change"],
        "nl_NL": ["Datum", "Omschrijving", "Verandering"],
    }
    column_length = [11, 26, 13]
    table = [
        "| ".join(
            [
                column.ljust(length)
                for column, length in zip(column_name_dict[locale], column_length)
            ]
        )
    ]
    entries = sorted(entries)
    for entry in entries:
        line = []

        date_str = entry.date.strftime(date_format)
        if locale == "nl_NL":
            date_str = entry.date.strftime("%d-%m-%Y")

        line.append(date_str)

        if len(entry.description) > 25:
            line.append(entry.description[:22] + "...")
        else:
            line.append(entry.description.ljust(25))

        currency_dict = {"USD": "$", "EUR": "€"}
        change_str = currency_dict[currency]
        if locale == "en_US":
            change_str = change_str + f"{abs(entry.change)/100:,.2f}"
        elif locale == "nl_NL":
            change_str = change_str + " " f"{entry.change/100:n}"
        if entry.change < 0 and locale == "en_US":
            change_str = "(" + change_str + ")"
        else:
            change_str += " "
        change_str = change_str.rjust(13)
        line.append(change_str)
        table.append(" | ".join(line))
    return "\n".join(table)
