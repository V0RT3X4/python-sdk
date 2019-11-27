# VortexaSDK

[![CircleCI](https://circleci.com/gh/V0RT3X4/python-sdk.svg?style=svg)](https://circleci.com/gh/V0RT3X4/python-sdk)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

The VortexaSDK is Vortexa's Software Development Kit (SDK) for Python, which allows
Data Scientists, Analysts and Developers to query [Vortexa's API](https://docs.vortexa.com)



## Quick Start

##### Installation

```bash
$ pip install vortexasdk
```

##### Authentication

Set your `VORTEXA_API_KEY` environment variable, that's all.

Refer to [Vortexa API Authentication](https://docs.vortexa.com/reference/intro-authentication)
 for more details, including instructions on where to find your API key.

##### Example

```python
>>> from datetime import datetime
>>> from vortexasdk import CargoMovements
>>> df = CargoMovements()\
        .search(filter_activity='loading_state',
            filter_time_min=datetime(2017, 8, 1, 23),
            filter_time_max=datetime(2017, 8, 1, 23))\
        .to_df()
```
returns

|    |   quantity | vessels.0.name   | product.group.label   | product.grade.label   | events.cargo_port_load_event.0.end_timestamp   | events.cargo_port_unload_event.0.start_timestamp   |
|---:|-----------:|:-----------------|:----------------------|:----------------------|:-----------------------------------------------|:---------------------------------------------------|
|  0 |       1998 | ALSIA SWAN       | Clean products        | Lube Oils             | 2017-08-01T06:10:45+0000                       | 2017-08-27T14:38:15+0000                           |
|  1 |      16559 | IVER AMBITION    | Dirty products        | nan                   | 2017-08-02T17:20:51+0000                       | 2017-09-07T07:52:20+0000                           |
|  2 |     522288 | BLUE SUN         | Crude                 | Gharib                | 2017-08-02T04:22:09+0000                       | 2017-08-13T10:32:09+0000                           |
|  3 |      46260 | XINWANYU16       | Clean products        | Chemicals             | 2017-08-01T01:07:40+0000                       | 2017-08-10T06:21:43+0000                           |


## Next Steps

Learn how to call [Endpoints](https://v0rt3x4.github.io/python-sdk/endpoints/about-endpoints/)

## Documentation

Read the documentation at [VortexaSDK Docs](https://v0rt3x4.github.io/python-sdk/)

## Contributing

We welcome contributions! Please read our [Contributing Guide](https://github.com/V0RT3X4/python-sdk/blob/master/CONTRIBUTING.md) for ways to offer feedback and contributions.

## Glossary

The Glossary can be found at [Vortexa API Documentation](https://docs.vortexa.com)

This outlines key terms, functions and assumptions aimed at
helping to extract powerful findings from our data.

