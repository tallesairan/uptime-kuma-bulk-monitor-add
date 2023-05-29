Bulk Website Add for Kuma Uptime using the API
==============================================

This project allows you to bulk add websites to Kuma Uptime using the API.

Requirements
-----------------

Python 3.6+

tldextract
uptime-kuma-api
python-dotenv


API Documentation
-----------------

The API documentation for Kuma Uptime can be found at: [Uptime Kuma API Documentation](https://uptime-kuma-api.readthedocs.io/en/latest/api.html)

Monitor Documentation
---------------------

Detailed information on how to add monitors using the Kuma Uptime API can be found at: [Monitor Documentation](https://uptime-kuma-api.readthedocs.io/en/latest/api.html#uptime_kuma_api.UptimeKumaApi.add_monitor)

Features
----------
This is a simple script to help with repetitive tasks

1. automatic and fast to create monitors in kuma
2. simple and safe
3. no need to manually add monitors one by one
4. Summarizer for NSFW websites

How to Use
----------

To use this project, follow these steps:

1.  Create a file named `urls.txt`.
2.  Add one website URL per line in the `urls.txt` file.
3.  Run the project and it will automatically add the websites to Kuma Uptime.
4.  Set up your environment data based on .env.example.

````
python3 kuma-add.py
````

Libraries Used
--------------

This project utilizes the following library:

-   [Uptime Kuma API](https://github.com/lucasheld/uptime-kuma-api)

Make sure to install the required dependencies before running the project. Refer to the library's documentation for installation instructions.

Feel free to contribute to this project by submitting pull requests or reporting issues. Happy monitoring!

Examples
-----------------
### add_monitor(***kwargs*) → dict[](https://uptime-kuma-api.readthedocs.io/en/latest/api.html#uptime_kuma_api.UptimeKumaApi.add_monitor "Permalink to this definition")

Adds a new monitor.

Parameters:

-   **type** ([*MonitorType*](https://uptime-kuma-api.readthedocs.io/en/latest/api.html#uptime_kuma_api.MonitorType "uptime_kuma_api.MonitorType")) -- Monitor Type

-   **name** (*str*) -- Friendly Name

-   **description** (*str**, **optional*) -- Description, defaults to None

-   **interval** (*int**, **optional*) -- Heartbeat Interval, defaults to 60

-   **retryInterval** (*int**, **optional*) -- Retry every X seconds, defaults to 60

-   **resendInterval** (*int**, **optional*) -- Resend every X times, defaults to 0

-   **maxretries** (*int**, **optional*) -- Retries. Maximum retries before the service is marked as down and a notification is sent., defaults to 0

-   **upsideDown** (*bool**, **optional*) -- Upside Down Mode. Flip the status upside down. If the service is reachable, it is DOWN., defaults to False

-   **notificationIDList** (*list**, **optional*) -- Notifications, defaults to None

-   **url** (*str**, **optional*) -- URL, defaults to None

-   **expiryNotification** (*bool**, **optional*) -- Certificate Expiry Notification, defaults to False

-   **ignoreTls** (*bool**, **optional*) -- Ignore TLS/SSL error for HTTPS websites, defaults to False

-   **maxredirects** (*int**, **optional*) -- Max. Redirects. Maximum number of redirects to follow. Set to 0 to disable redirects., defaults to 10

-   **accepted_statuscodes** (*list**, **optional*) -- Accepted Status Codes. Select status codes which are considered as a successful response., defaults to None

-   **proxyId** (*int**, **optional*) -- Proxy, defaults to None

-   **method** (*str**, **optional*) -- Method, defaults to "GET"

-   **httpBodyEncoding** (*str**, **optional*) -- Body Encoding, defaults to "json". Allowed values: "json", "xml".

-   **body** (*str**, **optional*) -- Body, defaults to None

-   **headers** (*str**, **optional*) -- Headers, defaults to None

-   **authMethod** ([*AuthMethod*](https://uptime-kuma-api.readthedocs.io/en/latest/api.html#uptime_kuma_api.AuthMethod "uptime_kuma_api.AuthMethod")*, **optional*) -- Method, defaults to [`NONE`](https://uptime-kuma-api.readthedocs.io/en/latest/api.html#uptime_kuma_api.AuthMethod.NONE "uptime_kuma_api.AuthMethod.NONE")

-   **tlsCert** (*str**, **optional*) -- Cert for `authMethod` [`MTLS`](https://uptime-kuma-api.readthedocs.io/en/latest/api.html#uptime_kuma_api.AuthMethod.MTLS "uptime_kuma_api.AuthMethod.MTLS"), defaults to None.

-   **tlsKey** (*str**, **optional*) -- Key for `authMethod` [`MTLS`](https://uptime-kuma-api.readthedocs.io/en/latest/api.html#uptime_kuma_api.AuthMethod.MTLS "uptime_kuma_api.AuthMethod.MTLS"), defaults to None.

-   **tlsCa** (*str**, **optional*) -- Ca for `authMethod` [`MTLS`](https://uptime-kuma-api.readthedocs.io/en/latest/api.html#uptime_kuma_api.AuthMethod.MTLS "uptime_kuma_api.AuthMethod.MTLS"), defaults to None.

-   **basic_auth_user** (*str**, **optional*) -- Username for `authMethod` [`HTTP_BASIC`](https://uptime-kuma-api.readthedocs.io/en/latest/api.html#uptime_kuma_api.AuthMethod.HTTP_BASIC "uptime_kuma_api.AuthMethod.HTTP_BASIC") and [`NTLM`](https://uptime-kuma-api.readthedocs.io/en/latest/api.html#uptime_kuma_api.AuthMethod.NTLM "uptime_kuma_api.AuthMethod.NTLM"), defaults to None

-   **basic_auth_pass** (*str**, **optional*) -- Password for `authMethod` [`HTTP_BASIC`](https://uptime-kuma-api.readthedocs.io/en/latest/api.html#uptime_kuma_api.AuthMethod.HTTP_BASIC "uptime_kuma_api.AuthMethod.HTTP_BASIC") and [`NTLM`](https://uptime-kuma-api.readthedocs.io/en/latest/api.html#uptime_kuma_api.AuthMethod.NTLM "uptime_kuma_api.AuthMethod.NTLM"), defaults to None

-   **authDomain** (*str**, **optional*) -- Domain for `authMethod` [`NTLM`](https://uptime-kuma-api.readthedocs.io/en/latest/api.html#uptime_kuma_api.AuthMethod.NTLM "uptime_kuma_api.AuthMethod.NTLM"), defaults to None

-   **authWorkstation** (*str**, **optional*) -- Workstation for `authMethod` [`NTLM`](https://uptime-kuma-api.readthedocs.io/en/latest/api.html#uptime_kuma_api.AuthMethod.NTLM "uptime_kuma_api.AuthMethod.NTLM"), defaults to None

-   **keyword** (*str**, **optional*) -- Keyword. Search keyword in plain HTML or JSON response. The search is case-sensitive., defaults to None

-   **hostname** (*str**, **optional*) -- Hostname, defaults to None

-   **packetSize** (*int**, **optional*) -- Packet Size, defaults to None

-   **port** (*int**, **optional*) -- Port, `type` [`DNS`](https://uptime-kuma-api.readthedocs.io/en/latest/api.html#uptime_kuma_api.MonitorType.DNS "uptime_kuma_api.MonitorType.DNS") defaults to `53` and `type` [`RADIUS`](https://uptime-kuma-api.readthedocs.io/en/latest/api.html#uptime_kuma_api.MonitorType.RADIUS "uptime_kuma_api.MonitorType.RADIUS") defaults to `1812`

-   **dns_resolve_server** (*str**, **optional*) -- Resolver Server, defaults to "1.1.1.1"

-   **dns_resolve_type** (*str**, **optional*) -- Resource Record Type, defaults to "A"

-   **mqttUsername** (*str**, **optional*) -- MQTT Username, defaults to None

-   **mqttPassword** (*str**, **optional*) -- MQTT Password, defaults to None

-   **mqttTopic** (*str**, **optional*) -- MQTT Topic, defaults to None

-   **mqttSuccessMessage** (*str**, **optional*) -- MQTT Success Message, defaults to None

-   **databaseConnectionString** (*str**, **optional*) -- Connection String, defaults to None

-   **databaseQuery** (*str**, **optional*) -- Query, defaults to None

-   **docker_container** (*str**, **optional*) -- Container Name / ID, defaults to ""

-   **docker_host** (*int**, **optional*) -- Docker Host, defaults to None

-   **radiusUsername** (*str**, **optional*) -- Radius Username, defaults to None

-   **radiusPassword** (*str**, **optional*) -- Radius Password, defaults to None

-   **radiusSecret** (*str**, **optional*) -- Radius Secret. Shared Secret between client and server., defaults to None

-   **radiusCalledStationId** (*str**, **optional*) -- Called Station Id. Identifier of the called device., defaults to None

-   **radiusCallingStationId** (*str**, **optional*) -- Calling Station Id. Identifier of the calling device., defaults to None

-   **game** (*str**, **optional*) -- Game, defaults to None

Returns:

The server response.

Return type:

dict

Raises:

[**UptimeKumaException**](https://uptime-kuma-api.readthedocs.io/en/latest/api.html#uptime_kuma_api.UptimeKumaException "uptime_kuma_api.UptimeKumaException") -- If the server returns an error.

Example:

>>> api.add_monitor(
...     type=MonitorType.HTTP,
...     name="Google",
...     url="https://google.com"
... )
{
 'msg': 'Added Successfully.',
 'monitorID': 1
}

### edit_monitor(*id_: int*, ***kwargs*) → dict[](https://uptime-kuma-api.readthedocs.io/en/latest/api.html#uptime_kuma_api.UptimeKumaApi.edit_monitor "Permalink to this definition")

Edits an existing monitor.

Parameters:

-   **id** (*int*) -- The monitor id.

-   **type** ([*MonitorType*](https://uptime-kuma-api.readthedocs.io/en/latest/api.html#uptime_kuma_api.MonitorType "uptime_kuma_api.MonitorType")*, **optional*) -- Monitor Type

-   **name** (*str**, **optional*) -- Friendly Name

-   **description** (*str**, **optional*) -- Description, defaults to None

-   **interval** (*int**, **optional*) -- Heartbeat Interval, defaults to 60

-   **retryInterval** (*int**, **optional*) -- Retry every X seconds, defaults to 60

-   **resendInterval** (*int**, **optional*) -- Resend every X times, defaults to 0

-   **maxretries** (*int**, **optional*) -- Retries. Maximum retries before the service is marked as down and a notification is sent., defaults to 0

-   **upsideDown** (*bool**, **optional*) -- Upside Down Mode. Flip the status upside down. If the service is reachable, it is DOWN., defaults to False

-   **notificationIDList** (*list**, **optional*) -- Notifications, defaults to None

-   **url** (*str**, **optional*) -- URL, defaults to None

-   **expiryNotification** (*bool**, **optional*) -- Certificate Expiry Notification, defaults to False

-   **ignoreTls** (*bool**, **optional*) -- Ignore TLS/SSL error for HTTPS websites, defaults to False

-   **maxredirects** (*int**, **optional*) -- Max. Redirects. Maximum number of redirects to follow. Set to 0 to disable redirects., defaults to 10

-   **accepted_statuscodes** (*list**, **optional*) -- Accepted Status Codes. Select status codes which are considered as a successful response., defaults to None

-   **proxyId** (*int**, **optional*) -- Proxy, defaults to None

-   **method** (*str**, **optional*) -- Method, defaults to "GET"

-   **httpBodyEncoding** (*str**, **optional*) -- Body Encoding, defaults to "json". Allowed values: "json", "xml".

-   **body** (*str**, **optional*) -- Body, defaults to None

-   **headers** (*str**, **optional*) -- Headers, defaults to None

-   **authMethod** ([*AuthMethod*](https://uptime-kuma-api.readthedocs.io/en/latest/api.html#uptime_kuma_api.AuthMethod "uptime_kuma_api.AuthMethod")*, **optional*) -- Method, defaults to [`NONE`](https://uptime-kuma-api.readthedocs.io/en/latest/api.html#uptime_kuma_api.AuthMethod.NONE "uptime_kuma_api.AuthMethod.NONE")

-   **tlsCert** (*str**, **optional*) -- Cert for `authMethod` [`MTLS`](https://uptime-kuma-api.readthedocs.io/en/latest/api.html#uptime_kuma_api.AuthMethod.MTLS "uptime_kuma_api.AuthMethod.MTLS"), defaults to None.

-   **tlsKey** (*str**, **optional*) -- Key for `authMethod` [`MTLS`](https://uptime-kuma-api.readthedocs.io/en/latest/api.html#uptime_kuma_api.AuthMethod.MTLS "uptime_kuma_api.AuthMethod.MTLS"), defaults to None.

-   **tlsCa** (*str**, **optional*) -- Ca for `authMethod` [`MTLS`](https://uptime-kuma-api.readthedocs.io/en/latest/api.html#uptime_kuma_api.AuthMethod.MTLS "uptime_kuma_api.AuthMethod.MTLS"), defaults to None.

-   **basic_auth_user** (*str**, **optional*) -- Username for `authMethod` [`HTTP_BASIC`](https://uptime-kuma-api.readthedocs.io/en/latest/api.html#uptime_kuma_api.AuthMethod.HTTP_BASIC "uptime_kuma_api.AuthMethod.HTTP_BASIC") and [`NTLM`](https://uptime-kuma-api.readthedocs.io/en/latest/api.html#uptime_kuma_api.AuthMethod.NTLM "uptime_kuma_api.AuthMethod.NTLM"), defaults to None

-   **basic_auth_pass** (*str**, **optional*) -- Password for `authMethod` [`HTTP_BASIC`](https://uptime-kuma-api.readthedocs.io/en/latest/api.html#uptime_kuma_api.AuthMethod.HTTP_BASIC "uptime_kuma_api.AuthMethod.HTTP_BASIC") and [`NTLM`](https://uptime-kuma-api.readthedocs.io/en/latest/api.html#uptime_kuma_api.AuthMethod.NTLM "uptime_kuma_api.AuthMethod.NTLM"), defaults to None

-   **authDomain** (*str**, **optional*) -- Domain for `authMethod` [`NTLM`](https://uptime-kuma-api.readthedocs.io/en/latest/api.html#uptime_kuma_api.AuthMethod.NTLM "uptime_kuma_api.AuthMethod.NTLM"), defaults to None

-   **authWorkstation** (*str**, **optional*) -- Workstation for `authMethod` [`NTLM`](https://uptime-kuma-api.readthedocs.io/en/latest/api.html#uptime_kuma_api.AuthMethod.NTLM "uptime_kuma_api.AuthMethod.NTLM"), defaults to None

-   **keyword** (*str**, **optional*) -- Keyword. Search keyword in plain HTML or JSON response. The search is case-sensitive., defaults to None

-   **hostname** (*str**, **optional*) -- Hostname, defaults to None

-   **packetSize** (*int**, **optional*) -- Packet Size, defaults to None

-   **port** (*int**, **optional*) -- Port, `type` [`DNS`](https://uptime-kuma-api.readthedocs.io/en/latest/api.html#uptime_kuma_api.MonitorType.DNS "uptime_kuma_api.MonitorType.DNS") defaults to `53` and `type` [`RADIUS`](https://uptime-kuma-api.readthedocs.io/en/latest/api.html#uptime_kuma_api.MonitorType.RADIUS "uptime_kuma_api.MonitorType.RADIUS") defaults to `1812`

-   **dns_resolve_server** (*str**, **optional*) -- Resolver Server, defaults to "1.1.1.1"

-   **dns_resolve_type** (*str**, **optional*) -- Resource Record Type, defaults to "A"

-   **mqttUsername** (*str**, **optional*) -- MQTT Username, defaults to None

-   **mqttPassword** (*str**, **optional*) -- MQTT Password, defaults to None

-   **mqttTopic** (*str**, **optional*) -- MQTT Topic, defaults to None

-   **mqttSuccessMessage** (*str**, **optional*) -- MQTT Success Message, defaults to None

-   **databaseConnectionString** (*str**, **optional*) -- Connection String, defaults to None

-   **databaseQuery** (*str**, **optional*) -- Query, defaults to None

-   **docker_container** (*str**, **optional*) -- Container Name / ID, defaults to ""

-   **docker_host** (*int**, **optional*) -- Docker Host, defaults to None

-   **radiusUsername** (*str**, **optional*) -- Radius Username, defaults to None

-   **radiusPassword** (*str**, **optional*) -- Radius Password, defaults to None

-   **radiusSecret** (*str**, **optional*) -- Radius Secret. Shared Secret between client and server., defaults to None

-   **radiusCalledStationId** (*str**, **optional*) -- Called Station Id. Identifier of the called device., defaults to None

-   **radiusCallingStationId** (*str**, **optional*) -- Calling Station Id. Identifier of the calling device., defaults to None

-   **game** (*str**, **optional*) -- Game, defaults to None

Returns:

The server response.

Return type:

dict

Raises:

[**UptimeKumaException**](https://uptime-kuma-api.readthedocs.io/en/latest/api.html#uptime_kuma_api.UptimeKumaException "uptime_kuma_api.UptimeKumaException") -- If the server returns an error.

Example:

>>> api.edit_monitor(1,
...     interval=20
... )
{
 'monitorID': 1,
 'msg': 'Saved.'
}