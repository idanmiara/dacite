# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [2.0b1] - 2022-11-28

### Added

- Add explicit `__all__` configuration
- Support [PEP 604] unions through `types.UnionType` #184
- numpy.typing.NDArray dataclass members #156
- Add `allow_missing_fields_as_none` option for missing fields #199
- Ability to customize `from_dict` per dataclass #122
- more general type hint for `type_hooks` #120
- Add Generic Hook Types #83
- Add stricter mypy type check flags #76

[PEP 604]: https://peps.python.org/pep-0604/

### Fixed

- Do not suppress `KeyError` in a type hook
- `from_dict` in case of frozen dataclass with non-init default #196
- empty tuple used for Sequence type #175
- Type_hooks not applied to InitVar fields #172
- extract_optional for Optional of Union. #164
- change Data from Dict to Mapping #159
- Fix encoding of PKG-INFO file #86

## [1.6.0] - 2020-11-30

### Added

- Support `Type` fields

### Fixed

- Handle generic collections with implicit `Any` inner types in Python 3.9
- Fix `InitVar` with inner data classes
- Improve support for fixed length and undefined length tuples

## [1.5.1] - 2020-07-03

### Added

- Python 3.9 support

## [1.5.0] - 2020-05-02

### Added

- Add `strict_unions_match` config parameter
- Support `Tuple`

### Fixed

- The order of run type hooks in `Union`  

## [1.4.0] - 2020-04-10

### Added

- Support `InitVar`

### Fixed 

- Fix `Union` type hooks

## [1.3.0] - 2020-03-14

### Added

- Support `Literal`
- Support [PEP 561](https://www.python.org/dev/peps/pep-0561/)

## [1.2.1] - 2020-03-02

### Fixed

- Fix problem with a "numeric tower" and optional/new type

## [1.2.0] - 2020-01-05

### Added

- Support base classes in `cast`
- Support collections in `cast`

### Changed

- Handle "numeric tower" as described in [PEP 484](https://www.python.org/dev/peps/pep-0484/#the-numeric-tower)

## [1.1.0] - 2019-11-27

### Added

- Python 3.8 support
- `cast` config parameter

### Changed

- Validate type for generic collection fields

[Unreleased]: https://github.com/konradhalas/dacite/compare/v1.6.0...HEAD
[1.6.0]: https://github.com/konradhalas/dacite/compare/v1.5.1...v1.6.0
[1.5.1]: https://github.com/konradhalas/dacite/compare/v1.5.0...v1.5.1
[1.5.0]: https://github.com/konradhalas/dacite/compare/v1.4.0...v1.5.0
[1.4.0]: https://github.com/konradhalas/dacite/compare/v1.3.0...v1.4.0
[1.3.0]: https://github.com/konradhalas/dacite/compare/v1.2.1...v1.3.0
[1.2.1]: https://github.com/konradhalas/dacite/compare/v1.2.0...v1.2.1
[1.2.0]: https://github.com/konradhalas/dacite/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/konradhalas/dacite/compare/v1.0.2...v1.1.0
