"""
This file specifies different kinds of tests and the functions to be run within each test.
"""
from mltrace.base_test import Test


class Outliers(Test):
    def __init__(self):
        super().__init__("Outliers")
    def testZscore(self, df ): # pass in arguments directly in to here
        """
        Checks to make sure there are no outliers using z score cutoff.
        """
        z_scores = (
                (df - df.mean(axis=0, skipna=True)) / df.std(axis=0, skipna=True)
        ).abs()

        stdev_cutoff = 5.0
        if (z_scores > stdev_cutoff).to_numpy().sum() > 0:
            raise Exception("There are outlier values!")

    def testDistributionCheck(self):
        pass