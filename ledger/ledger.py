from __future__ import annotations

from datetime import datetime


class LedgerEntry:
    def __init__(self, date: datetime, description: str, change: int) -> None:
        self.date = date
        self.description = description
        self.change = change

    def __lt__(self, other: LedgerEntry) -> bool:
        return (self.date, self.change, self.description) < (
            other.date,
            other.change,
            other.description,
        )


def create_entry(date: str, description: str, change: int) -> LedgerEntry:
    return LedgerEntry(datetime.strptime(date, "%Y-%m-%d"), description, change)


def format_entries(currency: str, locale: str, entries: list[LedgerEntry]) -> str:
    date_formats = {
        "en_US": "%m/%d/%Y",
        "nl_NL": "%d-%m-%Y",
    }
    date_format = date_formats[locale]
    column_names = {
        "en_US": ["Date", "Description", "Change"],
        "nl_NL": ["Datum", "Omschrijving", "Verandering"],
    }
    currency_dict = {"USD": "$", "EUR": "€"}
    column_length = [11, 26, 13]
    table = [
        "| ".join(
            [
                column.ljust(length)
                for column, length in zip(
                    column_names[locale],
                    column_length,
                    strict=False,
                )
            ],
        ),
    ]
    entries = sorted(entries)
    for entry in entries:
        line = []
        date_str = entry.date.strftime(date_format)

        line.append(date_str)

        field = (
            entry.description[:22] + "..."
            if len(entry.description) > 25
            else entry.description
        )
        line.append(field.ljust(25))
        change_str = currency_dict[currency]
        if locale == "en_US":
            change_str = change_str + f"{abs(entry.change)/100:,.2f}"
        elif locale == "nl_NL":
            change_str = change_str + " " f"{entry.change/100:,.2f}".replace(
                ".",
                "\n",
            ).replace(",", ".").replace("\n", ",")
        if entry.change < 0 and locale == "en_US":
            change_str = "(" + change_str + ")"
        else:
            change_str += " "
        change_str = change_str.rjust(13)
        line.append(change_str)
        table.append(" | ".join(line))
    return "\n".join(table)
