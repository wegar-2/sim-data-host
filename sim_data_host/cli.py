import argparse

from sim_data_host.host import host
from sim_data_host.config import GbmSimulationConfig

def main():

    parser = argparse.ArgumentParser(
        prog="start_host",
        description="Start the local simulated data host"
    )

    parser.add_argument("--start_value", default=100.00, type=float)
    parser.add_argument("--mu_daily", default=0.005, type=float)
    parser.add_argument("--sigma_daily", default=0.02, type=float)
    parser.add_argument("--value_seed", default=654_321, type=int)
    parser.add_argument("--lambda_arrival_time", default=5.0, type=float)
    parser.add_argument("--arrival_time_seed", default=123_456, type=int)

    args = parser.parse_args()

    host(
        gbm_sim_config=GbmSimulationConfig(
            start_value=args.start_value,
            mu_daily=args.mu_daily,
            sigma_daily=args.sigma_daily,
            value_seed=args.value_seed,
            lambda_arrival_time=args.lambda_arrival_time,
            arrival_time_seed=args.arrival_time_seed
        ),
        port=args.port
    )

if __name__ == "__main__":
    main()
