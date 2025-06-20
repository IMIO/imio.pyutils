Changelog
=========

1.1.5 (unreleased)
------------------

- Tested with python 3.12, 3.13.
  [sgeulette]

1.1.4 (2025-06-06)
------------------

- Fixed `IndexError` in `utils.get_ordinal_clusters` when `numbers=[]`.
  [gbastien]

1.1.3 (2025-02-05)
------------------

- Improved datetime import in system to correct load_var evaluation.
  [sgeulette]

1.1.2 (2024-12-19)
------------------

- Improved `batching.batch_delete_files`.
  [sgeulette]

1.1.1 (2024-09-18)
------------------

- Generated universal wheel version.
  [sgeulette]

1.1.0 (2024-09-17)
------------------

- Added `utils.add_key_if_value` to add a key in a dic only if value or is not None.
  [sgeulette]
- Moved `batching.batch_delete_files` from imio.helpers to be used commonly.
  [sgeulette]

1.0.4 (2024-06-11)
------------------

- Blacked files.
  [sgeulette]
- Added `system.post_request` to send a POST request.
  [sgeulette]

1.0.3 (2024-05-24)
------------------

- Fix bad release for python2.
  [aduchene]

1.0.2 (2024-05-15)
------------------

- Added a new helper `utils.get_ordinal_clusters` to cluster ordinal numbers based on an offset.
  [aduchene]

1.0.1 (2024-04-08)
------------------

- Added patterns parameter in `system.read_dir_filter`.
  [sgeulette]
- Returned original filename in `system.hashed_filename` if string to hash is empty.
  [sgeulette]

1.0.0 (2024-03-05)
------------------

- Require `six>=1.16.0`.
  [sgeulette]
- Added `system.hashed_filename` to get a new filename differentiated by a hashed string.
  [sgeulette]

1.0.0a1 (2024-02-08)
--------------------

- Handled set in `load_var`.
  [sgeulette]
- Added `load_pickle` and `dump_pickle`
  [sgeulette]
- Improved `bs.is_empty`
  [sgeulette]

1.0.0a (2023-11-28)
-------------------

- Made py2 and py3 compliant
  [sgeulette]
- Improved `utils_safe_encode`
  [sgeulette]
- Added `bs.is_empty` function.
  [sgeulette]
- Added `bs.remove_some_childrens` function.
  [sgeulette]
- Added `bs.replace_strings_by_pattern` function
  [sgeulette]
- Added `exclude_patterns` parameter in `system.read_recursive_dir`
  [sgeulette]

0.31 (2023-09-26)
-----------------

- Added `utils.listify` that will make sure a given value
  is always returned as list-like iterable.
  [gbastien]
- Improved `system.get_git_tag` with new parameter to get last tag from all branches
  [sgeulette]
- Added `utils.radix_like_starting_1` to get list of positional numbers following a given base but starting with 1
  [sgeulette]
- Added `utils.letters_sequence` to get a letters string corresponding to nth position
  [sgeulette]

0.30 (2023-07-24)
-----------------

- Added `system.read_recursive_dir` to get files recursively (with relative or full name).
  [sgeulette]

0.29 (2023-05-12)
-----------------

- Improved `utils.all_of_dict_values` to include optionally a label.
  [sgeulette]
- Added `setup_logger` to modify a given logger independently
  [sgeulette]
- Added `full_path` to prefix filename with path if necessary
  [sgeulette]

0.28 (2023-03-29)
-----------------

- Added `utils.one_of_dict_values` that gives the first non empty value of a list of keys.
  [sgeulette]
- Added `utils.all_of_dict_values` that returns a not empty values list from a dict following a keys list
  [sgeulette]

0.27 (2023-02-27)
-----------------

- Added `utils.sort_by_indexes` that will sort a list of values
  depending on a list of indexes.
  [gbastien]

0.26 (2022-12-12)
-----------------

- Added `stop` to print error and exit.
  [sgeulette]

0.25 (2022-09-16)
-----------------

- Added `get_git_tag`.
  [sgeulette]

0.24 (2022-08-19)
-----------------

- Added `utils.time_start` and `utils.time_elapsed` to print elapsed time from start.
  Intended to be easily used when debugging...
  [sgeulette]

0.23 (2022-07-01)
-----------------

- Added `utils.append` to append a value and return it.
  [sgeulette]

0.22 (2022-04-28)
-----------------

- Added `utils.get_clusters` to display a list of number grouped by clusters.
  [gbastien]

0.21 (2022-04-26)
-----------------

- Added `utils.merge_dicts` to be able to merge several dicts for which values
  are list, list are extended in final result.
  [gbastien]

0.20 (2022-02-10)
-----------------

- Modified `memory` to return more useful information.
  [sgeulette]

0.19 (2022-01-21)
-----------------

- Added `process_memory` to return current process memory.
  [sgeulette]
- Added `memory` to return RAM information.
  [sgeulette]

0.18 (2022-01-12)
-----------------

- Made `insert_in_ordereddict` python3 compatible.
  [sgeulette]
- Added `odict_pos_key` to get key at position in ordereddict.
  [sgeulette]

0.17 (2022-01-04)
-----------------

- Added `timed` and `ftimed` functions.
  [sgeulette]
- Added OrderedDict for load_var function
  [sgeulette]

0.16 (2021-10-27)
-----------------

- Added `iterable_as_list_of_list` function.
  [sgeulette]
- Added date in runCommand output
  [sgeulette]

0.15 (2021-04-27)
-----------------

- Added `ln_key` parameter in `read_dictcsv` method.
  [sgeulette]

0.14 (2021-04-21)
-----------------

- Added `read_dictcsv` function.
  [sgeulette]
- Added `utils.replace_in_list` function to ease replacement of values in a list.
  [gbastien]
- Added `safe_encode` function.
  [sgeulette]

0.13 (2020-10-07)
-----------------

- Added `insert_in_ordereddict` function to easier insert a new key at needed position.
  [sgeulette]

0.12 (2020-05-19)
-----------------

- Update syntax for py 3.
  [odelaere]

0.11 (2018-10-12)
-----------------

- Added warning log level function
  [odelaere]

0.10 (2018-07-23)
-----------------

- Added to_skip parameter in read_dir functions.
  [sgeulette]

0.9 (2017-07-28)
----------------

- Added read_csv function.
  [sgeulette]

0.8 (2017-07-19)
----------------

- runCommand can append to file.
  [sgeulette]

0.7 (2017-06-26)
----------------

- Just release on pypi for collective.documentgenerator.
  [sgeulette]

0.6 (2017-02-08)
----------------

- runCommand: return as third value the return code of the command.
  [sgeulette]

0.5 (2017-02-08)
----------------

- Added outfile parameter to runCommand.
  [sgeulette]

0.4 (2016-12-07)
----------------

- Added param to get only files in dir.
  [sgeulette]
- Added methods for bs4 (beautifulsoup)
  [sgeulette]

0.3 (2016-09-21)
----------------

- Return empty list when file doesn't exist.
  [sgeulette]

0.2 (2016-04-15)
----------------

- Added options on read_file.
  [sgeulette]

0.1 (2015-06-03)
----------------

- Initial release.
  [sgeulette]
