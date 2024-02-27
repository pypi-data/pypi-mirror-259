from pytoniq_core.tl import TlGenerator


def get_schemas(auto_deser: bool = True):
    generator = TlGenerator.with_default_schemas()
    schemas = generator.generate()
    if not auto_deser:
        schemas._auto_deserialize = False  # for tests only
    return schemas


def test_geneartor():
    get_schemas()


def test_serialization():
    schemas = get_schemas()

    ser1 = schemas.serialize(
        schema=schemas.get_by_name('dht.ping'),
        data={'random_id': 142536475324}
    )

    ser2 = schemas.serialize(
        schema=schemas.get_by_class_name('dht.Pong')[-1],
        data={'random_id': 142536475324}
    )

    assert ser1 == ser2 == b'\x18?\xeb\xcb' + b'\xbc\x02\xd6/!\x00\x00\x00'  # tag + little-endian random id


def test_adnl_deser():
    schemas = get_schemas()
    data = bytes.fromhex('89cd42d10781daac064514ebc801000002000000392d45fde3e4874067c9cbadfe030fc52ca06e864d4844f0134205fed7eea0eb21a44871b004000000000000fe0004001684ac0f117466765e9ffe41f536927f536ec37c71e15fd64e8e9f7c3b0ce349ce397c0ffe860400b5ee9c72e1021e0100043a00001c00c400de0170020402a0033c036a037c0387039e03b6041c048204ce04ea0536055405a005ec0604062007000722077807ce081a0867086e0875041011ef55aaffffff110102030402a09bc7a987000000008401026472130000000100000000000000000000000000655cadad000026d485759d80000026d485759d81878c011a0007ae82020b304d020b17c3c400000003000000000000002e05060211b8e48dfb43b9aca00407080a8a042cb6278d52be40121ee9a6a1e9f3b8d6e56dc1c638df3620069a43fae4925bddf4ea7d1450ab32446793b0f6b277d3cf59e4f2869922c9f8e1f52748437ddf89021a021a0c0d03894a33f6fd667ca9b35def16bea65ae144c4120e8b5a75c352e41b8c6f0287abb329b963449e8f7f82f7dab7070ea745472ef9d11534f7ad3fbfb4c0d15f3142a4575c56a2401c1d1d0098000026d48547d6c4020b304ecd6aa7f79842da3745c4852bed1aba6b01d03c44276b3632f68f8eb8100703fb1165a051e8a995b27a0a51e79e8dc1f031d5da61c162d4e83b63af4fe1cf65e30098000026d485665b4102647212686fe392eac6c329229eb7d17979f8c8a925a57aeecaa941b69aca8545bdd32b02dbba12148420976138c4a768e12c2da3150493bfedf98e473cb91edfbc7c2d022582c294eab2ce3bd54c1614a7559671deaa40080909000d0010ee6b2800080201200a0b0013be000003bc91627aea900013bfffffffbc8b96fc9c50235b9023afe2ffffff11000000000000000000000000000264721200000001655cadaa000026d485665b41020b304d200e0f10235b9023afe2ffffff11000000000000000000000000000264721300000001655cadad000026d485759d81020b304d2014151628480101e140cdf6cee77de8e345101fd40b3b9252549fca5d0e705c41e197650c0cbde400012213820b0a53aacb38ef5530111b284801011d3dda670bea7a8a399d53844b9d102377f5e590702319c560e356c84bb5963a0002231301058529d5659c77aa9812131b284801011e65d214dd1a93c83a66ff7f7a951c79d9905d92349d138056d6d8dfd5ede5fa02172848010174707c9bc9af6ed29af4be364fd67587ddd3c66d8f9482358a6c10b938f01ee801d90111000000000000000050172213820b0a53aacb38ef55301a1b21d90000000000000000ffffffffffffffff82c294eab2ce3bd54bc8cb67491db5ba9000026d48547d6c4020b304ecd6aa7f79842da3745c4852bed1aba6b01d03c44276b3632f68f8eb8100703fb1165a051e8a995b27a0a51e79e8dc1f031d5da61c162d4e83b63af4fe1cf65e381b0219af40000000000000000105982718392d45fde3e4874067c9cbadfe030fc52ca06e864d4844f0134205fed7eea0eb21a44871b004000000040000b01900515000026d485571904fd1609154b311f71225915a65e265b0fd368dca46d9d27ea9ef6e5a77340efb3800514000026d48547d6c3ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff828480101815feaec13651f12b946d7709da403995dadcecc1e8802da513cda851c0aef87021828480101b3e9649d10ccb379368e81a3a7e8e49c8eb53f6acc69b0ba2ffa80082f70ee3900010003002000010230e024da000000000006000000000000000500000000000000b6ad5c65075324babc420afc')
    deserialized, len_ = schemas.deserialize(data)

    assert len_ == 1344

    assert isinstance(deserialized, dict)

    assert deserialized['@type'] == 'adnl.packetContents'

    assert len(deserialized['messages']) == 2

    assert deserialized['messages'][0]['@type'] == deserialized['messages'][1]['@type'] == 'adnl.message.part'

    assert isinstance(deserialized['messages'][0]['data'], bytes)

    assert deserialized['seqno'] == 6
    assert deserialized['confirm_seqno'] == 5

    schemas = get_schemas(False)

    answer_data = bytes.fromhex('1684ac0f49b543ed8b6ef7c67c5571ac02f4ee31efc191e71a55d827d31efb50e79aee34fe5805002de78f09ffffffff000000000000008054350b0255a9a6327c7574bf622812c60d543cade7cb26a1bde03347c7539e554a99989669727308a41b36c7e72e32ea96625d275950987b682e14aab9f52c4b2cdb8d48fe6a0400b5ee9c720102170200045d0100094603317c07e05a84c31c145ff1a558083a2a4e770b02db19c2ba7e6643e36bea52d8016f0209460355a9a6327c7574bf622812c60d543cade7cb26a1bde03347c7539e554a99989600160f245b9023afe2ffffff1100ffffffff0000000000000000020b355400000001655cc0d2000026d4db9690c4020b355160030405062848010174ff843ab7c4f2447eccb886f2a0bb4f30fabe2f4af169f120610752dc4b1693000128480101707fd3307904007fb75fe52ded0c54d29ead8294f8046e5d4f0264f8d61c3cd9016e22330000000000000000ffffffffffffffff81a979375cd85facb82807082455cc26aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac23609be851c75037e090a0b0c28480101a5a7d24057d8643b2527709d986cda3846adcb3eddc32d28ec21f69e17dbaaef000128480101d0a97ca181bc56e0cf7ec9567cf5f56acb89d2c3ef1f76cdcb08289360b57169001a28480101231de66bbe179746a50c19ccdc19c16781b1f22befaf4c0687ae3d230229386b000228480101cc9df6af98b7bf4c07af120a8f56417935fe44bec4a29c2c40e729688dd4ba17001122bf00014fb9fb1c0007adbf600004da9b70e9d088000136971382a0201058be1b1b53fbdcd5af6c00006c119fe662e1977ceae52c9a58fe9b39ff59f10d19060818af9545dfabc359e64b94ac5bab14e4ff6c45e5bfcf7e9c4df3d8f082aa55c0be0d0e28480101b20e36a3b36a4cdee601106c642e90718b0a58daf200753dbb3189f956b494b600012848010169ce858878f99690d19bb21218c6f5bc70443dd7c73042fc444bc948c62eed28001a284801014027806346e557030c7744a9f75960f1ef8893a7b52657c6eb2f43ec106e285b0012241011ef55aaffffff111011121301a09bc7a987000000000401020b35540000000100ffffffff0000000000000000655cc0d2000026d4db9690c0000026d4db9690c4d901973a0007adbf020b3551020b17c3c400000003000000000000002e1428480101da7cce64fe1ad3ed0bf47f77dc1d23220066bb4a103bc564a8634d265f8e276400032a8a04697819dede9e32cfa7113cd913dc2f3d65c3925acd2790dd1f20158d459b1315317c07e05a84c31c145ff1a558083a2a4e770b02db19c2ba7e6643e36bea52d8016f016f151628480101581092bfa21b6fa34674217aca72d2a5a0f752dfc34a04c8c0afe31e05af57dc00070098000026d4db874e84020b3553e48d1d98d7f08c4be4c0363df4fb5f17005cc729a444b1eded7c8f5629b4ca9a2e55b4bd4ac36530160e712b3ff1fd47e07e9b90e3c7b605c21c698f94404c5f688c0103697819dede9e32cfa7113cd913dc2f3d65c3925acd2790dd1f20158d459b1315ba298899d2a475383fdafd6e49a4d657ca4f3d52be4224a976725ff49006a847016f0014688c0103317c07e05a84c31c145ff1a558083a2a4e770b02db19c2ba7e6643e36bea52d82db28efbd15fc1c2b659dc9ca16b1378e57256660c76a5a1ddba0aa8b709f207016f0014000091b5ee9c72010104010086000101c0010103d0400201db501323bcc01059aaa0000136a6dc3a7400000136a6dc3a74322593cd542ed45a8de9bb37ceb9b0f91e8eed5a28960c1cb763f1b6da926f7973cf71abcace6e65034309bbb972528ba31d65386cc1fd8467c6ee4504567a73c880003d74ac00000000000000001059aa8b2ae6066a03001343d3a04ed21dcd6500200000')

    deserialized_bytes, _ = schemas.deserialize(answer_data)

    assert isinstance(deserialized_bytes['answer'], bytes)


def test_adnl_ser():

    data = {'@type': 'overlay.broadcast', 'src': {'@type': 'pub.ed25519', 'key': '7b0e60981dbb4dfd10f784627159cc497bd67332c3e67d4f2c565582fb011c47'}, 'certificate': {'@type': 'overlay.emptyCertificate'}, 'flags': 0, 'data': {'@type': 'tonNode.externalMessageBroadcast', 'message': { 'data': b'\xb5\xee\x9crA\x01\x02\x01\x00\xc7\x00\x01\xdf\x88\x01\\\xd0\xb5\x97\x93V\xc2\x16R&aE\xa1\x07\xa2\xc3\xcby\xcbS\xd6\xb6\xb0\x1e-\xfe]Z\xdb\xb6\x18\xa0\x05\x82\x91[\x9c\x0c\xe4\xab\xc4*F]\xfc\xca<Y\xf5\xa3sM*\\\xc8\x874\xbb\x91a\xe0\xd0\xc1\x9aT\xaf\x07\xe5\xf9\xf1\xc4$F`\x0c\xeb\xc3\x8d\x90\xeb\x91\xc0\xd3\xf9JS\xca\x90vl\x18>\xc2Y\xc4@qMM\x18\xbb*\xfa\xc2\x90\x00\x00\x04(\x1c\x01\x00\xa4b\x00\x02u50uSn\xde\x1c\x0e\x82\xc7\x9d\xde\xfb\xfa\x86\xd3\x15\xd2K\xac\xdb\xe6"\x91&\x81\xff\xee\x16\x15\x98\x0c5\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00Hello\nDo you buy GROKAI ID?\xc7F0R', '@type': 'tonNode.externalMessage'}}, 'date': 1700747287, 'signature': b'\xce&Rp\xa5\xc9j\xda\x83\x02\xea\x0f\x8f\xb6\rhd\x9e\x86F-\xb2r\xe5\x82"n\x19Tb\xe6%\xda2\xd8\xe9\xca\xf35\x13\t\xb2MP\x00\xe9~&\x93\xb2\xd0\x9d\x9a\xa9a\x86/\xcb\x89\x92( =\x01'}

    schemas = get_schemas()

    ser = schemas.serialize(
        schemas.get_by_name(data['@type']),
        data
    )

    deser, len_ = schemas.deserialize(ser)

    assert len_ == len(ser)

    assert deser['@type'] == 'overlay.broadcast'
