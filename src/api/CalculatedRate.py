class CalculatedRate:
    """
    Class to represent a rate with its calculated value
    """

    def __init__(self, name: str, rate: float, calculated: float):
        """
        Constructor

        :param name: Name of the Rate (EUR, USD, ...)
        :param rate: What is the conversion rate to the base rate
        :param calculated: What is the calculated amount
        """
        self.name = name
        self.rate = rate
        self.calculated = calculated

    def __str__(self) -> str:
        """
        Converts to formated list item
        """
        return "<li><b>{:.2f} {}</b> (Kurs: {:f}</li>".format(self.calculated, self.name, self.rate)
