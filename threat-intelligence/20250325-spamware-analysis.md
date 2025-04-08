# Spamware Analysis
*This report is still being created... it is unfinished.*

Here are the steps I followed to investigate an interesting malware spam email message I received on March 24, 2025.

The message said I had mined $80000 in crypto, so I thought I should check it to see if it was legit!

### URLs

* translate.google.com/translate
  * Query string: ?sl=auto&tl=en&hl=en&u= 
* sparscreations[.]com
  * `urlencoded` link makes visual analysis difficult. %3F == '?', %3D == '='
  * sparscreations.com/stagging/web/go.php?click=
* rolastopas[.]cc/go/33b4z2/y2?label=0074_12_copy
* A different URL was available at a different time when the message was opened:
  * translate.google[.]com/translate?sl=auto&tl=en&hl=en&u=sparscreations[.]com/stagging/web/go.php?click=0045_copy%26googlePIDR=aackler@aol[.]com%26id_list=GPGkvWSuoVONnsSVOiZ
  * translate.google[.]com/translate?sl=auto&tl=en&hl=en&u=sparscreations[.]com/stagging/web/go.php?click=0074_12_copy%26googlePIDR=utavligenc08@gmail[.]com%26id_list=RTZSzvNVtxUWwTZppzWTvZNvy
* Value of id_list=GPGkvWSuoVONnsSVOiZ looks Base64 encoded: but likely isn't. Unless it results in an unusual character set, or is the Chinese words "Yun Fan"
* Use reqbin.com/curl to execute curl command to try and download the script.
  * The link to go.php was not accessible
  * The full translate... link returns the page seen in the Any.run sandbox
  * The base tag contains a new url: sparscreations.com/stagging/web/url2[.]php and it returns a page with the Russian comment: "для предотвращения загрузки через Google Translate" which translates to "to prevent loading through Google Translate" so another technique would be required to grab the file.
* sparscreations.com `whois` data shows nameservers in India, registered by GoDaddy via Domains By Proxy (see https://en.wikipedia.org/wiki/Domains_by_Proxy)
* `curl -X GET rolastopas[.]cc/go/33b4z2/y2?label=0074_12_copy` also returns the Bitcoin page from the Any.run test.
  * Domain info hidden, uses CloudFlare DNS, registered by Nicenic, State listed as "Use Popkas". Popkas is Russian slang for ass, as well as the name of a series of cartoon images by an online artist.
  * NiceNIC is a Hong Kong based company, though may be associated with a high number of fraudulant and malicious sites. See https://ca.trustpilot.com/review/nicenic.net.
  * `rolastopas` may be Latvian for "roller coaster"
    * The results from the curl command show interesting details, see below. Accprding to Microsoft CoPilot, it is likely config info for a Nuxt-baesd website. Nuxt is a web framework used with Vue.js which is also used for web front-end UI.
    * The root rolastopas[.]cc simply returns a 200 OK from an nginx server.
    * `curl -X GET rolastopas.cc/pay.php` returns a 500 server error
    * `curl -X GET rolastopas.cc/go/pay.php` returns a 200 with the simple text "Error go 1" - likely a basic error meaning there was no value passed to the function
    * `curl -X GET rolastopas.cc/go/pay.php/p=15` returns the same
    * Attempting other values and trying to access payout and payout/_nuxt were unsuccessful. After developing a simple Nuxt app it might be more clear what to poke at.
    * Also tried alternative curl commands as a last ditch effor.


  ### Result from curl -X Get Rolastopas

  ```html
  <!DOCTYPE html>
  <html>

  <head>
    <meta charset="utf-8">
    <title>Bitcoin Mining</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Bitcoin Mining!">
    <link rel="icon" type="image/png" href="/favicon.png">
    <link rel="modulepreload" as="script" crossorigin href="/_nuxt/entry.4e713294.js">
    <link rel="preload" as="style" href="/_nuxt/entry.816a5a0f.css">
    <link rel="prefetch" as="script" crossorigin href="/_nuxt/url.0b90d914.js">
    <link rel="prefetch" as="script" crossorigin href="/_nuxt/error-component.e8645654.js">
    <link rel="stylesheet" href="/_nuxt/entry.816a5a0f.css">
  </head>

  <body>
    <div id="__nuxt"></div>
    <script>
        window.__NUXT__ = (function(a) {
            return {
                serverRendered: false,
                config: {
                    public: {
                        paymentLink: a,
                        payExchange: "\u002Fpay.php?p=53",
                        payExchangeFee: 64,
                        payCommissionfp: "\u002Fpay.php?p=63",
                        payCommissionfpFee: 56,
                        payCommissionsp: "\u002Fpay.php?p=y264",
                        payCommissionspFee: 48,
                        payExpress: "\u002Fpay.php?p=y274",
                        payExpressFee: 92,
                        payCadastr: "\u002Fpay.php?p=y284",
                        payCadastrFee: 86,
                        payTransitbooking: "\u002Fpay.php?p=y294",
                        payTransitbookingFee: 105,
                        payTransitactivation: "\u002Fpay.php?p=y2a4",
                        payTransitactivationFee: 97,
                        paySignature: "\u002Fpay.php?p=y2b4",
                        paySignatureFee: 127,
                        paySignatureverify: "\u002Fpay.php?p=y2c4",
                        paySignatureverifyFee: 166,
                        payTls: "\u002Fpay.php?p=y2d4",
                        payTlsFee: 182,
                        payManual: "\u002Fpay.php?p=y2e4",
                        payManualFee: 208,
                        payLimitex: "\u002Fpay.php?p=y2f4",
                        payLimitexFee: 229,
                        payMomentum: "\u002Fpay.php?p=z264",
                        payMomentumFee: 268
                    },
                    app: {
                        baseURL: "\u002Fpayouts",
                        buildAssetsDir: "\u002F_nuxt\u002F",
                        cdnURL: a
                    }
                },
                data: {},
                state: {}
            }
        }(""))
    </script>
    <script type="module" src="/_nuxt/entry.4e713294.js" crossorigin></script>
  </body>
  </html>
```

