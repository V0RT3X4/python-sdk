# About VortexaSDK Endpoints

The endpoints module allows you to query Vortexa's data.

The VortexaSDK currently contains 4 different endpoints:

1. Cargo Movements
2. Charterers
3. Geographies
4. Products
5. Vessels


Each endpoint offers either one, or both, of two different functionalities:


1. **Lookup by ID**. Retreive an object matching a certain id. In sql speak this is the equivalent of `SELECT * FROM vessels WHERE id = 12345;`
2. **Search**. Retrieve a number of objects matching given search parameters. In sql speak this is the equivalent of `SELECT * FROM vessels WHERE name ~* 'ocean' AND vessel_class = 'vlcc';`


Let's explain with some examples:

Find all aframax vessels
```python
from vortexasdk import Vessels
df = Vessels().search(vessel_classes='aframax').to_df()
```

Find the vessel that has with id 1245
```python
vessel = Vessels().reference(id='12345')
```
