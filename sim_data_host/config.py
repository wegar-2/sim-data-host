from pydantic import BaseModel


class GbmSimulationConfig(BaseModel):
    start_value: float = 100
    mu_daily: float = 0.005
    sigma_daily: float = 0.02
    value_seed: int = 654_321
    lambda_arrival_time: float = 5
    arrival_time_seed: int = 123_456
