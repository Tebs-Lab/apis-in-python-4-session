# Big Picture: What Are "Application Program Interfaces"

* *Instructor note: goto the whiteboard for this.*

* API stands for Application Program interface.
    * Unfortunately it can mean a *lot* of things in different contexts...
    * In general it just means a set of rules, restrictions, and possible ways to interact with some piece of software.
    * In software it most commonly means two things:
        * Libraries and software packages have an "API" which is the set of modules, functions, etc. that they expose. 
        * "Web APIs" are software systems accessed via the web.
            * These are what this class is about
            * They are generally (but not always) accessed via HTTP requests.
            * The rules and restrictions in this case are a set of "routes" or "endpoints" that users can send requests to. "endpoint" is basically a fancy term for "URL" in this context.

* Quick review of the client-server paradigm
    * Servers are computers that are always listening/waiting for other computers (clients) to interact with them.
    * Every server has its own rules for what kinds of connections to accept, respond to, etc.
    * Clients that make requests according to those rules receive a response. 
    * A typical "request-response cycle" goes something like:
        1) Client sends a message to the server, the "request."
        2) The server parses the request and determines what the user is requesting.
        3) If needed, the server communicates with it's database or other systems.
        4) The server sends a "response" indicating if the request was handled successfully or not, and sends any relevant data (such as some requested information, or the cause of the failure.)

* Common Web API uses...
    * **Are you aware of any web APIs and what they're used for?**
    * Hopefully there are some good answers, APIs do *everything* these days. Here are some interesting ones:
    * Github -- used to manage repos, automate deployments, stuff like that.
    * Social Media APIs -- used to automate posts, replies, etc. 
    * GenAI APIs -- so hot right now, used to request an AI system generate a response to a prompt
    * Remote Procedure Calling / Function execution -- cause an external system to take some specific pre-defined action.
    * ... and so on ... 


* A note about Python...
    * There is built in support to use 

