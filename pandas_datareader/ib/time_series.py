import pandas as pd
import warnings

from pandas_datareader.base import _BaseReader

IB_BASE_URL = "https://localhost:5000/v1/api/iserver"


class IBTimeSeriesReader(_BaseReader):
    """
    Returns DataFrame of the Interactive Brokers Market Data History endpoint

    .. versionadded:: 0.9.0

    Parameters
    ----------
    symbols : string
        Single contract id, a unique numeric identifier.  Use the
        /iserver/secdef/search endpoint to search for these.
    exchange : string, optional
        Exchange of the conid (e.g. ISLAND, NYSE, etc.). Default value is empty
        which corresponds to primary exchange of the conid.
    period : string, default 1y
        Time period for the request.  Possible values: {1-30}min, {1-8}h,
        {1-1000}d, {1-792}w, {1-182}m, {1-15}y
    bar: string, optional
        Bar width for the request.  Possible values: 1min, 2min, 3min, 5min,
        10min, 15min, 30min, 1h, 2h, 3h, 4h, 8h, 1d, 1w, 1m
    outsideRth: boolean, default True
        For contracts that support it, will determine if historical data
        includes outside of regular trading hours.
    retry_count : int, default 3
        Exchange of the conid (e.g. ISLAND, NYSE, etc.). Default value is empty which corresponds to primary exchange of the conid.
    pause : int, default 0.1
        Time, in seconds, to pause between consecutive queries of chunks. If
        single value given for symbol, represents the pause between retries.
    session : Session, default None
        requests.sessions.Session instance to be used

    """

    _format = "json"

    def __init__(
        self,
        symbols,
        exchange=None,
        period="1y",
        bar=None,
        outsideRth=True,
        retry_count=3,
        pause=0.1,
        session=None,
    ):

        super(IBTimeSeriesReader, self).__init__(
            symbols=symbols,
            retry_count=retry_count,
            pause=pause,
            session=session,
        )

        self._exchange = exchange
        self._period = period
        self._bar = bar
        self._outsideRth = outsideRth

    @property
    def url(self):
        """ API URL """
        return IB_BASE_URL + '/marketdata/history'

    @property
    def params(self):
        return {
            "conid": self.symbols,
            "exchange": self.exchange,
            "period": self.period,
            "bar": self.bar,
            "outsideRth": self.outsideRth,
        }

    @property
    def exchange(self):
        return self._exchange

    @property
    def period(self):
        return self._period

    @property
    def bar(self):
        return self._bar

    @property
    def outsideRth(self):
        # if self._outsideRth =
        return self._outsideRth

    def _read_lines(self, out):
        df = pd.DataFrame.from_dict(out["data"])
        df.columns = ["open", "close", "high", "low", "volume", "time"]
        df["time"] = pd.to_datetime(df["time"], unit="ms")
        df.set_index("time", inplace=True)
        if len(df) == 1000:
            warnings.warn(
                "DataFrame returned is exactly 1000 lines long,"
                " the data returned is probably truncated."
            )

        return df

    def _output_error(self, out):

        if out.status_code == 401:
        #try to reuthenticate
            url = self.url + '/reauthenticate'
            response = self.session.post(
                url, params=params, timeout=self.timeout
            )

        return False #returns False to not exit the loop
