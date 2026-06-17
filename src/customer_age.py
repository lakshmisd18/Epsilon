import numpy as np

def add_age_group(df):

    np.random.seed(42)

    df["Age"] = np.random.randint(
        18,
        65,
        len(df)
    )

    conditions = [

        df["Age"] < 25,

        (df["Age"] >= 25)
        &
        (df["Age"] < 40),

        (df["Age"] >= 40)
        &
        (df["Age"] < 55),

        df["Age"] >= 55
    ]

    labels = [

        "18-24",

        "25-39",

        "40-54",

        "55+"
    ]

    df["AgeGroup"] = np.select(
        conditions,
        labels,
        default="25-39"
    )

    return df