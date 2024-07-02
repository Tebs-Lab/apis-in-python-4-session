# Other Kinds of APIs

* Most APIs are about data/resources. These are basically wrappers around CRUD operations.
* Some APIs are focused on actions rather than data/resources
    * Some do both.
    * Sometimes the lines are blurred -- is posting on social media an action that "creates data" or "takes an action?"

## Remote Procedure Call (RPC)

* General term for a system that performs some action in response to a web request. 
    * The procedure can be literally anything
    * Unlike REST this is not a set of rules for making things simple
    * Technically speaking, REST does support remote function calling... but it's uncommon and perhaps lightly frowned upon
    * I urge you not to be too pedantic... lines are often blurred in this corner of software.

* An RPC API is fundamentally "Turing complete" which is to say: anything that can be done with software can be exposed with an RPC styled API. 

* An RPC API is going to be centered around "verbs" whereas a REST or CRUD API will be centered around nouns. 

* RPC APIs may or may not be "stateless" like a REST API
    * APIs with state can be tricky because:
        * they introduce possible race conditions 
        * each call is no longer independent, and those dependencies may become hard to manage and track
    * Stateful APIs can be beneficial because:
        * Streaming data can be more performant
        * Some applications 

* There are specific frameworks and tools for building these, like gRPC.
    * But none of that is specifically needed to build or use an RPC API.

## Examples

* Twillio or ClickSnd:
    * API for sending text messages

* SendGrid, Gmail, others
    * API for sending emails

* OpenAI and other GenAI APIs
    * API for calling a generative model and retrieving the output.

* https://math.tools/api/numbers/
    * Do math on someone else's server, without implementing it yourself.

* Lots of firms may develop internal APIs to do specific tasks.
    * Kick of a training session for an ML model
    * Deploy one of their pieces of software 
    * Generate a report
    * and so on

## Note: Unfortunately...

* The vast majority of RPC based APIs require money, significant amounts of configuration, and usually both.
* So, for this class session we're going to BUILD an API server that performs actions.
* After that, we're going to write a client that uses our API servers.

## A New Tool

* I want everyone to download Postman
    * https://www.postman.com/downloads/

* It's a super useful tool for probing, testing, building, and exploring APIs
* **Instructor note: demonstrate its use to make a couple simple requests to the Github API**
* **Micro-exercise: Students do the same, for a different API route**