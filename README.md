# restaurant-json-dataset

Sample restaurant data (15 records) for practicing JSON loading, filtering and validation in Python.

```bash
python validate.py
```

## Fields
`code`, `name`, `address`, `URL`, `type_of_food`, `rating`, optional `avg_Price`, `postcode`.

## Known data issues (kept on purpose for practice)
- Optional fields are missing in many records.
- `postcode` is sometimes a number and sometimes a string.
- Some ratings (5.5, 6) exceed a 0–5 scale.
- Record 7: `name` ("Nasr Street") looks like an address — name/address may be swapped.
