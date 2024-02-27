"""util functions for tests."""

import typing

from django.core import checks
from django.urls import URLPattern
from django.urls.resolvers import RoutePattern


# noinspection PyProtectedMember
def route_pattern_eql(route_pattern: RoutePattern, expected_route_pattern: RoutePattern) -> bool:
    """Compare two RoutePatterns.

    Args:
        route_pattern: The RoutePattern to compare.
        expected_route_pattern: The expected RoutePattern.

    Returns:
         True if the RoutePatterns are equal, False otherwise.
    """
    return (
        route_pattern._route == expected_route_pattern._route
        and route_pattern._is_endpoint == expected_route_pattern._is_endpoint
    )


def url_pattern_eql(urlpatterns: URLPattern, expected_urlpatterns: URLPattern) -> bool:
    """Compare two URLPatterns.

    Args:
        urlpatterns: The URLPattern to compare.
        expected_urlpatterns: The expected URLPattern.

    Returns:
         True if the URLPatterns are equal, False otherwise.

    """
    return (
        urlpatterns.callback == expected_urlpatterns.callback
        and urlpatterns.default_args == expected_urlpatterns.default_args
        and route_pattern_eql(urlpatterns.pattern, expected_urlpatterns.pattern)
    )


def error_eql(
    error: typing.Union[checks.Error, checks.Warning], expected_error: typing.Union[checks.Error, checks.Warning]
) -> bool:
    """Compare two Error objects.

    Args:
        error: The Error to compare.
        expected_error: The expected Error.

    Returns:
        True if the Error objects are equal, False otherwise.
    """
    if isinstance(error.obj, URLPattern) and isinstance(expected_error.obj, URLPattern):
        obj_equal = url_pattern_eql(error.obj, expected_error.obj)
    elif isinstance(error.obj, type) and isinstance(expected_error.obj, type):
        obj_equal = error.obj == expected_error.obj
    else:
        obj_equal = False
    return (
        error.msg == expected_error.msg
        and error.hint == expected_error.hint
        and error.id == expected_error.id
        and obj_equal
    )
