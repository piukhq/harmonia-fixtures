from typing import NamedTuple


class TokenUserInfoCardInformation(NamedTuple):
    first_six: str
    last_four: str
    expiry_year: int
    expiry_month: int


class TokenUserInfo(NamedTuple):
    loyalty_id: str
    credentials: dict
    card_information: TokenUserInfoCardInformation


# maps loyalty scheme slugs to token: user_info pairs
token_user_info_map = {
    "iceland-bonus-card": {
        "test-token-1": TokenUserInfo(
            loyalty_id="card-number-1",
            credentials={
                "merchant_identifier": "iceland-merchant-identifer-1",
            },
            card_information=TokenUserInfoCardInformation(
                first_six="123456",
                last_four="1234",
                expiry_year=22,
                expiry_month=6,
            ),
        ),
        "test-token-2": TokenUserInfo(
            loyalty_id="card-number-2",
            credentials={
                "merchant_identifier": "iceland-merchant-identifer-2",
            },
            card_information=TokenUserInfoCardInformation(
                first_six="789012",
                last_four="5678",
                expiry_year=22,
                expiry_month=5,
            ),
        ),
    },
    "harvey-nichols": {
        "test-token-3": TokenUserInfo(
            loyalty_id="card-number-3",
            credentials={
                "card_number": "hn-card-number-1",
            },
            card_information=TokenUserInfoCardInformation(
                first_six="098765",
                last_four="0987",
                expiry_year=22,
                expiry_month=6,
            ),
        ),
        "test-token-4": TokenUserInfo(
            loyalty_id="card-number-4",
            credentials={
                "card_number": "hn-card-number-2",
            },
            card_information=TokenUserInfoCardInformation(
                first_six="432109",
                last_four="6543",
                expiry_year=22,
                expiry_month=5,
            ),
        ),
    },
    "wasabi-club": {
        "test-token-5": TokenUserInfo(
            loyalty_id="card-number-5",
            credentials={
                "email": "wasabi-email-1",
            },
            card_information=TokenUserInfoCardInformation(
                first_six="067457",
                last_four="8674",
                expiry_year=22,
                expiry_month=6,
            ),
        ),
        "test-token-6": TokenUserInfo(
            loyalty_id="card-number-6",
            credentials={
                "email": "wasabi-email-2",
            },
            card_information=TokenUserInfoCardInformation(
                first_six="949567",
                last_four="8519",
                expiry_year=22,
                expiry_month=5,
            ),
        ),
    },
    "squaremeal": {
        "test-token-7": TokenUserInfo(
            loyalty_id="card-number-7",
            credentials={
                "card_number": "squaremeal-card-number-1",
            },
            card_information=TokenUserInfoCardInformation(
                first_six="776655",
                last_four="4477",
                expiry_year=22,
                expiry_month=6,
            ),
        ),
        "test-token-8": TokenUserInfo(
            loyalty_id="card-number-8",
            credentials={
                "card_number": "squaremeal-card-number-2",
            },
            card_information=TokenUserInfoCardInformation(
                first_six="776666",
                last_four="4488",
                expiry_year=22,
                expiry_month=5,
            ),
        ),
    },
    "bpl-asos": {
        "test-token-9": TokenUserInfo(
            loyalty_id="card-number-9",
            credentials={
                "merchant_identifier": "asos-merchant-identifer-1",
            },
            card_information=TokenUserInfoCardInformation(
                first_six="889900",
                last_four="3344",
                expiry_year=22,
                expiry_month=6,
            ),
        ),
        "test-token-10": TokenUserInfo(
            loyalty_id="card-number-10",
            credentials={
                "merchant_identifier": "asos-merchant-identifer-2",
            },
            card_information=TokenUserInfoCardInformation(
                first_six="889999",
                last_four="3355",
                expiry_year=22,
                expiry_month=5,
            ),
        ),
    },
}
