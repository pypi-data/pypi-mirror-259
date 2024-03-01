# DNS Archiver

A Simple DNS lookup tool that dumps all records for archiving.

Useful to run on a schedule to monitor DNS changes which can help if a customer modifies their DNS and breaks their site you can quickly debug and tell what the old (correct) records were.

## Install

The recommended way to install is to use `pipx`:

`pipx install dns-archiver`

## Usage

```
% dns-archiver --help

 Usage: dns-archiver [OPTIONS] NAME

╭─ Arguments ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    name      TEXT  DNS name to lookup [default: None] [required]                                                                                                │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --record                      [ALL|A|AAAA|CNAME|TXT|NS|MX|SOA]  The DNS record to archive [default: DNSRecord.ALL]                                                │
│ --version             -v                                                                                                                                          │
│ --install-completion          [bash|zsh|fish|powershell|pwsh]   Install completion for the specified shell. [default: None]                                       │
│ --show-completion             [bash|zsh|fish|powershell|pwsh]   Show completion for the specified shell, to copy it or customize the installation.                │
│                                                                 [default: None]                                                                                   │
│ --help                                                          Show this message and exit.                                                                       │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```
