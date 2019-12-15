# VortexaSDK
[![All Contributors](https://img.shields.io/badge/all_contributors-12-orange.svg?style=flat-square)](#contributors)

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


## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore -->
<table>
  <tr>
    <td align="center"><a href="http://vortexa.com/"><img src="https://avatars1.githubusercontent.com/u/33626692?v=4" width="100px;" alt="Kit Burgess"/><br /><sub><b>Kit Burgess</b></sub></a><br /><a href="#design-KitBurgess" title="Design">🎨</a> <a href="https://github.com/V0RT3X4/python-sdk/commits?author=KitBurgess" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/cvonsteg"><img src="https://avatars2.githubusercontent.com/u/28671095?v=4" width="100px;" alt="tinovs"/><br /><sub><b>tinovs</b></sub></a><br /><a href="https://github.com/V0RT3X4/python-sdk/commits?author=cvonsteg" title="Code">💻</a> <a href="#review-cvonsteg" title="Reviewed Pull Requests">👀</a></td>
    <td align="center"><a href="http://star-www.st-and.ac.uk/~ds207/"><img src="https://avatars3.githubusercontent.com/u/11855684?v=4" width="100px;" alt="David Andrew Starkey"/><br /><sub><b>David Andrew Starkey</b></sub></a><br /><a href="https://github.com/V0RT3X4/python-sdk/commits?author=dstarkey23" title="Code">💻</a> <a href="https://github.com/V0RT3X4/python-sdk/commits?author=dstarkey23" title="Documentation">📖</a> <a href="#example-dstarkey23" title="Examples">💡</a></td>
    <td align="center"><a href="https://github.com/syed1992"><img src="https://avatars2.githubusercontent.com/u/45287337?v=4" width="100px;" alt="syed"/><br /><sub><b>syed</b></sub></a><br /><a href="#review-syed1992" title="Reviewed Pull Requests">👀</a></td>
    <td align="center"><a href="https://www.vortexa.com/"><img src="https://avatars0.githubusercontent.com/u/503380?v=4" width="100px;" alt="Jakub Korzeniowski"/><br /><sub><b>Jakub Korzeniowski</b></sub></a><br /><a href="#ideas-kujon" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/eadwright"><img src="https://avatars0.githubusercontent.com/u/17048626?v=4" width="100px;" alt="Edward Wright"/><br /><sub><b>Edward Wright</b></sub></a><br /><a href="#userTesting-eadwright" title="User Testing">📓</a></td>
    <td align="center"><a href="https://paddyroddy.github.io/"><img src="https://avatars3.githubusercontent.com/u/15052188?v=4" width="100px;" alt="Patrick Roddy"/><br /><sub><b>Patrick Roddy</b></sub></a><br /><a href="#userTesting-paddyroddy" title="User Testing">📓</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/rugg2"><img src="https://avatars3.githubusercontent.com/u/37453675?v=4" width="100px;" alt="Romain"/><br /><sub><b>Romain</b></sub></a><br /><a href="#userTesting-rugg2" title="User Testing">📓</a> <a href="#ideas-rugg2" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/Natday"><img src="https://avatars3.githubusercontent.com/u/38128493?v=4" width="100px;" alt="Natday"/><br /><sub><b>Natday</b></sub></a><br /><a href="#business-Natday" title="Business development">💼</a> <a href="#ideas-Natday" title="Ideas, Planning, & Feedback">🤔</a> <a href="#userTesting-Natday" title="User Testing">📓</a></td>
    <td align="center"><a href="https://github.com/ArthurD1"><img src="https://avatars0.githubusercontent.com/u/44548105?v=4" width="100px;" alt="ArthurD1"/><br /><sub><b>ArthurD1</b></sub></a><br /><a href="#userTesting-ArthurD1" title="User Testing">📓</a></td>
    <td align="center"><a href="https://github.com/ChloeConnor"><img src="https://avatars2.githubusercontent.com/u/42340891?v=4" width="100px;" alt="Chloe Connor"/><br /><sub><b>Chloe Connor</b></sub></a><br /><a href="#userTesting-ChloeConnor" title="User Testing">📓</a></td>
    <td align="center"><a href="https://www.vortexa.com/"><img src="https://avatars1.githubusercontent.com/u/31421156?v=4" width="100px;" alt="Achilleas Sfakianakis"/><br /><sub><b>Achilleas Sfakianakis</b></sub></a><br /><a href="#userTesting-asfakianakis" title="User Testing">📓</a></td>
  </tr>
</table>

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!