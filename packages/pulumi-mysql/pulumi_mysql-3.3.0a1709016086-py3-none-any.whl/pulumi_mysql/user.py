# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['UserArgs', 'User']

@pulumi.input_type
class UserArgs:
    def __init__(__self__, *,
                 user: pulumi.Input[str],
                 auth_plugin: Optional[pulumi.Input[str]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 plaintext_password: Optional[pulumi.Input[str]] = None,
                 tls_option: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a User resource.
        :param pulumi.Input[str] user: The name of the user.
        :param pulumi.Input[str] auth_plugin: Use an [authentication plugin][ref-auth-plugins] to authenticate the user instead of using password authentication.  Description of the fields allowed in the block below. Conflicts with `password` and `plaintext_password`.
        :param pulumi.Input[str] host: The source host of the user. Defaults to "localhost".
        :param pulumi.Input[str] password: Deprecated alias of `plaintext_password`, whose value is *stored as plaintext in state*. Prefer to use `plaintext_password` instead, which stores the password as an unsalted hash. Conflicts with `auth_plugin`.
        :param pulumi.Input[str] plaintext_password: The password for the user. This must be provided in plain text, so the data source for it must be secured. An _unsalted_ hash of the provided password is stored in state. Conflicts with `auth_plugin`.
        :param pulumi.Input[str] tls_option: An TLS-Option for the `CREATE USER` or `ALTER USER` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `CREATE USER ... REQUIRE SSL` statement. See the [MYSQL `CREATE USER` documentation](https://dev.mysql.com/doc/refman/5.7/en/create-user.html) for more. Ignored if MySQL version is under 5.7.0.
               
               [ref-auth-plugins]: https://dev.mysql.com/doc/refman/5.7/en/authentication-plugins.html
        """
        pulumi.set(__self__, "user", user)
        if auth_plugin is not None:
            pulumi.set(__self__, "auth_plugin", auth_plugin)
        if host is not None:
            pulumi.set(__self__, "host", host)
        if password is not None:
            warnings.warn("""Please use plaintext_password instead""", DeprecationWarning)
            pulumi.log.warn("""password is deprecated: Please use plaintext_password instead""")
        if password is not None:
            pulumi.set(__self__, "password", password)
        if plaintext_password is not None:
            pulumi.set(__self__, "plaintext_password", plaintext_password)
        if tls_option is not None:
            pulumi.set(__self__, "tls_option", tls_option)

    @property
    @pulumi.getter
    def user(self) -> pulumi.Input[str]:
        """
        The name of the user.
        """
        return pulumi.get(self, "user")

    @user.setter
    def user(self, value: pulumi.Input[str]):
        pulumi.set(self, "user", value)

    @property
    @pulumi.getter(name="authPlugin")
    def auth_plugin(self) -> Optional[pulumi.Input[str]]:
        """
        Use an [authentication plugin][ref-auth-plugins] to authenticate the user instead of using password authentication.  Description of the fields allowed in the block below. Conflicts with `password` and `plaintext_password`.
        """
        return pulumi.get(self, "auth_plugin")

    @auth_plugin.setter
    def auth_plugin(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auth_plugin", value)

    @property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[str]]:
        """
        The source host of the user. Defaults to "localhost".
        """
        return pulumi.get(self, "host")

    @host.setter
    def host(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        Deprecated alias of `plaintext_password`, whose value is *stored as plaintext in state*. Prefer to use `plaintext_password` instead, which stores the password as an unsalted hash. Conflicts with `auth_plugin`.
        """
        warnings.warn("""Please use plaintext_password instead""", DeprecationWarning)
        pulumi.log.warn("""password is deprecated: Please use plaintext_password instead""")

        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter(name="plaintextPassword")
    def plaintext_password(self) -> Optional[pulumi.Input[str]]:
        """
        The password for the user. This must be provided in plain text, so the data source for it must be secured. An _unsalted_ hash of the provided password is stored in state. Conflicts with `auth_plugin`.
        """
        return pulumi.get(self, "plaintext_password")

    @plaintext_password.setter
    def plaintext_password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "plaintext_password", value)

    @property
    @pulumi.getter(name="tlsOption")
    def tls_option(self) -> Optional[pulumi.Input[str]]:
        """
        An TLS-Option for the `CREATE USER` or `ALTER USER` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `CREATE USER ... REQUIRE SSL` statement. See the [MYSQL `CREATE USER` documentation](https://dev.mysql.com/doc/refman/5.7/en/create-user.html) for more. Ignored if MySQL version is under 5.7.0.

        [ref-auth-plugins]: https://dev.mysql.com/doc/refman/5.7/en/authentication-plugins.html
        """
        return pulumi.get(self, "tls_option")

    @tls_option.setter
    def tls_option(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tls_option", value)


@pulumi.input_type
class _UserState:
    def __init__(__self__, *,
                 auth_plugin: Optional[pulumi.Input[str]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 plaintext_password: Optional[pulumi.Input[str]] = None,
                 tls_option: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering User resources.
        :param pulumi.Input[str] auth_plugin: Use an [authentication plugin][ref-auth-plugins] to authenticate the user instead of using password authentication.  Description of the fields allowed in the block below. Conflicts with `password` and `plaintext_password`.
        :param pulumi.Input[str] host: The source host of the user. Defaults to "localhost".
        :param pulumi.Input[str] password: Deprecated alias of `plaintext_password`, whose value is *stored as plaintext in state*. Prefer to use `plaintext_password` instead, which stores the password as an unsalted hash. Conflicts with `auth_plugin`.
        :param pulumi.Input[str] plaintext_password: The password for the user. This must be provided in plain text, so the data source for it must be secured. An _unsalted_ hash of the provided password is stored in state. Conflicts with `auth_plugin`.
        :param pulumi.Input[str] tls_option: An TLS-Option for the `CREATE USER` or `ALTER USER` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `CREATE USER ... REQUIRE SSL` statement. See the [MYSQL `CREATE USER` documentation](https://dev.mysql.com/doc/refman/5.7/en/create-user.html) for more. Ignored if MySQL version is under 5.7.0.
               
               [ref-auth-plugins]: https://dev.mysql.com/doc/refman/5.7/en/authentication-plugins.html
        :param pulumi.Input[str] user: The name of the user.
        """
        if auth_plugin is not None:
            pulumi.set(__self__, "auth_plugin", auth_plugin)
        if host is not None:
            pulumi.set(__self__, "host", host)
        if password is not None:
            warnings.warn("""Please use plaintext_password instead""", DeprecationWarning)
            pulumi.log.warn("""password is deprecated: Please use plaintext_password instead""")
        if password is not None:
            pulumi.set(__self__, "password", password)
        if plaintext_password is not None:
            pulumi.set(__self__, "plaintext_password", plaintext_password)
        if tls_option is not None:
            pulumi.set(__self__, "tls_option", tls_option)
        if user is not None:
            pulumi.set(__self__, "user", user)

    @property
    @pulumi.getter(name="authPlugin")
    def auth_plugin(self) -> Optional[pulumi.Input[str]]:
        """
        Use an [authentication plugin][ref-auth-plugins] to authenticate the user instead of using password authentication.  Description of the fields allowed in the block below. Conflicts with `password` and `plaintext_password`.
        """
        return pulumi.get(self, "auth_plugin")

    @auth_plugin.setter
    def auth_plugin(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auth_plugin", value)

    @property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[str]]:
        """
        The source host of the user. Defaults to "localhost".
        """
        return pulumi.get(self, "host")

    @host.setter
    def host(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        Deprecated alias of `plaintext_password`, whose value is *stored as plaintext in state*. Prefer to use `plaintext_password` instead, which stores the password as an unsalted hash. Conflicts with `auth_plugin`.
        """
        warnings.warn("""Please use plaintext_password instead""", DeprecationWarning)
        pulumi.log.warn("""password is deprecated: Please use plaintext_password instead""")

        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter(name="plaintextPassword")
    def plaintext_password(self) -> Optional[pulumi.Input[str]]:
        """
        The password for the user. This must be provided in plain text, so the data source for it must be secured. An _unsalted_ hash of the provided password is stored in state. Conflicts with `auth_plugin`.
        """
        return pulumi.get(self, "plaintext_password")

    @plaintext_password.setter
    def plaintext_password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "plaintext_password", value)

    @property
    @pulumi.getter(name="tlsOption")
    def tls_option(self) -> Optional[pulumi.Input[str]]:
        """
        An TLS-Option for the `CREATE USER` or `ALTER USER` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `CREATE USER ... REQUIRE SSL` statement. See the [MYSQL `CREATE USER` documentation](https://dev.mysql.com/doc/refman/5.7/en/create-user.html) for more. Ignored if MySQL version is under 5.7.0.

        [ref-auth-plugins]: https://dev.mysql.com/doc/refman/5.7/en/authentication-plugins.html
        """
        return pulumi.get(self, "tls_option")

    @tls_option.setter
    def tls_option(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tls_option", value)

    @property
    @pulumi.getter
    def user(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the user.
        """
        return pulumi.get(self, "user")

    @user.setter
    def user(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user", value)


class User(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_plugin: Optional[pulumi.Input[str]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 plaintext_password: Optional[pulumi.Input[str]] = None,
                 tls_option: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The ``User`` resource creates and manages a user on a MySQL
        server.

        ## Examples

        ### Basic Usage

        ```python
        import pulumi
        import pulumi_mysql as mysql

        jdoe = mysql.User("jdoe",
            host="example.com",
            plaintext_password="password",
            user="jdoe")
        ```

        ### Example Usage with an Authentication Plugin

        ```python
        import pulumi
        import pulumi_mysql as mysql

        nologin = mysql.User("nologin",
            auth_plugin="mysql_no_login",
            host="example.com",
            user="nologin")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] auth_plugin: Use an [authentication plugin][ref-auth-plugins] to authenticate the user instead of using password authentication.  Description of the fields allowed in the block below. Conflicts with `password` and `plaintext_password`.
        :param pulumi.Input[str] host: The source host of the user. Defaults to "localhost".
        :param pulumi.Input[str] password: Deprecated alias of `plaintext_password`, whose value is *stored as plaintext in state*. Prefer to use `plaintext_password` instead, which stores the password as an unsalted hash. Conflicts with `auth_plugin`.
        :param pulumi.Input[str] plaintext_password: The password for the user. This must be provided in plain text, so the data source for it must be secured. An _unsalted_ hash of the provided password is stored in state. Conflicts with `auth_plugin`.
        :param pulumi.Input[str] tls_option: An TLS-Option for the `CREATE USER` or `ALTER USER` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `CREATE USER ... REQUIRE SSL` statement. See the [MYSQL `CREATE USER` documentation](https://dev.mysql.com/doc/refman/5.7/en/create-user.html) for more. Ignored if MySQL version is under 5.7.0.
               
               [ref-auth-plugins]: https://dev.mysql.com/doc/refman/5.7/en/authentication-plugins.html
        :param pulumi.Input[str] user: The name of the user.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The ``User`` resource creates and manages a user on a MySQL
        server.

        ## Examples

        ### Basic Usage

        ```python
        import pulumi
        import pulumi_mysql as mysql

        jdoe = mysql.User("jdoe",
            host="example.com",
            plaintext_password="password",
            user="jdoe")
        ```

        ### Example Usage with an Authentication Plugin

        ```python
        import pulumi
        import pulumi_mysql as mysql

        nologin = mysql.User("nologin",
            auth_plugin="mysql_no_login",
            host="example.com",
            user="nologin")
        ```

        :param str resource_name: The name of the resource.
        :param UserArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_plugin: Optional[pulumi.Input[str]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 plaintext_password: Optional[pulumi.Input[str]] = None,
                 tls_option: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UserArgs.__new__(UserArgs)

            __props__.__dict__["auth_plugin"] = auth_plugin
            __props__.__dict__["host"] = host
            __props__.__dict__["password"] = None if password is None else pulumi.Output.secret(password)
            __props__.__dict__["plaintext_password"] = None if plaintext_password is None else pulumi.Output.secret(plaintext_password)
            __props__.__dict__["tls_option"] = tls_option
            if user is None and not opts.urn:
                raise TypeError("Missing required property 'user'")
            __props__.__dict__["user"] = user
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["password", "plaintextPassword"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(User, __self__).__init__(
            'mysql:index/user:User',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            auth_plugin: Optional[pulumi.Input[str]] = None,
            host: Optional[pulumi.Input[str]] = None,
            password: Optional[pulumi.Input[str]] = None,
            plaintext_password: Optional[pulumi.Input[str]] = None,
            tls_option: Optional[pulumi.Input[str]] = None,
            user: Optional[pulumi.Input[str]] = None) -> 'User':
        """
        Get an existing User resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] auth_plugin: Use an [authentication plugin][ref-auth-plugins] to authenticate the user instead of using password authentication.  Description of the fields allowed in the block below. Conflicts with `password` and `plaintext_password`.
        :param pulumi.Input[str] host: The source host of the user. Defaults to "localhost".
        :param pulumi.Input[str] password: Deprecated alias of `plaintext_password`, whose value is *stored as plaintext in state*. Prefer to use `plaintext_password` instead, which stores the password as an unsalted hash. Conflicts with `auth_plugin`.
        :param pulumi.Input[str] plaintext_password: The password for the user. This must be provided in plain text, so the data source for it must be secured. An _unsalted_ hash of the provided password is stored in state. Conflicts with `auth_plugin`.
        :param pulumi.Input[str] tls_option: An TLS-Option for the `CREATE USER` or `ALTER USER` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `CREATE USER ... REQUIRE SSL` statement. See the [MYSQL `CREATE USER` documentation](https://dev.mysql.com/doc/refman/5.7/en/create-user.html) for more. Ignored if MySQL version is under 5.7.0.
               
               [ref-auth-plugins]: https://dev.mysql.com/doc/refman/5.7/en/authentication-plugins.html
        :param pulumi.Input[str] user: The name of the user.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _UserState.__new__(_UserState)

        __props__.__dict__["auth_plugin"] = auth_plugin
        __props__.__dict__["host"] = host
        __props__.__dict__["password"] = password
        __props__.__dict__["plaintext_password"] = plaintext_password
        __props__.__dict__["tls_option"] = tls_option
        __props__.__dict__["user"] = user
        return User(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authPlugin")
    def auth_plugin(self) -> pulumi.Output[Optional[str]]:
        """
        Use an [authentication plugin][ref-auth-plugins] to authenticate the user instead of using password authentication.  Description of the fields allowed in the block below. Conflicts with `password` and `plaintext_password`.
        """
        return pulumi.get(self, "auth_plugin")

    @property
    @pulumi.getter
    def host(self) -> pulumi.Output[Optional[str]]:
        """
        The source host of the user. Defaults to "localhost".
        """
        return pulumi.get(self, "host")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[Optional[str]]:
        """
        Deprecated alias of `plaintext_password`, whose value is *stored as plaintext in state*. Prefer to use `plaintext_password` instead, which stores the password as an unsalted hash. Conflicts with `auth_plugin`.
        """
        warnings.warn("""Please use plaintext_password instead""", DeprecationWarning)
        pulumi.log.warn("""password is deprecated: Please use plaintext_password instead""")

        return pulumi.get(self, "password")

    @property
    @pulumi.getter(name="plaintextPassword")
    def plaintext_password(self) -> pulumi.Output[Optional[str]]:
        """
        The password for the user. This must be provided in plain text, so the data source for it must be secured. An _unsalted_ hash of the provided password is stored in state. Conflicts with `auth_plugin`.
        """
        return pulumi.get(self, "plaintext_password")

    @property
    @pulumi.getter(name="tlsOption")
    def tls_option(self) -> pulumi.Output[Optional[str]]:
        """
        An TLS-Option for the `CREATE USER` or `ALTER USER` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `CREATE USER ... REQUIRE SSL` statement. See the [MYSQL `CREATE USER` documentation](https://dev.mysql.com/doc/refman/5.7/en/create-user.html) for more. Ignored if MySQL version is under 5.7.0.

        [ref-auth-plugins]: https://dev.mysql.com/doc/refman/5.7/en/authentication-plugins.html
        """
        return pulumi.get(self, "tls_option")

    @property
    @pulumi.getter
    def user(self) -> pulumi.Output[str]:
        """
        The name of the user.
        """
        return pulumi.get(self, "user")

