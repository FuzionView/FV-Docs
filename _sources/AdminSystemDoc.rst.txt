Admin System Documentation
===========================

This document provides information about the development of the FV-Admin tools, a Ruby on Rails administration interface for FuzionView that is used to manage:
 * Data Providers
 * Datasets
 * Users
 * System Settings

.. note::

   FV-Admin tools are only available to authorized users who have executed a user agreement with their system operator. FV-Engine is used for the more public components of FuzionView and is in a separate repository. Check out the Developer documentation for more information.


Development Environment
------------------------
* APIs - TBD
* Ruby version: 3.0+
* Rails version: 7.1.x
* Database: PostgreSQL

System Dependencies
--------------------

* Implementation of Fuzionview PostgreSQL application
* Ruby 3.0+

Security
^^^^^^^^^^^

* Authentication: OpenID Connect (Keycloak or other OIDC provider)
* Authorization: Pundit, based on two externally defined roles set in FV_ADMINISTRATOR, FV_DATA_PROVIDER environment variables

Admin Tools Interface
^^^^^^^^^^^^^^^^^^^^^^

* UI: Bootstrap 5.3

Configuration
---------------

Rename env_example to .env and fill in the required environment variables:

.. code-block::

   SECRET_KEY_BASE=

   PG_DB=
   PG_USER=
   PG_PASS=
   PG_HOST=
   PG_PORT=

   OP_CLIENT_ID=
   OP_SECRET_KEY=
   OP_REDIRECT_URI=
   OP_HOST=
   OP_REALM=
   OP_AUTH_ENDPOINT="/protocol/openid-connect/auth"
   OP_TOKEN_ENDPOINT="/protocol/openid-connect/token"
   OP_USERINFO_ENDPOINT="/protocol/openid-connect/userinfo"
   OP_JWKS_ENDPOINT="/protocol/openid-connect/certs"
   OP_LOGOUT_ENDPOINT="/protocol/openid-connect/logout"

   FV_ADMINISTRATOR=Administrator
   FV_DATA_PROVIDER="Data Provider"

   TEST_TICKET_URL=https://localhost/api/tickets/

.. note::

    Most text in the application is externalized and can be updated in config/locales/en.yml.

Deployment
-----------

* Phusion Passenger is the recommended production deployment method.
* Precompile assets in production RAILS_ENV=production RAILS_RELATIVE_URL_ROOT=/admin rails assets:precompile

Development
------------

**Development Setup**
Clone the repository.
Install dependencies

.. code-block::

   bundle install

**Start the server**

.. code-block::

   bin/rails server

Testing
--------

Running tests

.. code-block::

   RAILS_ENV=test bundle exec rails db:drop db:create db:schema:load
   bin/rails test

Migration
----------

.. code-block::

   bin/rails db:migrate


Last Updated: |today|
