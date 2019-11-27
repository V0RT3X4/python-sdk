#!/usr/bin/env bash

#CURL --silent --header "Content-Type: application/json" -X POST \
#    --data '{"size":2}' \
#    "https://api.vortexa.com/v5/reference/charterers?apikey=${VORTEXA_API_KEY}" | jq ".data" \
#    > ../tests/api/examples/corporations.json
#
#CURL --silent --header "Content-Type: application/json" -X POST \
#    --data '{"size":2}' \
#    "https://api.vortexa.com/v5/reference/vessels?apikey=${VORTEXA_API_KEY}" | jq ".data" \
#    > ../tests/api/examples/vessels.json
#
#CURL --silent --header "Content-Type: application/json" -X POST \
#    --data '{"size":2}' \
#    "https://api.vortexa.com/v5/reference/products?apikey=${VORTEXA_API_KEY}" | jq ".data" \
#    > ../tests/api/examples/products.json

CURL --header "Content-Type: application/json" -X POST \
    --data '{"filter_time_max":"2017-11-21T23:59:59.999Z","filter_time_min":"2017-11-21T00:00:00.000Z","unit":"b","size":2}' \
    "https://api.vortexa.com/v5/vessel-movements/search?apikey=${VORTEXA_API_KEY}" \
    | jq ".data" \
    > ../tests/api/examples/vessel_movements.json
