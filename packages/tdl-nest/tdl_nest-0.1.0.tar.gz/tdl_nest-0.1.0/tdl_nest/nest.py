from typing import Any, Callable, Iterator, List, Tuple

NEST_TYPES = {dict, list, tuple}


def nest_iter(inputs: Any) -> Iterator:
    '''Iterate through nested dict, list, and/or tuples'''
    if isinstance(inputs, (list, tuple)):
        for vi in inputs:
            yield from nest_iter(vi)
    elif isinstance(inputs, dict):
        for vi in inputs.values():
            yield from nest_iter(vi)
    else:
        yield inputs


def nest_map(inputs: Any, map_fn: Callable) -> Any:
    '''Compute function across nested structure'''
    if isinstance(inputs, (list, tuple)):
        return type(inputs)(
            nest_map(vi, map_fn=map_fn)
            for vi in inputs
        )
    elif isinstance(inputs, dict):
        return type(inputs)({
            ki: nest_map(vi, map_fn=map_fn)
            for ki, vi in inputs.items()
        })
    else:
        return map_fn(inputs)


def nest_spec(inputs: Any) -> Any:
    '''Get the specs of the nested inputs'''
    return nest_map(inputs, lambda x: None)


def nest_flatten(inputs: Any) -> List:
    '''flatten the nested structure in a list'''
    return list(nest_iter(inputs))


def nest_unflatten(inputs: List | Tuple, spec: Any) -> Any:
    '''re-arange inputs as nested structure'''
    flatten = [vi for vi in inputs]
    return nest_map(spec, lambda x: flatten.pop(0))
