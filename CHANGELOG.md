# Changelog

## [0.8.3](https://github.com/V0RT3X4/python-sdk/tree/0.8.3) (2019-11-27)

[Full Changelog](https://github.com/V0RT3X4/python-sdk/compare/0.8.2...0.8.3)

**Fixed bugs:**

- IDLayer class has attributes `name` instead of `layer` [\#70](https://github.com/V0RT3X4/python-sdk/issues/70)

**Closed issues:**

- Geographies document reference method. [\#66](https://github.com/V0RT3X4/python-sdk/issues/66)
- Improved logging to make sure the right entity is selected in a query \(or at least make it clear to user what entity is being used\) [\#37](https://github.com/V0RT3X4/python-sdk/issues/37)
- Contributing to VortexaSDK: Setting up environment bug `pip install -e .\[test\]` [\#25](https://github.com/V0RT3X4/python-sdk/issues/25)

**Merged pull requests:**

- feat: Log searches [\#93](https://github.com/V0RT3X4/python-sdk/pull/93) ([KitBurgess](https://github.com/KitBurgess))

## [0.8.2](https://github.com/V0RT3X4/python-sdk/tree/0.8.2) (2019-11-26)

[Full Changelog](https://github.com/V0RT3X4/python-sdk/compare/0.8.1...0.8.2)

## [0.8.1](https://github.com/V0RT3X4/python-sdk/tree/0.8.1) (2019-11-26)

[Full Changelog](https://github.com/V0RT3X4/python-sdk/compare/0.8.0...0.8.1)

## [0.8.0](https://github.com/V0RT3X4/python-sdk/tree/0.8.0) (2019-11-26)

[Full Changelog](https://github.com/V0RT3X4/python-sdk/compare/0.7.0...0.8.0)

**Implemented enhancements:**

- filter\_time\_min and filter\_time\_max parameters should be python datetime objects [\#45](https://github.com/V0RT3X4/python-sdk/issues/45)

**Merged pull requests:**

- feat: Use datetime type as time argument, closes \#45 [\#92](https://github.com/V0RT3X4/python-sdk/pull/92) ([KitBurgess](https://github.com/KitBurgess))
- feat: Add vessel movements endpoint [\#63](https://github.com/V0RT3X4/python-sdk/pull/63) ([KitBurgess](https://github.com/KitBurgess))

## [0.7.0](https://github.com/V0RT3X4/python-sdk/tree/0.7.0) (2019-11-26)

[Full Changelog](https://github.com/V0RT3X4/python-sdk/compare/0.6.1...0.7.0)

**Closed issues:**

- Where do I get an API key from [\#75](https://github.com/V0RT3X4/python-sdk/issues/75)
- change 'filter\_vessel' argument to 'filter\_vessel\_name' to make it clearer that this is filtering vessels and not vessel classes [\#38](https://github.com/V0RT3X4/python-sdk/issues/38)

**Merged pull requests:**

- feat: Filter cargo movements on vessel class, closes \#38 [\#91](https://github.com/V0RT3X4/python-sdk/pull/91) ([KitBurgess](https://github.com/KitBurgess))

## [0.6.1](https://github.com/V0RT3X4/python-sdk/tree/0.6.1) (2019-11-25)

[Full Changelog](https://github.com/V0RT3X4/python-sdk/compare/0.6.0...0.6.1)

**Implemented enhancements:**

- Add DataFrame example to all endpoints [\#58](https://github.com/V0RT3X4/python-sdk/issues/58)

**Fixed bugs:**

- CargoMovements filter\_activity illegal state [\#71](https://github.com/V0RT3X4/python-sdk/issues/71)

**Closed issues:**

- Bounding box is lon/lat not lat/lon [\#88](https://github.com/V0RT3X4/python-sdk/issues/88)
- Add instructions on how to install pre-commit hooks. [\#86](https://github.com/V0RT3X4/python-sdk/issues/86)
- Show Dataframe result in main README example [\#78](https://github.com/V0RT3X4/python-sdk/issues/78)
- Fix broken docs links [\#77](https://github.com/V0RT3X4/python-sdk/issues/77)
- List available vessel classes [\#73](https://github.com/V0RT3X4/python-sdk/issues/73)

**Merged pull requests:**

- fix: rename IDLayer attribute [\#90](https://github.com/V0RT3X4/python-sdk/pull/90) ([cvonsteg](https://github.com/cvonsteg))
- Incorporate features / requests from SDK battletesting [\#89](https://github.com/V0RT3X4/python-sdk/pull/89) ([KitBurgess](https://github.com/KitBurgess))

## [0.6.0](https://github.com/V0RT3X4/python-sdk/tree/0.6.0) (2019-11-22)

[Full Changelog](https://github.com/V0RT3X4/python-sdk/compare/0.5.0...0.6.0)

**Closed issues:**

- Add Charterers `to\_df` endpoint. [\#34](https://github.com/V0RT3X4/python-sdk/issues/34)

**Merged pull requests:**

- feat: Flatten columns in product result [\#62](https://github.com/V0RT3X4/python-sdk/pull/62) ([KitBurgess](https://github.com/KitBurgess))
- Serde mixin [\#61](https://github.com/V0RT3X4/python-sdk/pull/61) ([KitBurgess](https://github.com/KitBurgess))

## [0.5.0](https://github.com/V0RT3X4/python-sdk/tree/0.5.0) (2019-11-21)

[Full Changelog](https://github.com/V0RT3X4/python-sdk/compare/0.4.3...0.5.0)

**Closed issues:**

- Test SDK against different python versions [\#53](https://github.com/V0RT3X4/python-sdk/issues/53)

**Merged pull requests:**

- Bulk out Corporations endpoint [\#60](https://github.com/V0RT3X4/python-sdk/pull/60) ([KitBurgess](https://github.com/KitBurgess))

## [0.4.3](https://github.com/V0RT3X4/python-sdk/tree/0.4.3) (2019-11-20)

[Full Changelog](https://github.com/V0RT3X4/python-sdk/compare/0.3.4-alpha...0.4.3)

**Implemented enhancements:**

- add a list of available columns in the SDK documents [\#40](https://github.com/V0RT3X4/python-sdk/issues/40)

**Closed issues:**

- include an explanation in the docs of the flattened cargo movement structure and how this links to the column naming convention [\#48](https://github.com/V0RT3X4/python-sdk/issues/48)
- make 'filter\_activity' a required argument [\#43](https://github.com/V0RT3X4/python-sdk/issues/43)
- How to serve docs isn't clear, which directory from? [\#20](https://github.com/V0RT3X4/python-sdk/issues/20)
- unclear how to import the different endpoints [\#19](https://github.com/V0RT3X4/python-sdk/issues/19)

**Merged pull requests:**

- docs: Make it clearer how to import endpoints, closes \#19 [\#57](https://github.com/V0RT3X4/python-sdk/pull/57) ([KitBurgess](https://github.com/KitBurgess))
- docs: Add about-endpoints explanation [\#55](https://github.com/V0RT3X4/python-sdk/pull/55) ([KitBurgess](https://github.com/KitBurgess))

## [0.3.4-alpha](https://github.com/V0RT3X4/python-sdk/tree/0.3.4-alpha) (2019-11-20)

[Full Changelog](https://github.com/V0RT3X4/python-sdk/compare/0.3.3...0.3.4-alpha)

## [0.3.3](https://github.com/V0RT3X4/python-sdk/tree/0.3.3) (2019-11-20)

[Full Changelog](https://github.com/V0RT3X4/python-sdk/compare/0.3.2...0.3.3)

## [0.3.2](https://github.com/V0RT3X4/python-sdk/tree/0.3.2) (2019-11-20)

[Full Changelog](https://github.com/V0RT3X4/python-sdk/compare/0.2.3...0.3.2)

**Implemented enhancements:**

- Allow for filtering by product name in vessel endpoint filters  [\#31](https://github.com/V0RT3X4/python-sdk/issues/31)

**Merged pull requests:**

- fix: Move to pytest, run mock setup before each test [\#52](https://github.com/V0RT3X4/python-sdk/pull/52) ([KitBurgess](https://github.com/KitBurgess))
- ci: Add git change log [\#51](https://github.com/V0RT3X4/python-sdk/pull/51) ([KitBurgess](https://github.com/KitBurgess))
- feat: Filter vessels using products name [\#50](https://github.com/V0RT3X4/python-sdk/pull/50) ([KitBurgess](https://github.com/KitBurgess))

## [0.2.3](https://github.com/V0RT3X4/python-sdk/tree/0.2.3) (2019-11-19)

[Full Changelog](https://github.com/V0RT3X4/python-sdk/compare/0.2.2...0.2.3)

## [0.2.2](https://github.com/V0RT3X4/python-sdk/tree/0.2.2) (2019-11-19)

[Full Changelog](https://github.com/V0RT3X4/python-sdk/compare/0.2.1...0.2.2)

**Implemented enhancements:**

- Create Products endpoint [\#7](https://github.com/V0RT3X4/python-sdk/issues/7)

**Fixed bugs:**

- Tried to pull out a reference df of all vessels but only got 200 results? [\#29](https://github.com/V0RT3X4/python-sdk/issues/29)

**Closed issues:**

- searching vessel reference database only ever gives me back 100 results [\#30](https://github.com/V0RT3X4/python-sdk/issues/30)

**Merged pull requests:**

- perf: Call API in parallel [\#44](https://github.com/V0RT3X4/python-sdk/pull/44) ([KitBurgess](https://github.com/KitBurgess))

## [0.2.1](https://github.com/V0RT3X4/python-sdk/tree/0.2.1) (2019-11-18)

[Full Changelog](https://github.com/V0RT3X4/python-sdk/compare/0.2.0...0.2.1)

**Closed issues:**

- filter arguments for origins/destinations must be passed as vortexa ids \(a user will not know what our ID's are\) [\#17](https://github.com/V0RT3X4/python-sdk/issues/17)

**Merged pull requests:**

- fix: Return all vessels from search, not just arbitrary 100 [\#41](https://github.com/V0RT3X4/python-sdk/pull/41) ([KitBurgess](https://github.com/KitBurgess))
- style: Remove status token from README [\#32](https://github.com/V0RT3X4/python-sdk/pull/32) ([KitBurgess](https://github.com/KitBurgess))
- Products endpoint test [\#11](https://github.com/V0RT3X4/python-sdk/pull/11) ([dstarkey23](https://github.com/dstarkey23))

## [0.2.0](https://github.com/V0RT3X4/python-sdk/tree/0.2.0) (2019-11-18)

[Full Changelog](https://github.com/V0RT3X4/python-sdk/compare/0.1.0...0.2.0)

**Closed issues:**

- Importing entities does not work \(or maybe im doing this wrong\)? [\#18](https://github.com/V0RT3X4/python-sdk/issues/18)
- filter arguments must be passed in array form \(this is not made clear to the user\) [\#16](https://github.com/V0RT3X4/python-sdk/issues/16)

**Merged pull requests:**

- test: Fix global client state [\#28](https://github.com/V0RT3X4/python-sdk/pull/28) ([KitBurgess](https://github.com/KitBurgess))
- Filter on name [\#27](https://github.com/V0RT3X4/python-sdk/pull/27) ([KitBurgess](https://github.com/KitBurgess))
- Run tests against live API in circle ci [\#26](https://github.com/V0RT3X4/python-sdk/pull/26) ([KitBurgess](https://github.com/KitBurgess))
- Revert "ci: Run live tests in circleci" [\#24](https://github.com/V0RT3X4/python-sdk/pull/24) ([KitBurgess](https://github.com/KitBurgess))
- test: Correctly set client in tests [\#23](https://github.com/V0RT3X4/python-sdk/pull/23) ([KitBurgess](https://github.com/KitBurgess))
- ci: Run live tests in circleci [\#22](https://github.com/V0RT3X4/python-sdk/pull/22) ([KitBurgess](https://github.com/KitBurgess))
- feat: Allow user to search cargo movements with single filter, fixes \#16 [\#21](https://github.com/V0RT3X4/python-sdk/pull/21) ([KitBurgess](https://github.com/KitBurgess))

## [0.1.0](https://github.com/V0RT3X4/python-sdk/tree/0.1.0) (2019-11-13)

[Full Changelog](https://github.com/V0RT3X4/python-sdk/compare/f34a5627d0047e9a9a56ecf4b19cb4af91395d01...0.1.0)

**Merged pull requests:**

- ci: Add export packages [\#15](https://github.com/V0RT3X4/python-sdk/pull/15) ([KitBurgess](https://github.com/KitBurgess))
- docs: Add tips to contributing docs [\#13](https://github.com/V0RT3X4/python-sdk/pull/13) ([KitBurgess](https://github.com/KitBurgess))
- refactor: Rename root dir from vortexa to vortexasdk [\#12](https://github.com/V0RT3X4/python-sdk/pull/12) ([KitBurgess](https://github.com/KitBurgess))
- docs: Improve the contributing guide [\#9](https://github.com/V0RT3X4/python-sdk/pull/9) ([KitBurgess](https://github.com/KitBurgess))
- refactor: Allow clients to import classes without knowledge of internals [\#8](https://github.com/V0RT3X4/python-sdk/pull/8) ([KitBurgess](https://github.com/KitBurgess))
- docs: Add quickstart to docs [\#5](https://github.com/V0RT3X4/python-sdk/pull/5) ([KitBurgess](https://github.com/KitBurgess))
- ci: Create the setup.py file [\#4](https://github.com/V0RT3X4/python-sdk/pull/4) ([KitBurgess](https://github.com/KitBurgess))
- test: Vessel dataframe test actually does something [\#3](https://github.com/V0RT3X4/python-sdk/pull/3) ([KitBurgess](https://github.com/KitBurgess))
- Consistent types [\#2](https://github.com/V0RT3X4/python-sdk/pull/2) ([KitBurgess](https://github.com/KitBurgess))



\* *This Changelog was automatically generated by [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator)*
