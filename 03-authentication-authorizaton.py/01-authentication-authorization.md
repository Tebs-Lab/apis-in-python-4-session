# Authentication and Authorization 

* Authentication is the process of validating that a connection belongs to a particular user.
* Authorization refers to the levels of access any given user might have.
* Both are sometimes referred to jointly or separately as "auth"

## Connection Sessions vs Authentication/Authorization

* HTTP is "stateless" by default, and it is the responsibility of the client & server applications to manage any required state.
* HTTP does have persistent connections, but it is purely a performance feature
    * Meaning a single port is assigned to a single client and continues to be used for that "connection" or "session"
    * However, the HTTP protocol does not assign any special meaning, or remember any stateful information about the client beyond what data has been properly sent and received and information about the connection speed.
* As a result, there are multiple schemes for performing authentication and authorization over HTTP.
    * These rely on features of HTTP, but must go above and beyond the core protocol to allow auth

* Lets go to the code to talk about two of the most popular methods to manage a connections state (including authentication/authorization)

## Cookies

* Historically, in web browsers this has mostly been done using login credentials and Cookies. Looks like this:
    * User goes to login page
    * User enters their credentials (**pop quiz, which HTTP Method?**)
    * Server tests credentials against their database, refuses incorrect combos
    * If the user is authenticated, server sends a "cookie" which is an HTTP header.
        * This cookie has enough information for the server to identify this individual user or user-session
        * Technically, cookies can contain any data at all, so servers have a lot of flexibility
    * Once the client (the browser) has received a cookie for a particular website it will *always* add the cookie to all of it's HTTP requests for that website
    * Upon receiving subsequent requests the server performs Authorization based on the information in the cookie.
        * Browsers do this by default
        * In Python (and most other programming languages) you have to do extra work to explicitly store and send cookies.

* Random tidbits: 
    * Cookies predated the Local Storage and Session Storage APIs and the IndexedDB API, so Cookies used to be used for all kinds of data persistence in the client though that's no longer recommended. 
    * Cookies are used to track you from website to website! Ads on the page use a specific domain (e.g. doubleclick.com)

* Note that: Cookies are sometimes frowned upon in the REST standard because cookies are inherently "stateful"
    * Cookies are not explicitly forbidden, but they have the capability to store state information, which can be tempting to use.

**Micro-exercise: Go to your browser, open up the developer tools, open the network tab, go to a website where you're 'logged in' and find the any set-cookie headers. How does this information relate to your authentication/authorization within that website?**

## Authorization Headers and Tokens

* Most APIs are designed to be used directly by programmers outside of the web browser context
    * Cookies aren't that popular because they require more work to manage.

* These days most APIs rely on the "Authorization" header and the use of "tokens" to perform the same authentication functions that Cookies provide for web browsers. Useful documentation:
    * https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization
    * https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication

* Like cookies, these are driven by HTTP headers
* Like cookies, the values of the headers contain enough information to authenticate a particular user
    * Sometimes Authorization headers include the username:password combo
    * Sometimes they contain a token generated by the server
    * Etc.

* The general idea is the same, but often the flow of interactions look different. For example, we're about to authenticate with the Github API, and the flow will go like this...
    * Login to Github with our credentials via the web browser.
    * Navigate to a specific place within the Github Web App, and explicitly generate a "token"
        * Github servers associate this token with our account, which is authenticated via the Cookie
        * **NOTE: KEEP THIS TOKEN SECRET, IT IS EFFECTIVELY YOUR USERNAME AND PASSWORD COMBINED**
    * Take that token, and explicitly embed into our web requests in Python code.
        * It would work, but is not secure, to just copy/paste the value into our Python code
        * We'll use something called an "environment variable" to help keep our tokens secret

* **Mini-Exercise** Follow Along as we go ahead and generate our Github Access Tokens!
    * [https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token)
    * Login to Github
    * Click your profile in the top right corner
    * Click "settings" 
    * On the left hand pane, at the bottom, click "developer settings"
    * On the left hand pane, click Personal access tokens
    * On the left hand pane click Tokens (classic)
        * Fine-Grained tokens also work, but are in beta and require more configuration
    * In the middle of the screen click "generate a personal access token" 
        * This step will probably invoke your 2-step verification system, so follow those instructions
    * Set the expiry date to 7 days
        * You can actually do whatever you want, but you'll forget about this token and it's a good security practice to expire tokens when you're done with them!
    * Select privileges, for today's exercise you'll need to use:
        * repo: status and repo: public_repo
        * gist
        * user: read:user
        * Obviously we could select any or all of these. 
        * It's a good idea to follow the "principle of least privilege" i.e. only grant the smallest number of privileges needed to achieve your goals. 
    * Click "Generate token"
        * Don't leave the page until you've copied it, because you won't be able to see it again, instead you'll have to generate another token.
    * We're going to save this to an "environment variable" in our terminal
        * To make this persist across multiple sessions you'll need to add the following line to your `.zshrc` or `.bashrc` file
        * You can simply run the command in a single terminal session to create this variable for one time access.
        * `export GITHUB_ACCESS_TOKEN=your_token`
        * One liner: `echo -e '\nexport GITHUB_ACCESS_TOKEN=your_token' >> ~./zshrc`
        * Once you've done that, get a new terminal session or run `source ~/.zshrc` 
        * Finally, you can prove it worked with `echo $GITHUB_ACCESS_TOKEN`

* **Pop Quiz** Why is this considered a safe place for your access token? Didn't we basically just write down our password?