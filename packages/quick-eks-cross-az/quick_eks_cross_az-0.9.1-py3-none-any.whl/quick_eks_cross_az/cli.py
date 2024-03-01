"""Console script for the_answer_asaf."""

import argparse
import sys

from wakepy import keep

from .lib import CrossAzLogger


def main():
    """Console script for the_answer_asaf."""

    parser = argparse.ArgumentParser(description="EKS Cross AZ Log")

    parser.add_argument("--minutes", metavar="N", type=int, default=15, help="minutes of flow logs accumulation")
    parser.add_argument(
        "--quiet",
        action=argparse.BooleanOptionalAction,
        help="run without manual confirmation",
    )
    parser.add_argument("--verbose", action=argparse.BooleanOptionalAction, help="verbose log")
    parser.add_argument(
        "--cleanup",
        action=argparse.BooleanOptionalAction,
        help="cleanup a previous interrupted run",
    )
    parser.add_argument(
        "--output",
        action=argparse.BooleanOptionalAction,
        help="output file name",
        default="cross-az.csv",
    )
    parser.add_argument(
        "--stack-name",
        action=argparse.BooleanOptionalAction,
        help="override CloudFormation stack name",
        default="quick-eks-cross-az",
    )

    args = parser.parse_args()

    try:
        cazl = CrossAzLogger(
            accumulation_minutes=args.minutes,
            verbose=args.verbose,
            output_file_name=args.output,
            cf_stack_name=args.stack_name,
        )
        cazl.setup_clients()
        credentials_ok = cazl.test_credentials()
        if not credentials_ok:
            return 1
        if args.cleanup:
            print("Cleaning up...", flush=True)
            cazl.cleanup_and_delete_cf_stack()
            return 0
        cluster_name = cazl.get_cluster_name_from_kube_context()
        if not args.quiet:
            print(
                "This script will activate flow logs for the cluster VPC using CloudFormation. It then turns them off.\n"
                'If this script is interrupted make sure to clean up resources by running script with "--cleanup" argument\n'
                "\n"
                f"Running on cluster from active kubernetes context: {cluster_name}\n"
                "Continue? [Y/n]",
                flush=True,
            )
            validation = input()
            if validation.strip().lower() == "n":
                print("Aborting...", flush=True)
                return 0
        with keep.running() as _k:
            cazl.run()

    except Exception as e:
        print(f"Exception while running script: {e}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
