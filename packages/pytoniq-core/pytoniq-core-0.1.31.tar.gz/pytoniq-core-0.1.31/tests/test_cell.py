from pytoniq_core.boc import begin_cell, Builder, Address, Cell


def test_boc():

    empty_cell = Cell.one_from_boc('b5ee9c72010101010002000000')

    assert empty_cell == Cell.empty()
    assert empty_cell == begin_cell().end_cell()
    assert empty_cell == begin_cell().store_cell(empty_cell).end_cell()

    block_boc = 'te6ccuICAS0AAQAAJCwAAAAkAMwA8gGIAmoDBgM4A1oDaQOCA5wEDAR8BMgFcAWwBqIGvAdkB6QIlgkGCVMJdgmaCkYKZgqGCqYKwgreCvoLFgsyC04LagwQDJQMuAzYDSQNcA2QDbAN0A3wDhAOMA5QDnAOkA86D8IQIBAyELAQ/BHIEegR9hIUEjISUBJwEo4SrBLKEugTBhMkE0IT2BPmE/QUAhQQFB4ULBQ6FEgUVhRkFLAUvhTMFNoU6BT2FQQVEhUgFS4VPBVKFZYVpBWyFcAVzhXcFeoV+BYGFhQWYBaEFqgW9RegF8AX4BgtGHkYmBi0GQEZTRloGYQZ0RodGjgaVBqhGu0bCBtVG3AcFhxjHOYdMx2FHdAd8B49HokeqB7IHxUfNB+BH80f7CA5IFggeCDFIOQhMSF9IZwh6SIIIrIi/yOGI9MkMCR9JI4lDCVZJaUl8Sa8JwknKCc2J4MnoCftKAooVyh0KMEo4CktKUoplym0KgEqHiprKogq1SryKz8rXCupK8Yr5CySLN8tKy3ALc4uGy4oLnUugi7PLtwu6i83L0QvkS/dL+owNzBEMFIwnzDrMPgxRTFSMggyvjLMMtoy6DM1M0IzjzOcM+kz9jRDNFA0nTSqNPc1BDVRNV41qzW4NgU2EjZfNmw3IDeYOEw4mTimOPM5ADkOOVs5aDm1OgE6DjocOmk6tTrCOtA7HTtpO3Y7hDvRPIQ9OD1EPUo9VD18PdA94D6IPyw/OD9EP8pAikEQQSJBxkKGQo1DE0MkQ8hD1UQYRCJFBkUeRSxFO0X7RgRGikamR1dH+EhZBBAR71Wq////EQABAAIAAwAEAaCbx6mHAAAAAAQBAdHTkQAAAAEA/////wAAAAAAAAAAZJNGvQAAIytVnj7AAAAjK1WePsRmCjexAAbd4wHR044B0cxnxAAAAAMAAAAAAAAALgAFAhk+v5i3ShLwAhGgIpAgAAYABwqKBHcnLbWka4q4JX8MhsFTI/0CwNLe3/+kfvCvGWSAsmiEoK6AEZACeTQ9rc+nKRkHRCwsJNuq0JTOO8GaAv/FEHgBbwFvAAsADBSJFoK6PDgitV/i0p6hVSc7xPn89VdQs4lH7NVh+dqWZ8cAB0oz9v17aJIMOuyKIRFvBqwa4+vNEgK0tdqBMT6l4LG7c3IKcvNyrp2zKPVw79imQ+S4nBQLirAMFU+zLeGJVUSEe5qUwAELAQwBDQEOAJgAACMrVY78hAHR05APHr7T/pjE/C43nR62mCo7UnYhvwrD4h5NYkQYYzeqvL5J1te9TC708fkIg3qVN7wa/+el3IYZiGDNtqN5WZCrAiWCDTVNw3/nMuwQaapubJa5p8AIAAgACAAdQ8G1RBJQl4AQkZVPxAAIAgEgAAkACgAVvgAAA7yzVatGatAAFb////+8vQ79pWPQJFuQI6/i////EQD/////AAAAAAAAAAAB0dOQAAAAAWSTRroAACMrVY78hAHR041gAA0ADgAPABAkW5Ajr+L///8RAP////8AAAAAAAAAAAHR05EAAAABZJNGvQAAIytVnj7EAdHTjmAAEQASABMAFChIAQHo/UpefHxb7wZC13+d4AVmD75LBWPeSeTRaGy7L4TK9AABMhOhFvHb4JB9I+Ah1Ya0jUBIUEHk4PHbo6rkVHa3M9kBWfUAndG57reWRedPnHBE4cgPLHLahfpturIynmLG/kTHAW4AE4IINNU3Df+cy7AAFwCHIjMAAAAAAAAAAP//////////gg01TcN/5zLoKACHABY0VTeL9buqOhZU3hiuxA2Iqj9Ebubu1SpDqpCqLcNqaYNYC2BU3AOX5tZWmaABPGFJgKr99lTTJFPIji+Z5fJVep8AGwAOzCaqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqsI05EmHrktDfgA4AKQAOQCmAREAAAAAAAAAAFAAFTITE9qczXJO4sUi1WCTCIdl4qoYHJ7okWwU3mfzc8GGea4CF+14eDoYNjJzKGUFwEEZzmWuXkTzULWA+ZlotELnqAFuABOCCDTVNzZLXNPwAGkAhyIzAAAAAAAAAAD//////////4INNU3Nktc0+CgAhwAWNFUKI4yZuR/eVe2CyY3pWHKni91EfQgg7MYekj/l6ZS1ng0wZACmPUuN/nPFhHnae3M2TzFWR6KIGwpC5bIsctqOABsAEMwmqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqrCNORJjLXBG34BHwCkAKUApgBrsEAAAAAAAAAAAOjpyIAAEZWqx35B///////////////////////////////////////////AKEgBAR3hOHbX+8lPBVMbGWN1gwlSJ00Aiqv8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'

    assert Cell.from_boc(block_boc)[0] == Cell.one_from_boc(block_boc)

    assert Cell.one_from_boc(block_boc).hash.hex() == 'b0c09b7c116f951092b3d1b258fb98adc01c698a227b3b2e268469c24173eeb2'


def test_copy():

    cell = begin_cell().store_uint(10, 10).end_cell()

    cell_copy = cell.copy()

    cs = cell.begin_parse()

    cs.load_uint(10)

    assert cell == cell_copy
    assert cs.remaining_bits == 0

    cb = cell.to_builder()
    cb.store_uint(1, 32)

    assert cell == cell_copy
    assert cb.used_bits == 42


def test_hashes():

    exotic = Builder(type_=1).store_uint(1, 8).store_bytes(b'\x01').store_bytes(Cell.empty().hash).store_uint(0, 16).end_cell()

    assert exotic.is_exotic
    assert exotic.hash != exotic.get_hash(0)
    assert exotic.get_hash(0) == Cell.empty().hash
