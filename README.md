# OctoPrint-Xmatters-integration

This plugin helps to send notifications by using [xMatters](https://xmatters.com) integration.

## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)

### Manually using this URL:

    https://github.com/svv2014/OctoPrint-Xmatters-integration/archive/master.zip

### Using `pip`

    pip install https://github.com/svv2014/OctoPrint-Xmatters-integration/archive/master.zip

### After install
    You better to do full restatart after installing plugin, there is an issue that is listed in TODO section.

## xMatter integration setup 

* Open your xMatters page
* go to page: Developer > Communication Plans
* Import zip file from `xMatters/OctoPrintIntegration.zip` 
    * this will create communication plan for integration
* On communication plan press `Edit` and choose `Integration Builder`
* You should see one configured `Inbound integration`  
    * Note if `Inbound integrations` configuration was not imported you may need to create once with `authentication method` equals to `API key`. 
* Open this configuration and at the bottom you will find all needed credentials

## Configuration

* Take `API Key`, `Secret`, `Integration URL` from xMatters integration and set it in plugin configuration
    * Note: for `recipients` field use comma separated user id
* Choose events you interested in and enjoy.

## TODO
* prompt usert to do full restart after plugin install
* Add test button to check integration with xMatters 
* custom messages
* option to send a photo with notification
