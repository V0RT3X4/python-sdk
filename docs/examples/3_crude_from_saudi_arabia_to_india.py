"""
Let's find all crude cargo movements from Saudi Arabia to India that loaded in the last month.

The below script returns a `pd.DataFrame`, similar to the table given in the movements tab of `https://analytics.vortexa.com`,
 filtering on `Products: Crude` with `Origin: Saudi Arabia`, `Destination: India` and `Date Range: Departures in the last Month`.

"""
from datetime import datetime

from dateutil.relativedelta import relativedelta

from docs.utils import to_markdown
from vortexasdk import CargoMovements, Geographies, Products

now = datetime.utcnow()
one_month_ago = now - relativedelta(months=1)

# First we find the ID for the country India. Note that when searching geographies with the term 'india', we'll
# retreive all geographies with india in the name, ie Indiana, British Indian Ocean Territory...
all_geogs_with_india_in_the_name = Geographies().search("india").to_list()

# We're only interested in the country India here
india = [g.id for g in all_geogs_with_india_in_the_name if g.name == "India"]
# Check we've only got one ID for India
assert len(india) == 1

saudi_arabia = [
    g.id
    for g in Geographies().search("saudi arabia").to_list()
    if "country" in g.layer
]
# Check we've only got one ID for Saudi Arabia
assert len(saudi_arabia) == 1

# Let's find the Crude ID
crude = [
    p.id for p in Products().search("crude").to_list() if p.name == "Crude"
]
# Check we've only got one Crude ID
assert len(crude) == 1

# Query the API.
search_result = CargoMovements().search(
    filter_activity="loading_end",
    filter_origins=saudi_arabia,
    filter_destinations=india,
    filter_products=crude,
    filter_time_min=one_month_ago,
    filter_time_max=now,
)

# A complete list of available columns can be found at https://v0rt3x4.github.io/python-sdk/endpoints/cargo_movements/#notes
# We only require a subset of available columns here
required_columns = [
    # A cargo movement can be carried by multiple vessels across various STS transfers. You can find all the vessels that
    # the cargo was onboard by inspecting the 'vessels.0', 'vessels.1' columns etc.
    # The 'vessels.0' columns shows the primary vessel associated with the cargo movement
    "vessels.0.name",
    "vessels.0.vessel_class",
    # Here we show any corporate information associated with the primary vessel
    "vessels.0.corporate_entities.charterer.label",
    "vessels.0.corporate_entities.time_charterer.label",
    "vessels.0.corporate_entities.commercial_owner.label",
    # Show the product information and quantity
    "product.group.label",
    "product.grade.label",
    "quantity",
    # Is the vessel in transit, has it already discharged, or is it in floating storage?
    "status",
    # Show the loading Port name, and the loading timestamp
    "events.cargo_port_load_event.0.location.port.label",
    "events.cargo_port_load_event.0.end_timestamp",
    # Show the discharge Port name, and the discharge timestamp
    "events.cargo_port_unload_event.0.location.port.label",
    "events.cargo_port_unload_event.0.end_timestamp",
]

# Convert the search result to a dataframe
df = search_result.to_df(columns=required_columns)

# Sort the dataframe by loading timestamp
df = df.sort_values(by=["events.cargo_port_load_event.0.end_timestamp"])

print(to_markdown(df))
