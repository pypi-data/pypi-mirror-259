
from pydantic import BaseModel

class Trading(BaseModel):

    symbol: str = "TNA"
    notional: float = 200.0
    is_crypto: bool = False
    side :str = 'buy'
    type :str = 'market'
    time_in_force :str = 'market'
    stop_loss :float = 195.0
    client_order_id :str = 'Client Id'
    tag :str = "test"
    is_paper :bool = True


class TradingConfig(BaseModel):

    symbol: str = "TNA"
    capital :float = 100
    active :bool = True 
    stop_loss_max :str = 95
    is_crypto :bool = True
    broker_id :str = "123123123123"