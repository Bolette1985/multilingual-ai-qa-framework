import os
import pandas as pd


def save_results(results, output_path="results/output.csv"):
    """
    Saves evaluation results to CSV and returns DataFrame.
    """

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df = pd.DataFrame(results)

    df.to_csv(output_path, index=False)

    print(f"💾 Results saved to: {output_path}")

    return df
