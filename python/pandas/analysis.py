import pandas as pd


def get_dummy_var(df=None, column=None):
  result_ = pd.get_dummies(df[column], prefix =column)
  df = pd.concat([df, result_], axis =1)
  df = df.drop(column, axis =1)
  return df