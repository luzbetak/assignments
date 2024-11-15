Data Science Pipelines
======================

This repository includes various data science and analytics projects. Each subdirectory contains scripts, data, and tools for specific projects, ranging from word processing to relational database analytics.

## Project Structures

```
data-science-pipelines/
│
├── README.md                                # Project documentation
│
├── amberdata-word-processor/                # Word processing project
│   ├── README.md
│   ├── test_word_processor.py
│   ├── word_processor.py
│   └── words.json
│
├── authorize-decorator/                     # Script for authorization decorator
│   ├── 1-run-permissions.sh
│   ├── README.md
│   ├── output.txt
│   └── permissions.py
│
├── auto-insurance-analytics/                # Auto insurance data analysis project
│   ├── 0-start-jupyter.sh
│   ├── 1-Data-Engineering.ipynb
│   ├── 2-Data-Analytics.ipynb
│   ├── 3-Training-Prep.ipynb
│   ├── CARS.csv
│   ├── CUSTOMERS.csv
│   ├── HOUSEHOLDS.csv
│   ├── README.md
│   ├── Untitled.ipynb
│   └── combined_dataset.parquet
│
├── insurance-policy-number-scanner/         # Policy number scanner project
│   ├── 1-write_policy_numbers.py
│   ├── 2-read_validate_ascii_numbers.py
│   ├── 3-fix_ill_policy_numbers.py
│   ├── README.md
│   ├── ascii_numbers_bronze.txt
│   ├── ascii_numbers_gold.txt
│   ├── ascii_numbers_platinum.txt
│   ├── ascii_numbers_silver.txt
│   └── checksum.py
│
├── medical-insurance-eligibility/           # Medical insurance eligibility app
│   ├── 1-run-app.sh
│   ├── PROJECT_FILES_INSTRUCTIONS.md
│   ├── README.md
│   ├── data/
│   │   ├── eligibility.csv
│   │   └── medical.csv
│   ├── requirements.txt
│   └── src/
│       ├── app.py
│       ├── main/
│       │   ├── __init__.py
│       │   ├── base/
│       │   │   ├── __init__.py
│       │   │   └── schema.py
│       │   └── job/
│       │       ├── __init__.py
│       │       └── pipeline.py
│       └── tests/
│           ├── __init__.py
│           └── test_pipeline.py
│
├── python-algorithms/                       # Various Python algorithm scripts
│   ├── Anagram/
│   │   ├── anagram-basic.py
│   │   └── anagram-function.py
│   ├── Arguments/
│   │   └── arguments.py
│   ├── Calendars/
│   │   ├── calendar-day.py
│   │   ├── calendar-general.py
│   │   ├── calendar-month.py
│   │   ├── compare-dates.py
│   │   ├── date-time.py
│   │   └── time-permutation.py
│   ├── Characters/
│   │   └── count-char-occurrence.py
│   ├── Class/
│   │   ├── Inheritance.py
│   │   └── MyClass.py
│   ├── Collection/
│   │   ├── dictionary-group-by-puzzle.py
│   │   └── relationship-puzzle.py
│   ├── Decorator/
│   │   └── main.py
│   ├── Dictionary/
│   │   ├── dictionary-basic.py
│   │   └── dictionary-features.py
│   ├── Exception/
│   │   ├── my-exception-general.py
│   │   └── raise-catch-exception.py
│   ├── Fibonacci/
│   │   ├── fibonacci-reverse.py
│   │   └── fibonacci.py
│   ├── Generator/
│   │   └── Fibonacci-Generator.py
│   ├── HashTable/
│   │   └── linearprobing.py
│   ├── Heap/
│   │   ├── check_heap.py
│   │   ├── convert_heap.py
│   │   ├── heap.py
│   │   └── prims-heapq.py
│   ├── Integers/
│   │   ├── find_max_second_puzzle.py
│   │   └── sum-of-two-puzzle.py
│   ├── JSON/
│   │   ├── cities.json
│   │   ├── json-collection-puzzle.py
│   │   └── my-json.py
│   ├── List/
│   │   ├── my-list-basic.py
│   │   └── my-list-of-records.py
│   ├── Queue/
│   │   ├── deque-linked-list.py
│   │   └── my-queue.py
│   ├── README.md
│   ├── Random/
│   │   └── random-number.py
│   ├── Regex/
│   │   ├── links.dat
│   │   └── my-regex.py
│   ├── SQL/
│   │   ├── Insert-Data/
│   │   │   ├── employee-table.sql
│   │   │   └── populate-data.sql
│   │   ├── Ledger/
│   │   │   ├── 1-earn-spent-report.py
│   │   │   ├── create-ledger-table.sql
│   │   │   └── earn-spent.db
│   │   └── Subquery/
│   │       ├── subquery-from.sql
│   │       ├── subquery-in.sql
│   │       ├── subquery-join.sql
│   │       └── subquery-where.sql
│   ├── Set/
│   │   └── my-set-remove-discard.py
│   ├── Sorting/
│   │   ├── bubble.py
│   │   ├── insertion.py
│   │   ├── merge.py
│   │   ├── quick.py
│   │   └── selection.py
│   ├── Stack/
│   │   ├── stack-max.py
│   │   └── stack.py
│   ├── String/
│   │   ├── distinct-subsequences.py
│   │   ├── find-longest-substring-puzzle.py
│   │   ├── find-substrings-count-chars.py
│   │   ├── random-strings.py
│   │   ├── slice-string.py
│   │   ├── split-strings-to-words.py
│   │   └── substring-counter.py
│   ├── Threads/
│   │   ├── my-threads-class.py
│   │   └── my-threads.py
│   ├── Trees/
│   │   ├── avl.py
│   │   ├── bellmanford.py
│   │   ├── binary-search-tree.py
│   │   ├── breadth-first-search.py
│   │   ├── compare_trees.py
│   │   ├── depth-first-search.py
│   │   ├── dijkstra.py
│   │   ├── k_smallest_element_tree.py
│   │   ├── kruskal.py
│   │   └── tst.py
│   ├── Tuples/
│   │   └── my-tuple.py
│   └── identifier.sqlite
│
└── relational-db-analytics/                 # Relational database analytics project
    ├── 1-bash-solution.sh
    ├── 2-python-algorithm-solution.py
    ├── 3-sql-sqlite3-solution.py
    └── sandbox.db
```

## Overview

This repository provides different projects and exercises that cover a wide range of data science, analytics, and algorithm challenges.

For more details, please refer to the individual README files in each project directory.
