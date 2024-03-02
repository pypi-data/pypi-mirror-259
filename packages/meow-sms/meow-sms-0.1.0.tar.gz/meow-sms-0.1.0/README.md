# **MeowSMS Python Package**

![](./img.webp)

The MeowSMS Python package is an asynchronous module designed for seamless interaction with the Meow SMS API. It
provides a comprehensive set of features for sending SMS messages, customizing SMS content, checking domain status, and
more. Whether you're looking to integrate SMS notifications into your application or automate messaging based on
specific triggers, MeowSMS has got you covered.

## **Features**

- **Async Support**: Designed with asyncio in mind, enabling efficient I/O operations.
- **Comprehensive API Coverage**: From sending SMS and custom SMS to checking domain status and retrieving service information.
- **Dynamic Service Updates**: Automatically updates service lists and patterns daily.
- **User Profile Management**: Access and manage your Meow SMS profile information with ease.
- **Flexible Proxy Configuration**: Supports proxy settings for requests allowing usage behind firewalls or for anonymity.

## **Installation**

Install the package using pip:
```bash
pip install moonheimsms
```

## **Quick Start**

Here's a quick example to get you started with sending an SMS:

```python
from meowsms import MeowSMS

# Initialize MeowSMS with your API token
sms = MeowSMS(token="your_api_token_here")

# Send an SMS
response = await sms.sendSms(number="1234567890", service="your_service_id", link="http://yourlink.com", template=1)

print(response)
```

## Documentation

For detailed documentation on all available methods and their usage, please refer to the official Meow SMS API documentation.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](./LICENSE) file for details.

## Contributing

Contributions are welcome! Please read the contributing guidelines before starting any work.

## Support

If you encounter any issues or have questions, please file an issue on the GitHub repository.


> [!IMPORTANT]
> This package is not officially affiliated with Meow SMS. All trademarks belong to their respective owners.