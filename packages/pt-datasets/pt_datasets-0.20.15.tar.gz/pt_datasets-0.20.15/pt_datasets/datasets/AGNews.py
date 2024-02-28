# PyTorch Datasets utility repository
# Copyright (C) 2020-2023  Abien Fred Agarap
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""Class for AG News dataset"""
import os
from pathlib import Path
from typing import Any, Tuple

import numpy as np
import torch

from pt_datasets.utils import (
    download_agnews_glove,
    preprocess_data,
    read_data,
    vectorize_text,
)

__author__ = "Abien Fred Agarap"


class AGNews(torch.utils.data.Dataset):
    _supported_vectors = ("ngrams", "tfidf", "glove")

    def __init__(
        self,
        train: bool = True,
        vectorizer: str = "tfidf",
        ngram_range: Tuple = (3, 3),
        return_vectorizer: bool = False,
    ):
        """
        Loads the AG News dataset.

        Parameters
        ----------
        train: bool
            Whether to load the training set or not.
        vectorizer: str
            The vectorizer to use, options: [tfidf (default) | ngrams]
        ngram_range: Tuple
            The lower and upper bound of ngram range to use.
            Default: [(3, 3)]
        return_vectorizer: bool
            Whether to return the vectorizer object or not.
        """
        assert vectorizer in AGNews._supported_vectors
        path = str(Path.home())
        path = os.path.join(path, "datasets")
        if vectorizer in ("ngrams", "tfidf"):
            if train:
                path = os.path.join(path, "ag_news.train")
                dataset = read_data(path)
                features, labels = (list(dataset.keys()), list(dataset.values()))
                features, labels = preprocess_data(features, labels)
                if return_vectorizer:
                    features, vectorizer = vectorize_text(
                        features,
                        vectorizer,
                        return_vectorizer=return_vectorizer,
                        ngram_range=ngram_range,
                    )
                    self.vectorizer = vectorizer
                else:
                    features = vectorize_text(
                        features,
                        vectorizer,
                        return_vectorizer=return_vectorizer,
                        ngram_range=ngram_range,
                    )
            else:
                path = os.path.join(path, "ag_news.test")
                dataset = read_data(path)
                features, labels = (list(dataset.keys()), list(dataset.values()))
                features, labels = preprocess_data(features, labels)
                features = vectorize_text(features, vectorizer, ngram_range=ngram_range)
        elif vectorizer == "glove":
            glove_train, glove_test = "ag_news_train_300d.npy", "ag_news_test_300d.npy"
            if (not os.path.isfile(os.path.join(path, glove_train))) or (
                not os.path.isfile(os.path.join(path, glove_test))
            ):
                download_agnews_glove()
            if train:
                dataset = np.load(os.path.join(path, glove_train))
                features, labels = dataset[:, :-1], dataset[:, -1]
            else:
                dataset = np.load(os.path.join(path, glove_test))
                features, labels = dataset[:, :-1], dataset[:, -1]
        self.data = features
        self.targets = labels
        self.classes = ["World", "Sports", "Business", "Sci/Tech"]

    def __getitem__(self, index: int) -> Tuple[Any, Any]:
        text, target = self.data[index], self.targets[index]
        target = target.astype("int64")
        return (text, target)

    def __len__(self) -> int:
        return len(self.data)
