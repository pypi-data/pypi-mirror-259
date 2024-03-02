"""Market Module."""


class Market:
    """Market Class."""

    def __init__(self, parent):
        """Class constructor."""
        self.parent = parent

    def reference_prices(self, expiry, currency_pair):
        """Get reference prices."""
        body = {"expiry": expiry, "currencyPair": currency_pair}
        return self.parent.post("/clientapi/referencePrices", json=body)

    def spot_prices(self):
        """Get spot prices."""
        return self.parent.post("/clientapi/spotPrices")
