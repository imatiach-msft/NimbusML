# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
CharTokenizer
"""

__all__ = ["CharTokenizer"]


from sklearn.base import TransformerMixin

from ...base_transform import BaseTransform
from ...internal.core.preprocessing.text.chartokenizer import \
    CharTokenizer as core
from ...internal.utils.utils import trace


class CharTokenizer(core, BaseTransform, TransformerMixin):
    """

    Text transforms that can be performed on data before training
    a model.

    .. remarks::
        The ``CharTokenizer`` transform is a character-oriented tokenizer
        where
        text is considered a sequence of characters.

    :param columns: a dictionary of key-value pairs, where key is the output
        column name and value is the input column name.

        * Multiple key-value pairs are allowed.
        * Input column type: string.
        * Output column type:
         `Vector Type </nimbusml/concepts/types#vectortype-column>`_.
        * If the output column names are same as the input column names, then
        simply specify ``columns`` as a list of strings.

        The << operator can be used to set this value (see
        `Column Operator </nimbusml/concepts/columns>`_)

        For example
         * CharTokenizer(columns={'out1':'input1', 'out2':'input2'})
         * CharTokenizer() << {'out1':'input1', 'out2':'input2'}

        For more details see `Columns </nimbusml/concepts/columns>`_.

    :param use_marker_chars: Whether to mark the beginning/end of each row/slot
        with start of text character (0x02)/end of text character (0x03).

    :param params: Additional arguments sent to compute engine.

    .. seealso::
        :py:class:`FromKey <nimbusml.preprocessing.FromKey>`,
        :py:class:`ToKey <nimbusml.preprocessing.ToKey>`,
        :py:class:`OneHotHashVectorizer
        <nimbusml.feature_extraction.categorical.OneHotHashVectorizer>`,
        :py:class:`OneHotVectorizer
        <nimbusml.feature_extraction.categorical.OneHotVectorizer>`,
        :py:class:`NGramFeaturizer
        <nimbusml.feature_extraction.text.NGramFeaturizer>`.

    .. index:: transform, preprocessing, text

    Example:
       .. literalinclude:: /../nimbusml/examples/CharTokenizer.py
              :language: python
    """

    @trace
    def __init__(
            self,
            use_marker_chars=True,
            columns=None,
            **params):

        if columns:
            params['columns'] = columns
        BaseTransform.__init__(self, **params)
        core.__init__(
            self,
            use_marker_chars=use_marker_chars,
            **params)
        self._columns = columns

    def get_params(self, deep=False):
        """
        Get the parameters for this operator.
        """
        return core.get_params(self)
