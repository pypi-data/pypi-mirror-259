# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200909

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias
from services.sch.src.oci_cli_sch.generated import sch_service_cli


@click.command(cli_util.override('connector_plugins.connector_plugins_root_group.command_name', 'connector-plugins'), cls=CommandGroupWithAlias, help=cli_util.override('connector_plugins.connector_plugins_root_group.help', """Use the Connector Hub API to transfer data between services in Oracle Cloud Infrastructure.
For more information about Connector Hub, see
[the Connector Hub documentation].
Connector Hub is formerly known as Service Connector Hub."""), short_help=cli_util.override('connector_plugins.connector_plugins_root_group.short_help', """Connector Hub API"""))
@cli_util.help_option_group
def connector_plugins_root_group():
    pass


@click.command(cli_util.override('connector_plugins.connector_plugin_summary_group.command_name', 'connector-plugin-summary'), cls=CommandGroupWithAlias, help="""Summary information for a connector plugin. Example connector plugins include the Streaming source and the Notifications target. For more information about flows defined by connectors, see [Overview of Connector Hub]. For configuration instructions, see [Creating a Connector].""")
@cli_util.help_option_group
def connector_plugin_summary_group():
    pass


@click.command(cli_util.override('connector_plugins.connector_plugin_group.command_name', 'connector-plugin'), cls=CommandGroupWithAlias, help="""A service source or service target used to create a connector. Example connector plugins include the Queue source and the Notifications target. For more information about flows defined by connectors, see [Overview of Connector Hub]. For configuration instructions, see [Creating a Connector].""")
@cli_util.help_option_group
def connector_plugin_group():
    pass


sch_service_cli.sch_service_group.add_command(connector_plugins_root_group)
connector_plugins_root_group.add_command(connector_plugin_summary_group)
connector_plugins_root_group.add_command(connector_plugin_group)


@connector_plugin_group.command(name=cli_util.override('connector_plugins.get_connector_plugin.command_name', 'get'), help=u"""Gets the specified connector plugin configuration information. \n[Command Reference](getConnectorPlugin)""")
@cli_util.option('--connector-plugin-name', required=True, help=u"""The name of the connector plugin. This name indicates the service to be called by the connector plugin. For example, `QueueSource` indicates the Queue service.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'sch', 'class': 'ConnectorPlugin'})
@cli_util.wrap_exceptions
def get_connector_plugin(ctx, from_json, connector_plugin_name):

    if isinstance(connector_plugin_name, six.string_types) and len(connector_plugin_name.strip()) == 0:
        raise click.UsageError('Parameter --connector-plugin-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('sch', 'connector_plugins', ctx)
    result = client.get_connector_plugin(
        connector_plugin_name=connector_plugin_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connector_plugin_summary_group.command(name=cli_util.override('connector_plugins.list_connector_plugins.command_name', 'list-connector-plugins'), help=u"""Lists connector plugins according to the specified filter. \n[Command Reference](listConnectorPlugins)""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only resources that match the given lifecycle state.

Example: `ACTIVE`""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the given display name exactly.

Example: `example_service_connector`""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the given connector plugin name ignoring case.

Example: `QueueSource`""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--page', help=u"""For list pagination. The value of the opc-next-page response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for `timeCreated` is descending. Default order for `displayName` is ascending. If no value is specified `timeCreated` is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'sch', 'class': 'ConnectorPluginCollection'})
@cli_util.wrap_exceptions
def list_connector_plugins(ctx, from_json, all_pages, page_size, lifecycle_state, display_name, name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if name is not None:
        kwargs['name'] = name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('sch', 'connector_plugins', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_connector_plugins,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_connector_plugins,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_connector_plugins(
            **kwargs
        )
    cli_util.render_response(result, ctx)
