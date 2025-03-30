ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://ibm.github.io/watsonx-ai-python-sdk/rate_limit.html#furo-main-content)

[Back to top](https://ibm.github.io/watsonx-ai-python-sdk/rate_limit.html#)

[View this page](https://ibm.github.io/watsonx-ai-python-sdk/_sources/rate_limit.rst.txt "View this page")

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Rate Limits [¶](https://ibm.github.io/watsonx-ai-python-sdk/rate_limit.html\#rate-limits "Link to this heading")

Note

Supported since version 1.2.10

A **rate limit** is the maximum rate of API calls allowed for a service instance per second. In IBM Cloud services, the rate limit depends on the instance.

## Use Cases for Rate Limiting [¶](https://ibm.github.io/watsonx-ai-python-sdk/rate_limit.html\#use-cases-for-rate-limiting "Link to this heading")

The main purposes of rate limiting include:

- Enforcing granular access control to resources.

- Managing load to maintain a smooth and consistent user experience.

- Protecting REST APIs from resource exhaustion (e.g., targeted DDoS attacks) and preventing general abuse.


## Handling Rate Limits [¶](https://ibm.github.io/watsonx-ai-python-sdk/rate_limit.html\#handling-rate-limits "Link to this heading")

If the limit is reached, an HTTP **429 Too Many Requests** error response is returned. The response header will also contain information about the limit.

## Mitigation Strategies [¶](https://ibm.github.io/watsonx-ai-python-sdk/rate_limit.html\#mitigation-strategies "Link to this heading")

These values can be configured for the following classes: **ModelInference, Embeddings**.

The `ibm-watsonx-ai` client includes an in-built retry mechanism and traffic optimization to minimize excessive requests and respect the request rate limit for each instance. It is recommended to start with the default settings. However, since predicting instance usage can be difficult, the retry mechanism provides three configurable options for handling unsuccessful requests:

- **max\_retries** – The maximum number of retry attempts when an error code in `retry_status_codes` is received. Defaults to 10.

- **delay\_time** – The factor used in exponential backoff: `min(delay_time * pow(2.0, attempt), MAX_RETRY_DELAY)`. The default value for `delay_time` is 0.5, and `MAX_RETRY_DELAY` is 8 seconds.

- **retry\_status\_codes** – The list of HTTP status codes for which the retry mechanism should be applied. Defaults to `[429, 503, 504, 520]`. The **429 Too Many Requests** error is handled differently: retries occur as soon as the next available slot is free, whereas other status codes follow an exponential backoff strategy.


## Summary [¶](https://ibm.github.io/watsonx-ai-python-sdk/rate_limit.html\#summary "Link to this heading")

The default values should be sufficient to handle requests without requiring additional configuration while avoiding excessive requests. However, depending on traffic patterns, they may still interfere with operations. To mitigate this, the retry mechanism prioritizes **429 responses** while allowing customization of **max\_retries, delay\_time, and retry\_status\_codes**.