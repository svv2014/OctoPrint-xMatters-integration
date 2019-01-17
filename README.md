# OctoPrint-Xmatters-integration

This plugin helps to send notifications by using [xMatters](https://xmatters.com) integration.

## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)

### Manually using this URL:

    https://github.com/svv2014/OctoPrint-Xmatters-integration/archive/master.zip

### Using `pip`

    pip install https://github.com/svv2014/OctoPrint-Xmatters-integration/archive/master.zip

## xMatter integration setup 

* Open your xMatters page
* go to page: Developer > Communication Plans
* Import zip file from `xMatters/OctoPrintIntegration.zip` 
    * this will create communication plan for integration
* On communication plan press `Edit` and choose `Integration Builder`
* You should see one configured `Inbound integration`  
    * Note if `Inbound integrations` configuration was not imported you may need to create once with `authentication method` equals to `API key`. 
* Open this configuration and at the bottom you will find all needed credential you ne

## Configuration

* Take `API Key`, `Secret`, `Integration URL` from xMatters integration and set it in plugin configuration
    * Note: for `recipients` field use comma separated user id
* Choose events you interested in and enjoy.

## TODO
* custom messages
* option to send a photo with notification
