#!/usr/bin/env python3

import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'


def retrieve_events(url):
    """Download GitHub events from url and return them as a list of dicts."""
    response = requests.get(url).text
    return json.loads(response)


def print_events(events, n=5):
    """Print the type and repo name of the first n events, one per line."""
    for x in events[:n]:
        event = x['type'] + ' :: ' + x['repo']['name']
        print(event)


def main():
    """Fetch recent GitHub events for GITHUB_USER and print a summary."""
    print(GHUSER)
    print(url)
    events = retrieve_events(url)
    print_events(events)


if __name__ == "__main__":
    main()
