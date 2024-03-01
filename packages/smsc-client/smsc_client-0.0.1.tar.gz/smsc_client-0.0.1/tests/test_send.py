from uuid import uuid1


def test_send(smsc_client):
    response = smsc_client.default.send(
        phones='79226036452',
        mes='test msg',
        id=uuid1(),
        sender='liga.school'
    )
    print(response)
