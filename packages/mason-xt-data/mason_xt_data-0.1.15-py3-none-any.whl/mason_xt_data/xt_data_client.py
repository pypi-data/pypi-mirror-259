import time

from mason_tools import RpcClient


class XtDataClient(RpcClient):
    """
    Test RpcClient
    """

    def __init__(self):
        """
        Constructor
        """
        super().__init__()

    def callback(self, topic, data):
        """
        Realize callable function
        """
        print(f"client received topic:{topic}, data:{data}")


if __name__ == "__main__":
    req_address = "tcp://localhost:2014"
    sub_address = "tcp://localhost:4102"

    tc = XtDataClient()
    tc.subscribe_topic("")
    tc.start(req_address, sub_address)

    start_date = "20230110"
    end_date = "20240112"
    period = "1d"
    symbol = "rb2405.SF"
    while 1:
        # df = tc.get_history_data(symbol, period, start_date, end_date)
        print(tc.history_main_symbols("rb00.SF", start_date, end_date))
        # print(df.head())
        # time.sleep(3)
        # data = tc.api(
        #     "get_market_data",
        #     [],
        #     [symbol],
        #     start_time=start_date,
        #     end_time=end_date,
        #     period=period,
        # )
        # print(data)
