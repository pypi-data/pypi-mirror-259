# Frequenz Weather API Release Notes

## Summary

This release includes a breaking change to how `validity_times` are specified in
calls to `Forecasts.to_ndarray_vlf`.  It also includes a couple of dependency
updates.

## Upgrading

- The required `channels` package version is now updated to `1.0.0b2`

- `validity_times` in the `to_ndarray_vlf` method on received `Forecasts` is now
  specified as a list of `datetime`s, and no longer a list of `timedelta`s.

## New Features

<!-- Here goes the main new features and examples or instructions on how to use them -->

## Bug Fixes
