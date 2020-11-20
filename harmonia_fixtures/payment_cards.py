from typing import NamedTuple


class TokenUserInfoCardInformation(NamedTuple):
    first_six: str
    last_four: str


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
            ),
        ),
    },
}
