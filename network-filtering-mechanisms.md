### Network Filtering Mechanisms

School networks use multi-layered security systems to enforce usage policies and protect devices on the local network. These systems evaluate web requests using several techniques:

1. **DNS Filtering**

- **Mechanism:** When a browser requests access to a website, it sends a Domain Name System (DNS) query to translate the domain name (e.g., `example.com`) into an IP address.
- **Inspection:** A DNS filter inspects the requested domain name against blocklists or category databases before returning the IP address. If the domain is restricted, the DNS server returns a block page IP or drops the request.

2. **Server Name Indication (SNI) Inspection**

- **Mechanism:** During the TLS handshake (which establishes an encrypted HTTPS connection), the client sends the target server's hostname in plaintext within the SNI extension.
- **Inspection:** Firewalls observe this handshake phase to identify the destination server even before the encrypted HTTP payload is transmitted. Encrypted Client Hello (ECH), where supported and enabled, can conceal the SNI from network observers.

3. **URL and Payload Classification**

- **Mechanism:** Firewalls and secure web gateways (SWGs) examine the full URL path and HTTP request headers. For HTTPS traffic, inspecting this information generally requires authorized TLS inspection or endpoint-level visibility.
- **Inspection:** Traffic directed to web hosting platforms, cloud function endpoints, or unclassified IP addresses is often inspected for proxy signatures or blocked by default if it violates established security rules.

### Standard Web Traffic Routing

In standard web architecture, a proxy server functions as an intermediate node handling requests on behalf of a client:

```text
+--------+            +--------------+            +-------------------+
| Client |  ------->  | Proxy Server |  ------->  | Target Server     |
|        |  <-------  | (Intermediary)|  <-------  | (Web Host)        |
+--------+            +--------------+            +-------------------+
```

- **Client Request:** The client routes its HTTP/HTTPS traffic to the proxy server's IP address and port.
- **Forwarding:** The proxy reads the target address, creates a new socket connection to the target server, and forwards the request data.
- **Response Relay:** The proxy receives the target server's response and relays the HTTP headers and payload back to the client.

Network administrators typically restrict outbound connections on non-standard ports and monitor high-volume traffic to unrecognized proxy nodes to ensure network integrity.
