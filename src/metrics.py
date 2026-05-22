def print_summary(df):
    """
    Prints evaluation summary metrics.
    """

    if df is None or len(df) == 0:
        print("❌ No results generated - check API or dataset")
        return

    accuracy = df["passed"].mean()

    category_scores = df.groupby("category")["score"].mean()

    print("\n==============================")
    print("✅ EVALUATION COMPLETE")
    print("==============================")

    print(f"📊 Total Tests: {len(df)}")
    print(f"📈 Accuracy: {accuracy:.2%}")

    print("\n📊 Category Performance")
    print((category_scores * 100).round(2).astype(str) + "%")

    print("==============================")
