"""
Auth hooks for Terra Nanotech theme
"""

# Standard Library
from urllib.parse import urljoin

# Django
from django.conf import settings

# Alliance Auth
from allianceauth import hooks
from allianceauth.theme.hooks import ThemeHook


class TerraNanotechThemeHook(ThemeHook):
    """
    Terra Nanotech Corp Auth Theme
    https://github.com/terra-nanotech/tn-nt-auth-templates/
    """

    def __init__(self):
        """
        Init
        """

        ThemeHook.__init__(
            self,
            "Terra Nanotech",
            "Terra Nanotech Corp Auth Theme",
            css=[
                {
                    "url": urljoin(
                        settings.STATIC_URL,
                        "tnnt_templates/theme/terra-nanotech/aav4/libs/bootstrap/v5.3.2/css/bootstrap.min.css",
                    ),
                    "integrity": "sha512-1y2MKGMn41OgOgazBAujc8GPUCUDUoS4+3nPlH7mLDmgzIpcLsrAj0m/01xhpGbqbSWiqrnNUxkM/RhugT7ZIA==",
                },
                {
                    "url": urljoin(
                        settings.STATIC_URL,
                        "tnnt_templates/theme/terra-nanotech/aav4/css/terra-nanotech-defaults.min.css",
                    ),
                    # "integrity": "sha512-QS9YNAMZjh4rsJu4c1DXSaZe7t8Be5rBw969fQ/5BEsRvS2dAtdSFPoox7FPLi5pkmERejd9y1ZCrzwZVIybaQ==",
                },
                {
                    "url": urljoin(
                        settings.STATIC_URL,
                        "tnnt_templates/theme/terra-nanotech/aav4/css/terra-nanotech-fonts.min.css",
                    ),
                    # "integrity": "sha512-TUJ+bjmcwW1QAu0YBrMajs8S3S2HZqLY+BakLxjTqJQR1/RDRQJ5BPjAE1dzJBd99C4X1pS7ZIGgN8vXpBWhsw==",
                },
                {
                    "url": urljoin(
                        settings.STATIC_URL,
                        "tnnt_templates/theme/terra-nanotech/aav4/css/terra-nanotech.min.css",
                    ),
                    # "integrity": "sha512-UN9+ko7uibsWja8iTqgt2NacgyXYC7bOi1emCQEUcmEOd3LjzqYt/EY6/AKXvqLpfY2mj+V5UfzVMJGKBNxtCg==",
                },
                {
                    "url": urljoin(
                        settings.STATIC_URL,
                        "tnnt_templates/theme/terra-nanotech/aav4/css/community-app-fixes.min.css",
                    ),
                    # "integrity": "sha512-UN9+ko7uibsWja8iTqgt2NacgyXYC7bOi1emCQEUcmEOd3LjzqYt/EY6/AKXvqLpfY2mj+V5UfzVMJGKBNxtCg==",
                },
            ],
            js=[
                {
                    "url": urljoin(
                        settings.STATIC_URL,
                        "tnnt_templates/theme/terra-nanotech/aav4/libs/popper/v2.11.8/popper.min.js",
                    ),
                    "integrity": "sha512-fhcY1KxngNJ4jVhZBdmrLv4/NH31jrNM45fpxytokYp06cd7Ug05E3gximUQmukhES9Xf0kbV5F1nHVqWq2bvQ==",
                },
                {
                    "url": urljoin(
                        settings.STATIC_URL,
                        "tnnt_templates/theme/terra-nanotech/aav4/libs/bootstrap/v5.3.2/javascript/bootstrap.min.js",
                    ),
                    "integrity": "sha512-BPNIL/15RLxikcVNXWuFX/0zOtsuNphZCXgIL9im3QZ8ZB3oyGgbokg2pC757WCbpDRLxFnf89pdm6KHO8fehA==",
                },
                {
                    "url": urljoin(
                        settings.STATIC_URL,
                        "tnnt_templates/javascript/terra-nanotech.min.js",
                    ),
                    # "integrity": "sha512-+n8YwzG7fZV5ZL4Cnq5jZ3mW5JjYt2tVpZ9h9wZ6gYJ1H+3bZ3k1z
                },
            ],
            header_padding="3.6em",
        )


@hooks.register("theme_hook")
def register_terra_nanotech_hook():
    """
    Registers the Terra Nanotech theme hook

    :return:
    :rtype:
    """

    return TerraNanotechThemeHook()
