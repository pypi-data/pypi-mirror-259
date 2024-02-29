import json
from enum import Enum

import dns.exception
import dns.resolver
import typer
from click import ClickException
from dns_archiver.__version__ import version_callback
from rich.console import Console

app = typer.Typer()
console = Console()
err_console = Console(stderr=True)


class Error(ClickException):
    def __init__(self, message: str, exit_code=1) -> None:
        super().__init__(message)
        self.exit_code = exit_code


class DNSRecord(str, Enum):
    ALL = "ALL"
    A = "A"
    AAAA = "AAAA"
    CNAME = "CNAME"
    TXT = "TXT"
    NS = "NS"
    MX = "MX"
    SOA = "SOA"


@app.command()
def main(
    name: str = typer.Argument(help="DNS name to lookup"),
    record: DNSRecord = typer.Option(DNSRecord.ALL.value, help="The DNS record to archive", case_sensitive=False),
    _: bool = typer.Option(None, "-v", "--version", callback=version_callback, is_eager=True),
):
    output = {}
    if record is DNSRecord.ALL:
        records = list(DNSRecord)
        records.remove(DNSRecord.ALL)
    else:
        records = [record]

    for r in records:
        try:
            answers = dns.resolver.resolve(name, r)
            for rdata in answers:
                if r.value == "TXT":
                    # TXT records can have double quotes already in them that do not play nicely with JSON dumping
                    # If we load it in as JSON now it means it will be dumped correctly without needing escaping
                    data = json.loads(rdata.to_text())
                else:
                    data = rdata.to_text()
                output.setdefault(r.value, []).append({"data": data, "ttl": answers.rrset.ttl})
        except dns.exception.DNSException as exc:
            if not isinstance(exc, dns.resolver.NoAnswer):
                raise Error(str(exc))

    console.print_json(data=output)


if __name__ == "__main__":
    app()
