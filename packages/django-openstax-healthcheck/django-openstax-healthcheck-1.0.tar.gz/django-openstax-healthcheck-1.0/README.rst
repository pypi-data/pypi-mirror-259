===========================
django-openstax-healthcheck
===========================

``django-openstax-healthcheck`` is a Django middleware to intercept ``/ping`` and ``/ping/`` requests from AWS.
This is required when using OpenStax IaC for deployment.

Quick start
-----------

Add the following settings to your settings file:::

    # Add to middleware, be sure it's before CommonMiddleware
    MIDDLEWARE = [
        # ... (optional before)
        'healthcheck.middleware.HealthCheckMiddleware',
        # ... (optional between)
        'django.middleware.common.CommonMiddleware',
        # ... (optional after CommonMiddleware)
    ]


Usage
-----

Add something like this to your logging configuration::

    import logging
    logging.config.dictConfig({
        # ...
        'filters': {
            'healthcheck_filter': {
                '()': 'healthcheck.filter.HealthCheckFilter'
            },
        },
        # ...
    })

