# HTTP Fundamentals

* HTTP is a key protocol for internet applications
    * It is a set of strict rules governing data transfer between two computers
    * HTTP is built on top of several other protocols (e.g. TCP, IP...)
    * There are a *ton* of details, we're focusing on the high level implications for *using* the protocol and ignoring a lot of implementation details..

*Instructor note: goto the blackboard*

## A Typical Web Connection For a Modern Website

* Client initiates request to a URL
* Server responds with HTML for the site
* HTML includes several assets as URLs (images, CSS, JS, etc.)
    * These might live on different servers (AWS S3 buckets, CDN services, and so on)
* Client requests those resources
* The various servers respond with them

All of these request/responses are done using the HTTP protocol

## HTTP Message Structure

* HTTP requests and responses are both broken into 3 components:
    * The first section is different between requests and responses
        * Requests: The HTTP version, type, and path being requested 
            * e.g. GET /path/to/resource.php?var=data1&othervar=data2 HTTP/2.0
        * Responses: The HTTP Version and a "status code"
            * e.g. HTTP/2.0 404 NOT FOUND or HTTP/2.0 200 OK
    * Headers
        * Key: value pairs that specify a wide range of metadata 
        * Host: google.com (big one)
        * Also specify things like payload type, cookies (important for authentication!), custom metadata from the server... and a LOT more.
    * The Body
        * The actual data
        * All responses have a body, some requests do not. (e.g. a simple GET has no body)

**Open a browser, open the network tab, show a few request/responses for a page**

## HTTP Request Methods

* There are 9 HTTP Request Methods, but 5 of them comprise ~95% of all requests.
* GET is by far the most common, followed by POST, everything else is used much less.
* All 9 documented here: [https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
* In the next lesson we'll learn about the REST pattern, which assigns *very specific* meaning to each of these methods.
* In general usage (outside REST) they still are meant to have some semantic meaning:
* In the "REST" pattern these semantic meanings are even more tightly followed.

* GET
    * You're asking for a resource that should exist at the specified URL
    * In REST, GET means you're __retrieving__ an existing resource
* POST
    * You're sending data (submitting a form, for example).
    * The response might have more data, or it might just say "your data has been received"
    * In REST, POST specifically means you're __creating__ a new resource.
* PUT
    * Like POST you're sending data.
    * PUT implies that whatever you send should replace any existing data at the specified location (URL/URI)
    * In REST, PUT means you are __replacing__ an existing resource
* PATCH
    * Like POST but implies partial information (updating just a first name, for example)
    * In REST, PATCH means you are __modifying__ an existing resource
* DELETE
    * Deletes a resource at the specified URL
    * In REST, DELETE means you're __deleting__ an existing resource.


## HTTP Response Codes

An exhaustive list of established response codes can be found here: [https://developer.mozilla.org/en-US/docs/Web/HTTP/Status](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

* Big picture...
    * 0-99 These codes do not exist. 
    * 100-199 These codes are for niche "informational" purposes, you will almost never encounter them while simply using APIs. If you implement complex web servers, or work on protocol level implementations you might.
    * 200-299 These codes mean "everything worked" 
        * 200 is the single most used status code and just means "everything worked exactly as expected."
        * Some other codes mean specific things...
            * 201 means "a resource was successfully created" 
            * 204 means "the request was successful, but there is no body content to return" perhaps because the resource was cached
    * 300-399 These codes mean "the server is redirecting you" 
        * Usually this means a resource used to live at the location you specified, but has since mover.
            * 304 means "the resource has not changed since I last gave it to you, use a cached version"
            * 300 means "there are many choices for this resource, you must choose one" and the body of the response typically contains some data allowing the client to choose from a list.
    * 400-499 These codes mean "the client did something wrong"
        * 404 is the most well known, you requested a resource that doesn't exist.
        * 401 means "the server doesn't know you, so you must authenticate with the server before you can access this resource"
        * 403 means "although you've been authenticated by the server, you don't have access privileges to this resource"
    * 500-599 Means the server encountered an error while processing the request.
        * 500 means "internal error occurred" and gives no additional information (common, you don't often want to expose exactly what went wrong to the general public)
        * 504 means "timeout" -- the server didn't respond in time,

In brief:

* 1xx -- niche info
* 2xx -- success
* 3xx -- qualified success (go elsewhere to succeed)
* 4xx -- client screwed up
* 5xx -- server screwed up

## REST

* REST stands for REpresentational State Transfer.
* It's a set of rules, constraints, and guiding principles for developing Web APIs
* An API that applies these rules is called "restful"
* Some API's do not fully conform to REST principles, but do conform to most, we still usually call them restful. That's life.
* All of this is officially codified: [https://restfulapi.net/](https://restfulapi.net/)

### REST Principles:

#### 1 Uniform Interface

* In simple terms: 
    * All RESTful APIs should feel similar to use, and have similar structure.
    * Any given REST API should have a consistent and predictable structure.

* In the codified language:
    * Identification of resources – The interface must uniquely identify each resource involved in the interaction between the client and the server.

    * Manipulation of resources through representations – The resources should have uniform representations in the server response. API consumers should use these representations to modify the resource state in the server.

    * Self-descriptive messages – Each resource representation should carry enough information to describe how to process the message. It should also provide information of the additional actions that the client can perform on the resource.

    * Hypermedia as the engine of application state – The client should have only the initial URI of the application. The client application should dynamically drive all other resources and interactions with the use of hyperlinks.


* In practice this means:
    * REST APIs are almost always centered around CRUD operations on data ("resources"), though they can technically allow some function calling.
    * URLs in REST APIs follow a predictable structure
    * Each URL (or "endpoint") identifies a specific resource, collection of resources, or (rarely) a function calling endpoint.
    * host.com/resource_name/[individual_resource_identifier]
    * The API sends a consistent representation of the resource, and if the client wants to manipulate it, they must follow that same representation. 

#### 2. Client-Server

* Separation of concerns
* The API server manages the resources and data.
* The client uses that data to control the application
* If an underlying resource must be changed by the client, the server must be invoked to persist that change. e.g., To update the database, the client must go through the API.

### 3. Stateless

* When the client calls on the API it must provide ALL the relevant information in EVERY such call.
* Clients may have as much state as they wish, but the server will never store any information about a particular client or a particular session.
* i.e., servers are stateless and clients MAY or MAY NOT be stateful depending on the application.

### 4. Cacheable

* If a resource is cacheable the server should identify it as such.
* Typically a resource will have a cache expiry period, that indicates how long the client can store that resource before it should re-request it from the server (to ensure it hasn't changed, or get the new version)

#### 5. Layered System

* Individual components of the larger application should only interact with the layer "adjacent" to them.
* For example:
    * Web App (layer 1)
    * Server API (layer 2)
    * Database (layer 3)
    * In such a setup the Web App should never interact directly with the Database. 

* There is a lot of flexibility in defining the layers, but API designers should take care in doing so.
    * Clearly define the separation of concerns and which component is responsible for what process.

#### 6. Code on Demand (Optional)

* REST servers are allowed to return bits of code for the client to execute.
* But it's pretty rare.