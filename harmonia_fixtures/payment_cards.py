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
            credentials={},
            card_information=TokenUserInfoCardInformation(
                first_six="123456",
                last_four="1234",
            ),
        ),
        "test-token-2": TokenUserInfo(
            loyalty_id="card-number-2",
            credentials={},
            card_information=TokenUserInfoCardInformation(
                first_six="789012",
                last_four="5678",
            ),
        ),
    },
    "harvey-nichols": {
        "test-token-3": TokenUserInfo(
            loyalty_id="card-number-3",
            credentials={},
            card_information=TokenUserInfoCardInformation(
                first_six="098765",
                last_four="0987",
            ),
        ),
        "test-token-4": TokenUserInfo(
            loyalty_id="card-number-4",
            credentials={},
            card_information=TokenUserInfoCardInformation(
                first_six="432109",
                last_four="6543",
            ),
        ),
    },
}
