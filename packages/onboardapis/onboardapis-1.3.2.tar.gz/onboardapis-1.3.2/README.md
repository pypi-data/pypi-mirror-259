# onboardapis

[![PyPI-Versions](https://img.shields.io/pypi/pyversions/onboardapis)](https://pypi.org/project/onboardapis)
[![PyPI version](https://badge.fury.io/py/onboardapis.svg)](https://pypi.org/project/onboardapis)
[![build](https://img.shields.io/github/workflow/status/felix-zenk/onboardapis/publish-to-pypi)](https://github.com/felix-zenk/onboardapis)
[![Documentation](https://img.shields.io/readthedocs/onboardapis)](https://onboardapis.readthedocs.io/en/latest/)
[![License](https://img.shields.io/github/license/felix-zenk/onboardapis)](https://github.com/felix-zenk/onboardapis/blob/main/LICENSE)

## Description

onboardapis allows you to interact with different on-board APIs.
You can connect to the WI-FI of a supported transportation provider
and access information about your journey, the vehicle you are travelling in and much more.

> **Note:** Coverage across operators is not great yet.

> **Note:** For now the only vehicle type covered by this package is trains.

> **Note:** At the time this package supports the DB ICE Portal from germany and the ÖBB Railnet Regio from austria.

---

## Installation

Install the latest version of onboardapis from [PyPI](https://pypi.org/project/onboardapis) using [pip](https://pip.pypa.io/en/stable/installation/):

```shell
$ python -m pip install onboardapis
```

---

## Quickstart

To begin with development you will need to know a few things first:

* What vehicle type you want to use
* Who operates the vehicle
* What country is the operator from

With this information you can get the needed module from the package 
``onboardapis.<vehicle-type>.<country>.<operator>`` 
and import the API wrapper class from it.

Let's say you want to use the on-board API called ICE Portal of Deutsche Bahn trains in Germany.

```python
from onboardapis.trains.germany.db import ICEPortal
```

Every implementation of an API wrapper class is a subclass of the abstract class of its vehicle type
(here ``Train``) found in the vehicle package. Every vehicle type itself is a subclass of ``Vehicle``.

```python
from onboardapis import Vehicle
from onboardapis.trains import Train
from onboardapis.trains.germany.db import ICEPortal

assert issubclass(Train, Vehicle)
assert issubclass(ICEPortal, Train)
assert issubclass(ICEPortal, Vehicle)

assert isinstance(ICEPortal(), Train)
assert isinstance(ICEPortal(), Vehicle)
```

The abstract base class defines common attributes that are used by all implementations.

For example, the ``Train`` class defines the attributes ``speed`` and ``delay`` alongside with the ``current station``
(the next station you will arrive at) and others.

```python
from onboardapis.trains.germany.db import ICEPortal
from onboardapis.utils.conversions import ms_to_kmh

train = ICEPortal()
train.init()

print(
    "Travelling at", train.speed, "m/s",
    f"({ms_to_kmh(train.speed):.2f} km/h)",
    "with a delay of", train.delay, "seconds"
)

print(
    "Next stop:", train.current_station.name, 
    "at", train.current_station.arrival.actual.strftime("%H:%M")
)

print(
    f"Distance to {train.current_station.name}:",
    f"{train.calculate_distance(train.current_station) / 1000:.1f} km"
)
```

And there you go!
You can read more information about available attributes in the [trains documentation](https://onboardapis.readthedocs.io/en/latest/source/onboardapis.trains.html).

---

## Documentation
[![Documentation](https://img.shields.io/readthedocs/onboardapis)](https://onboardapis.readthedocs.io/en/latest/)

[ReadTheDocs](https://onboardapis.readthedocs.io/en/latest/)
