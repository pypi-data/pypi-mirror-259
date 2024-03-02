# satosacontrib.perun

Microservices, backends and add-ons
for [SATOSA](https://github.com/IdentityPython/SATOSA) authentication proxy.

## Backends

### Seznam backend

A backend for SATOSA which implements login
using [Seznam OAuth](https://partner.seznam.cz/seznam-oauth/).

Use the [example config](./example/plugins/backends/seznam.yaml) and fill in your client
ID and client secret.

## Microservices

### AuthSwitcher Lite

This request microservice takes ACRs (AuthnContextClassRefs in SAML, acr_values in OIDC)
from a frontend
and sets them as requested ACRs for the backends. It relies
on [SATOSA!419](https://github.com/IdentityPython/SATOSA/pull/419)

### Context attributes microservice

The microservice adds the target IdP data to attributes:

- display name
- logo
- target issuer

The [MetaInfoIssuer](https://github.com/SUNET/swamid-satosa/blob/main/src/swamid_plugins/metainfo/metainfo.py)
microservice needs to be run beforehand with the
following [patch](https://github.com/SUNET/swamid-satosa/compare/main...kofzera:swamid-satosa:add_collector_metadata.patch).
Another [patch](https://github.com/IdentityPython/SATOSA/compare/master...kofzera:SATOSA:decorate_context_with_metadata.patch)
is
also needed for the satosa package until they are incorporated into the upstream.

### Is banned microservice

The microservice connects to database storing user bans and redirects banned users to
configured URL.

Requires a MongoDB database (specified in config).

### Persist authorization params microservice

This request microservice retrieves configured parameters from GET or POST request (if
available) and
stores the values to internal context state.

### Forward authorization params microservice

This request microservice retrieves configured parameters from GET or POST request (if
available) and
forwards them through a context parameter. Optionally, `default_values` can be
provided in the config file. These will be forwarded for configured SP and/or IdP if
not provided in the GET/POST request. If the parameter with preconfigured
default value is sent via GET/POST request anyway, the value form the request will be
used instead of the default.

### Session started with microservice

This Satosa microservice checks, if configured attribute's value is present
in "session_started_with" values (retrieved by Persist authorization params
microservice).
If so, adds attribute with configured name. The value is expected to be converted
to boolean by Attribute typing microservice.

### Compute eligibility microservice

The microservice obtains dict with format { eligiblility_type: <unix_timestamp> }
from the internal data and runs a function configured for the
given eligibility type. The config is of format `type: function_path`.

The function should have a following signature:  
`example_func(data: InternalData, *args, **kwargs) -> timestamp | bool`, and it either
returns `False` or
a new timestamp, in which case the time in the dictionary is
updated in internal data. It strongly relies on the PerunAttributes microservice to fill
the dict
beforehand. If you want to update eligibility in the IDM, use the UpdateUserExtSource
microservice.

### NameID Attribute microservice

This microservice copies SAML NameID to an internal attribute with preconfigured name (
and format).

It has two modes of operation. The deprecated way of configuring the microservice
requires the config to
include `nameid_attribute: saml2_nameid_persistent`, where `saml2_nameid_persistent`
stands for the name of the SAML NameID
attribute in format: `urn:oasis:names:tc:SAML:2.0:nameid-format:persistent`. The new way
of configuring this
microservice expects a dictionary named `nameid_attributes` containing items
like `saml2_nameid_format: saml2_nameid_attribute`. In case of the newer configuration,
both the format and attribute need
to be configured correctly in order for the NameID attribute to be copied to the
internal attribute.

If one of the ways to use the microservice is configured, it will be used. If both ways
are configured, the newer way of
configuration - dictionary, will be used.

Demonstrations of both ways of configuration are shown in the example config.

### Attribute typing microservice

Converts boolean attributes specified in config under `boolean_attributes` to bool type.
It does this by having list of possible values for both `true` and `false`. Unknown values are converted to None.

### Auth event logging microservice

Captures and logs authentication and authorization events. It extracts data from incoming requests
and records this information in a database.

Requires a PostgreSQL database.

### Cardinality single microservice

Convert single-valued attributes specified in `config["attributes"]` from lists to strings.

### Is eligible microservice

Obtains dict with format { eligiblility_type: <unix_timestamp> } and compares the eligibility timestamp
of each type with preconfigured thresholds. All applicable eligibility
intervals for each eligibility_type are included in the result.

Thresholds are defined in config under `supported_eligibility_types: type: suffixes:`.
To get a clearer idea, see example config.

Targeted attributes are specified in the configuration under the `target_attributes` parameter.
If it isn't provided, it the defaults to using `eduPersonAssurance` instead.

### Multi Idp hint microservice

Microservice designed to process multi-valued identity provider hints (idphint) in authentication requests.
It maps entity IDs based on `entity_id_mapping` in config, generates a WAYF filter, and updates the discovery service URL accordingly.

### Proxy statistics microservice

Collects and logs statistics related to authentication and authorization events.
It interacts with a database to store data about IDPs, SPs, and user logins.

Depends on external PostgreSQL db. Needs package driver `psycopg2-binary`.
If driver is changed in the config, corresponding package needs to be installed instead.

### Requester client ID microservices

`SendRequesterClientID` reads the current requester ID and puts it into a query parameter for next authentication.
`ForwardRequesterClientID` reads requester client ID from a query parameter
and puts it into state for the SAML backend to send as SAML requester ID.

## Perun Microservices

Subpackage of microservices connecting to perun. These have to be allowed (or not
denied) for
a given combination of requester/target_entity in order to run.

### Additional Identifiers

Takes user attributes by config, checks values with regexes and creates hashes by
specified algorithm. Values prepared to hash are parsed into List of List of strings and
serialized with json. User ext source and user is found by mathing this hashes.
If not even one hash can be created, user will be redirected to error page.
If user is not found, he will be redirected to registration page.

This microservice does not update the user in Perun with new values. To update save
freshly computed values for the
current user, you need to run `update_user_ext_source` microservice.

[RFC - eduTEAMS Identifier Generation](https://docs.google.com/document/d/1UwnEnzFG6SM9cv6gx1AsjDXw09ZkUmkyl-NqcXg0OVo/edit#heading=h.y5g6a74d5ukn) <br/>
Differences between our soulution and RFC:

- the selections are represented as list of list of attributes values serialized to JSON
- all identifiers are hashed by same hash function and with same salt
- The user’s home IdP entity-id does not need to be part of selection
- hashed values can be scoped but does not have to be

### Attributes

This Satosa microservice fetches user attributes by its names listed
as keys of `attrMap` config property and sets them as Attributes
values to keys specified as attrMap values. Old values of
Attributes are replaced.

It strongly relays on PerunIdentity microservice to obtain perun
user id. Configure it properly before using this microservice.

It offers two modes: PARTIAL and FULL, configurable via the `mode` setting in the config, with FULL being the default.
FULL mode includes all `attrMap` attributes, while PARTIAL mode includes them only if they're false/empty in both `attrMap` or given data.

### Entitlement

Calculates Perun user's entitlements by joining `eduPersonEntitlements`,
`forwardedEduPersonEntitlements`, resource capabilities and facility capabilities.

Without the `group_entitlement_disabled` attribute set, user's entitlements are
computed based on all user's groups on facility.

When `group_entitlement_disabled` is set, resources
which have this attribute set to `true` are excluded from the computation.
This means that for a group to be included in the computation,
it needs to be assigned through at least one resource without this attribute set to
`true`.

### Ensure member

This Satosa microservice checks member status of the user and calls registration if needed.
Register page is set in `config['register_url']`.

### Perun user

Registers a new perunuser endpoint which looks for user's credentials in external service defined by `config["proxy_extsource_name"]`.
Found user is registered and if the registration was successful, also loaded.

If a user wasn't found in the external system. Redirects user to a registration page if possible,
otherwise raises SATOSAError.

Registration page url is taken from config's `registration_page_url`. Failure to initiate registration results in unauthorized access.

### SP Authorization

Provides group based access control.

Without the `proxy_access_control_disabled` attribute set, this microservice denies access
to users who are not members of any group assigned to any resource on the current
facility.

If the `proxy_access_control_disabled` attribute is defined in config, resources which
have this attribute set to true are excluded. Groups assigned to these resources are
not counted towards user's groups on the current facility. This means, that the user
has to be a member of at least one group assigned to a resource without this
attribute set.

This feature allows computing entitlements while excluding groups which should not be
allowed to access the current service.

### Update user ext source

This microservice updates `userExtSource` attributes when the user logs in.

## Addons for SATOSA-oidcop frontend

### Userinfo perun updates

SATOSA by default caches user data in subsequent calls of the userinfo endpoint.
Thanks to this addon the data is loaded from Perun IDM on each call so they are always
up to date.

Requires a configuration for the entitlement microservice in `/etc/satosa/plugins/microservices/perun_entitlement_idm.yaml`.

How to use:

1. add this to the configuration file of satosa-oidcop frontend, under the key `add_on`:

   ```yaml
   userinfo_perun_updates:
     function: satosacontrib.perun.addons.userinfo_perun_updates.add_support
     kwargs: {}
   ```

### Extended introspection response

Implements [RFC 9470](https://datatracker.ietf.org/doc/rfc9470/)
which states that two attributes(acr and auth_time) should be in introspection endpoint. This addon gets them from session manager.

How to use:

1. add this to the configuration file of satosa-oidcop frontend, under the key `add_on`:

   ```yaml
   extended_introspection_response:
     function: satosacontrib.perun.addons.extended_introspection_response.add_support
     kwargs: {}
   ```
