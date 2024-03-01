## Overview
A python module to deal with modified semantic versioning.

### Motivation
There are three numbers as main part of a version in semantic version ([semver.org](https://semver.org)). Third number, patch, is defined as:
> PATCH version when you make backward compatible bug fixes

However, sometimes we need to distinguish two types of a bugfix.
1. bugfix which is released in a standard way
1. bugfix which has to be release immidiately as hotfix

The first type is released in a standard release process and at the end the patch of a version is increased.

The second one is the case we identified a bug which has to be fixed and released immidiately. In this case, a version witch increased patch can potentially already exists as any sort of pre-release version.
<br>Let's assume there is version *0.4.2* deployed in production. Versions *0.4.3-rc* and *0.4.4-rc* already exist in our non prod environment but they are not ready to be released. The question is what version should have fixed code. If we want to increase patch we would have to jump to *0.4.5* which may (and will) brings confusion in the versioning.

### Fix version part
To solve to the scenario described above, we introduce 4th number to main version part. Let's call it fix version and define it as:
> FIX version when you make hot fixes released immidiately

So the new version in the described scenario would be *0.4.2.1*

At the end, the modification means only the one number.

## Usage
```python
from semver4 import Version


version = Version(major=2, minor=4, path=4, prerelease='beta')
print(version)
# '2.4.4-beta'
print(version.minor)
# 4

version > Version('0.4.2.4')
# True

version.inc_fix()
print(version)
# '2.4.4.1-beta'
print(version.fix)
# 1

version.inc_minor().inc_major().dec_patch()
print(version)
# '3.5.3.1-beta'
```

## Known limitations
- Comparing of two Versions only by major, minor, patch and fix. Prerelease and build do not affect any comparison operation.
- pre release and build metadata parts can not be modified