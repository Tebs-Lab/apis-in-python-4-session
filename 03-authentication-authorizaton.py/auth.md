# Authentication and Authorization

## Connection Sessions vs Authentication/Authorization

* HTTP is "stateless" by default, and it is the responsibility of the web server to manage any required state.
* HTTP does have persistent connections, but it is purely a performance feature
    * Meaning a single port is assigned to a single client and continues to be used for that "connection" or "session"
    * However, the HTTP protocol does not assign any special meaning, or remember any stateful information about the client beyond what data has been properly sent and received and information about the connection speed.
* As a result, there are multiple schemes for performing authentication and authorization over HTTP.
    * These rely on features of HTTP, but must go above and beyond the core protocol to allow auth

* Lets go to the code to talk about two of the most popular methods to manage a connections state (including authentication/authorization)