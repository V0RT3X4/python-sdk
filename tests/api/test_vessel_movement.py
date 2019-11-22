from unittest import TestCase

from tests.mock_client import example_vessel_movements
from vortexasdk.api import CorporateEntity, GeographyEntity, VesselEntity, VesselMovement
from vortexasdk.api.entity_flattening import convert_vessel_movement_to_flat_dict
from vortexasdk.api.serdes import serialize_to_dict
from vortexasdk.api.vessel_movement import VesselEvent


class TestVesselMovement(TestCase):
    vm = VesselMovement(vessel_movement_id='7e0fb931ec1117d102f957048a6cce473a7eaf3f2b95f6bccdcc7b50dc3d8ab7',
                        voyage_id='7a29c4880276cbbdfade2ec6a0ee2dbbebf9e41bb47b18657196fff7cd3dc32e',
                        vessel=VesselEntity(
                            id='6d8a8f0863ca087204dd68e5fc3b6469a879829e6262856e34856aea3ca20509',
                            name='17 FEBRUARY', mmsi=248896000, imo=9380893, dwt=160391,
                            vessel_class='suezmax', corporate_entities=[CorporateEntity(
                                id='19b1bf392f474ca942b7b25ddcba363638516b2e40268ea7a70888021575a4dd',
                                label='VITOL', layer='charterer', probability=1.0, source='external'),
                                CorporateEntity(
                                    id='01ec474e7324c7633ffaf2a5c92bb7348cc02adc4d10b85daa3dd2cc5458df59',
                                    label='CORE PETROLEUM',
                                    layer='commercial_owner',
                                    probability=1.0,
                                    source='external')], tags=[],
                            status='vessel_status_ballast', start_timestamp=None, cubic_capacity=172092,
                            voyage_id=None, fixture_fulfilled=None, end_timestamp=None, fixture_id=None),
                        origin=VesselEvent(event_type='discharge', location=[GeographyEntity(
                            id='934c47f36c16a58d68ef5e007e62a23f5f036ee3f3d1f5f85a48c572b90ad8b2',
                            label='China', layer='country', probability=1.0, source='model'), GeographyEntity(
                            id='c901cc99a794afe1a7a9146c4573420e87c629717651c3a0d2ee3628cdaf0bc5',
                            label='Bayuquan [CN]', layer='port', probability=1.0, source='model'),
                            GeographyEntity(
                                id='e6955a2c59dc90833986fe0894cf6718dddaa7816bb51bc955cdd3eb4470e554',
                                label='Asia', layer='region',
                                probability=1.0,
                                source='model'),
                            GeographyEntity(
                                id='07ac020aa082d5d116f829ef28a40e9876c0644aeb4f0480202c1a86bb8adf7f',
                                label='Far East',
                                layer='shipping_region',
                                probability=1.0,
                                source='model'),
                            GeographyEntity(
                                id='2b394b41a7ff9e48b40b4ba8e6a6b045340261dfc02133d04af13fe754a71a48',
                                label='East Asia',
                                layer='shipping_region',
                                probability=1.0,
                                source='model'),
                            GeographyEntity(
                                id='a63890260e29d859390fd1a23c690181afd4bd152943a04c00cd6a5ecf3f7d1e',
                                label='North China',
                                layer='shipping_region',
                                probability=1.0,
                                source='model'),
                            GeographyEntity(
                                id='b5fafce6e20de2dc307fb7e0b89978ee91a49a7b6ec6f5461daf2633f3c56674',
                                label='China (excl. HK & Macau)',
                                layer='shipping_region',
                                probability=1.0,
                                source='model'),
                            GeographyEntity(
                                id='956b03529510459d298c4e537d23c6fbb22ffd8414af933b3475310c661f337a',
                                label='Non-OPEC',
                                layer='trading_block',
                                probability=1.0,
                                source='model'),
                            GeographyEntity(
                                id='2b394b41a7ff9e48b40b4ba8e6a6b045340261dfc02133d04af13fe754a71a48',
                                label='East Asia',
                                layer='trading_region',
                                probability=1.0,
                                source='model'),
                            GeographyEntity(
                                id='87f8d059ed2f57c1f54dd883cb0fc90f83633d736f763982f2503f6f803eb333',
                                label='Liaoning Province',
                                layer='trading_subregion',
                                probability=1.0,
                                source='model'),
                            GeographyEntity(
                                id='977573e3782428763edf580be53c73b7d04172037e6d6ba8282ea1de66dd36cb',
                                label='Xianrendao Crude Oil Terminal',
                                layer='terminal',
                                probability=1.0,
                                source='model')],
                                           pos=[121.95271103090423, 40.20963715299812],
                                           event_id='5769995a932e152f9ded42706cebe90992ba6cc06208e32833d29ea91e37a68f',
                                           start_timestamp='2017-11-19T06:59:05+0000',
                                           end_timestamp='2017-11-21T00:00:08+0000'),
                        destination=VesselEvent(event_type='discharge', location=[GeographyEntity(
                            id='934c47f36c16a58d68ef5e007e62a23f5f036ee3f3d1f5f85a48c572b90ad8b2',
                            label='China', layer='country', probability=1.0, source='model'), GeographyEntity(
                            id='056054a06d321e21ac868558a099751b324b675e05c11df7c041c8ad0edf5445',
                            label='Dalian [CN]', layer='port', probability=1.0, source='model'),
                            GeographyEntity(
                                id='e6955a2c59dc90833986fe0894cf6718dddaa7816bb51bc955cdd3eb4470e554',
                                label='Asia',
                                layer='region',
                                probability=1.0,
                                source='model'),
                            GeographyEntity(
                                id='07ac020aa082d5d116f829ef28a40e9876c0644aeb4f0480202c1a86bb8adf7f',
                                label='Far East',
                                layer='shipping_region',
                                probability=1.0,
                                source='model'),
                            GeographyEntity(
                                id='2b394b41a7ff9e48b40b4ba8e6a6b045340261dfc02133d04af13fe754a71a48',
                                label='East Asia',
                                layer='shipping_region',
                                probability=1.0,
                                source='model'),
                            GeographyEntity(
                                id='a63890260e29d859390fd1a23c690181afd4bd152943a04c00cd6a5ecf3f7d1e',
                                label='North China',
                                layer='shipping_region',
                                probability=1.0,
                                source='model'),
                            GeographyEntity(
                                id='b5fafce6e20de2dc307fb7e0b89978ee91a49a7b6ec6f5461daf2633f3c56674',
                                label='China (excl. HK & Macau)',
                                layer='shipping_region',
                                probability=1.0,
                                source='model'),
                            GeographyEntity(
                                id='956b03529510459d298c4e537d23c6fbb22ffd8414af933b3475310c661f337a',
                                label='Non-OPEC',
                                layer='trading_block',
                                probability=1.0,
                                source='model'),
                            GeographyEntity(
                                id='2b394b41a7ff9e48b40b4ba8e6a6b045340261dfc02133d04af13fe754a71a48',
                                label='East Asia',
                                layer='trading_region',
                                probability=1.0,
                                source='model'),
                            GeographyEntity(
                                id='87f8d059ed2f57c1f54dd883cb0fc90f83633d736f763982f2503f6f803eb333',
                                label='Liaoning Province',
                                layer='trading_subregion',
                                probability=1.0,
                                source='model'),
                            GeographyEntity(
                                id='e4694abfad48f9135cdd6634ebb0624c3a91097fc8e83b084747d5bdbd8c2c8e',
                                label='Dalian Xingang Oil Terminal',
                                layer='terminal',
                                probability=1.0,
                                source='model')],
                                                pos=[121.9107237155891, 38.965178213026206],
                                                event_id='487d3eba7cc29724ce6b8aca3822dfbe85eaa0a61500c3cd5fa5f705bf95c832',
                                                start_timestamp='2017-11-27T06:39:50+0000',
                                                end_timestamp='2017-11-29T02:49:32+0000'),
                        start_timestamp='2017-11-19T06:59:05+0000', end_timestamp='2017-11-29T02:49:32+0000')

    def test_deserialize(self):
        vm1 = example_vessel_movements[0]

        deserialized = VesselMovement.from_dict(vm1)

        assert self.vm == deserialized

    def test_flatten(self):
        d = serialize_to_dict(self.vm)
        flat = convert_vessel_movement_to_flat_dict(d)

        expected = {'destination.end_timestamp': '2017-11-29T02:49:32+0000',
                    'destination.event_id': '487d3eba7cc29724ce6b8aca3822dfbe85eaa0a61500c3cd5fa5f705bf95c832',
                    'destination.event_type': 'discharge',
                    'destination.location.country.id': '934c47f36c16a58d68ef5e007e62a23f5f036ee3f3d1f5f85a48c572b90ad8b2',
                    'destination.location.country.label': 'China', 'destination.location.country.layer': 'country',
                    'destination.location.country.probability': 1.0, 'destination.location.country.source': 'model',
                    'destination.location.port.id': '056054a06d321e21ac868558a099751b324b675e05c11df7c041c8ad0edf5445',
                    'destination.location.port.label': 'Dalian [CN]', 'destination.location.port.layer': 'port',
                    'destination.location.port.probability': 1.0, 'destination.location.port.source': 'model',
                    'destination.location.region.id': 'e6955a2c59dc90833986fe0894cf6718dddaa7816bb51bc955cdd3eb4470e554',
                    'destination.location.region.label': 'Asia', 'destination.location.region.layer': 'region',
                    'destination.location.region.probability': 1.0, 'destination.location.region.source': 'model',
                    'destination.location.shipping_region.id': 'b5fafce6e20de2dc307fb7e0b89978ee91a49a7b6ec6f5461daf2633f3c56674',
                    'destination.location.shipping_region.label': 'China (excl. HK & Macau)',
                    'destination.location.shipping_region.layer': 'shipping_region',
                    'destination.location.shipping_region.probability': 1.0,
                    'destination.location.shipping_region.source': 'model',
                    'destination.location.trading_block.id': '956b03529510459d298c4e537d23c6fbb22ffd8414af933b3475310c661f337a',
                    'destination.location.trading_block.label': 'Non-OPEC',
                    'destination.location.trading_block.layer': 'trading_block',
                    'destination.location.trading_block.probability': 1.0,
                    'destination.location.trading_block.source': 'model',
                    'destination.location.trading_region.id': '2b394b41a7ff9e48b40b4ba8e6a6b045340261dfc02133d04af13fe754a71a48',
                    'destination.location.trading_region.label': 'East Asia',
                    'destination.location.trading_region.layer': 'trading_region',
                    'destination.location.trading_region.probability': 1.0,
                    'destination.location.trading_region.source': 'model',
                    'destination.location.trading_subregion.id': '87f8d059ed2f57c1f54dd883cb0fc90f83633d736f763982f2503f6f803eb333',
                    'destination.location.trading_subregion.label': 'Liaoning Province',
                    'destination.location.trading_subregion.layer': 'trading_subregion',
                    'destination.location.trading_subregion.probability': 1.0,
                    'destination.location.trading_subregion.source': 'model',
                    'destination.location.terminal.id': 'e4694abfad48f9135cdd6634ebb0624c3a91097fc8e83b084747d5bdbd8c2c8e',
                    'destination.location.terminal.label': 'Dalian Xingang Oil Terminal',
                    'destination.location.terminal.layer': 'terminal', 'destination.location.terminal.probability': 1.0,
                    'destination.location.terminal.source': 'model', 'destination.pos.0': 121.9107237155891,
                    'destination.pos.1': 38.965178213026206, 'destination.start_timestamp': '2017-11-27T06:39:50+0000',
                    'end_timestamp': '2017-11-29T02:49:32+0000', 'origin.end_timestamp': '2017-11-21T00:00:08+0000',
                    'origin.event_id': '5769995a932e152f9ded42706cebe90992ba6cc06208e32833d29ea91e37a68f',
                    'origin.event_type': 'discharge',
                    'origin.location.country.id': '934c47f36c16a58d68ef5e007e62a23f5f036ee3f3d1f5f85a48c572b90ad8b2',
                    'origin.location.country.label': 'China', 'origin.location.country.layer': 'country',
                    'origin.location.country.probability': 1.0, 'origin.location.country.source': 'model',
                    'origin.location.port.id': 'c901cc99a794afe1a7a9146c4573420e87c629717651c3a0d2ee3628cdaf0bc5',
                    'origin.location.port.label': 'Bayuquan [CN]', 'origin.location.port.layer': 'port',
                    'origin.location.port.probability': 1.0, 'origin.location.port.source': 'model',
                    'origin.location.region.id': 'e6955a2c59dc90833986fe0894cf6718dddaa7816bb51bc955cdd3eb4470e554',
                    'origin.location.region.label': 'Asia', 'origin.location.region.layer': 'region',
                    'origin.location.region.probability': 1.0, 'origin.location.region.source': 'model',
                    'origin.location.shipping_region.id': 'b5fafce6e20de2dc307fb7e0b89978ee91a49a7b6ec6f5461daf2633f3c56674',
                    'origin.location.shipping_region.label': 'China (excl. HK & Macau)',
                    'origin.location.shipping_region.layer': 'shipping_region',
                    'origin.location.shipping_region.probability': 1.0,
                    'origin.location.shipping_region.source': 'model',
                    'origin.location.trading_block.id': '956b03529510459d298c4e537d23c6fbb22ffd8414af933b3475310c661f337a',
                    'origin.location.trading_block.label': 'Non-OPEC',
                    'origin.location.trading_block.layer': 'trading_block',
                    'origin.location.trading_block.probability': 1.0, 'origin.location.trading_block.source': 'model',
                    'origin.location.trading_region.id': '2b394b41a7ff9e48b40b4ba8e6a6b045340261dfc02133d04af13fe754a71a48',
                    'origin.location.trading_region.label': 'East Asia',
                    'origin.location.trading_region.layer': 'trading_region',
                    'origin.location.trading_region.probability': 1.0, 'origin.location.trading_region.source': 'model',
                    'origin.location.trading_subregion.id': '87f8d059ed2f57c1f54dd883cb0fc90f83633d736f763982f2503f6f803eb333',
                    'origin.location.trading_subregion.label': 'Liaoning Province',
                    'origin.location.trading_subregion.layer': 'trading_subregion',
                    'origin.location.trading_subregion.probability': 1.0,
                    'origin.location.trading_subregion.source': 'model',
                    'origin.location.terminal.id': '977573e3782428763edf580be53c73b7d04172037e6d6ba8282ea1de66dd36cb',
                    'origin.location.terminal.label': 'Xianrendao Crude Oil Terminal',
                    'origin.location.terminal.layer': 'terminal', 'origin.location.terminal.probability': 1.0,
                    'origin.location.terminal.source': 'model', 'origin.pos.0': 121.95271103090423,
                    'origin.pos.1': 40.20963715299812, 'origin.start_timestamp': '2017-11-19T06:59:05+0000',
                    'start_timestamp': '2017-11-19T06:59:05+0000',
                    'vessel.corporate_entities.0.id': '19b1bf392f474ca942b7b25ddcba363638516b2e40268ea7a70888021575a4dd',
                    'vessel.corporate_entities.0.label': 'VITOL', 'vessel.corporate_entities.0.layer': 'charterer',
                    'vessel.corporate_entities.0.probability': 1.0, 'vessel.corporate_entities.0.source': 'external',
                    'vessel.corporate_entities.1.id': '01ec474e7324c7633ffaf2a5c92bb7348cc02adc4d10b85daa3dd2cc5458df59',
                    'vessel.corporate_entities.1.label': 'CORE PETROLEUM',
                    'vessel.corporate_entities.1.layer': 'commercial_owner',
                    'vessel.corporate_entities.1.probability': 1.0, 'vessel.corporate_entities.1.source': 'external',
                    'vessel.cubic_capacity': 172092, 'vessel.dwt': 160391, 'vessel.end_timestamp': None,
                    'vessel.fixture_fulfilled': None, 'vessel.fixture_id': None,
                    'vessel.id': '6d8a8f0863ca087204dd68e5fc3b6469a879829e6262856e34856aea3ca20509',
                    'vessel.imo': 9380893, 'vessel.mmsi': 248896000, 'vessel.name': '17 FEBRUARY',
                    'vessel.start_timestamp': None, 'vessel.status': 'vessel_status_ballast',
                    'vessel.vessel_class': 'suezmax', 'vessel.voyage_id': None,
                    'vessel_movement_id': '7e0fb931ec1117d102f957048a6cce473a7eaf3f2b95f6bccdcc7b50dc3d8ab7',
                    'voyage_id': '7a29c4880276cbbdfade2ec6a0ee2dbbebf9e41bb47b18657196fff7cd3dc32e',
                    'vessels.corporate_entities.charterer.id': '19b1bf392f474ca942b7b25ddcba363638516b2e40268ea7a70888021575a4dd',
                    'vessels.corporate_entities.charterer.label': 'VITOL',
                    'vessels.corporate_entities.charterer.layer': 'charterer',
                    'vessels.corporate_entities.charterer.probability': 1.0,
                    'vessels.corporate_entities.charterer.source': 'external',
                    'vessels.corporate_entities.commercial_owner.id': '01ec474e7324c7633ffaf2a5c92bb7348cc02adc4d10b85daa3dd2cc5458df59',
                    'vessels.corporate_entities.commercial_owner.label': 'CORE PETROLEUM',
                    'vessels.corporate_entities.commercial_owner.layer': 'commercial_owner',
                    'vessels.corporate_entities.commercial_owner.probability': 1.0,
                    'vessels.corporate_entities.commercial_owner.source': 'external', 'vessels.cubic_capacity': 172092,
                    'vessels.dwt': 160391, 'vessels.end_timestamp': None, 'vessels.fixture_fulfilled': None,
                    'vessels.fixture_id': None,
                    'vessels.id': '6d8a8f0863ca087204dd68e5fc3b6469a879829e6262856e34856aea3ca20509',
                    'vessels.imo': 9380893, 'vessels.mmsi': 248896000, 'vessels.name': '17 FEBRUARY',
                    'vessels.start_timestamp': None, 'vessels.status': 'vessel_status_ballast',
                    'vessels.vessel_class': 'suezmax', 'vessels.voyage_id': None}

        assert expected == flat
