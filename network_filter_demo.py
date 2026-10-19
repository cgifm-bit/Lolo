"""Offline demonstration of layered network filtering decisions.

This script uses sample data only and does not make network connections.
"""


BLOCKED_DOMAINS = {"restricted.example"}
BLOCKED_PATH_MARKERS = {"/proxy", "/tunnel"}


SAMPLE_REQUESTS = [
    {"domain": "learning.example", "path": "/course/intro"},
    {"domain": "restricted.example", "path": "/"},
    {"domain": "hosting.example", "path": "/proxy/start"},
]


def inspect_request(request):
    domain = request["domain"]
    path = request["path"]

    print(f"Request: https://{domain}{path}")
    print(f"  DNS filter: {domain}")
    if domain in BLOCKED_DOMAINS:
        print("  Result: BLOCKED by DNS policy\n")
        return

    print(f"  SNI inspection: {domain} (allowed in this simulation)")
    print(f"  URL policy: {path}")
    if any(marker in path.lower() for marker in BLOCKED_PATH_MARKERS):
        print("  Result: BLOCKED by URL policy\n")
        return

    print("  Result: ALLOWED by the simulated policies")
    print("  Example route: Client -> School Proxy -> Target Server\n")


def main():
    print("Network filtering demo (offline simulation; no connections are made)\n")
    for sample_request in SAMPLE_REQUESTS:
        inspect_request(sample_request)


if __name__ == "__main__":
    main()